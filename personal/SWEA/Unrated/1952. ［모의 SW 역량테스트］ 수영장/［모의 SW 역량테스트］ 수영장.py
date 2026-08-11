def rec_func(idx, fee_3m, monthly, now_sum):
    global now_min

    if idx >= 14:
        now_min = min(now_min, now_sum)
    else:
        if idx < 12:
            rec_func(idx+3, fee_3m, monthly, now_sum+fee_3m)
        rec_func(idx+1, fee_3m, monthly, now_sum+monthly[idx])


T = int(input())
for test_case in range(1, T + 1):
    fees = list(map(int, input().split()))
    monthly_plan = map(int, input().split())
    monthly_fee = list(map(lambda x: x * fees[0] if x * fees[0] < fees[1] else fees[1], monthly_plan)) + [0, 0]
    now_min = fees[3]
    rec_func(0, fees[2], monthly_fee, 0)

    print(f"#{test_case} {now_min}")
