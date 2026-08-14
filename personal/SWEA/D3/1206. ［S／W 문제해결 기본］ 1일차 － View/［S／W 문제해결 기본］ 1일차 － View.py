T = 10#int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lst = [0]+list(map(int, input().split()))
    sun = 0
    for i in range(3, n-1):
        sun += max(lst[i] - max(lst[i-2:i]+lst[i+1:i+3]), 0)
    print(f"#{test_case} {sun}")