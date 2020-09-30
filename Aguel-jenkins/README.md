# Simple Jenkins Configuration 
Jenkins for clone build and push image to registry

## Requirements
1. Docker
2. Make sure You have Dockerfile in your github repository for building the image

## Credentials Configuration
To login docker registry and github, we need to input our login credentials into the jenkins  
1. In the menu click 'People'
2. Choose account with admin privilege
3. Click 'Credentials' on the sidebar
4. Choose the scope (If you don't know just Stores from parent and click 'Jenkins')
5. Click 'Global credentials (unrestricted)'
6. Click 'Add Credentials'
7. Kind is up to you but the simple one is 'Username with password'
8. Input username and password
9. You can leave the ID as it is (will be generated random ID) or you can specificaly input the ID with anything you want
10. In the Description just input what account it is so you know where credential belong to
11. Change credentialRegistry and credentialsGit in the Jenkinsfile with your credential ID

## How to create Jenkins Job
1. Install jenkins
```bash
#Create network
$ docker network create jenkins

#Create volume for cert and data
$ docker volume create jenkins-docker-certs
$ docker volume create jenkins-data

##Install docker bind to run docker command inside the jenkins
$ docker container run \
  --name jenkins-docker \
  --rm \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind

## Install Jenkins
$ docker container run \
  --name jenkins-blueocean \
  --rm \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  jenkinsci/blueocean
```
2. Open 127.0.0.1:8080 and there will appear a form to input admin password. Use this command to get admin password and input the result to the form.
```bash
$ docker exec -it jenkins-blueocean /bin/cat /var/jenkins_home/secrets/initialAdminPassword
```
3. To create new job follow these steps
```
Click 'New Item' → Enter the job name → Chose 'Pipeline' and click 'OK' →
Input the Description → Click 'pipeline' on the menu bar →
Copy Jenkinsfile's content into the pipeline's textbox → Click 'Save'
```
4. To test click Build now.


