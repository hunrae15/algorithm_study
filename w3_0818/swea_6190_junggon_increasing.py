import io
import sys

sample_input = """
1
4
2 4 7 10
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    now_max = -1
    for i in range(n):
        for j in range(n):
            if i < j and arr[i] * arr[j] > now_max:
                num = arr[i] * arr[j]
                if str(num) == "".join(sorted(str(num))):
                    now_max = num

    print(f"#{test_case} {now_max}")
