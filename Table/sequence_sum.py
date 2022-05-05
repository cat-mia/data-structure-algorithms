# 打表适用于输入简单：一个数 or char
# 输出也简单的题目

# 一个数是否是连续几个数的和

def is_seq_sum(n):
    if n < 1:
        return False
    for i in range(1, n):
        cur = i
        for j in range(i+1, n):
            cur += j
            if cur == n:
                return True
            if cur > n:
                break
    return False

def print_table():
    for n in range(100):
        print(n, is_seq_sum(n))

# print_table() # 找到规律

def func(n):
    if n<=2: return False
    # 判断是否是2的n次方
    return n & (n-1) != 0

print(func(10))
print(func(16))