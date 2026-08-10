import io
import sys

sample_input = """
3
4 B 2 O 1 O 2 B 4
3 B 5 B 8 O 100
2 O 2 O 1
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
for test_case in range(1, T + 1):
    buttons = input().split()[1:]
    robots = {
        "B": {"now": 1, "available": 0, "other": "O"},
        "O": {"now": 1, "available": 0, "other": "B"}
    }

    result = 0
    for i in range(0, len(buttons), 2):
        robot = buttons[i]
        goto = int(buttons[i+1])
        other = robots[robot]["other"]
        elapsed = max(0, abs(robots[robot]["now"] - goto) - robots[robot]["available"]) + 1
        result += elapsed
        robots[robot]["now"] = goto
        robots[robot]["available"] = 0
        robots[other]["available"] += elapsed

    print(f"#{test_case} {result}")