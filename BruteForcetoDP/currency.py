# arr[5,2,50]面值的货币
# aim 100，凑出100元
# 有多少种方式？

# 用arr[i]及以后的所有元素，凑rest

def process(i, rest, arr):
    if len(arr) == 0 or rest < 0:
        return 0
    if i == len(arr):
        return 1 if rest == 0 else 0
    r = rest
    ans = 0
    k = 0 # 多少张此时的货币
    while r >= 0 and arr[i]*k <= rest:
        ans += process(i+1, rest-arr[i]*k, arr)
        k += 1
    return ans

print(process(0, 100, [5,2,50]))

# 暴力递归加dp缓存
def dp_cache(i, rest, arr, dp):
    if dp[i][rest] != -1:
        return dp[i][rest]
    if len(arr) == 0 or rest < 0:
        dp[i][rest] = 0
        return dp[i][rest]
    if i == len(arr):
        dp[i][rest] =  1 if rest == 0 else 0
        return dp[i][rest]
    ans = 0
    k = 0 # 多少张此时的货币
    while arr[i]*k <= rest:
        ans += process(i+1, rest-arr[i]*k, arr)
        k += 1
    dp[i][rest] = ans
    return ans

arr = [5,2,50]
aim = 100
dp = [[-1]*(aim+1) for _ in range(len(arr))] # -1表示没有计算过
print(dp_cache(0, aim, arr, dp))


# 改经典dp
def dp_func(arr, aim):
    dp = [[-1]*(aim+1) for _ in range(len(arr)+1)] # -1表示没有计算过
    for i in range(aim+1):
        dp[len(arr)][i] = 0
    for i in range(len(arr)+1):
        dp[i][0] = 1
    for i in range(len(arr)-1,-1,-1):
        for rest in range(aim+1):
            ans = 0
            k = 0 # 多少张此时的货币
            # 这里的枚举行为可以优化
            # while arr[i]*k <= rest:
            #     ans += dp[i+1][rest-arr[i]*k]
            #     k += 1
            ans = dp[i+1][rest]
            if rest - arr[i] >= 0:
                ans += dp[i][rest-arr[i]] 
            dp[i][rest] = ans
    # print(dp)
    return dp[0][aim]

print(dp_func(arr, aim))