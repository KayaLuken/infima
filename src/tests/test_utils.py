

from ..utils import C, direction, intermediate_and_final_coordinates, step


def test_coordinate_class():
    c = C(0, 0) - C(2, 2)
    assert (c.x, c.y)  == (-2, -2)
    c = C(0, 0) - C(-2, -2)
    assert (c.x, c.y)  == (2, 2)
    c = C(0, 0) + C(2, 2)
    assert (c.x, c.y) == (2, 2)
    c = C(3, 0) * 5
    assert (c.x, c.y) == (15, 0)

def test_direction():
    assert direction( (0, 0), (1, 1) ) == (1, 1)
    assert direction( (0, 0), (-1, -1) ) == (-1, -1)
    assert direction( (1, 1), (4, 1) ) == (1, 0)
    assert direction( (4, 1), (1, 1) ) == (-1, 0)


def test_get_intermediate_coordinates():
    assert intermediate_and_final_coordinates((0, 0), (5, 0)) == [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
    assert intermediate_and_final_coordinates((1, 1), (6, 6)) == [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
    assert intermediate_and_final_coordinates((1, 1), (2, 2)) == [(2, 2)]


def test_step():
    assert step( (2, 3), (1, -1)) == (3, 2)
    assert step( (5, 5), (-1, 0), 4) == (1, 5)