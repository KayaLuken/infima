import itertools as it

from .consts import MIN_PIECE_DENSITY, MAX_PIECE_DENSITY, MIN_GAME_DIMENSION


class Game:

    players = ['white', 'black']

    def __init__(self, width, length, number_of_pieces, pieces=(None)):
        if (width < MIN_GAME_DIMENSION) or (length < MIN_GAME_DIMENSION):
            raise ValueError

        piece_density = number_of_pieces/width*length
        if piece_density > MAX_PIECE_DENSITY or piece_density < MIN_PIECE_DENSITY:
            raise ValueError

        empty_board = self.create_board(width, length)
        self.board = self.fill_board(empty_board, number_of_pieces, pieces)

        self.current_player = self.players[0]


    def update_board(self, directions):
        start_position, target_position = directions[0], directions[1]
        if not self.is_correct_player(start_position):
            return
        current_piece = self.board[start_position[1]][start_position[0]]
        if not current_piece.is_correct_displacement(start_position, target_position):
            return




    def is_correct_player(self, position):
        return self.board[position[1]][position[0]].player == self.current_player


    @staticmethod
    def create_board(width, length):
        return [
            [None for _ in range(width)]
            for _ in range(length)
        ]

    @staticmethod
    def fill_board(board, number_of_pieces, pieces):
        width = len(board[0]) ; length = len(board)
        piece_generator = it.cycle(pieces)
        for j, i in it.product(range(length), (range(width))):
            piece_number = i + (j * width)
            if piece_number == number_of_pieces/2:
                break
            piece_to_add = next(piece_generator)
            board[j][i] = piece_to_add(Game.players[0])
            board[-(j+1)][i] = piece_to_add(Game.players[1])
        return board


    def naive_update(self):
        pass
