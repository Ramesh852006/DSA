#Bubble Sort
def BubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
          
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting:", arr)
BubbleSort(arr)
print("After sorting:", arr)
