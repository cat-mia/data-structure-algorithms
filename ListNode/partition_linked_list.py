from list_node import LinkedList

# 4->2->3->5->3
# 断开成4->5 2 3->3
# 合并成2->3->3->4->5
def partition_linked(head, val):
    less_h = less_t = equal_h = equal_t = more_h = more_t = None
    cur = head
    while cur is not None:
        if cur.value < val:
            if less_h is None:
                less_h = cur
                less_t = cur
            else:
                less_t.next = cur
                less_t = cur
            
        elif cur.value == val:
            if equal_h is None:
                equal_h = cur
                equal_t = cur
            else:
                equal_t.next = cur
                equal_t = cur

        else:
            if more_h is None:
                more_h = cur
                more_t = cur
            else:
                more_t.next = cur
                more_t = cur
        cur = cur.next

    less_t.next = equal_h
    equal_t.next = more_h
    return less_h


l = LinkedList()
l.insert([5,3,2,-1,4,5,3,6,7])
l.reverse()
l.output()
l.head = partition_linked(l.head,4)
l.output()