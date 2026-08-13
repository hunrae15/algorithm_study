# import io
# import sys
# 
# sample_input = """
# 10
# 4
# 1 2 3 4
# 5
# 3 10 1 2 5
# 7
# 12 48 28 21 67 75 85
# 8
# 245 108 162 400 274 358 366 166
# 10
# 866 919 840 944 761 895 701 912 848 799
# 1
# 500
# 3
# 5 8 3
# 6
# 414 390 205 614 184 236
# 9
# 255 137 779 89 258 747 393 544 701
# 2
# 100 200
# """.strip()
# 
# sys.stdin = io.StringIO(sample_input)


def hammer(blocks):
    key = tuple(blocks)
    if key in memo:
        return memo[key]

    b_len = len(blocks)
    if b_len == 1:
        return blocks[0]

    max_score = 0
    for i in range(b_len):
        if i == 0:
            get_score = blocks[1]
        elif i == b_len - 1:
            get_score = blocks[0]
        else:
            get_score = blocks[i - 1] * blocks[i + 1]

        next_blocks = blocks[:i] + blocks[i + 1:]

        total = get_score + hammer(next_blocks)
        max_score = max(max_score, total)

    memo[key] = max_score
    return max_score


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    origin_blocks = list(map(int, input().split()))

    memo = {}
    result = hammer(origin_blocks)

    print(f"#{test_case} {result}")


