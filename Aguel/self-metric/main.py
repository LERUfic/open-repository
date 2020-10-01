import os.path
import random
import shutil
import time

import prometheus_client as prom
import requests


def readNewFile():
    file_time = 0
    file_sum = 0
    file_n = 0
    file_new = open("/app/new.log", "r")
    for file_line in file_new:
        file_data = file_line.split(" ")
        file_time = float(file_data[1])

        file_sum = file_sum + file_time
        file_n = file_n + 1

    file_new.close()
    if file_n == 0:
        file_avg = 0
    else:
        file_avg = file_sum / file_n
    return file_avg


def checkFirstLine():
    flag = 0
    file_new = open("/app/new.log", "r")
    file_old = open("/app/old.log", "r")
    for line1 in file_new:
        for line2 in file_old:
            if line1 == line2:
                flag = 1
                break
            else:
                flag = 0
                break
    file_new.close()
    file_old.close()
    return flag


def diffFile():
    old = set((line.strip() for line in open("/app/old.log")))
    new = set((line.strip() for line in open("/app/new.log")))

    file_sum = 0
    file_n = 0

    for line in new:
        if line not in old:
            file_data = line.split(" ")
            file_time = float(file_data[1])

            file_sum = file_sum + file_time
            file_n = file_n + 1

    if file_n == 0:
        file_avg = 0
    else:
        file_avg = file_sum / file_n
    return file_avg


if __name__ == "__main__":

    active_conn = prom.Gauge(
        "konghq_active", "Gauge untuk mendapatkan jumlah active connection")
    # accept_conn = prom.Gauge('konghq_accept', 'Counter untuk mendapatkan total accepted connection')
    # handle_conn = prom.Gauge('konghq_handle', 'Counter untuk mendapatkan total hundled connection')
    # request_conn = prom.Gauge('konghq_request', 'Counter untuk mendapatkan total client request')
    accept_conn = prom.Counter(
        "konghq_accept", "Counter untuk mendapatkan total accepted connection")
    handle_conn = prom.Counter(
        "konghq_handle", "Counter untuk mendapatkan total hundled connection")
    request_conn = prom.Counter(
        "konghq_request", "Counter untuk mendapatkan total client request")
    read_conn = prom.Gauge(
        "konghq_reading", "Gauge untuk mendapatkan jumlah reading connection")
    write_conn = prom.Gauge(
        "konghq_writing", "Gauge untuk mendapatkan jumlah writing connection")
    wait_conn = prom.Gauge(
        "konghq_waiting", "Gauge untuk mendapatkan jumlah waiting connection")

    rtime_desc = prom.Gauge(
        "konghq_rtime", "Gauge untuk mendapatkan rata-rata rtime tiap 1 detik")

    prom.start_http_server(8888)
    url = "http://127.0.0.1:8001/nginx_status"
    # url= "https://schematics.its.ac.id/server_stats"

    file_flag = 1
    while True:
        try:
            rtime_value = 0
            if os.path.exists("/cuslog/custom_nginx.log"):
                if file_flag == 1:
                    shutil.copyfile("/cuslog/custom_nginx.log", "/app/new.log")
                    rtime_value = readNewFile()
                    file_flag = 0
                else:
                    shutil.copyfile("/cuslog/custom_nginx.log", "/app/new.log")
                    same_line = checkFirstLine()
                    if same_line == 1:
                        rtime_value = diffFile()
                    else:
                        rtime_value = readNewFile()

                shutil.move("/app/new.log", "/app/old.log")

            r = requests.get(url)
            data = r.text.split(" ")
            active_value = int(data[2])
            accept_value = int(data[7])
            handle_value = int(data[8])
            request_value = int(data[9])
            read_value = int(data[11])
            write_value = int(data[13])
            wait_value = int(data[15])

            active_conn.set(active_value)
            accept_conn.inc(accept_value)
            handle_conn.inc(handle_value)
            request_conn.inc(request_value)
            # accept_conn.set(accept_value)
            # handle_conn.set(handle_value)
            # request_conn.set(request_value)
            read_conn.set(read_value)
            write_conn.set(write_value)
            wait_conn.set(wait_value)

            rtime_desc.set(rtime_value)

        except:
            pass

        time.sleep(1)
