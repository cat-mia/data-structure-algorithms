from list_node import LinkedList, ListNode

# 奇数节点返回中点
# 偶数节点放回上中点
def mid_point(head):
    if head is None or head.next is None or head.next.next is None:
        return head
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


l = LinkedList()
l.insert([1,3,2,3,4,5,3,6,7])
l.output()
l.reverse()
l.output()
print(mid_point(l.head).value)