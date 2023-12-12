from util import Parent, LeftChild, RightChild

def max_heapify(A, n, i):

    """To maintain the max-heap property, we can call this function max_heapify

    - Arguments:
        - A: Array
        - n: heap-size
        - i: index at which the max-heap property is violeted
    """
    largest = i
    l = LeftChild(i) # Index of left child
    r = RightChild(i) # Index of right child

    # finding the largest of three: parent, left child, and right child
    if l <= (n-1) and A[i] < A[l]:
        largest = l

    if r <= (n-1) and A[r] > A[largest]:
        largest = r

    # if parent is not largest of three then replacing the parent with the largest child
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)
    

if __name__ == "__main__":

    arr = [16, 3, 10, 14, 7, 9, 3, 2, 8, 1] # here 3 is violating the max-heap property
    max_heapify(arr, 10, 1) # index of 3 is 1
    print(arr)





