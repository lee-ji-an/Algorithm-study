import sys
input = sys.stdin.readline

dice_list = list(map(int, input().split()))

# 게임판 만들기
red_map = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 14,
           11: 12, 12: 22, 14: 15, 15: 16, 16: 17, 17: 18, 18: 23, 19: 20, 20: 21,
           21: 22, 22: 31, 23: 24, 24: 25, 25: 26, 26: 27, 27: -1, 28: 29, 29: 30, 30: 22,
           31: 32, 32: 27}
blue_map = {5: 28, 18: 19, 10: 11}
score_map = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20,
             11: 22, 12: 24, 14: 22, 15: 24, 16: 26, 17: 28, 18: 30, 19: 28, 20: 27,
             21: 26, 22: 25, 23: 32, 24: 34, 25: 36, 26: 38, 27: 40, 28: 13, 29: 16, 30: 19,
             31: 30, 32: 35, 0: 0, -1: 0}

piece_info = {0: 0, 1: 0, 2: 0, 3: 0}


def dfs(order, piece_info, score):
    global ans
    if order == 10:
        ans = max(ans, score)
        return

    my_piece_info = {key: item for key, item in piece_info.items()}
    for i in range(4):
        if my_piece_info[i] == -1:
            continue

        origin_pos = my_piece_info[i]
        move_dist = dice_list[order]

        destination = piece_info[i]
        for j in range(move_dist):
            if destination == -1:
                break

            if j == 0 and destination in blue_map:
                destination = blue_map[destination]
            else:
                destination = red_map[destination]

        if destination != -1 and destination in list(piece_info.values()):
            continue

        my_piece_info[i] = destination
        dfs(order + 1, my_piece_info, score + score_map[destination])
        my_piece_info[i] = origin_pos


ans = float('-inf')
dfs(0, piece_info, 0)
print(ans)
