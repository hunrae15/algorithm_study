import io
import sys

sample_input = """
3
||||||
(|..|)
.|.(|...||)|...()..
""".strip()

sys.stdin = io.StringIO(sample_input)


T = int(input())
for test_case in range(1, T + 1):
    field = input()
    result = field.count("()") + field.count("(|") + field.count("|)")
    print(f"#{test_case} {result}")