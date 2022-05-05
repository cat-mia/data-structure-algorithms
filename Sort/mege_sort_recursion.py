# recursion
def merge_sort(nums, left, right):
    if left == right:
        return [nums[left]]
    mid = int(left + (right-left)/2)
    arr1 = merge_sort(nums, left, mid)
    arr2 = merge_sort(nums, mid+1, right)
    return merge(arr1, arr2)

def merge(arr1, arr2):
    merged_arr = []
    p1 = 0
    p2 = 0
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
    return merged_arr

nums = [9,7,6,8,2,4,1,0,5]
print(merge_sort(nums, 0, len(nums)-1))