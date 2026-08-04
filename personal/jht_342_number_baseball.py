import sys
import io

sample_input = """
3
1 2 3 4
1 3 2 4
1 2 2 4
2 1 2 4
1 2 3 4
5 6 7 8
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    answer = list(map(int, input().split()))
    guess = list(map(int, input().split()))
    b, s = 0, 0

    for idx, num in enumerate(guess):
        if answer[idx] == num:
            s += 1
        elif num in answer:
            b += 1

    print(f"#{test_case} {s, b}")