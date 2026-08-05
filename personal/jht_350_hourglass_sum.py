import io
import sys

sample_input = """
3
3
1 1 1
0 1 0
1 1 1
5
1 2 3 4 5
0 1 2 3 0
0 0 1 0 0
0 1 2 3 0
1 2 3 4 5
1
9
""".strip()

sys.stdin = io.StringIO(sample_input)

it = iter(sys.stdin.read().split())
T = int(next(it))

for test_case in range(1, T + 1):
    n = int(next(it))
    vals = [int(next(it)) for _ in range(n * n)]
    arr = [vals[i * n : (i + 1) * n] for i in range(n)]

    mid = n // 2
    result = 0

    for r in range(n):
        for c in range(n):
            if abs(mid - c) <= abs(mid - r):
                result += arr[r][c]

    print(f"#{test_case} {result}")