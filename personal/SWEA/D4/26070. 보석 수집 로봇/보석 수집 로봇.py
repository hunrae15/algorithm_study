# import io
# import sys
# 
# sample_input = """
# 7
# 5
# 0 0 0 0 0
# 0 0 0 3 0
# 0 1 0 0 0
# 0 0 2 0 0
# 0 0 0 0 0
# 5
# 0 0 0 0 0
# 0 3 0 0 0
# 0 0 2 0 0
# 0 0 4 1 0
# 0 0 0 0 0
# 5
# 0 0 0 0 0
# 0 0 1 4 0
# 0 5 3 0 0
# 0 2 0 0 0
# 0 0 0 0 0
# 7
# 0 0 0 0 0 0 0
# 0 2 0 4 0 0 0
# 0 0 0 0 0 6 0
# 0 0 0 0 5 0 0
# 0 0 0 0 1 3 0
# 0 0 7 0 0 0 0
# 0 0 0 0 0 0 0
# 10
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 5 0 0 0 0
# 0 0 0 0 4 0 0 0 0 0
# 0 0 0 10 0 0 0 0 0 0
# 0 0 0 0 0 0 8 0 0 0
# 0 0 0 0 0 0 0 0 2 0
# 0 0 0 0 0 0 0 1 0 0
# 0 0 0 0 6 9 0 0 0 0
# 0 0 3 0 0 0 0 0 7 0
# 0 0 0 0 0 0 0 0 0 0
# 6
# 0 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 4 0 0 0
# 0 0 2 0 0 0
# 0 3 0 5 0 0
# 0 0 0 0 0 0
# 8
# 0 0 0 0 0 0 0 0
# 0 0 1 0 6 0 0 0
# 0 0 4 0 0 0 0 0
# 0 5 0 3 0 7 0 0
# 0 0 0 0 0 0 0 0
# 0 8 0 0 0 0 0 0
# 0 0 0 0 2 0 0 0
# 0 0 0 0 0 0 0 0
# """.strip()
# 
# sys.stdin = io.StringIO(sample_input)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    t_xy = sorted([(grid[x][y], x, y) for x in range(n) for y in range(n) if grid[x][y] > 0])

    dr = [1, 2, 3, 3]
    r, c, d = 0, 0, 0
    turn_cnt = 0
    for _, tr, tc in t_xy:
        diff_r = tr - r
        diff_c = tc - c
        turn = 0
        if diff_r > 0 and diff_c > 0:
            turn = dr[(4 - d) % 4]
        elif diff_r > 0 and diff_c < 0:
            turn = dr[(4 - d + 1) % 4]
        elif diff_r < 0 and diff_c < 0:
            turn = dr[(4 - d + 2) % 4]
        elif diff_r < 0 and diff_c > 0:
            turn = dr[(4 - d + 3) % 4]
        turn_cnt += turn
        d = (d + turn) % 4
        r, c = tr, tc

    print(f"#{test_case} {turn_cnt}")


