from binary_tree_parents import TreeParents
# 一个有parent节点的树
# 给定node，不给root节点
# 怎么找node后继or前驱: 在中序遍历中一个节点的后一个or前一个节点
# 笔试：从node出发找到root，中序遍历，输出前后即可
# 面试：需要判断node是否有right，如果有，输出right子树的最左节点
# 否则，沿着parent往上走，直到parent为左子树为止
# 因为一个有左子树的节点的前驱一定是其左子树上最右的节点

def most_left(node):
    while node.left is not None:
        node = node.left
    return node

def most_right(node):
    while node.right is not None:
        node = node.right
    return node

def find_successor(node):
    if node is None:
        return None
    if node.right is not None:
        return most_left(node.right)
    cur = node
    while cur.parent is not None:
        if cur.parent.left == cur:
            break
        cur = cur.parent
    return cur.parent

def find_pre(node):
    if node is None:
        return None
    if node.left is not None:
        return most_right(node.left)
    cur = node
    while cur.parent is not None:
        if cur.parent.right == cur:
            break
        cur = cur.parent
    return cur.parent

t = TreeParents()
t.build([1,2,3,4,5,6,7])
t.output()
print(find_successor(t.root.right.left).val)
print(find_pre(t.root.right.left).val)