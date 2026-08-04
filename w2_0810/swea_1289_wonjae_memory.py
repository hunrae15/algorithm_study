import io
import sys

sample_input = """
2
0011
100
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    lst = input()
    cnt = 0
    now = '0'
    for i in lst:
        if i != now:
            cnt += 1
            now = i

    print(f"#{test_case} {cnt}")