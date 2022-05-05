# 一个会议室，n个活动，每个活动有开始时间和结束时间
# 返回会议室最多能办多少场活动

# 最先安排最早结束的活动

def max_activity(time_arr):
    time_arr.sort(key=lambda x:x[1])
    ans = 0
    cur_t = 0
    for t in time_arr:
        if t[0] >= cur_t:
            ans += 1
            cur_t = t[1]
    return ans