import io
import sys

sample_input = """
40
""".strip()

sys.stdin = io.StringIO(sample_input)

T = int(input())
result = []
for n in range(1,T+1):
    cnt_369 = str(n).count("3") + str(n).count("6") + str(n).count("9")
    if cnt_369 > 0:
        result.append("-"*cnt_369)
    else:
        result.append(n)
print(*result)
