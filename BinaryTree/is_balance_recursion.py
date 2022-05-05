# 二叉树的递归序，每个节点回访问3次
# 递归的时间复杂度是O(N)
# 递归可以解决大部分树的dp问题
# 需要从左右要什么信息？
# 拿到左右信息之后，如何在root合并


# 给定一棵树，判断是否是平衡二叉树: 左右高度差小于1，每颗子树都平衡
# 需要从左右树要什么信息？高度多少？是否平衡
def is_balance(root):
    ans, _ = get_info(root)
    return ans

def get_info(root):
    if root is None:
        return True, 0
    l_balance, left_h = get_info(root.left)
    r_balance, right_h = get_info(root.right)
    return (l_balance and r_balance and abs(right_h-left_h)<= 1), max(left_h,right_h)+1