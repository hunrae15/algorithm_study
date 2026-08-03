import io
import sys

sample_input = """
3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    deck = input().split()
    half = n//2 + 1 if n % 2 == 1 else n//2

    left_half = deck[:half]
    right_half = deck[half:]

    result = []
    for i in range(half):
        result.append(left_half[i])
        if n % 2 == 0 or i < half - 1:
            result.append(right_half[i])

    joined = ' '.join(result)
    print(f"#{test_case} {joined}")