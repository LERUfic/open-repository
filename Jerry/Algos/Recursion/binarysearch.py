def binary_search(target_list, target, first_index, last_index):
    
    if(first_index > last_index):
        return -1
    else:
        middle_index = first_index + ((last_index - first_index) // 2)

        if target_list[middle_index] > target:
            return binary_search(target_list, target, first_index, middle_index - 1)
        elif target_list[middle_index] < target:
            return binary_search(target_list, target, middle_index + 1, last_index)
        else:
            return middle_index

test_list = [2,7,19,34,53,72]
print(binary_search(test_list, 19, 0, len(test_list) - 1))
print(binary_search(test_list, 11, 0, len(test_list) - 1))