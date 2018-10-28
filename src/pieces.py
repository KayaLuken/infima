
import inspect
import sys


class Piece:
    def __init__(self, ):
        pass


class Captor(Piece):
    def __init__(self, ):
        pass

class Displacor(Piece):
    def __init__(self, ):
        pass


class Effector(Piece):
    pass


class Advancer(Captor):
    pass


class Replacer(Captor):
    pass


class LongLeaper(Captor):
    pass


class LongReplacer(Captor):
    pass


class Immobiliser(Effector):
    pass


def get_pieces():
    all_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    return [cls for _, cls in all_classes if cls is not Piece and cls not in Piece.__subclasses__()]