

def binarySearch(lst, num):

    """Implmentation of binary search algorithm
    
    Keyword arguments:
    - lst -- The list that we need to traverse   (For binary search to work, lst should be sorted in non-decreasing order)
    - num -- the num that we need to search inside lst  
    
    Return: index of num in lst  
    """

    left_index = 0
    right_index = len(lst) - 1
    mid_index = 0

    while (left_index <= right_index):
        mid_index = (left_index + right_index) // 2
        mid_num = lst[mid_index]

        if num == mid_num:
            return mid_index
        
        if num > mid_num:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1 


def binarySearchRecursiveApproach(lst, num, left_index, right_index):

    """Implmentation of binary search algorithm
    
    Keyword arguments:
    - lst -- The list that we need to traverse   
    - num -- the num that we need to search inside lst  
    
    Return: index of num in lst  
    """

    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_num = lst[mid_index]

    if num == mid_num:
        return mid_index
    
    if num > mid_num:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binarySearchRecursiveApproach(lst, num, left_index, right_index)




if __name__ == "__main__":
    
    number_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 24


    print("Searching using while loop binary search implementation: ")
    index = binarySearch(number_list, number_to_find)

    if index == -1:
        print(f"The number {number_to_find} is not present in the list {number_list}.\n")
    else:
        print(f"The number {number_to_find} was found out at index {index}.\n")


    print("Searching using recursive approach to binary search: ")
    index = binarySearchRecursiveApproach(number_list, number_to_find, 0, len(number_list) -1)

    if index == -1:
        print(f"The number {number_to_find} is not present in the list {number_list}.\n")
    else:
        print(f"The number {number_to_find} was found out at index {index}.\n")