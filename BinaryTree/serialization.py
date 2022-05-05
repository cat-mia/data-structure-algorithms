from queue import Queue
from tkinter.messagebox import NO

from bfs_max_width import bfs
from binary_tree import Tree, TreeNode
# 序列化一颗二叉树
# 反序列化：还原一颗二叉树

# 先序递归序列化
def pre_serial(root, q):
    if root is None:
        q.put(None)
        return
    q.put(root.val)
    pre_serial(root.left, q)
    pre_serial(root.right, q)

def pre_deserial(q):
    cur = q.get()
    if cur is None:
        return None
    cur = TreeNode(cur)
    cur.left = pre_deserial(q)
    cur.right = pre_deserial(q)
    return cur

def pre_serial_deserial(root):
    q = Queue()
    pre_serial(root, q)
    print(q.queue)
    root = pre_deserial(q)
    bfs(root)

# 层序遍历序列化反序列化
# 要用两个队列，一个管理bfs，一个记录序列化结果
def bfs_serial(root):
    q = Queue()
    q.put(root)
    serial_q = Queue()
    serial_q.put(root.val)
    while not q.empty():
        cur = q.get()
        if cur.left is not None:
            q.put(cur.left)
        if cur.right is not None:
            q.put(cur.right)
        if cur.left is not None:
            serial_q.put(cur.left.val)
        else:
            serial_q.put(None)
        if cur.right is not None:
            serial_q.put(cur.right.val)
        else:
            serial_q.put(None)
    return serial_q

# 同样要用两个队列
# 一个管理bfs，一个记录序列化结果
def bfs_deserial(serial_q):
    q = Queue()
    root =  TreeNode(serial_q.get())
    q.put(root)
    while not q.empty():
        cur = q.get()
        left = serial_q.get()
        right = serial_q.get()
        cur.left = None if left is None else TreeNode(left)
        cur.right = None if right is None else TreeNode(right)
        if cur.left is not None:
            q.put(cur.left)
        if cur.right is not None:
            q.put(cur.right)
    return root

def bfs_serial_deserial(root):
    q = bfs_serial(root)
    print(q.queue)
    root = bfs_deserial(q)
    bfs(root)

t = Tree()
t.build([1,2,3,4,5,6,7])
bfs_serial_deserial(t.root)

    

