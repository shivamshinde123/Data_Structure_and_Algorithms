

from MaxHeapify import max_heapify


def build_heapsort(A):

    """This function will sort the elements of an array using heap data structure properties.
    Note that in order for heapsort to work, the arr should follow heap properties i.e. max-heap in this case
    
    - Keyword arguments:
        - A -- array

    Return: A array after sorting
    """
    

    n = len(A)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, i, 0)

    return A


if __name__ == "__main__":

    arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] # always give the array that follows the heap property,, in this case a max-heap property
    sorted_arr = build_heapsort(arr)
    print(sorted_arr)