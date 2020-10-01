def binary_search(target_list, target):
    first_index = 0
    last_index = len(target_list) - 1

    while first_index <= last_index:
        index_middle = (first_index+last_index) // 2
        
        if target_list[index_middle] == target:
            return index_middle
        
        if target_list[index_middle] < target:
            first_index = index_middle + 1
        
        else:
            last_index = index_middle - 1

    return -1


test_list = [2,7,19,34,53,72]
print(binary_search(test_list, 19))
print(binary_search(test_list, 11))