# is_same_set: 判断元素x y是否属于一个集合
# union：合并x和y所属的两个集合
# 单位时间O(1)
# 初始状态认为每个元素都是单独的集合，指向自己
# 以最低复杂度

# 优化：扁平化，将所有节点的father指向father，而不是前一个元素


class Node:
    def __init__(self, val) -> None:
        self.val = val

class DisjointSet:
    def __init__(self, data_list) -> None:
        self.size_map = {} # 只存每个集合头节点
        self.father = {}
        self.nodes = {}
        self.add(data_list)

    def add(self, data_list):
        for v in data_list:
            node = Node(v)
            self.nodes[v] = node
            self.father[node] = node
            self.size_map[node] = 1

    def ancestor(self, node):
        path = []
        cur = node
        while cur != self.father[cur]:
            path.append(cur)
            cur = self.father[cur]
        for n in path:
            self.father[n] = cur
        return cur

    def is_same_set(self, x, y):
        if self.ancestor(self.nodes[x]) == self.ancestor(self.nodes[y]):
            return True
        else:
            return False

    # 小的集合挂到大的集合上
    def union(self, x, y):
        x_a = self.ancestor(self.nodes[x])
        y_a = self.ancestor(self.nodes[y])
        small = x_a if self.size_map[x_a] > self.size_map[y_a] else y_a
        big = y_a if self.size_map[x_a] > self.size_map[y_a] else x_a
        self.father[small] = big
        self.size_map[big] = self.size_map[small] + self.size_map[big]
        del self.size_map[small]

s = DisjointSet([1,2,3,4,5])
s.union(1, 2)
s.union(2, 3)
s.union(5, 4)

print(s.is_same_set(1, 3))
print(s.is_same_set(5, 4))
print(s.is_same_set(1, 4))


print(s.size_map)