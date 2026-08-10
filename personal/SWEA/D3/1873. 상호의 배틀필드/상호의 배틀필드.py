T = int(input())
for test_case in range(1, T + 1):
    h, w = map(int, input().split())
    board = []
    tanks = {"<": "L", ">": "R", "v": "D", "^": "U"}
    now_direction = ""
    nr, nc = -1, -1
    for r in range(h):
        row = input()
        for char in row:
            if char in tanks:
                now_direction = tanks[char]
                nr = r
                nc = row.index(char)
                break
        board.append(list(row))

    n_action = int(input())
    actions = input()

    tank_dict = {
        "U": {"form": "^", "dr": -1, "dc": 0},
        "D": {"form": "v", "dr": 1, "dc": 0},
        "L": {"form": "<", "dr": 0, "dc": -1},
        "R": {"form": ">", "dr": 0, "dc": 1}
    }

    for action in actions:
        if action in tank_dict:
            board[nr][nc] = tank_dict[action]["form"]
            now_direction = tanks[tank_dict[action]["form"]]
            dr = tank_dict[action]["dr"]
            dc = tank_dict[action]["dc"]
            if 0 <= nr + dr < h and 0 <= nc + dc < w and board[nr + dr][nc + dc] == ".":
                board[nr + dr][nc + dc] = tank_dict[action]["form"]
                board[nr][nc] = "."
                nr = nr + dr
                nc = nc + dc

        elif action == "S":
            sdr = tank_dict[now_direction]["dr"]
            sdc = tank_dict[now_direction]["dc"]
            sr = nr + sdr
            sc = nc + sdc
            while 0 <= sr < h and 0 <= sc < w:
                if board[sr][sc] == "*":
                    board[sr][sc] = "."
                    break
                elif board[sr][sc] == "#":
                    break
                sr += sdr
                sc += sdc

    print(f"#{test_case} ", end="")
    for i in range(h):
        print(''.join(board[i]))
