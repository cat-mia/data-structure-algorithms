# N positions marked as 1 to N
# initial pos of the robot is M
# 1只能往右，N只能往左
# return走K步，来到P位置的方法数

# cur: 当前位置
# rest: 还剩多少步没走
# return 方法数

#-----------------暴力递归
def process(N, cur, rest, P):
    if rest == 0:
        return 1 if cur == P else 0
    if cur == N:
        return process(N, cur-1, rest-1, P)
    elif cur == 1:
        return process(N, cur+1, rest-1, P)
    else:
        return process(N, cur-1, rest-1, P) + process(N, cur+1, rest-1, P)

N = 5
M = 2
K = 3
P = 3
print(process(N, M, K, P))

# 有重复计算，f(N, cur, rest, P)相同的cur和rest可能被多次计算了
# 转DP
# cur: 1~N  rest: 0~K
def dp_cache(N, M, K, P):
    dp = [[-1]*(K+1) for _ in range(N+1)] # -1表示没有计算过
    # for i in range(N+1):
    #     for j in range(K+1):
    return walk_dp_cache(N, M, K, P, dp)

#--------------------加缓存
def walk_dp_cache(N, cur, rest, P, dp):
    if dp[cur][rest] != -1:
        return dp[cur][rest]
    if rest == 0:
        dp[cur][rest] = 1 if cur == P else 0
        return dp[cur][rest]
    if cur == N:
        dp[cur][rest] = walk_dp_cache(N, cur-1, rest-1, P, dp)
        return dp[cur][rest]
    elif cur == 1:
        dp[cur][rest] = walk_dp_cache(N, cur+1, rest-1, P, dp)
        return dp[cur][rest]
    else:
        dp[cur][rest] = walk_dp_cache(N, cur-1, rest-1, P, dp) + walk_dp_cache(N, cur+1, rest-1, P, dp)
        return dp[cur][rest]

# Python func arguments: integers & lists
# https://stackoverflow.com/questions/575196/why-can-a-function-modify-some-arguments-as-perceived-by-the-caller-but-not-oth
print(dp_cache(N, M, K, P))


# 不是所有暴力递归都可以改动态规划的
# 是所有动态规划都来自暴力递归

#-------------推导dp依赖的顺序关系
# dp[cur][rest] 依赖 dp[cur-1][rest-1]和dp[cur+1][rest-1]
def dp_walk(N, M, K, P):
    dp = [[0]*(K+1) for _ in range(N+1)]
    # initialize
    for i in range(N+1):
        dp[i][0] = 0
        if i == P:
            dp[i][0] = 1
    for j in range(1, K+1):
        for i in range(1, N+1):
            if i+1 < N+1:
                dp[i][j] = dp[i-1][j-1] + dp[i+1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1]
    print(dp)
    return dp[M][K]

dp_walk(7, 2, 5, 3)