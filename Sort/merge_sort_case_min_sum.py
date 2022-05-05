# 最小和
# [1,3,4,2,5]
# 1左边比1小的 None
# 3左边比3小的 1
# 4左边比4小的 1+3
# 2左边比2小的 1
# 5左边比5小的 1+3+4+2

def merge(arr, L, M, R, ans):
    merged_arr = []
    p1 = 0
    p2 = 0
    arr1 = arr[L:M+1]
    arr2 = arr[M+1:R+1]
    # merge 2 sorted array
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            ans += arr1[p1] * (len(arr2)-p2)
            merged_arr.append(arr1[p1])
            p1 += 1
        else:
            # 相等则优先拷贝arr2, 不产生小和
            merged_arr.append(arr2[p2])
            p2 += 1
    # p1越界 or p2越界 or 同时越界
    if p1 < len(arr1):
        merged_arr += arr1[p1:]
    if p2 < len(arr2):
        merged_arr += arr2[p2:]
    
    arr[L:R+1] = merged_arr
    return ans

def min_sum(nums):
    ans = 0
    ans = merge_sort_recursion(nums, 0, len(nums)-1, ans)
    return ans

def merge_sort_recursion(nums, left, right, ans):
    if left == right:
        return ans
    mid = int(left + (right-left)/2)
    ans = merge_sort_recursion(nums, left, mid, ans)
    ans = merge_sort_recursion(nums, mid+1, right, ans)
    return merge(nums, left, mid, right, ans)

nums = [1,3,4,2,5]
# merge_sort_recursion(nums, 0, len(nums)-1)
print(min_sum(nums)) # 16