import pytest

from ..game import Game
from ..pieces import Piece


@pytest.fixture
def game_no_init():
    Game.__init__ = object.__init__
    game = Game()
    game.current_player = game.players[0]
    game.board = [ [] ]
    return game