import io
import sys

sample_input = """
2
2 3
ab a
a ac ba
3 3
aa bb cc
dd cc aa
""".strip()

sys.stdin = io.StringIO(sample_input)


T = int(input())
for test_case in range(1, T + 1):
    _ = input()
    set_a = set(input().split())
    set_b = set(input().split())

    print(f"#{test_case} {len(set_a & set_b)}")