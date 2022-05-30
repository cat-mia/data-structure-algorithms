

def pop_reverse(s):
    result = s.pop()
    # 对长度为1的栈，弹出其唯一元素并返回
    if len(s) == 0:
        return result
    # 否则，再弹出一个，赋值给last
    # 将刚弹出的元素再入栈
    # 返回last, pop_reverse最后返回的一定是栈
    last = pop_reverse(s)
    s.append(result)
    return last
    


s = [1,2,3,4]
pop_reverse(s)