def are_points_collinear(x1, y1, x2, y2, x3, y3):
    if (y2 - y1)*(x3 - x2) == (y3 - y2)*(x2 - x1):
        print("Points lie on a straight line")
    else:
        print("Points do not lie on a straight line")
