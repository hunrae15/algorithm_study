# import io
# import sys
# 
# sample_input = """
# 10
# 2
# 0 0 1 0 0 1 0 0
# 1 0 0 1 1 1 0 1
# 0 0 1 0 1 1 0 0
# 0 0 1 0 1 1 0 1
# 1 1
# 3 -1
# 2
# 1 0 0 1 0 0 0 0
# 0 1 1 1 1 1 1 1
# 0 1 0 1 0 0 1 0
# 0 1 0 0 1 1 0 1
# 3 1
# 1 1
# 5
# 0 0 1 1 1 1 1 1
# 1 1 1 1 1 0 1 0
# 0 0 0 0 1 0 0 1
# 0 1 0 1 0 1 0 1
# 4 -1
# 3 1
# 4 -1
# 3 -1
# 1 -1
# 2
# 1 0 1 0 0 1 0 1
# 0 0 1 0 1 1 1 1
# 0 0 1 1 0 0 0 1
# 0 1 0 1 1 0 0 0
# 2 -1
# 1 1
# 7
# 0 0 1 1 0 1 1 1
# 0 1 0 1 1 0 0 0
# 1 1 1 0 0 0 0 1
# 1 1 1 0 0 1 0 0
# 4 1
# 2 1
# 2 -1
# 3 1
# 2 1
# 4 1
# 2 -1
# 10
# 1 0 0 0 0 0 0 1
# 1 0 1 0 1 1 0 1
# 1 0 0 1 0 0 0 1
# 1 1 0 1 0 1 1 1
# 2 1
# 1 1
# 2 -1
# 3 1
# 3 -1
# 2 -1
# 2 -1
# 1 1
# 4 1
# 4 1
# 10
# 0 1 0 0 1 1 0 0
# 0 1 1 0 1 0 1 1
# 0 0 0 0 0 1 1 0
# 0 0 1 0 1 0 1 1
# 3 1
# 1 -1
# 2 1
# 4 -1
# 3 1
# 3 -1
# 4 -1
# 2 -1
# 1 -1
# 3 -1
# 10
# 0 1 0 1 0 1 0 0
# 0 1 1 1 1 1 0 1
# 1 0 0 0 0 1 1 0
# 1 0 0 0 0 0 0 1
# 1 1
# 4 -1
# 4 -1
# 2 -1
# 2 -1
# 2 -1
# 3 -1
# 2 1
# 3 1
# 3 -1
# 20
# 1 0 0 0 1 1 0 0
# 1 0 0 1 1 1 0 0
# 0 1 1 1 0 1 1 1
# 1 1 1 1 0 1 1 1
# 1 1
# 4 -1
# 4 -1
# 2 -1
# 3 -1
# 1 1
# 4 1
# 4 -1
# 4 -1
# 4 -1
# 3 -1
# 3 -1
# 4 -1
# 4 -1
# 2 -1
# 1 1
# 3 -1
# 3 -1
# 2 1
# 1 1
# 20
# 0 0 1 1 1 0 1 0
# 0 1 0 0 1 0 1 0
# 1 1 1 0 1 0 1 0
# 0 0 1 0 0 1 1 1
# 1 -1
# 4 -1
# 3 -1
# 1 1
# 4 1
# 2 1
# 1 -1
# 4 1
# 2 -1
# 4 -1
# 1 1
# 4 -1
# 1 1
# 2 -1
# 1 -1
# 3 -1
# 1 1
# 2 1
# 3 1
# 3 -1
# """.strip()
# 
# sys.stdin = io.StringIO(sample_input)


def rotation(idx, to, lists, prev):
    left, right = lists[idx][6], lists[idx][2]
    lists[idx] = lists[idx][-to:] + lists[idx][:-to]
    if idx - 1 > 0 and idx - 1 != prev and lists[idx - 1][2] != left:
        rotation(idx - 1, -to, lists, idx)
    if idx + 1 < 5 and idx + 1 != prev and lists[idx + 1][6] != right:
        rotation(idx + 1, -to, lists, idx)


T = int(input())
for test_case in range(1, T + 1):
    k = int(input())
    magnets = [["1-idx"]] + [input().split() for _ in range(4)]

    for _ in range(k):
        t_idx, direction = map(int, input().split())
        rotation(t_idx, direction, magnets, -1)

    score = 0
    for i in range(1, 5):
        score += int(magnets[i][0]) * (2 ** (i-1))

    print(f"#{test_case} {score}")