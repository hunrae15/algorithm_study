import io
import sys

sample_input = """
3
5
2 2
UURDDLL
3
0 0
UULLDD
4
1 1
RRRR
""".strip()

sys.stdin = io.StringIO(sample_input)
it = iter(sys.stdin.read().split())

T = int(next(it))
for test_case in range(1, T + 1):
    n = int(next(it))
    r = int(next(it))
    c = int(next(it))
    commands = next(it)

    action = {
        "U": {"dr": -1, "dc": 0},
        "D": {"dr": 1, "dc": 0},
        "L": {"dr": 0, "dc": -1},
        "R": {"dr": 0, "dc": 1}
    }

    for comm in commands:
        nr = r + action[comm]["dr"]
        nc = c + action[comm]["dc"]
        if 0 <= nr < n and 0 <= nc < n:
            r = nr
            c = nc

    print(f"#{test_case} {r, c}")
