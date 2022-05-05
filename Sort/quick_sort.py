# arr:[5,3,4,2,3,4,1]
# num:3
# 小于等于区右边界idx = -1
# cur->5 > 3, move cur
# cur->3 <= 3, swap(arr[cur],arr[idx+1]), cur += 1, idx += 1

# arr:[5,3,4,2,3,4,1]
# num:3
# + 小于区，等于区，大于区
# 小于区右边界less_idx = -1
# 大于区左边界more_idx = len(arr)
# cur->5 > 3, swap(arr[cur], arr[more_idx-1]), more_idx -= 1, DON'T move cur
# cur->3 == 3, cur += 1
# cur->1 < 3, swap(arr[cur],arr[less_idx+1]), cur += 1, less_idx += 1
# 退出条件：cur >= more_idx

# random shuffle arr makes it faster
# arr有序，最差时间O(N^2)
# 平均最差时间O(N*logN)

def partition(arr, num, L, R):
    less_idx = L-1
    more_idx = R+1
    cur = L
    while cur < more_idx:
        if arr[cur] > num:
            arr[cur], arr[more_idx-1] = arr[more_idx-1], arr[cur]
            more_idx -= 1
        elif arr[cur] < num:
            arr[cur],arr[less_idx+1] = arr[less_idx+1],  arr[cur]
            less_idx += 1
            cur += 1
        else:
            cur += 1
    # 等于区左右边界
    return less_idx+1, more_idx-1


def quick_sort(arr):
    if len(arr) <=1:
        return arr
    R = len(arr) - 1
    L = 0
    process(arr, L, R)
    return arr

def process(arr, L, R):
    if L >= R:
        return
    equal_L, equal_R = partition(arr, arr[R], L, R)
    process(arr, L, equal_L-1)
    process(arr, equal_R+1, R)

arr = [5,1,9,3,7,0,-1,4,2,3,4]
# print(partition(arr, 3, 0, len(arr)-1))
# print(arr)
print(quick_sort(arr))