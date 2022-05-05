from binary_tree import Tree
from queue import Queue
# 统计树的最大宽度
# 按层遍历，用队列

def bfs(root):
    q = Queue()
    q.put(root)
    while not q.empty():
        cur = q.get()
        print(cur.val)
        if cur.left is not None:
            q.put(cur.left)
        if cur.right is not None:
            q.put(cur.right)

def max_width_with_map(root):
    # use hash map to save each node's level
    level_map = {}
    q = Queue()
    q.put(root)
    cur_level = 1
    cur_level_nodes = 0
    max_w = 0
    level_map[root] = 1
    while not q.empty():
        cur = q.get()
        if cur.left is not None:
            q.put(cur.left)
            level_map[cur.left] = level_map[cur] +1
        if cur.right is not None:
            q.put(cur.right)
            level_map[cur.right] = level_map[cur] + 1

        if level_map[cur] != cur_level:
            # 每到新一层，更新上一层宽度
            max_w = max(max_w, cur_level_nodes)
            cur_level += 1
            cur_level_nodes = 1
        else:
            cur_level_nodes += 1
    # 更新最后一层宽度
    max_w = max(max_w, cur_level_nodes)
    return max_w

# ！！！！！！！！！！！！！！！
# 设置flag变量，标记层的结束
def max_width(root):
    # use curEnd and nextEnd to record level change
    q = Queue()
    q.put(root)
    cur_end = root
    next_end = None
    cur_level_nodes = 0
    max_w = 0
    while not q.empty():
        cur = q.get()
        if cur.left is not None:
            q.put(cur.left)
            next_end = cur.left
        if cur.right is not None:
            q.put(cur.right)
            next_end = cur.right
        cur_level_nodes += 1
        if cur == cur_end:
            # 每结束新一层，更新当前层宽度
            max_w = max(max_w, cur_level_nodes)
            cur_level_nodes = 0
            cur_end = next_end
    return max_w
            


t = Tree()
t.build([1,2,3,4,5,6,7])
# bfs(t.root)
max_width(t.root)