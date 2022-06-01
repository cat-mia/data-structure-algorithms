# 111 -> AAA'1 1 1' or KA'11 1' or AK'1 11'
# 给字符串，返回一共有多少种构成

# 0~i-1已经转化完了
def process(str, i):
    if i == len(str):
        # a valid solution if found
        return 1
    # 1 - A
    # 0不对应任何的
    if str[i] == '0':
        return 0

    if str[i] == '1':
        res = process(str, i+1) # 转a
        if i+1 < len(str):
            res += process(str, i+2) # 转k+
        return res

    if str[i] == '2':
        res = process(str, i+1) # 转a
        if i+1 < len(str) and str[i+1] <= '6':
            res += process(str, i+2) # 转k+
        return res
    
    # '3' to '9'
    return process(str, i+1)


s = '111'
print(process(s, 0))

def dp_ways(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [0]*(n+1)
    # i依赖i+1 和 i+2
    dp[n] = 1
    for i in range(n-1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        
        if s[i] == '1':
            dp[i] = dp[i+1]
            if i+1 < len(s):
                dp[i] += dp[i+2]
        
        if s[i] == 2:
            dp[i] = dp[i+1]
            if i+1 < len(s) and s[i+1] <= '6':
                dp[i] += dp[i+2]

    return dp[0]

print(dp_ways(s))