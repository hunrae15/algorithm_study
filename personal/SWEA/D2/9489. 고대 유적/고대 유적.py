def check_long(grid_row):
    joined = ''.join(grid_row)
    split_text = joined.split("0")
    len_list = list(map(len, split_text))
    return max(len_list)


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    field = [input().split() for _ in range(n)]
    t_field = list(zip(*field))
    now_max = 0
    for r in range(n):
        h_max = check_long(field[r])
        now_max = max(now_max, h_max)
    for c in range(m):
        v_max = check_long(t_field[c])
        now_max = max(now_max, v_max)
    print(f"#{test_case} {now_max}")
