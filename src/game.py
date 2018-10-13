

from .consts import MIN_PIECE_DENSITY, MAX_PIECE_DENSITY, MIN_GAME_DIMENSION


class Game:

    def __init__(self, width, length, number_of_pieces):
        if (width < MIN_GAME_DIMENSION) or (length < MIN_GAME_DIMENSION):
            raise ValueError

        piece_density = number_of_pieces/width*length
        if piece_density > MAX_PIECE_DENSITY or piece_density < MIN_PIECE_DENSITY:
            raise ValueError
