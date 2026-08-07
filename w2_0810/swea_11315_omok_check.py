import io
import sys

sample_input = """
4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    field = [input() for _ in range(n)]
    result = False
    for r in range(n):
        for c in range(n):
            # 가로
            if c + 5 <= n and all(x == "o" for x in field[r][c:c + 5]):
                result = True
            # 세로
            elif r + 5 <= n and all(field[r + x][c] == "o" for x in range(5)):
                result = True
            # 우상
            elif r + 5 <= n and 0 <= c - 5 + 1 and all(field[r + x][c - x] == "o" for x in range(5)):
                result = True
            # 우하
            elif r + 5 <= n and c + 5 <= n and all(field[r + x][c + x] == "o" for x in range(5)):
                result = True
            if result:
                break
        if result:
            break

    print(f"#{test_case} {'YES' if result else 'NO'}")