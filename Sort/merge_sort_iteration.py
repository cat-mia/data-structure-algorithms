def merge(arr, L, M, R):
    merged_arr = []
    p1 = 0
    p2 = 0
    arr1 = arr[L:M+1]
    arr2 = arr[M+1:R+1]
    # merge 2 sorted array
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged_arr.append(arr1[p1])
            p1 += 1
        else:
            merged_arr.append(arr2[p2])
            p2 += 1
    # p1越界 or p2越界 or 同时越界
    if p1 < len(arr1):
        merged_arr += arr1[p1:]
    if p2 < len(arr2):
        merged_arr += arr2[p2:]
    
    arr[L:R+1] = merged_arr

def merge_sort(nums):
    merge_size = 1
    N = len(nums)
    while True:
        left = 0
        while left < N:
            mid = left + merge_size - 1
            right = min(mid + merge_size, N-1)
            merge(nums, left, mid, right)
            left = right + 1
        if merge_size > N/2:
            break
        merge_size *= 2

def merge_sort_recursion(nums, left, right):
    if left == right:
        return
    mid = int(left + (right-left)/2)
    merge_sort_recursion(nums, left, mid)
    merge_sort_recursion(nums, mid+1, right)
    merge(nums, left, mid, right)

'''
递归自顶向下 O(N*logN)
迭代自底向上 O(N*logN)
'''
nums = [9,7,6,8,2,4,1,0,5]
# merge_sort_recursion(nums, 0, len(nums)-1)
merge_sort(nums)
print(nums)