import io
import sys

sample_input = """
5
1
2
11
1295
1692
""".strip()

sys.stdin = io.StringIO(sample_input)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    set_10 = set()
    now = n
    times = 1

    while len(set_10) < 10:
        now = n * times
        times += 1
        for i in str(now):
            set_10.add(i)

    print(f"#{test_case} {now}")