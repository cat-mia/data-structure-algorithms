# 拿一张纸条面对自己，
# 对折N次再展开，注意不要颠倒方向
# 从上到下，打印所有痕迹是凹还是凸

def print_folds(level, n, down):
    if level == n+1:
        return
    print_folds(level+1, n, True)
    if down:
        print("凹")
    else:
        print("凸")
    print_folds(level+1,n, False)

print_folds(1,3, True)