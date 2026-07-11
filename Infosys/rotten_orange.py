# Q. Given an m x n grid where each cell can have one of three values: 0 representing an empty cell,
#  1 representing a fresh orange, or 2 representing a rotten orange. 
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. 
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
# If it is impossible, return -1.

from collections import deque

def orangesRotting(grid):
    if not grid:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    fresh = 0

    # Find all rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    # No fresh oranges
    if fresh == 0:
        return 0

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    minutes = 0

    while queue and fresh > 0:

        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

        minutes += 1

    return minutes if fresh == 0 else -1

grid = [
 [2,1,1],
 [1,1,0],
 [0,1,1]
]
print(orangesRotting(grid))