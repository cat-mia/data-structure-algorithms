# 2链表可能有环，也可能无环
# 找到第一个相交的node
# 不相交返回None

# 一个node只有唯一的next，故入环后不能出环
# 所以一个有环链表，不可能和无环链表相交

# 情况1: 2无环链表相交
# 不想测了，没测
'''
X -> X ->X -> X -> X
              |
         X -> X
链表1四步走到tail，链表2三步走到tail
4-3 = 1
再走一次，链表1比链表2先走1步
相遇的点就是解
'''
# 情况2: 2有环链表相交
# 可能相交于环中同一点，也可能相交于环中不同点，也可能相较于环外一个点
def encounter_node(h1, h2):
    n1 = circle_node(h1)
    n2 = circle_node(h2)
    if n1 is None and n2 is None:
        cur1 = h1
        cur2 = h2
        step_gap = 0
        while cur1 is not None and cur2 is not None:
            if cur1 == cur2:
                # l1 l2长度一样
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        cur = cur2 if cur1 is None else cur1
        long_h = h2 if cur1 is None else h1
        short_h = h1 if cur1 is None else h2
        while cur is not None:
            cur = cur.next
            step_gap += 1
        while step_gap > 0:
            step_gap -= 1
            long_h = long_h.next
        while long_h != short_h:
            long_h = long_h.next
            short_h = short_h.next
        return long_h
    elif n1 is not None and n2 is not None:
        if n1 == n2:
            # 类似无环链表相交问题, tail改成入环node
            cur1 = h1
            cur2 = h2
            step_gap = 0
            while cur1 is not n1 and cur2 is not n2:
                if cur1 == cur2:
                    # l1 l2长度一样
                    return cur1
                cur1 = cur1.next
                cur2 = cur2.next
            cur = cur2 if cur1 is None else cur1
            long_h = h2 if cur1 is None else h1
            short_h = h1 if cur1 is None else h2
            while cur is not None:
                cur = cur.next
                step_gap += 1
            while step_gap > 0:
                step_gap -= 1
                long_h = long_h.next
            while long_h != short_h:
                long_h = long_h.next
                short_h = short_h.next
            return long_h
        cur1 = n1
        while cur1.next != n1:
            if cur1 == n2:
                return n1 # or n2, both right
        return None
    else:
        return None


# 判断链表是否有环，返回入环node
# 快慢指针，相遇则有环
# 相遇后slow不动，fast移到head
# fast和slow都一次一步，再次相遇就是入环node
def circle_node(head):
    # at least 3 nodes to circle
    if head is None or head.next is None or head.next.next is None:
        return head
    slow = head
    fast = head
    circle = False
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            circle = True
            break
    if circle:
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
    return None

