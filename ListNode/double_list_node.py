class DoubleListNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
        self.pre = None

class DoubleList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        # self.capacity = 10
        # self.cur_size = 0

    def insert_node_from_head(self, val):
        node = DoubleListNode(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node
    
    def insert_node_from_tail(self, val):
        node = DoubleListNode(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node

    def remove_node_from_head(self):
        if self.head is None:
            raise Exception("Double list already empty!")
        val = self.head.value
        self.head = self.head.next
        self.head.pre = None
        return val
    
    def remove_node_from_tail(self):
        if self.tail is None:
            raise Exception("Double list already empty!")
        val = self.tail.value
        self.tail = self.tail.pre
        self.tail.next = None
        return val
    
    def insert(self, nums):
        for n in nums:
            self.insert_node_from_tail(n)
    
    def output(self):
        ans = []
        cur = self.head
        while cur is not None:
            ans.append(cur.value)
            cur = cur.next
        print(ans)
    
    def reverse(self):
        pre = None
        tmp = None
        # 1 2 3 4
        while self.head is not None:
            tmp = self.head.next
            self.head.next = pre
            self.head.pre = tmp #双向
            pre = self.head
            self.head = tmp
        self.head = pre

# l = DoubleList()
# l.insert([1, 2, 3, 4]) # head 1, tail 4
# print(l.head.value)
# print(l.tail.value)
# l.output()