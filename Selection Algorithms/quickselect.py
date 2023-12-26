import random

def Partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p,r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def randomizedPartition(arr, p, r):
    i = random.randrange(p,r) ## getting a random index 
    arr[i], arr[r] = arr[r], arr[i] ## swapping the random number at random index with the last number of the list
    return Partition(arr, p, r)


def RandomizedQuickselect(arr, p, r, i):

    """Finding the ith smallest element of the array arr[p...r]"""

    if p == r:
        return arr[p]
    
    if (i > 0 and i <= (r-p+1)): 

        q = randomizedPartition(arr, p, r)
        k = q - p + 1

        if i == k:
            return arr[q]
        elif i < k:
            return RandomizedQuickselect(arr, p, q-1, i)
        else:
            return RandomizedQuickselect(arr, q+1, r, i-k) 
  
    print("Index out of bound")

if __name__ == "__main__":

    arr = [11, 9, 29, 7, 2, 15, 28]
    smallest_number3 = RandomizedQuickselect(arr, 0, len(arr)-1, 4)
    print(smallest_number3)

