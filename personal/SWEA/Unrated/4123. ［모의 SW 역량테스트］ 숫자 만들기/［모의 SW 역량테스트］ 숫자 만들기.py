# import io
# import sys
#
# sample_input = """
# 10
# 5
# 2 1 0 1
# 3 5 3 7 9
# 6
# 4 1 0 0
# 1 2 3 4 5 6
# 5
# 1 1 1 1
# 9 9 9 9 9
# 6
# 1 4 0 0
# 1 2 3 4 5 6
# 4
# 0 2 1 0
# 1 9 8 6
# 6
# 2 1 1 1
# 7 4 4 1 9 3
# 7
# 1 4 1 0
# 2 1 6 7 6 5 8
# 8
# 1 1 3 2
# 9 2 5 3 4 9 5 6
# 10
# 1 1 5 2
# 8 5 6 8 9 2 6 4 3 2
# 12
# 2 1 6 2
# 2 3 7 9 4 5 1 9 2 5 6 4
# """.strip()
#
# sys.stdin = io.StringIO(sample_input)


def dfs(idx, current_val, plus, minus, multiply, divide):
    global now_max, now_min

    if idx == n:
        now_max = max(now_max, current_val)
        now_min = min(now_min, current_val)
        return

    if plus > 0:
        dfs(idx + 1, current_val + numbers[idx], plus - 1, minus, multiply, divide)

    if minus > 0:
        dfs(idx + 1, current_val - numbers[idx], plus, minus - 1, multiply, divide)

    if multiply > 0:
        dfs(idx + 1, current_val * numbers[idx], plus, minus, multiply - 1, divide)

    if divide > 0:
        dfs(idx + 1, int(current_val / numbers[idx]), plus, minus, multiply, divide - 1)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    plus, minus, multiply, divide = map(int, input().split())
    numbers = list(map(int, input().split()))

    now_min = float("inf")
    now_max = -float("inf")

    dfs(1, numbers[0], plus, minus, multiply, divide)

    print(f"#{test_case} {now_max - now_min}")



