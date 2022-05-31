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