
import inspect
import sys


class Piece:
    def __init__(self, player):
        self.player = player


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