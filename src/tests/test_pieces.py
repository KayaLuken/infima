

import pytest


from ..pieces import get_pieces, Piece



def test_returns_officers_only():
    pieces = get_pieces()
    are_correct_classes = map(lambda pce: pce is not Piece and pce not in Piece.__subclasses__(), pieces)
    assert all(are_correct_classes)