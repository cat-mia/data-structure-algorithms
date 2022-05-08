# xxxxx...xxxxx....x
# x表示墙，.表示居民点
# x不能放灯，不需要被照亮，.需要被照亮，能放灯
# i位置的灯能照亮i-1，i，i+1位置

# brute force search 
def process(str,idx,lights):
    pass


def lights_num(str):
    lights = 0
    i = 0
    while i < len(str):
        if str[i] == 'X':
            i += 1
        else:
            if i+1 == len(str):
                lights += 1
                i += 1
            else:
                # .的下一个是X
                if str[i+1] == 'X':
                    lights += 1
                    i += 2
                # .的下一个是.
                else:
                    lights += 1
                    i += 3
    return lights
            
print(lights_num("X.X...X"))