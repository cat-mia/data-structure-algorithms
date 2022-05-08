import heapq as hq
# costs[] profits[]: 做第i个项目的成本和收益
# M，初始资金，拿到新收益后可以串行做下一个项目
# K，最多可串行做多少项目

# costs进小根堆
# 从小根堆里解锁所有M可以完成的任务，弹出
# 将任务profits进大根堆
# 在K不超过的情况下，尽量完成大根堆的任务
# 完成一个任务就更新M，继续去小根堆解锁
def add_idx(list):
    ret = []
    for idx,v in enumerate(list):
        ret.append([v,idx])
    return ret

def max_profits(costs, profits, M, K):
    costs_h = add_idx(costs)
    profits_h = []
    hq.heapify(costs_h)
    for i in range(K):
        while len(costs_h)>0:
            # top of min heap
            item = costs_h[0]
            # 剩下的任务M无法完成
            if item[0] > M:
                break
            hq.heappop(costs_h)
            M -= item[0]
            hq.heappush(profits_h,profits[item[1]])
        if len(profits_h) == 0:
            return M
        M += hq.heappop(profits_h)
    
    return M


print(max_profits([1,2],[10,10],2,1))