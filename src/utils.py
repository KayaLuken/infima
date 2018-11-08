import itertools as it


class C:
    '''Simplifying coordinate arithmetic'''
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return C(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return C(self.x - other.x, self.y - other.y )

    def __mul__(self, other):
        return C(self.x*other, self.y*other)


def direction(start, finish)-> tuple:
    relative_coordinates = C(*finish) - C(*start)
    direction = tuple(map(
        lambda n: 0 if not n else int(n / n) if n>0 else int(-n/n),
        (relative_coordinates.x, relative_coordinates.y) ))
    return direction


def intermediate_and_final_coordinates(start, finish):
    x0, y0, x1, y1 = start[0], start[1], finish[0], finish[1]
    x_coordinates = it.repeat(x0, y1 - y0) if x0 == x1 else range(x0 + 1, x1+1)
    y_coordinates = it.repeat(y0, x1 - x0) if y0 == y1 else range(y0 + 1, y1+1)
    return [(x, y) for x, y in zip(x_coordinates,  y_coordinates)]


def step(start, direction, distance=1):
    c  = C(*start )+ C(*direction) * distance
    return (c.x, c.y)
        

