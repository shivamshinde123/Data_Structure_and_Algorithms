
from MaxHeapify import max_heapify

def heap_extract_max(A):

    """This function removes and returns the element of max-priority queue with the largest key"""

    n = len(A)

    if n < 1:
        print("Error underflow")

    max = A[0]

    A[0] = A[n-1]
    n -= 1
    max_heapify(A, n, 0)

    return max


if __name__ == "__main__":

    Arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    print(heap_extract_max(Arr))