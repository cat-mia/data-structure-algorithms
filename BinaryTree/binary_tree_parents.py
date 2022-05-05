from queue import Queue

from binary_tree import Tree


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class TreeParents(Tree):
    def __init__(self) -> None:
        super().__init__()

    def build(self, nums):
        # 用队列建立完全二叉树
        if len(nums) == 0:
            return
        q = Queue()
        self.root = TreeNode(nums[0])
        i = 1
        q.put(self.root)
        while q and i < len(nums):
            root = q.queue[0]
            node = TreeNode(nums[i])
            i += 1
            if root.left is None:
                root.left = node
                node.parent = root
            elif root.right is None:
                root.right = node
                node.parent = root
            else:
                q.get()
                q.put(root.left)
                q.put(root.right)
                i -= 1
    
   