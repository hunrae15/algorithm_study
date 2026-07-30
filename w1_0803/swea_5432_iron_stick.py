import io
import sys

sample_input = """
2
()(((()())(())()))(())
(((()(()()))(())()))(()())
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    pipes = input()
    stack = []
    result = 0
    cut = False
    for i in pipes:
        if i == "(":
            stack.append(i)
            cut = False
        else:
            if cut:
                stack.pop()
                result += 1
            else:
                stack.pop()
                result += len(stack)
                cut = True
    print(f"#{test_case} {result}")