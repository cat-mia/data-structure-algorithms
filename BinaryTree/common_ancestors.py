from binary_tree import Tree
# 给定root, node1, node2
# 如何找node12的最近公共祖先

# 需要左右树返回：node1是否在其上，node2是否在其上，如果都在其上，返回common ancestor
# 合并信息：和root有关？最近祖先为root，node1在左数，node2在右树
# 和root无关？node1，node2都在左or都在右，返回左or右。
# 和root无关？node1在，node2不在，返回None，vice versa
def find_ancestor(root, node1, node2):
    _, _, ans = process(root, node1, node2)
    return ans


def process(root, node1, node2):
    if root is None:
        return False, False, None
    if root == node1:
        return True, False, None
    if root == node2:
        return False, True, None
    l_n1, l_n2, l_ancestor = process(root.left, node1, node2)
    r_n1, r_n2, r_ancestor = process(root.right, node1, node2)
    if (l_n1 and r_n2) or (l_n2 and r_n1):
        return True, True, root
    if l_n1 and l_n2:
        return True, True, l_ancestor
    if r_n1 and r_n2:
        return True, True, r_ancestor
    return l_n1 or r_n1, l_n2 or r_n2, None

t = Tree()
t.build([1,2,3,4,5,6,7])
print(find_ancestor(t.root, t.root.left.left, t.root.right.right).val)