# import io
# import sys
#
# sample_input = """
# 2
# 4
# 9 8 9 8
# 4 6 9 4
# 8 7 7 8
# 4 5 3 5
# 5
# 8 2 9 6 6
# 1 9 3 3 4
# 8 2 3 3 6
# 4 3 4 4 9
# 7 4 6 3 5
# """.strip()
#
# sys.stdin = io.StringIO(sample_input)


def checker(r, c, d, lst):
    tr, tc = targets[d]
    while r != tr and c != tc:
        if field[r][c] in lst:
            return -1
        lst.append(field[r][c])
        r += d_row[d]
        c += d_col[d]
    if tr == ur and tc == uc:
        return len(lst)
    return checker(tr, tc, d + 1, lst)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    field = [input().split() for _ in range(n)]
    d_row = [1, 1, -1, -1]
    d_col = [1, -1, -1, 1]

    now_max = -1
    for ur in range(n - 2):
        for uc in range(1, n - 1):
            for dr in range(ur + 2, n):
                offset = dr - ur - 2
                for dc in range(uc - offset, uc + offset + 1, 2):
                    move = ((dr - ur) - abs(dc - uc))//2
                    if uc >= dc:
                        rr, rc = ur + move, uc + move
                        lr, lc = dr - move, dc - move
                    else:
                        rr, rc = dr - move, dc + move
                        lr, lc = ur + move, uc - move
                    if rc < n and 0 <= lc:
                        eaten = []
                        targets = [(rr, rc), (dr, dc), (lr, lc), (ur, uc)]
                        a = checker(ur, uc, 0, eaten)
                        now_max = max(now_max, a)

    print(f"#{test_case} {now_max}")

# - 디버깅의 흔적
# n = 6
# tmp = [["_"]*n for _ in range(n)]
#
# for ur in range(n - 2):
#     for uc in range(1, n - 1):
#         for dr in range(ur + 2, n):
#             offset = dr - ur - 2
#             for dc in range(uc - offset, uc + offset + 1, 2):
#                 move = ((dr - ur) - abs(dc - uc))//2
#                 if uc >= dc:
#                     rr, rc = ur + move, uc + move
#                     lr, lc = dr - move, dc - move
#                 else:
#                     rr, rc = dr - move, dc + move
#                     lr, lc = ur + move, uc - move
#                 if rc < n and 0 <= lc:
#                     tmp[ur][uc], tmp[lr][lc], tmp[rr][rc], tmp[dr][dc] = "O", "O", "O", "O"
#                     for q in tmp:
#                         print(*q)
#                     print(len(tmp))
#                     tmp[ur][uc], tmp[lr][lc], tmp[rr][rc], tmp[dr][dc] = "_", "_", "_", "_"
#                     #print(f"\t({ur},{uc})\n({lr},{lc})\t({rr},{rc})\n\t({dr},{dc})\n")
