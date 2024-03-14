def bubble_sort(arr):
    # 获取数组的长度
    n = len(arr)
    
    # 遍历数组
    for i in range(n):
        # 遍历数组中的每一行
        for j in range(0, n-i-1):
            # 如果当前行大于下一行，则交换位置
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

print()

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(arr, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")