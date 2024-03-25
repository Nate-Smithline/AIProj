"""

"""

class ATree:
    def __init__(self):
        self.value = 0

class Astar:
    def __init__(self, filename):
        self.gameBoard = [[0] * 50 for _ in range(30)]
        self.visitedNodes = []
        self.viableOptions = {}
        self.numVisited = 0
        self.currentPosition = []
        self.goalPosotion = []
        self.tree = ATree()
