# Input n: level of tower
# Output: 需要移动多少次，一次只能一个盘子

def hanoi(n):
    if n == 1:
        return n
    # 先把n-1个盘子移走 hanoi(n-1)
    # 再移第n个（最大的） 1
    # 再把n-1个移到第n个上 hanoi(n-1)
    return 1+2*hanoi(n-1)

def hanoi_method(n, from_, other, to):
    if n == 1:
        print("move {} from {} to {}".format(n, from_, to))
        return
    hanoi_method(n-1, from_, to, other)
    print("move {} from {} to {}".format(n, from_, to))
    hanoi_method(n-1, other, from_, to)


hanoi_method(3, "left", "mid", "right")
print(hanoi(3))
