import itertools as it

def get_intermediate_and_final_coordinates(start, finish):
    x0, y0, x1, y1 = start[0], start[1], finish[0], finish[1]
    x_coordinates = it.repeat(x0, y1 - y0) if x0 == x1 else range(x0 + 1, x1+1)
    y_coordinates = it.repeat(y0, x1 - x0) if y0 == y1 else range(y0 + 1, y1+1)
    return [(x, y) for x, y in zip(x_coordinates,  y_coordinates)]