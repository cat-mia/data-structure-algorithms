import sys
sys.path.append('..')
from ListNode.double_list_node import DoubleList

class Stack1:
    '''use double list
    '''
    def __init__(self) -> None:
        self.double_list = DoubleList()
    
    def push(self, val):
        self.double_list.insert_node_from_tail(val)
    
    def pop(self):
        return self.double_list.remove_node_from_tail()
    
    def get_top(self):
        return self.double_list.tail.value

class Stack2:
    '''use array
    '''
    def __init__(self, capacity) -> None:
        self.list = [0] * capacity
        self.top_pointer = -1 # 指向栈顶
    
    def push(self, val):
        self.top_pointer += 1
        try:
            self.list[self.top_pointer] = val
        except:
            raise Exception("Full stack!")
        
    
    def pop(self):
        self.top_pointer -= 1
        try:
            return self.list[self.top_pointer+1]
        except:
            raise Exception("Empty stack!")
    
    def get_top(self):
        try:
            return self.list[self.top_pointer]
        except:
            raise Exception("Empty stack!")
    

s = Stack2(5)
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.get_top())
