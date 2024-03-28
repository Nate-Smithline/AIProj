import math

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
        # print("G CHANGE: "+str(g)+" "+str(self.g))
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
    def __init__(self, input_name, output_name):
        self.gameBoard = [[0] * 50 for _ in range(30)]
        # will be of type [(i, j), (i1, j1), etc.]
        self.visitedNodes = []

        # will be of type [Node, Node, etc.]
        self.viableOptions = []
        
        # will be of type Node
        self.currentPosition = None
        
        # will be of type Node
        self.goalPosition = None

        self.numVisited = 0

        #call the readIn function
        self.readIn(input_name)

        #number of nodes generated
        self.numGenerated = 0

        #play
        self.play()

        #call the readOut function
        self.readOut(output_name)


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
        self.numGenerated = 1

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
    This function is going to evaluate the f(n) values for all next potential nodes in path.
    """
    def getChildren(self):
        i, j = self.currentPosition.getCoords()
        neighbors = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        for move_i, move_j in neighbors:
            new_i, new_j = i + move_i, j + move_j
            if 0 <= new_i < len(self.gameBoard) and 0 <= new_j < len(self.gameBoard[0]):
                if self.gameBoard[new_i][new_j] != '1' and not self.wasVisited((new_i, new_j)):
                    #horizontal or vertical move
                    if move_i == 0 or move_j == 0:
                        stepCost = 1
                    #diagonal move
                    else:
                        stepCost = math.sqrt(2)
                    parentCost = self.currentPosition.getG()
                    nodeCost = stepCost + parentCost
                    newNode = Node(self.currentPosition, new_i, new_j)
                    newNode.setG(nodeCost)
                    self.numGenerated += 1
                    self.setHeuristic(newNode)
                    self.viableOptions.append(newNode)
    
    """
    play
    ===================
    """
    def play(self):
        while self.goalHit() == False:
            self.numVisited += 1
            self.viableOptions = []
            self.getChildren()
            #find best node
            min_f = float('inf')
            indx = 0
            best_Node = None
            for node_indx in range(len(self.viableOptions)):
                node = self.viableOptions[node_indx]
                f = node.getF()
                if(f < min_f):
                    min_f = f
                    indx = node_indx
                    best_Node = node
            self.viableOptions.pop(indx)
            self.visitedNodes.append(best_Node.getCoords())
            self.currentPosition = best_Node
            print(str(best_Node.getCoords()))
        
    def readOut(self, filename):
        file = open(filename, 'a')

        #delete all file content
        file.truncate(0)

        #work to deduce work for A, C, & D
        depth_level = 0
        f_ns = []
        mve_vals = {-1: {-1: 5, 0: 4, 1: 3}, 0: {-1: 6, 1: 2}, 1: {-1: 7, 0: 0, 1: 1}}
        mves = []

        while self.currentPosition.getParent() != None:
            depth_level += 1
            f_ns.append(str(self.currentPosition.getF()))
            
            mcoords = self.currentPosition.getCoords()
            pcoords = self.currentPosition.getParent().getCoords()
            diff_i = mcoords[0] - pcoords[0]
            diff_j = mcoords[1] - pcoords[1]
            mves.append(str(mve_vals[diff_i][diff_j]))

            self.currentPosition = self.currentPosition.getParent()

        #A: depth level
        file.write(str(depth_level)+'\n')

        #B: total nodes generated
        file.write(str(self.numGenerated)+'\n')

        #C: solutions as move pattern
        file.write(' '.join(mves)+'\n')

        #D: f(n) of each node in solution
        file.write(' '.join(f_ns)+'\n')

        #E: gameboard reproduced
        for row in range(len(self.gameBoard)-1, -1, -1):
            line = ' '.join(self.gameBoard[row])
            if(row == 0):
                end = ''
            else:
                end = '\n'
            file.write(line+end)



Astar('Input2.txt', 'Input2Output.txt')