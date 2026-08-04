import io
import sys
from collections import deque

sample_input = """
3
3 3
0 0 0
0 1 0
1 1 1
3 3
0 0 0
0 1 0
0 0 0
2 4
1 1 1 0
1 0 1 1
""".strip()

sys.stdin = io.StringIO(sample_input)

it = iter(sys.stdin.read().split())
T = int(next(it))

for test_case in range(1, T + 1):
    n = int(next(it))
    m = int(next(it))
    arr = [[int(next(it)) for _ in range(m)] for _ in range(n)]

    q = deque()
    result = []
    for x in range(n):
        row = []
        for y in range(m):
            if arr[x][y] == 0:
                q.append((x, y))
                row.append(0)
            else:
                row.append(-1)
        result.append(row)

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    while q:
        qr, qc = q.popleft()
        for i in range(4):
            nr = qr + dr[i]
            nc = qc + dc[i]
            if 0 <= nr < n and 0 <= nc < m and result[nr][nc] == -1:
                result[nr][nc] = result[qr][qc] + 1
                q.append((nr, nc))

    print(f"#{test_case}")
    for row in result:
        print(*row)
