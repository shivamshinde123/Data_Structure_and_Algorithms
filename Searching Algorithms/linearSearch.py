
def linearSearch(lst, num):

    """Implmentation of linear search algorithm
    
    Keyword arguments:
    - lst -- The list that we need to traverse   
    - num -- the num that we need to search inside lst  
    
    Return: index of num in lst  
    """

    for index, element in enumerate(lst):
        if element == num:
            return index
        
    return -1
        

if __name__ == "__main__":
    
    number_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    index = linearSearch(number_list, number_to_find)

    if index == -1:
        print(f"The number {number_to_find} is not present in the list {number_list}.")
    else:
        print(f"The number {number_to_find} was found out at index {index}.")

    