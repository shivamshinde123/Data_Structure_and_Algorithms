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
    

def randomizedQuicksort(arr, p, r):
    if p < r:
        q = randomizedPartition(arr, p, r)
        randomizedQuicksort(arr, p, q-1)
        randomizedQuicksort(arr, q+1, r)

if __name__ == "__main__":


    tests = [
        [11, 9, 29, 7, 2, 15, 28], 
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for array in tests:
        randomizedQuicksort(array, 0, len(array)-1)
        print(array)


    