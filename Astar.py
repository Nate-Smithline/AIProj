"""

"""

class ATree:
    def __init__(self):
        self.value = 0

class Astar:
    def __init__(self, filename):
        self.gameBoard = [[0] * 50 for _ in range(30)]
        # will be of type (i, j)
        self.visitedNodes = []
        # will be of type Node() => f(n) value
        self.viableOptions = {}
        self.numVisited = 0
        # will be of type (i, j)
        self.currentPosition = []
        # will be of type (i, j)
        self.goalPosotion = []
        # not sure if necessary, basic linked list/tree
        self.tree = ATree()
