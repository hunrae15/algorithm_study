import io
import sys

sample_input = """
3
5
.....
..#..
.###.
..#..
.....
5
#####
#####
#####
#####
#####
7
..#....
..#....
#####..
..#.#..
..#####
....###
.....#.
""".strip()

sys.stdin = io.StringIO(sample_input)

it = iter(sys.stdin.read().split())

T = int(next(it))
for test_case in range(1, T + 1):
    n = int(next(it))
    grid = [next(it) for _ in range(n)]

    def my_func(r, c):
        k = 1
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        while True:
            for i in range(4):
                nr = r + dr[i] * k
                nc = c + dc[i] * k
                if not (0 <= nr < n and 0 <= nc < n and grid[nr][nc] == "#"):
                    return k - 1
            k += 1

    now_max = 0
    for row in range(n):
        for col in range(n):
            if grid[row][col] == "#":
                now_max = max(now_max, my_func(row, col))

    print(f"#{test_case} {now_max}")