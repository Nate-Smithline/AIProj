import math
import heapq


"""
Node
=======

This is a class for each node that goes into the subnodes for it as well as heuristic. This node can be seen at multiple places in A* with different path costs and paths
"""
class Node:
    def __init__(self, parent, i, j):
        self.parent = parent
        self.coords = (i, j)

        #important details
        self.h = 0
        self.f = 0
        self.g = 0


    def getCoords(self):
        return self.coords
    
    def getParent(self):
        return self.parent
    
    def setH(self, h):
        self.h = h
        self.f = self.g + self.h

    def getH(self):
        return self.h
    
    def setG(self, g):
        self.g = g
        self.f = self.g + self.h

    def getG(self):
        return self.g
    
    def getF(self):
        return self.f
    




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
        # will be of type [(i, j), (i1, j1), etc.]
        self.visitedNodes = []

        # will be of type [Node, Node, etc.]
        self.viableOptions = []
        
        # will be of type Node
        self.currentPosition = None
        
        # will be of type Node
        self.goalPosition = None

        self.readIn(filename)

        #testing
        self.getChildren()
        for i in self.viableOptions:
            print(str(i.getCoords())+" "+str(i.getF()))


    """
    readIn
    - reads through the input file, sets the current & goal position, and assigns all items in the gameboard
    """
    def readIn(self, filename):
        file = open(filename, "r")

        #isolate the first line and identify curent & goal state
        line = file.readline().split()
        self.currentPosition = Node(None, int(line[0]), int(line[1]))
        self.goalPosition = Node(None, int(line[2]), int(line[3]))

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
        currentPosCoords = self.currentPosition.getCoords()
        goalPosCoords = self.goalPosition.getCoords()
        if(currentPosCoords[0] == goalPosCoords[0]) and (currentPosCoords[1] == goalPosCoords[1]):
            return True
        else:
            return False

    
    """
    checkVisited
    ===================
    This function is going to go through the visitedNodes and see if the currentPosition is in that placed. If so, it will return True, else False
    """
    def wasVisited(self, tuple=''):
        for visitedNode in self.visitedNodes:
            if(visitedNode[0] == tuple[0] and visitedNode[1] == tuple[1]):
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
        goalPosCoords = self.goalPosition.getCoords()
        x_dist = abs(i - goalPosCoords[0])
        y_dist = abs(j - goalPosCoords[1])
        sldist = round(math.sqrt(x_dist**2 + y_dist**2), 2)
        node.setH(sldist)



    """
    viableOptions
    ===================
    @author aayushDaftary

    This function is going to evaluate the f(n) values for all next potential nodes in path.
    """
    def getChildren(self):
        i, j = self.currentPosition.getCoords()
        neighbors = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        for offset_i, offset_j in neighbors:
            new_i, new_j = i + offset_i, j + offset_j
            if 0 <= new_i < len(self.gameBoard) and 0 <= new_j < len(self.gameBoard[0]):
                if self.gameBoard[new_i][new_j] != 1 and not self.wasVisited((new_i, new_j)):
                    if offset_i == 0 or offset_j == 0:
                        stepCost = 1
                    else:
                        stepCost = math.sqrt(2)

                    parentCost = self.currentPosition.getG()
                    nodeCost = stepCost + parentCost

                    newNode = Node(self.currentPosition, new_i, new_j)
                    newNode.setG = nodeCost
                    self.setHeuristic(newNode)

                    self.viableOptions.append(newNode)
    
    """
    play
    ===================
    """
    def play(self):
        start_node = Node(self.currentPosition[0], self.currentPosition[1])
        open = [self.currentPosition]
        while open:
            _, current = heapq.heappop(open)
            if self.goalHit():
                return current #begin outputting, found goal
            
            self.getViableOptions(current)
            best = float('inf') #positive infinity
            best_next = None
            for next_coords, f_n in self.viableOptions.items():
                if self.wasVisited(next_coords):
                    continue
                next = Node(next_coords[0], next_coords[1])
                if f_n < best:
                    best = f_n
                    best_next = next
            if best_next:
                heapq.heappush(open, (best, best_next))
                self.visitedNodes.append(best_next.getCoords())
        return None

        
        

Astar('Input1.txt')