# import io
# import sys

# sample_input = """
# 3
# 3
# 10 20 30
# 2
# 1 2
# 4
# 5 6 7 8
# """.strip()

# sys.stdin = io.StringIO(sample_input)

# it = iter(sys.stdin.read().split())
# T = int(next(it))

# for test_case in range(1, T + 1):
#     n = int(next(it))
#     arr = [int(next(it)) for _ in range(n)]

#     print(f"#{test_case}")

#     for i in range(1, 2**n):
#         bin_code = bin(i)[2:].rjust(n, "0")[::-1]
#         row = []
#         for x, y in zip(arr, bin_code):
#             if y != "0":
#                 row.append(x)
#         print(*row)

# 비트 연산자 활용!
import io
import sys

sample_input = """
3
3
10 20 30
2
1 2
4
5 6 7 8
""".strip()

sys.stdin = io.StringIO(sample_input)

it = iter(sys.stdin.read().split())
T = int(next(it))

for test_case in range(1, T + 1):
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    print(f"#{test_case}")

    for i in range(1, 1 << n):
        row = []
        for j in range(n):
            if i & (1 << j):
                row.append(arr[j])
        print(*row)