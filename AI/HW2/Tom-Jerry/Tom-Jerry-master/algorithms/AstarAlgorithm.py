from node import Node
from time import process_time
import math


class StarAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.tomPos = self.firstNode.searchForTom()
        self.jerryPos = self.searchForJerry(world)
        self.stack = [self.firstNode]
        self.computingTime = ""
        self.length_world = world.shape[0]
        self.height_world = world.shape[1]

    def getNodeMinSumCostHeuristic(self, stack):
        minNode = min(stack, key=lambda node: node.getSumCostHeuristic())
        return minNode

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def searchForJerry(self, world):
        jerryPos = []
        for i in range(world.shape[0]):
            for j in range(world.shape[1]):
                if (world[i, j] == self.firstNode.PRINCESS):
                    jerryPos.append(i)
                    jerryPos.append(j)
        return jerryPos
    
    def Heuristic(self, tomPos, jerryPos):
        dx = abs(tomPos[0] - jerryPos[0]) 
        dy = abs(tomPos[1] - jerryPos[1])
        return math.sqrt(dx**2+dy**2)

    def start(self):
        startTime = process_time()
        stack = self.stack
        tomPos = self.tomPos
        expandedNodes = 0
        depth = 0

        # TODO: define currentNode
        currentNode = self.getNodeMinSumCostHeuristic(stack)


        while not (currentNode.isGoal()):
            if (not (tomPos[1]+1 >= self.length_world) and currentNode.getState()[tomPos[0], tomPos[1]+1] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "right", currentNode.getDepth() + 1, currentNode.getCost()+1, currentNode.getStar(), currentNode.getFlower())

                right = son.rightMovement(tomPos)
                son.setNewCost(right)
                son.setTomPos(right)
                son.setHeuristic(self.Heuristic(son.getTomPos(), self.jerryPos))
                son.setSumCostHeuristic(son.getHeuristic() + son.getCost())

                # TODO: implement the heuristic logic

                son.moveRight(tomPos)
                if (son.compareCicles2(right)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

            # Check if left side is free
            if (not (tomPos[1]-1 < 0) and currentNode.getState()[tomPos[0], tomPos[1]-1] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost()+1, currentNode.getStar(), currentNode.getFlower())

                left = son.leftMovement(tomPos)
                son.setNewCost(left)
                son.setTomPos(left)
                son.setHeuristic(self.Heuristic(son.getTomPos(), self.jerryPos))
                son.setSumCostHeuristic(son.getHeuristic() + son.getCost())
                # TODO: implement the heuristic logic

                son.moveLeft(tomPos)
                if (son.compareCicles2(left)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()


            # Check if down-side is free
            if (not (tomPos[0]+1 >= self.height_world) and currentNode.getState()[tomPos[0]+1, tomPos[1]] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost()+1, currentNode.getStar(), currentNode.getFlower())

                down = son.downMovement(tomPos)
                son.setNewCost(down)
                son.setTomPos(down)
                son.setHeuristic(self.Heuristic(son.getTomPos(), self.jerryPos))
                son.setSumCostHeuristic(son.getHeuristic() + son.getCost())
                # TODO: implement the heuristic logic

                son.moveDown(tomPos)
                if (son.compareCicles2(down)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()



            # Check if up-side is free
            if (not (tomPos[0]-1 < 0) and currentNode.getState()[tomPos[0]-1, tomPos[1]] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost()+1, currentNode.getStar(), currentNode.getFlower())

                up = son.upMovement(tomPos)
                son.setNewCost(up)
                son.setTomPos(up)
                son.setHeuristic(self.Heuristic(son.getTomPos(), self.jerryPos))
                son.setSumCostHeuristic(son.getHeuristic() + son.getCost())

                # TODO: implement the heuristic logic

                son.moveUp(tomPos)
                if (son.compareCicles2(up)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()


            # TODO Update the stack
            stack.remove(currentNode)
            # TODO: define currentNode
            currentNode = self.getNodeMinSumCostHeuristic(stack)

            expandedNodes += 1
            tomPos = currentNode.getTomPos()
        

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("Expanded nodes: ", expandedNodes+1)  # Good
        print("Depth: ", depth)
        print("The final cost of the solution is: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes+1, depth]
