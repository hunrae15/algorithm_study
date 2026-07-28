import sys
import io

sample_input = """
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
""".strip()

sys.stdin = io.StringIO(sample_input)


T = int(input())
for test_case in range(1, T + 1):
    n = 9
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    result = 1
    for i in range(n):
        if (len(set(puzzle[i])) < 9) or (len(set(list(zip(*puzzle))[i])) < 9):
            result = 0
            break
        if i in [0, 3, 6]:
            for j in [0, 3, 6]:
                check_list = puzzle[i][j:j+3]
                check_list.extend(puzzle[i+1][j:j+3])
                check_list.extend(puzzle[i+2][j:j+3])
                if len(set(check_list)) < 9:
                    result = 0
                    break
            if result == 0:
                break
    print(f"#{test_case} {result}")
