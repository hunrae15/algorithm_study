import io
import sys

sample_input = """
5
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
20 14
88F611AE414A751A767B
24 16
044D3EBA6A647B2567A91D0E
28 11
8E0B7DD258D4122317E3ADBFEA99
""".strip()
sys.stdin = io.StringIO(sample_input)


T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    numbers = list(input().strip())
    size = n // 4
    n_set = set()

    for _ in range(size):
        for j in range(0, n, size):
            n_set.add("".join(numbers[j:j + size]))
        numbers = numbers[-1:] + numbers[:-1]

    nums_10 = [int(x, 16) for x in n_set]
    result = sorted(nums_10, reverse=True)[k - 1]

    print(f"#{test_case} {result}")
    


