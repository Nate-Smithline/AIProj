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
        self.currentPosition = ()
        
        # will be of type (i, j)
        self.goalPosition = ()
        
        # not sure if necessary, basic linked list/tree
        self.tree = ATree()

        # commands
        self.readIn(filename)

    def readIn(self, filename):
        file = open(filename, "r")

        #isolate the first line and identify curent & goal state
        line = file.readline().split()
        self.currentPosition = (int(line[0]), int(line[1]))
        self.goalPosition = (int(line[2]), int(line[3]))

        #read in rest of board
        line = file.readline()
        start = 29
        while line:
            numbers = line.split()
            
            for number_indx in range(len(numbers)):
                number = numbers[number_indx]
                self.gameBoard[start][number_indx] = number

            start -= 1
            line = file.readline()



Astar('Input1.txt')