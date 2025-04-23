from math import sqrt
def point_in_circle(x, y, cx, cy, r):
    dist = sqrt((x - cx)**2 + (y - cy)**2)
    if dist < r:
        print("Point is inside the circle")
    elif dist == r:
        print("Point is on the circle")
    else:
        print("Point is outside the circle")
