#import io
#import sys

sample_input = """
10
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2
1 2 1
2 1 2
1 2 1
5 2
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
4 4
8 3 9 5
4 6 8 5
8 1 5 1
4 9 5 5
4 1
6 6 1 7
3 6 6 1
2 4 2 4
7 1 3 4
5 5
18 18 1 8 18
17 7 2 7 2
17 8 7 4 3
17 9 6 5 16
18 10 17 13 18
6 4
12 3 12 10 2 2
13 7 13 3 11 6
2 2 6 5 13 9
1 12 5 4 10 5
11 10 12 8 2 6
13 13 7 4 11 7
7 3
16 10 14 14 15 14 14
15 7 12 2 6 4 9
10 4 11 4 6 1 1
16 4 1 1 13 9 14
3 12 16 14 8 13 9
3 4 17 15 12 15 1
6 6 13 6 6 17 12
8 5
2 3 4 5 4 3 2 1
3 4 5 6 5 4 3 2
4 5 6 7 6 5 4 3
5 6 7 8 7 6 5 4
6 7 8 9 8 7 6 5
5 6 7 8 7 6 5 4
4 5 6 7 6 5 4 3
3 4 5 6 5 4 3 2
8 2
5 20 15 11 1 17 10 14
1 1 11 16 1 14 7 5
17 2 3 4 5 13 19 20
6 18 5 16 6 7 8 5
10 4 5 4 9 2 10 16
2 7 16 5 8 9 10 11
12 19 18 8 7 11 15 12
1 20 18 17 16 15 14 13
""".strip()

#sys.stdin = io.StringIO(sample_input)


def rec_func(n, r, c, field, dig, now_len, visited):
    global now_max
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if field[nr][nc] < field[r][c]:
                visited[nr][nc] = True
                rec_func(n, nr, nc, field, dig, now_len + 1, visited)
                visited[nr][nc] = False
            elif field[nr][nc] - dig < field[r][c] and not visited[nr][nc]:
                origin = field[nr][nc]
                field[nr][nc] = field[r][c] - 1
                visited[nr][nc] = True
                rec_func(n, nr, nc, field, 0, now_len + 1, visited)
                visited[nr][nc] = False
                field[nr][nc] = origin

    now_max = max(now_max, now_len)


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    field = []
    tops = [(0, -1, -1)]
    for r in range(n):
        row = []
        tmp = input().split()
        for c in range(n):
            t = int(tmp[c])
            row.append(t)
            if t > tops[0][0]:
                tops = [(t, r, c)]
            elif t == tops[0][0]:
                tops.append((t, r, c))
        field.append(row)
    visited = [[False]*n for _ in range(n)]

    now_max = 0
    for _, r, c in tops:
        visited[r][c] = True
        rec_func(n, r, c, field, k, 1, visited)
        visited[r][c] = False

    print(f"#{test_case} {now_max}")

# ## 디버깅의 흔적
# def rec_func(n, r, c, field, dig, now_len, path, visited):
#     global now_max
#     dr = [0, 0, 1, -1]
#     dc = [1, -1, 0, 0]
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < n and 0 <= nc < n:
#             if field[nr][nc] < field[r][c]:
#                 visited[nr][nc] = True
#                 rec_func(n, nr, nc, field, dig, now_len + 1, path+f"({nr},{nc})", visited)
#                 visited[nr][nc] = False
#             elif field[nr][nc] - dig < field[r][c] and not visited[nr][nc]:
#                 origin = field[nr][nc]
#                 field[nr][nc] = field[r][c] - 1
#                 visited[nr][nc] = True
#                 rec_func(n, nr, nc, field, 0, now_len + 1, path+f"({nr},{nc})", visited)
#                 visited[nr][nc] = False
#                 field[nr][nc] = origin
#     if now_max <= now_len:
#         print(path)
#     now_max = max(now_max, now_len)
# 
#
# T = int(input())
# for test_case in range(1, T + 1):
#     n, k = map(int, input().split())
#     field = []
#     tops = [(0, -1, -1)]
#     for r in range(n):
#         row = []
#         tmp = input().split()
#         for c in range(n):
#             t = int(tmp[c])
#             row.append(t)
#             if t > tops[0][0]:
#                 tops = [(t, r, c)]
#             elif t == tops[0][0]:
#                 tops.append((t, r, c))
#         field.append(row)
#     visited = [[False]*n for _ in range(n)]
# 
#     # 재귀
#     now_max = 0
#     for _, r, c in tops:
#         visited[r][c] = True
#         rec_func(n, r, c, field, k, 1, f"({r},{c})",visited)
#         visited[r][c] = False
# 
#     print(f"#{test_case} {now_max}")