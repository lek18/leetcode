from typing import List
from collections import deque


# bfs from buildings 

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        m, n = len(grid), len(grid[0])
        buildings = sum([ val for row in grid for val in row if val==1])
        distances = [[0] * n for _ in range(m)]
        reachable_buildings = [[0] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        def valid(row, col):

            return 0 <= row < m and 0 <= col < n 

        def bfs(row, col):
            
            queue = deque([(row, col, 0)])

            while queue:
                x, y, dist = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if valid(nx,ny) and (nx,ny) not in visited and grid[nx][ny] == 0:
                        queue.append((nx, ny, dist + 1))
                        visited.add((nx,ny))
                        distances[nx][ny] += dist + 1
                        reachable_buildings[nx][ny] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = set([(i,j)])
                    bfs(i, j)
        
        print(distances)
        print(reachable_buildings)

        min_distance = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reachable_buildings[i][j] == buildings:
                    min_distance = min(min_distance, distances[i][j])

        return min_distance if min_distance != float('inf') else -1



tests = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
test1_result = 7