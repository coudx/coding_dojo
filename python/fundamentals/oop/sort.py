def section_sort(arr):
    for x in range(len(arr)):
        if x == len(arr) - 1: break
        for y in range(x + 1, len(arr)):
            print("Comparing {} and {}".format(arr[x], arr[y]))
            if arr[x] > arr[y]:
                tmp = arr[x]
                arr[x] = arr[y]
                arr[y] = tmp
                print("Swapped")
                print("Array is now: ", arr)
    return arr


arr = [1, 5, 3, 2, 0, 8]

section_sort(arr)