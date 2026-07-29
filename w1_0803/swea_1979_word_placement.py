import io
import sys

sample_input = """
2
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    t_puzzle = list(zip(*puzzle))

    result = 0
    for r in range(n):
        for c in range(n - k + 1):
            if puzzle[r][c] == 1:
                # 가로 확인
                h1 = (c == 0 or puzzle[r][c - 1] == 0)
                h2 = (c + k == n or puzzle[r][c + k] == 0)
                h3 = sum(puzzle[r][c:c + k]) == k
                if h1 and h2 and h3:
                    result += 1

            if t_puzzle[r][c] == 1:
                # 세로 확인
                v1 = (c == 0 or t_puzzle[r][c - 1] == 0)
                v2 = (c + k == n or t_puzzle[r][c + k] == 0)
                v3 = sum(t_puzzle[r][c:c + k]) == k
                if v1 and v2 and v3:
                    result += 1

    print(f"#{test_case} {result}")
