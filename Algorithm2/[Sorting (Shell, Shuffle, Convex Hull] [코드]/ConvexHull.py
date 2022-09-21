import math
def grahamScan(points):
    points = sorted(points, key = lambda x : (x[1], -x[0]))
    px, py = points[0]
    points = points[1:]
    angle = []
    for i in range(len(points)):
        ax, ay = points[i][0], points[i][1]
        angle.append((ax, ay, math.atan2(ay-py, ax-px)))
    angle = sorted(angle, key = lambda x : x[2])
    stack = [(px, py), (angle[0][0], angle[0][1]), (angle[1][0], angle[1][1])]
    top = 2
    angle = angle[2:]
    for i in range(0, len(angle)+1):
        flag = False
        while not (ccw(stack[top-2], stack[top-1], stack[top])):
            if stack[top - 2][0] == stack[top - 1][0] or stack[top - 1][0] == stack[top][0]:
                if stack[top - 2][0] == stack[top - 1][0] and stack[top - 1][0] == stack[top][0]:
                    flag = True
            else:
                if ((stack[top-2][1]-stack[top-1][1])/(stack[top-2][0]-stack[top-1][0])) == ((stack[top-1][1]-stack[top][1])/(stack[top-1][0]-stack[top][0])):
                    flag = True
            stack.pop(top-1)
            top -= 1
            if flag: break
        if i == len(angle):
            break
        top += 1
        stack.append((angle[i][0], angle[i][1]))
    return stack

def ccw(i, j, k):
    area2 = (j[0]-i[0]) * (k[1]-i[1]) - (j[1]-i[1]) * (k[0]-i[0])
    if area2 > 0: return True
    else: return False

if __name__ == "__main__":
    print(grahamScan([(-1, 1), (1, -1), (3, -1), (-3, -1), (0, 0), (-2, -1)]))
    print(grahamScan([(4, 2), (3, -1), (2, -2), (1, 0), (0, 2), (0, -2), (-1, 1), (-2, -1), (-2, -3), (-4, -2), (-4, -4), (-3, 3), (-4, 0)]))