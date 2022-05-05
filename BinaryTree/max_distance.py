# 二叉树的递归序，每个节点回访问3次
# 递归的时间复杂度是O(N)
# 递归可以解决大部分树的dp问题
# 需要从左右要什么信息？
# 拿到左右信息之后，如何在root合并?
# 1)与root有关的可能性
# 2)与root无关的可能性

# 求一棵树上最远的2个点之间的距离
# 需要从左右要什么信息？左右树高度，左右树最远距离
# 1)与root有关的可能性：最长路径通过root，1+max(height(root.left),height(root.right))
# 2)与root无关的可能性: 最长路径不通过root，max(max_dist(root.left),max_dist(root.right))
# 合并，max(1),2))

def max_dist(root):
    _, dist = process(root)
    return dist

def process(root):
    if root is None:
        return 0, 0
    l_height, l_dist = process(root.left)
    r_height, r_dist = process(root.right)
    height = max(l_height, r_height)+1
    dist = max(l_dist, r_dist, 1+l_height+r_height)
    return height, dist