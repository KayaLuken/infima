
import pytest

from ..game import Game
from ..consts import MAX_PIECE_DENSITY, MIN_PIECE_DENSITY, MIN_GAME_DIMENSION


class TestGameCreation:
    
    def test_too_low_length_value_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            Game(6, MIN_GAME_DIMENSION-1, 10)

    def test_too_low_width_value_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            Game(MIN_GAME_DIMENSION-1, 7, 10)
        #assert 'zerooo' in str(excinfo.value)

    def test_too_low_density_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            Game(10, 10, 100*MIN_PIECE_DENSITY-1)

    def test_too_high_density_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            Game(10, 10, 100*MAX_PIECE_DENSITY+1)


