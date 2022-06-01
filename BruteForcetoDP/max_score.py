# given arr of positive integers
# player A starts first, the player B
# they take the left-most or right-most num
# return the score(sum num) of the winner

# first 先手
def first(arr, L, R):
    if L== R:
        return arr[L]
    return max(
        arr[L] + second(arr, L+1, R), # 在L+1 ~ R上变后手
        arr[R] + second(arr, L, R-1) # 在L ~ R-1上变后手
        )

# second 后手
def second(arr, L, R):
    if L == R:
        return 0
    return min(
        first(arr, L+1, R), # 先手挑走L
        first(arr, L, R-1) # 先手挑走R，留给后手最小的
        )

def func(arr):
    return max(first(arr, 0, len(arr)-1), second(arr, 0, len(arr)-1))

print(func([100,1,7]))

# 2 nested functions? how
# 2 dp tables
# 有用的只有矩阵上三角
def dp_func(arr):
    n = len(arr)
    dp_s = [[0]*n for _ in range(n)]
    dp_f = [[0]*n for _ in range(n)]
    for i in range(n):
        # dp_s[i][i] = 0  # 可以省略
        dp_f[i][i] = arr[i]
    for i in range(1,n):
        row = 0
        col = i
        while row < n and col < n:
            dp_f[row][col] = max(arr[row] + dp_s[row+1][col], arr[col] + dp_s[row][col-1])
            dp_s[row][col] = min(dp_f[row+1][col], dp_f[row][col-1])
            row += 1
            col += 1
    print(dp_f)
    print(dp_s)
    return max(dp_s[0][n-1], dp_f[0][n-1])

print(dp_func([100,1,7]))