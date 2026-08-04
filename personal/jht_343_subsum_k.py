import io
import sys

sample_input = """
3
4 3
1 1 1 1
5 5
1 2 3 4 5
6 0
2 -2 3 0 -3 1
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(arr[i:j]) == k:
                cnt += 1

    print(f"#{test_case} {cnt}")