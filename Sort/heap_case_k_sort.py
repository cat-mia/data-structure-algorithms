import imp


'''
给定基本有序的数组
其中每个数离自己正确位置最远为k

用k+1大小的小根堆, 每次弹出最小元素, 放到数组当前首位
O(N*logK)
'''
import heapq

def k_sort(arr, k):
    ans = []
    h = heapq.heapify(arr[:k+1])
    idx = k+1
    while idx < len(arr):
        ans.append(heapq.heappop())
        heapq.heappush(h, arr[idx])
        idx += 1