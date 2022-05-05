# 左子树都比root小，右子树都比root大，二叉搜索树

# 给定root，找最大的二叉搜索子树的root节点
# 若没有，返回空

# 求一棵树上最远的2个点之间的距离
# 需要从左右要什么信息？
#   左右是否是二叉搜索树，如果是，返回子树节点，和二叉搜索树的节点个数 l_size, r_size, r_min和l_max
# 1)与root有关的可能性：
#   二叉搜索树通过root，返回ans为root，更新size=l_size+r_size+1
#   l_max < root, root < r_min
# 2)与root无关的可能性:
#   二叉搜索树不通过root，返回ans为更大的子树，size=max(l_size,r_size)
# 左右合并到一起，求max和min，size，是否是bst


def process(root):
    if root is None:
        return float("inf"),float("-inf"),0,True, 
    max_l, min_l, size_l, bst_l = process(root.left)
    max_r, min_r, size_r, bst_r = process(root.right)
    min = min(min_l, min_r)
    max = max(max_l,max_r)
    size = max(size_l, size_r)
    bst = False
    if bst_l and bst_r and max_l < root.val and min_r > root.val:
        size = size_l+size_r+1
        bst = True
    return max, min, size, bst