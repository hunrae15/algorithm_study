import io
import sys

sample_input = """
3
5
2 2 0
GGLLRRGR
4
0 0 1
GGGRGG
3
1 1 3
LGLGLGLG
""".strip()

sys.stdin = io.StringIO(sample_input)

it = iter(sys.stdin.read().split())
T = int(next(it))

for test_case in range(1, T + 1):
    n = int(next(it))
    r, c, d = int(next(it)), int(next(it)), int(next(it))
    commands = next(it)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for comm in commands:
        if comm == "G" and 0 <= r + dr[d] < n and 0 <= c + dc[d] < n:
            r += dr[d]
            c += dc[d]
        elif comm == "L":
            d = (d - 1) % 4
        elif comm == "R":
            d = (d + 1) % 4

    print(f"#{test_case} {r} {c} {d}")