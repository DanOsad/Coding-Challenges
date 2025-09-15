
def binary_search(arr, target):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (hi + lo) // 2
        # print(hi, lo, mid)
        if target > arr[mid]:
            lo = mid + 1
        else:
            hi = mid
        if hi == lo and arr[mid] == target:
            return mid
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
target = 3

index = binary_search(arr, target)
print(index)