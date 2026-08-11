# import io
# import sys
# 
# sample_input = """
# 10
# 10 40 100 300
# 0 0 2 9 1 5 0 0 0 0 0 0
# 10 100 50 300
# 0 0 0 0 0 0 0 0 6 2 7 8
# 10 70 180 400
# 6 9 7 7 7 5 5 0 0 0 0 0
# 10 70 200 550
# 0 0 0 0 8 9 6 9 6 9 8 6
# 10 80 200 550
# 0 8 9 15 1 13 2 4 9 0 0 0
# 10 130 360 1200
# 0 0 0 15 14 11 15 13 12 15 10 15
# 10 180 520 1900
# 0 18 16 16 19 19 18 18 15 16 17 16
# 10 100 200 1060
# 12 9 11 13 11 8 6 12 8 7 15 6
# 10 170 500 1980
# 19 18 18 17 15 19 19 16 19 15 17 18
# 10 200 580 2320
# 12 28 24 24 29 25 23 26 26 28 27 22
# # """.strip()
# 
# sys.stdin = io.StringIO(sample_input)


def rec_func(idx, fee_3m, monthly, now_sum):
    global now_min

    if idx >= 12:
        now_min = min(now_min, now_sum)
        return
    else:
        rec_func(idx+3, fee_3m, monthly, now_sum+fee_3m)
        rec_func(idx+1, fee_3m, monthly, now_sum+monthly[idx])


T = int(input())
for test_case in range(1, T + 1):
    fees = list(map(int, input().split()))
    monthly_plan = map(int, input().split())
    monthly_fee = [min(fees[1], day * fees[0]) for day in monthly_plan]
    now_min = fees[3]
    rec_func(0, fees[2], monthly_fee, 0)

    print(f"#{test_case} {now_min}")
