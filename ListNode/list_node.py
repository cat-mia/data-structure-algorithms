class ListNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_node(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
    
    def insert(self, nums):
        for n in nums:
            self.insert_node(n)
    
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
            # self.head.pre = tmp #双向
            pre = self.head
            self.head = tmp
        self.head = pre
    
    def remove_value(self, val):
        while self.head is not None:
            if self.head.value == val:
                self.head = self.head.next
            else:
                break
        pre = self.head
        cur = self.head.next
        while cur is not None:
            # self.output()
            if cur.value != val:
                pre = pre.next
                cur = cur.next
            else:
                pre.next = cur.next
                cur = cur.next
        return None

# l = LinkedList()
# l.insert([3,3,1,2,3,4,5,3,3,6])
# l.output()
# l.reverse()
# l.output()
# l.remove_value(3)
# l.output()