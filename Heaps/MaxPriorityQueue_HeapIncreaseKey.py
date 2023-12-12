
from util import Parent

def heap_increase_key(A, i, key):

    """This function change the key at index i with the new key key
    
    - Keyword arguments:
        - A -- Array
        - i -- index of the key which we want to change
        - key -- new value of the key
    """
    
    if key < A[i]:
        raise Exception("The new key is smaller than the current key")
    
    A[i] = key

    while i > 0 and A[Parent(i)] < A[i]:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)

    return A

if __name__ == "__main__":

    Arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    print(heap_increase_key(Arr, 8, 11))
