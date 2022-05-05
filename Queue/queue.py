import sys

sys.path.append('..')
from ListNode.double_list_node import DoubleList

class Queue1:
    '''use double list
    '''
    def __init__(self) -> None:
        self.double_list = DoubleList()
    
    def push(self, val):
        self.double_list.insert_node_from_tail(val)
    
    def pop(self):
        return self.double_list.remove_node_from_head()
    
    def get_head(self):
        return self.double_list.head.value
    
    def get_tail(self):
        return self.double_list.tail.value
    
    def output(self):
        self.double_list.output()

class Queue2:
    '''use array
    ring buffer:
        current size
        limit
        push index
        pop index
    case:
        0 1 2 3 4 -- index
        A B C
        X B C D E
        X X C D E
        F X C D E
        |   |
        push|index(0 before F arrive)
            |
        pop index(2)
    '''
    def __init__(self, capacity) -> None:
        self.list = [None] * capacity
        self.limit = capacity
        self.cur_size = 0
        self.push_index = 0
        self.pop_index = 0
    
    def push(self, val):
        if self.cur_size >= self.limit:
            raise Exception("Full queue!")
        if self.push_index >= self.limit:
            self.push_index = 0
        self.list[self.push_index] = val
        self.push_index += 1
        self.cur_size += 1      
    
    def pop(self):
        if self.cur_size == 0:
            raise Exception("Empty queue!")
        self.pop_index += 1
        self.cur_size -= 1
        return self.list[self.pop_index-1]
            
    
    def get_head(self):
        try:
            return self.list[self.pop_index]
        except:
            raise Exception("Empty queue!")
    
    def get_tail(self):
        try:
            return self.list[self.push_index-1]
        except:
            raise Exception("Empty queue!")
    
    def output(self):
        print(self.list)
        print("HEAD:", self.get_head())
        print("TAIL:", self.get_tail())

# q = Queue2(5)
# q.push('a')
# q.push('b')
# q.push('c')
# print(q.pop())
# q.push('d')
# q.push('e')
# print(q.pop())
# q.push('f')
# q.push('g')
# q.push('h')
# q.output()