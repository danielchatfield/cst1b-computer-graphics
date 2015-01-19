
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)

    def __div__(self, other):
        return Point(self.x / other, self.y / other)

    def flip(self):
        self.x, self.y = self.y, self.x


class Bezier():
    tolerance = 1

    def __init__(self, p0, p1, p2, p3):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def distance(self, point):
        p = self.p3 - self.p0

        u = (point - self.p0) * p / float(p.x*p.x + p.y*p.y)

        if u > 1:
            u = 1
        elif u < 0:
            u = 0

        d = self.p0 + u * p

        return d.x*d.x + d.y*d.y

    def flat(self):
        distance = self.distance(self.p1) + self.distance(self.p2)

        return distance < self.tolerance

    def draw_curve(self):
        if self.flat():
            self.draw_line()
        else:
            left, right = self.subdivide()
            left.draw_curve()
            right.draw_curve()

    def draw_line(self):

        flipped = False

        if abs(self.p3.y-self.p0.y) > abs(self.p3.x-self.p0.x):
            flipped = True
            self.p0.flip()
            self.p3.flip()

        if self.p0.x > self.p3.x:
            self.p0, self.p3 = self.p3, self.p0

        delta_x = self.p3.x - self.p0.x
        delta_y = abs(self.p3.y - self.p0.y)
        error = delta_x / 2

        y = self.p0.y
        y_step = 1 if self.p0.y < self.p3.y else -1

        for x in range(self.p0.x, self.p3.x+1):
            if flipped:
                draw(y, x)
            else:
                draw(x, y)
                error -= delta_y
            if error < 0:
                y += y_step
                error += delta_x

    def subdivide(self):
        q0 = self.p0
        q1 = 0.5 * (self.p0 + self.p1)
        q2 = 0.25 * self.p0 + 0.5 * self.p1 + 0.25 * self.p2
        q3 = 0.125*(self.p0 + self.p3) + 0.375*(self.p1 + self.p2)
        r0 = q3
        r1 = 0.25 * self.p1 + 0.5 * self.p2 + 0.25 * self.p3
        r2 = 0.5 * self.p2 + 0.5 * self.p3
        r3 = self.p3
        return (Bezier(q0, q1, q2, q3), Bezier(r0, r1, r2, r3))
