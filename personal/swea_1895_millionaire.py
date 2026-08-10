import io
import sys

sample_input = """
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
""".strip()

sys.stdin = io.StringIO(sample_input)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    curr_max = 0
    money = 0
    for i in price[::-1]:
        if curr_max <= i:
            curr_max = i
        else:
            money += curr_max - i
    print(f"#{test_case} {money}")
