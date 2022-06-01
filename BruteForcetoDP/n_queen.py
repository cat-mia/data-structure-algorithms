# 注意对角线是两个方向上的
# 2*2格子，无解，一定同行/列/对角线
# 3*3格子，无解
# 4*4格子，有解

# 每行放一个，保证行上不打架
# DFS + 回溯

# 0~i-1 已经摆放好，记录在record里
# return 合理的摆放方法
def process(i, record, n):
    if i== n:
        return 1 # record记录的这一种
    ans = 0
    for j in range(n):
        if is_valid(record, i, j):
            record[i] = j
            ans += process(i+1, record, n)
            # 不用还原现场，直接改值
    return ans

def is_valid(record, i, j):
    # 必然不共行
    # 共列：record[i] == record[j]
    # 共斜线：abs(行1-行2) == abs(列1-列2)
    for k in range(i):
        # 只到第i行
        if j == record[k] or abs(record[k] - j) == abs(k - i):
            return False
    return True


n = 10
record = [0]*n
print(process(0, record, n))

# 常数优化，位运算
