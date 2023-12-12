from MaxHeapify import max_heapify


def build_max_heap(A):

    """This function is used to create a max heap out of the given array"""

    n = len(A) ## we want the heap to have n heap-size
    for i in range(n//2 - 1, -1, -1):
        max_heapify(A, n, i)
    
    return A

if __name__ == "__main__":

    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    new_heap = build_max_heap(arr)
    print(new_heap)



    