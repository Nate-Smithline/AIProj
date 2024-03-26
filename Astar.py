import math
"""

"""
class ATree:
    def __init__(self):
        self.value = 0



"""
Node
=======

This is a class for each node thatt goes into the subnodes for it as well as heuristic. This node can be seen at multiple places in A* with different path costs and paths
"""
class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.heur = 0

    """
    getCoords
    =========
    This is going to return the coordinates of the node
    """
    def getCoords(self):
        return (self.i, self.j)
    
    def setHeur(self, sldist):
        self.heur = sldist

    def getHeur(self):
        return self.heur


"""
AStar
=========

This is the class that runs the entire game. It is already incredibly chunky, so will need to be broken apart for simplicity later on
"""
class Astar:
    """
    def INIT
    gameBoard -- board directly from input file inverted
    visitedNodes -- lists all nodes that have been visited to block repeated states
    viableOptions -- dictionary of all options => f(n ) value
    numVisited -- number of nodes visited in the page
    currentPosition -- currentPosition
    goalPosition -- final position to check
    """
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

    """
    readIn
    - reads through the input file, sets the current & goal position, and assigns all items in the gameboard
    """
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

    """
    goalHit
    =================
    @author Nate-Smithline
    
    This function checks the currentPosition and runs it against the goalPosition to see if they are matching in values. If so, it will return True, and we can end the play mode
    """
    def goalHit(self):
        if(self.currentPosition[0] == self.goalPosition[0]) and (self.currentPosition[1] == self.goalPosition[1]):
            return True
        else:
            return False

    
    """
    checkVisited
    ===================
    @author Nate-Smithline

    This function is going to go through the visitedNodes and see if the currentPosition is in that placed. If so, it will return True, else False
    """
    def wasVisited(self):
        for visitedNode in self.visitedNodes:
            if(visitedNode[0] == self.currentPosition[0] and visitedNode[1] == self.currentPosition[1]):
                return True
        return False


    """
    getHeuristic
    ===================
    @author Nate-Smithline

    This function is going to take a node in Node(i, j) format and return the h(n), or straight line distance to the goal state. It is going to use the pythagorean theorem to do so.
    """
    def setHeuristic(self, node):
        # get coords of node
        coords = node.getCoords()
        i = coords[0]
        j = coords[1]

        # get the straightline dist
        x_dist = abs(i - self.goalPosition[0])
        y_dist = abs(j - self.goalPosition[1])
        sldist = round(math.sqrt(x_dist**2 + y_dist**2), 2)
        node.setHeur(sldist)

Astar('Input1.txt')