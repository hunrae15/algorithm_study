# import io
# import sys
from collections import deque
# 
# sample_input = """
# 5
# 3 10 10
# 0 0 0 0 0 0 0 0 0 0
# 1 0 1 0 1 0 0 0 0 0
# 1 0 3 0 1 1 0 0 0 1
# 1 1 1 0 1 2 0 0 0 9
# 1 1 4 0 1 1 0 0 1 1
# 1 1 4 1 1 1 2 1 1 1
# 1 1 5 1 1 1 1 2 1 1
# 1 1 6 1 1 1 1 1 2 1
# 1 1 1 1 1 1 1 1 1 5
# 1 1 7 1 1 1 1 1 1 1
# 2 9 10
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0
# 1 1 0 0 1 0 0 0 0
# 1 1 0 1 1 1 0 1 0
# 1 1 0 1 1 1 0 1 0
# 1 1 1 1 1 1 1 1 0
# 1 1 3 1 6 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 3 6 7
# 1 1 0 0 0 0
# 1 1 0 0 1 0
# 1 1 0 0 4 0
# 4 1 0 0 1 0
# 1 5 1 0 1 6
# 1 2 8 1 1 6
# 1 1 1 9 2 1
# 4 4 15
# 0 0 0 0 
# 0 0 0 0 
# 0 0 0 0 
# 1 0 0 0 
# 1 0 0 0 
# 1 0 0 0 
# 1 0 0 0 
# 1 0 5 0 
# 1 1 1 0 
# 1 1 1 9 
# 1 1 1 1 
# 1 6 1 2 
# 1 1 1 5 
# 1 1 1 1 
# 2 1 1 2 
# 4 12 15
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# """.strip()
# 
# sys.stdin = io.StringIO(sample_input)


def bomb(r, c, grid):
    p = grid[r][c]
    q = deque()
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    q.append((r, c, p))
    grid[r][c] = 0

    while q:
        row, col, power = q.popleft()
        for d in range(4):
            for p in range(1, power):
                nr = row + dr[d]*p
                nc = col + dc[d]*p
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != 0:
                    q.append((nr, nc, grid[nr][nc]))
                    grid[nr][nc] = 0


def drop_bomb(idx, num, grid):
    dp_gird = [row[:] for row in grid]
    now_min = float("inf")

    start = 0
    while start < h:
        if dp_gird[start][idx] == 0:
            start += 1
        else:
            bomb(start, idx, dp_gird)
            break

    total_bricks = sum(sum(1 for x in row if x > 0) for row in dp_gird)
    if total_bricks == 0 or num + 1 == n:
        return total_bricks

    t_grid = list(zip(*dp_gird))
    for lv in range(w):
        new_row = [x for x in t_grid[lv] if x > 0]
        t_grid[lv] = [0] * (h - len(new_row)) + new_row
    new_grid = [list(row) for row in zip(*t_grid)]

    for j in range(w):
        now_grid = [row[:] for row in new_grid]
        now_min = min(now_min, drop_bomb(j, num + 1, now_grid))

    return now_min


T = int(input())
for test_case in range(1, T + 1):
    n, w, h = map(int, input().split())
    origin_grid = [list(map(int, input().split())) for _ in range(h)]

    result = float("inf")
    for i in range(w):
        result = min(result, drop_bomb(i, 0, origin_grid))

    print(f"#{test_case} {result}")


