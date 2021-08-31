def insertion_sort(arr):
    for x in range(1, len(arr)):
        for y in range(0, x):
            print(f"comparing {arr[x]} and {arr[y]}")
            if arr[x] < arr[y]:
                print("applying insertion sort")
                tmp = arr[x]
                for z in range(x, y, -1):
                    arr[z] = arr[z - 1]
                arr[y] = tmp
                print("array is now: ", arr)
    return arr


arr = [1, 5, 3, 2, 0, 8]

print(insertion_sort(arr))