# 左移：i>>1, 更快的int(i/2)
# 右移：i<<1, 更快的i*2
# only support integers

# heap
# 完全二叉树
# 大顶堆，root.val > all children's val for all sub tree
# 小顶堆，root.val < all children's val for all sub tree
# 数组从0开始存heap
# lchild = 2*i +1, rchild = 2*i + 2, father = int((i-1)/2)
import functools
@functools.total_ordering
class MaxHeap:
    def __init__(self, capacity) -> None:
        self.list = [None]*capacity
        self.heap_index = 0
        self.capacity = capacity
    
    def __lt__(self, other) -> bool:
        return self.capacity < other.capacity

    def __eq__(self, other) -> bool:
        return self.capacity == other.capacity
    
    def heap_insert(self, val):
        self.list[self.heap_index] = val
        index = self.heap_index
        while index > 0 and self.list[index] > self.list[(index-1)>>1]:
            self.list[index], self.list[(index-1)>>1] = \
                self.list[(index-1)>>1], self.list[index]
            index = (index-1)>>1
        self.heap_index += 1

    def heapify(self, index):
        # 从上往下
        l_child = index*2 +1
        r_child = index*2 +2
        while l_child < self.heap_index:
            max_child = r_child if r_child < self.heap_index and self.list[r_child] > self.list[l_child] else l_child
            if self.list[index] < self.list[max_child]:
                self.list[max_child], self.list[index] = self.list[index], self.list[max_child]
            else:
                break

    def pop(self):
        if self.heap_index == 0:
            raise Exception("Pop from empty heap!")
        self.list[0], self.list[self.heap_index-1] = self.list[self.heap_index-1], self.list[0]
        self.heap_index -= 1
        self.heapify(0)
    
    def build(self, arr):
        for n in arr:
            self.heap_insert(n)

    def heap_sort(self, arr):
        self.build(arr)
        while self.heap_index >0:
            self.list[self.heap_index-1], self.list[0] = self.list[0], self.list[self.heap_index-1]
            self.heap_index -=1 
            self.heapify(0)
        return self.list
    
    def output(self):
        print(self.list[:self.heap_index])

# arr = [0,2,1,3,-1,9,4]
# h = MaxHeap(len(arr))
# print(h.heap_sort(arr))
# h.build(arr)
# h.output()
# h.pop()
# h.output()

# 比较器，重载
# h1= MaxHeap(30)
# h2 = MaxHeap(30)
# print(h1<=h2)

