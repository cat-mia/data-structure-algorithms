# leetcode 200
# https://leetcode-cn.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        for i in range(m):
            for j in range(n):
                # 为1的才开始infect，统计一个island
                if grid[i][j] == '1':
                    islands += 1
                    self.infect(grid,i,j)
        return islands

    def infect(self, grid, i, j):
        if i < 0 or j< 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] !='1':
            return
        grid[i][j] = 2 # 避免无限重复递归,下次递归到已访问过的时可以退出
        self.infect(grid, i-1, j)
        self.infect(grid, i+1, j)
        self.infect(grid, i, j-1)
        self.infect(grid, i, j+1)