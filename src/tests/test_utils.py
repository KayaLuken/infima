

from ..utils import get_intermediate_and_final_coordinates


def test_get_intermediate_coordinates():
    assert get_intermediate_and_final_coordinates((0, 0), (5, 0)) == [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
    assert get_intermediate_and_final_coordinates((1, 1), (6, 6)) == [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
    assert get_intermediate_and_final_coordinates((1, 1), (2, 2)) == [(2, 2)]