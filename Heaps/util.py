import math

"""Following function are utility functions needed in order to do operations on heaps"""

def Parent(i):

    """This function is used to find the parent of the element present at the index i
    """
    return math.floor((i+1)/2) - 1

def LeftChild(i):

    """This function is used to find the left child of the element present at the index i"""

    return  2*i + 1 # 2*(i+1) - 1

def RightChild(i):

    """This function is used to find the right child of the element present at the index i"""

    return  2*i + 2 # (2*(i+1)+1) - 1


if __name__ == "__main__":

    print("Parent of value at index 4 resides at index : ", Parent(4))
    print("Left Child of value at index 4 resides at index : ", LeftChild(4))
    print("Right Child of value at index 4 resides at index : ", RightChild(4))