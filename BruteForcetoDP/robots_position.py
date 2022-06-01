# N positions marked as 1 to N
# initial pos of the robot is M
# 1只能往右，N只能往左
# return走K步，来到P位置的方法数

# cur: 当前位置
# rest: 还剩多少步没走
# return 方法数

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