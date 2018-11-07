
import inspect
import sys

from .utils import get_intermediate_and_final_coordinates


class Piece:
    def __init__(self, player):
        self.player = player



    @staticmethod
    def is_valid_move(board, start, finish):
        return Piece.is_correct_displacement(start,finish)\
               and Piece.is_unobstructed(board, start, finish)

    @staticmethod
    def is_unobstructed(board, start, finish):
        print(get_intermediate_and_final_coordinates(start, finish))
        return  all(map(lambda c: board[c[1]][c[0]] is None, get_intermediate_and_final_coordinates(start, finish)))

    @staticmethod
    def is_correct_displacement(start, finish):
        '''default is straight line movement'''
        x0, y0, x1, y1 = start[0], start[1], finish[0], finish[1]
        is_straight_diagonal = x1 - x0 == y1 - y0
        is_straight_orthogonal = x0 == x1 or y0 == y1
        return is_straight_diagonal or is_straight_orthogonal



class Captor(Piece):
    pass

class Displacor(Piece):
    pass


class Effector(Piece):
    pass

class Enplacor(Piece):
    pass



class Advancer(Captor):
    pass


class Archer(Captor):
    pass


class Blocker(Effector):
    pass


class Immobiliser(Enplacor):
    pass


class LongLeaper(Captor):
    pass


class LongReplacer(Captor):
    pass


class Neutraliser(Effector):
    pass


class Replacer(Captor):
    pass



def get_pieces():
    all_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    return [cls for _, cls in all_classes if cls is not Piece and cls not in Piece.__subclasses__()]