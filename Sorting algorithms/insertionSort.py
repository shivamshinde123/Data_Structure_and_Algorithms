
def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while (j>=0 and elements[j] > anchor):
            elements[j+1] = elements[j]
            j -= 1
        elements[j + 1] = anchor
    return elements


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
        sorted_elements = insertion_sort(array)
        print(sorted_elements)