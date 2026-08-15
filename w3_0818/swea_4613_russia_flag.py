import io
import sys

sample_input = """
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]

    min_v = float("inf")
    for p1 in range(1, n - 1):
        for p2 in range(2, n):
            if p1 < p2:
                cnt = 0
                for white in flag[:p1]:
                    cnt += m - white.count("W")
                for blue in flag[p1:p2]:
                    cnt += m - blue.count("B")
                for red in flag[p2:]:
                    cnt += m - red.count("R")
                min_v = min(min_v, cnt)

    print(f"#{test_case} {min_v}")
