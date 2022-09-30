def collinearPoints(points):
    collinears = {}
    for i in range(len(points)):
        tans = []
        for j in range(0, len(points)):
            if i == j: continue
            if points[j][0]-points[i][0] != 0:
                tan = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
            else:
                tan = float('inf')
            tans.append((points[j][0], points[j][1], tan))
        tans = sorted(tans, key = lambda x : x[2])
        collinear = {}
        for j in range(0, len(tans)):
            angle = tans[j][2]
            if angle in collinear:
                collinear[angle].append((tans[j][0], tans[j][1]))
            else:
                collinear[angle] = [(tans[j][0], tans[j][1])]
        for key in collinear.keys():
            value = collinear[key]
            if len(value) >= 3:
                flag = False
                value = sorted(value, key=lambda x: (x[1] - points[i][1]) ** 2 + (x[0] - points[i][0] ** 2))
                if key in collinears:
                    dist1 = (collinears[key][0] - collinears[key][2]) ** 2 + (collinears[key][1] - collinears[key][3]) ** 2
                    dist2 = (points[i][0] - value[-1][0]) ** 2 + (points[i][1] - value[-1][1]) ** 2
                    if dist1 < dist2:
                        flag = True
                else:
                    flag = True
                if flag:
                    if points[i][0] < value[-1][0]:
                        collinears[key] = (points[i][0], points[i][1], value[-1][0], value[-1][1])
                    elif points[i][0] == value[-1][0]:
                        if points[i][1] < value[-1][1]:
                            collinears[key] = (points[i][0], points[i][1], value[-1][0], value[-1][1])
                        else:
                            collinears[key] = (value[-1][0], value[-1][1], points[i][0], points[i][1])
                    else:
                        collinears[key] = (value[-1][0], value[-1][1], points[i][0], points[i][1])
    res = sorted(list(collinears.values()), key = lambda x: (x[0], x[2], x[1], x[3]))
    return res




if __name__ == "__main__":
    collinearPoints([(1, 1), (2, 2), (3, 3), (4, 4), (2, 0), (3, -1), (4, -2), (0, 1), (-1, 1), (-2, 1), (-3, 1), (2, 1), (3, 1), (4, 1), (5, 1)])
    # collinearPoints([(19000, 10000), (18000, 10000), (32000, 10000), (21000, 10000), (1234, 5678), (14000, 10000)])
    # collinearPoints([(0, 0), (1, 1), (3, 3), (4, 4),   (6, 6), (7, 7), (9, 9)])
    # collinearPoints([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (8, 0)])
    # collinearPoints([(7, 0), (14, 0), (22, 0), (27, 0), (31, 0), (42, 0)])
    # collinearPoints([(12446, 18993), (12798, 19345), (12834, 19381), (12870, 19417), (12906, 19453), (12942, 19489)])
    # collinearPoints([(10000, 0), (0, 10000), (3000, 7000), (7000, 3000), (20000, 21000), (3000, 4000), (14000, 15000), (6000, 7000)])
    collinearPoints([(0, 0), (1, 1), (2, 2), (3, 3), (1, -1), (2, -2), (3, -3), (2, 2), (2, 1), (2, -1)])
    collinearPoints([(0, 0), (1, 1), (2, 2), (3, 3)])
