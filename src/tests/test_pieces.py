

import pytest


from ..pieces import get_pieces, Piece



def test_returns_officers_only():
    pieces = get_pieces()
    are_correct_classes = map(lambda pce: pce is not Piece and pce not in Piece.__subclasses__(), pieces)
    assert all(are_correct_classes)


class TestPiece:


    def test_is_correct_displacement_true(self):
        assert Piece.is_correct_displacement( (10, 0), (0, 10) ) # diagonal
        assert Piece.is_correct_displacement( (0, 0), (0, 10) ) # othogonal

    def test_is_correct_displacement_false(self):
        assert not Piece.is_correct_displacement( (0, 0), (5, 10) )

    def test_is_unobstructed(self):
        obstructed_board = [
            [None, None, None],
            [None, Piece, None],
            [None, None, None],
        ]
        assert not Piece.is_unobstructed(obstructed_board, (0, 0), (2, 2))
        assert not Piece.is_unobstructed(obstructed_board, (0, 0), (1, 1))
        un_obstructed_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        assert Piece.is_unobstructed(un_obstructed_board, (0, 0), (2, 2))
        assert Piece.is_unobstructed(un_obstructed_board, (0, 0), (1, 1))