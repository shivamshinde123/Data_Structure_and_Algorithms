

from MaxPriorityQueue_HeapIncreaseKey import heap_increase_key


def max_heap_insert(A, key):

    """This function is used to insert a new key into the max-priority queue
    
    - Keyword arguments:
        - A -- max-priority queue into which we want to add new key
        - key -- key that we want to add into max-priority key
    Return: updated max-priority queue
    """

    A.append(float("-inf"))
    return heap_increase_key(A, len(A)-1, key)



if __name__ == "__main__":

    Arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    print(max_heap_insert(Arr, 50))