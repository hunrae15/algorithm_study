import io
import sys

sample_input = """
2
8
2
1 3
2 3
25
1
1 1
""".strip()

sys.stdin = io.StringIO(sample_input)

it = iter(sys.stdin.read().split())
T = int(next(it))

for test_case in range(1, T + 1):
    n = int(next(it))
    m = int(next(it))

    sw = [0] * (n + 1)

    for _ in range(m):
        who = next(it)
        num = int(next(it))

        if who == "1":
            for i in range(num, n + 1, num):
                sw[i] ^= 1

        elif who == "2":
            sw[num] ^= 1
            offset = 1
            while num - offset >= 1 and num + offset <= n and sw[num - offset] == sw[num + offset]:
                sw[num - offset] ^= 1
                sw[num + offset] ^= 1
                offset += 1

    print(f"#{test_case}")
    result = sw[1:]
    for i in range(0, n, 20):
        print(*result[i : i + 20])

## 메모
# 1 - x 으로 1/0 토글 가능
# x ^ 1 (x ^= 1)로도 1/0 토글 가능