# cur_w: 之前做的选择已经达到的weight
# rest: 背包剩余容量
# return index往后的总价值最大多少
def process(w, v, index, rest):
    if rest < 0:
        return -1
    
    if index == len(w):
        # index 往后没价值了
        return 0
    
    p1 = process(w, v, index +1, rest) # 不要index
    p2 = process(w, v, index +1, rest - w[index])

    if p2 != -1:
        p2 = v[index] + p2
    return max(p1, p2)

print(process([5,5,3], [1,2,9], 0, 10))

# 暴搜改2D-dynamic programming
# 有重复计算的问题才有必要改dp
# dp[index][rest]
# 0~index已经放好
# index 0~N  rest 0~capacity
# w weight  v value
def dp_knapsack(w, v, capacity):
    dp = [[0]*(capacity+1) for _ in range(len(w)+1)]
    # dp[n][...] = 0
    for index in range(len(w)-2,-1,-1):
        for rest in range(0, capacity+1):
            if rest-w[index+1] >= 0:
                dp[index][rest] = max(dp[index+1][rest], dp[index+1][rest-w[index+1]]+v[index+1])
            else:
                dp[index][rest] = dp[index+1][rest]
    print(dp)
    return dp[0][capacity]

print(dp_knapsack([5,5,3], [1,2,9], 10))