def binary_search(array, target, start, end):
    array = sorted(array)
    if start > end or len(array) == 0:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)

arr = list(map(int, input().split()))
target = int(input("please enter the number you looking for: "))
start = 0
end = len(arr) - 1
print(binary_search(arr, target, start, end))
