
import pytest

from .fixtures import game_no_init
from ..game import Game
from ..pieces import Piece, Advancer, Blocker, Immobiliser, LongLeaper, Neutraliser
from ..consts import MAX_PIECE_DENSITY, MIN_PIECE_DENSITY, MIN_GAME_DIMENSION


class TestGameCreationParameterValidation:

    def test_too_low_length_value_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            Game(6, MIN_GAME_DIMENSION-1, 10)

    def test_too_low_width_value_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            Game(MIN_GAME_DIMENSION-1, 7, 10)

    def test_too_low_density_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            Game(10, 10, 100*MIN_PIECE_DENSITY-1)

    def test_too_high_density_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            Game(10, 10, 100*MAX_PIECE_DENSITY+1)


class TestBoardSetup:

    empty_board = [
        [ None, None, None, None, None, None ],
        [ None, None, None, None, None, None ],
        [ None, None, None, None, None, None ],
        [ None, None, None, None, None, None ],
        [ None, None, None, None, None, None ],
        [ None, None, None, None, None, None ],
    ]

    def test_create_board(self):
        assert Game.create_board(6, 6) == self.empty_board

    def test_fill_board(self):
        pieces = [Advancer, Blocker, Immobiliser, LongLeaper, Neutraliser]
        filled_board = Game.fill_board(self.empty_board, 22, pieces )

        piece_types = [
            [Advancer, Blocker, Immobiliser, LongLeaper, Neutraliser, Advancer],
            [Blocker, Immobiliser, LongLeaper, Neutraliser, Advancer, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [Blocker, Immobiliser, LongLeaper, Neutraliser, Advancer, None],
            [Advancer, Blocker, Immobiliser, LongLeaper, Neutraliser, Advancer]
        ]
        player1, player2 = Game.players[0], Game.players[1]

        for rank_index, rank in enumerate(piece_types):
            assert all([type(piece_instance) is piece_type or piece_type is None
                        for piece_instance, piece_type in zip(filled_board[rank_index], rank)])

            player_for_rank = player1 if rank_index < 2 else player2
            assert all([piece_instance.player == player_for_rank for piece_instance in filled_board[rank_index]
                        if piece_instance is not None])


class TestBoardUpdate:

    def test_is_correct_player(self, game_no_init):
        game_no_init.board = [
            [Piece(game_no_init.players[0]), Piece(game_no_init.players[1])] ]
        assert game_no_init.is_correct_player((0, 0))
        assert not game_no_init.is_correct_player((1, 0))
