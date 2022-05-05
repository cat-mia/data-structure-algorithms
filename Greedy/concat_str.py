# 给定字符串数组[ac,bk,sc,ket]
# 返回随意拼接之后，字典序最小的解 ac,bk,ket,sc

# 反例，单独比较X Y大小不可行
# [ba,b]
# ba,b
# X+Y > Y+X ? X+Y: Y+X



def min_order(strs):
    if len(strs) == 0:
        return "s"
    ans = strs[0]
    for i in range(1,len(strs)):
        cur = strs[i]
        if ans+cur < cur+ans:
            ans += cur
        else:
            ans = cur + ans
    return ans

print(min_order(["ba","b","ac","ca"]))