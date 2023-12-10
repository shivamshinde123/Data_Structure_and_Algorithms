
def merge_two_sorted_arrays(a, b):
    sorted_array = list()
    len_a = len(a)
    len_b = len(b)
    i = j =0

    while (i < len_a and j < len_b):
        if a[i] <= b[j]:
            sorted_array.append(a[i])
            i += 1
        else:
            sorted_array.append(b[j])
            j += 1

    while (i < len_a):
        sorted_array.append(a[i])
        i += 1

    while (j < len_b):
        sorted_array.append(b[j])
        j += 1

    return sorted_array


def merge_sort(unsorted_arr):

    if len(unsorted_arr) <= 1:
        return unsorted_arr

    mid = len(unsorted_arr) // 2

    ## recursive step
    left = unsorted_arr[:mid]
    right = unsorted_arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_arrays(left, right)



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
        sorted_elements = merge_sort(array)
        print(sorted_elements)