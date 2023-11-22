# https://contest.yandex.ru/contest/53027/problems/C/

import math

xa, ya, xb, yb = map(int, input().split())


def radius(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def from_center_route(xa, ya, xb, yb):
    return radius(xa, ya) + radius(xb, yb)


def radial_route(xa, ya, xb, yb):
    def straight_section(xa, ya, xb, yb):
        return abs(radius(xa, ya) - radius(xb, yb))

    def radial_section(xa, ya, xb, yb):
        r = radius(xb, yb) if radius(xa, ya) > radius(xb, yb) else radius(xa, ya)

        angle_a = math.atan2(ya, xa)
        angle_b = math.atan2(yb, xb)
        angle_difference = angle_b - angle_a
        angle_difference = (angle_difference + math.pi) % (2 * math.pi) - math.pi
        min_angle = abs(angle_difference)

        return r * min_angle

    return straight_section(xa, ya, xb, yb) + radial_section(xa, ya, xb, yb)



if from_center_route(xa, ya, xb, yb) < radial_route(xa, ya, xb, yb):
    print(from_center_route(xa, ya, xb, yb))
else:
    print(radial_route(xa, ya, xb, yb))

