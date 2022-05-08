import heapq as hq
# python heapq只提供了小根堆
# 如果想用大根堆，可以存相反数，取出时取反即可

# 给定金条[3,5,6]
# 输出最小化切分代价
# 1) 3, 11(花费14) -> 3,5,6(花费11) -> return 25
# 2) 8, 6(花费14) -> 3,5,6(花费8) -> return 22

# huffman tree

def min_cost(arr):
    h = arr
    hq.heapify(arr)
    cost = 0
    # print(hq.nsmallest(len(h),h))
    while len(h) > 1:
        item1 = hq.heappop(h)
        item2 = hq.heappop(h)
        cost += item1 + item2
        hq.heappush(h,item1+item2)
    return cost

print(min_cost([3,5,6]))