# import io
# import sys
# 
# sample_input = """
# 3
# 7    
# 0 0 1 0 0 0 0
# 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0
# 1 1 0 1 0 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 0 0
# 9  
# 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0
# 0 0 0 1 0 0 0 0 0
# 0 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0 1
# 11 
# 0 0 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 1
# 0 0 0 1 0 0 0 0 1 0 0
# 0 1 0 1 1 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0
# """.strip()
# 
# sys.stdin = io.StringIO(sample_input)


def link(idx, link_cnt, core_cnt, input_grid):
    global max_core, min_link
    if core_cnt + len(t_xy) - idx < max_core:
        return

    if idx >= len(t_xy):
        if max_core < core_cnt:
            max_core = core_cnt
            min_link = link_cnt
        elif max_core == core_cnt:
            min_link = min(min_link, link_cnt)

        return

    dp_grid = [row[:] for row in input_grid]
    r, c = t_xy[idx]
    if all(right == 0 for right in dp_grid[r][c + 1:]):
        # 그리드 변환
        dp_grid[r][c + 1:] = [1] * (n - c - 1)
        # idx 늘려서 재귀
        link(idx + 1, link_cnt + (n - c - 1), core_cnt + 1, dp_grid)
        # 그리드 백트래킹
        dp_grid = [row[:] for row in input_grid]

    if all(left == 0 for left in dp_grid[r][:c]):
        dp_grid[r][:c] = [1] * c
        link(idx + 1, link_cnt + c, core_cnt + 1, dp_grid)
        dp_grid = [row[:] for row in input_grid]

    if all(up == 0 for up in [dp_grid[u][c] for u in range(r)]):
        for u in range(r):
            dp_grid[u][c] = 1
        link(idx + 1, link_cnt + r, core_cnt + 1, dp_grid)
        dp_grid = [row[:] for row in input_grid]

    if all(down == 0 for down in [dp_grid[d][c] for d in range(r + 1, n)]):
        for d in range(r + 1, n):
            dp_grid[d][c] = 1
        link(idx + 1, link_cnt + (n - r - 1), core_cnt + 1, dp_grid)
        dp_grid = [row[:] for row in input_grid]

    link(idx + 1, link_cnt, core_cnt, dp_grid)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    t_xy = [(x, y) for x in range(1, n - 1) for y in range(1, n - 1) if grid[x][y] == 1]
    max_core = 0
    min_link = float("inf")
    link(0, 0, 0, grid)

    print(f"#{test_case} {min_link}")


