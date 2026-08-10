import io
import sys

sample_input = """
3
5 10
1 2 3 4 5
6 0
-2 -1 0 1 2 3
4 5
1 1 1 1
""".strip()

sys.stdin = io.StringIO(sample_input)

it = iter(sys.stdin.read().split())

T = int(next(it))
for test_case in range(1, T + 1):
    n = int(next(it))
    k = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    cnt = 0
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if arr[a] + arr[b] + arr[c] == k:
                    cnt += 1

    print(f"#{test_case} {cnt}")