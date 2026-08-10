import io
import sys

sample_input = """
3
5
14054
04222
01228
14853
11008
1
5
3
111
111
111
""".strip()

sys.stdin = io.StringIO(sample_input)

it = iter(sys.stdin.read().split())
T = int(next(it))

for test_case in range(1, T + 1):
    n = int(next(it))
    grid = [next(it) for _ in range(n)]
    mid = n // 2

    result = 0
    for r in range(n):
        for c in range(n):
            if abs(mid - r) + abs(mid - c) <= mid:
                result += int(grid[r][c])

    print(f"#{test_case} {result}")