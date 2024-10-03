#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [35,25,36,12,28,10]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)