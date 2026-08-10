import io
import sys

sample_input = """
3
3
4
1
""".strip()

sys.stdin = io.StringIO(sample_input)

it = iter(sys.stdin.read().split())
T = int(next(it))

for test_case in range(1, T + 1):
    n = int(next(it))
    arr = [[0] * n for _ in range(n)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c, d = 0, 0, 0

    for i in range(1, n**2 + 1):
        arr[r][c] = i
        nr = r + dr[d % 4]
        nc = c + dc[d % 4]

        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
            r = nr
            c = nc
        else:
            d += 1
            r += dr[d % 4]
            c += dc[d % 4]

    print(f"#{test_case}")
    for row in arr:
        print(*row)