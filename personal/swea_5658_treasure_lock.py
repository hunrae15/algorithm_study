import io
import sys

sample_input = """
2
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
""".strip()

sys.stdin = io.StringIO(sample_input)
it = iter(sys.stdin.read().split("\n"))

T = int(next(it))
for test_case in range(1, T + 1):
    n, k = list(map(int, next(it).split()))
    numbers = list(next(it))
    size = n // 4
    n_set = set()
    for _ in range(size):
        for j in range(0, n, size):
            n_set.add("".join(numbers[j:j + size]))
        numbers = numbers[-1:] + numbers[:-1]
    nums_10 = list(map(lambda x: int("0x"+x, base=0), list(n_set)))
    result = sorted(nums_10, reverse=True)[k - 1]
    print(f"#{test_case} {result}")
