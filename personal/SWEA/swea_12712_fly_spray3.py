import io
import sys

sample_input = """
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
""".strip()

sys.stdin = io.StringIO(sample_input)


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    drx = [1, 1, -1, -1]
    dcx = [1, -1, 1, -1]
    dr10 = [1, 0, -1, 0]
    dc10 = [0, -1, 0, 1]
    result = 0

    for r in range(n):
        for c in range(n):
            now_sum_10 = field[r][c]
            now_sum_x = field[r][c]
            for i in range(4):
                for k in range(1, m):
                    nr = r + drx[i]*k
                    nc = c + dcx[i]*k
                    if 0 <= nr < n and 0 <= nc < n:
                        now_sum_x += field[nr][nc]

                    nr = r + dr10[i] * k
                    nc = c + dc10[i] * k
                    if 0 <= nr < n and 0 <= nc < n:
                        now_sum_10 += field[nr][nc]

            result = max(result, now_sum_10, now_sum_x)

    print(f"#{test_case} {result}")
