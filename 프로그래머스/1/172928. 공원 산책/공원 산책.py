def solution(park, routes):
    len_row = len(park)
    len_col = len(park[0])
    
    # 시작 위치 찾기
    for i, row in enumerate(park):
        for j, col in enumerate(row):
            if col == "S":
                position = [i, j]
                break

    for route in routes:
        d, m = route.split()
        m = int(m)
        temp = position[:]

        if d == "N":
            temp[0] -= m
        elif d == "S":
            temp[0] += m
        elif d == "W":
            temp[1] -= m
        elif d == "E":
            temp[1] += m

        # 이동 후 좌표가 범위 내에 있는지 확인
        if not (0 <= temp[0] < len_row and 0 <= temp[1] < len_col):
            continue

        obstacle = False

        # 이동 경로에 장애물 있는지 확인
        if d in ["N", "S"]:
            step = 1 if temp[0] >= position[0] else -1
            for r in range(position[0], temp[0] + step, step):
                if park[r][position[1]] == "X":
                    obstacle = True
                    break
        else:
            step = 1 if temp[1] >= position[1] else -1
            for c in range(position[1], temp[1] + step, step):
                if park[position[0]][c] == "X":
                    obstacle = True
                    break

        if not obstacle:
            position = temp

    return position
