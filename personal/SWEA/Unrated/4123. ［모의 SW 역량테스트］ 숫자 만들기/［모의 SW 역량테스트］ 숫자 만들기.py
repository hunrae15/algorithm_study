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
