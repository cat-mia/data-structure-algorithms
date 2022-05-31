# cur_w: 之前做的选择已经达到的weight
# rest: 背包剩余容量
# return index往后的总价值最大多少
def process(w, v, index, rest):
    if rest < 0:
        return -1
    
    if index == len(w):
        # index 往后没价值了
        return 0
    
    p1 = process(w, v, index +1, rest) # 不要index
    p2 = process(w, v, index +1, rest - w[index])

    if p2 != -1:
        p2 = v[index] + p2
    return max(p1, p2)

print(process([5,5,3], [1,2,9], 0, 10))

# def dp_knapsack(w, v, capacity):
