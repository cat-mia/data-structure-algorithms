from queue import Queue

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
        self.root = None
        self.pre = []
        self.mid = []
        self.post = []
    
    def reset(self):
        self.pre = []
        self.mid = []
        self.post = []

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
            elif root.right is None:
                root.right = node
            else:
                q.get()
                q.put(root.left)
                q.put(root.right)
                i -= 1
    
    def pre_order(self, root):
        if root is None:
            return
        self.pre.append(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)
    
    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        self.mid.append(root.val)
        self.in_order(root.right)

    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        self.post.append(root.val)

    def output(self):
        self.reset()
        self.pre_order(self.root)
        self.in_order(self.root)
        self.post_order(self.root)
        print("Recursion")
        print("PreOrder Traverse", self.pre)
        print("MidOrder Traverse", self.mid)
        print("PostOrder Traverse", self.post)
    
    def pre_order_1(self):
        stack = []
        stack.append(self.root)
        # 1.弹出node，print
        # 2.node右节点入栈，node左节点入栈
        while stack:
            node = stack.pop()
            self.pre.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
    
    def post_order_1(self):
        stack = []
        stack.append(self.root)
        # 1.弹出node，print
        # 2.node左节点入栈，node右节点入栈
        # pre order出栈是根 左 右
        # 如果反过来出栈根 右 左，再用一个栈反一下，就是左 右 根，为后序遍历了
        while stack:
            node = stack.pop()
            self.post.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        self.post.reverse()
    
    def in_order_1(self):
        # 1.沿着左节点一路入栈
        # 2.遇到走不下去的情况，出栈打印
        # 3.到右节点上重复操作1。
        stack = []
        cur = self.root
        while stack or cur:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                self.mid.append(cur.val)
                cur = cur.right 

    def output_iteration(self):
        self.reset()
        self.pre_order_1()
        self.in_order_1()
        self.post_order_1()
        print("Iteration")
        print("PreOrder Traverse", self.pre)
        print("MidOrder Traverse", self.mid)
        print("PostOrder Traverse", self.post)


# t = Tree()
# t.build([1,2,3,4,5,6,7])
# t.output()
# t.output_iteration()
