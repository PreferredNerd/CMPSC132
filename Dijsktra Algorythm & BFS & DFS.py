# HW 6
# Due Date: 04/26/2019, 11:59PM
########################################
#
# Name: Nicholas C. Birosik
# Collaboration Statement: Just me, and a late night call (rather email to TA Larry Lee)! Yes he did respond to my email, come down to me in
# in the lobby at 10:20pm just to help me with my Dijkstra implementation! I am not quite sure how his assement goes as a TA, but
# definatley deserves an A, for dedication and commitmant to truly caring as to weather or not us students are learning!
# Thank you all for a great year!
#
########################################
import math


# ---Copy your code from labs 10 and 11 here (you can remove their comments)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

        __repr__ = __str__


class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top, out))

    __repr__ = __str__

    def isEmpty(self):
        # write your code here\
        if len(self) == 0:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty() == True:
            return "Stack is empty"
        else:
            return self.top.value

    def push(self, value):
        # write your code here
        # Create a new node and add it to the top of the stack, point to the next value in the stack at that point
        appendingNode = Node(value)
        appendingNode.next = self.top
        self.top = appendingNode

    def pop(self):
        # Determine weather or not there is anything to pop!
        if self.isEmpty() == True:
            return "Stack is empty"
        else:
            # Hold old value, unchain old vlaue, return old value
            topValue = self.top.value
            valueUnderTop = self.top.next
            self.top = valueUnderTop
            return topValue

    def __len__(self):
        # write your code here
        # Find length by determining the amount of objects in the Stack using a while loop looking for no further connections.
        if self.top == None:
            return 0
        else:
            # Count starting at one accounts for the starting node, head.
            count = 1
            currentNode = self.top
            while currentNode.next != None:
                count += 1
                currentNode = currentNode.next
            return count


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp = self.head
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = ' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head, self.tail, out))

    __repr__ = __str__

    def isEmpty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def __len__(self):
        # write your code here
        if self.head == None:
            return 0
        elif self.head == self.tail:
            return 1
        else:
            # Count starts at one to account for the head node starting it off
            count = 1
            currentQueuePosition = self.head
            while currentQueuePosition != self.tail:
                count += 1
                currentQueuePosition = currentQueuePosition.next
            return count

    def enqueue(self, value):
        # write your code here
        # Factor a quanity of appendingNode out of all functions to stop resuing code.
        appendingNode = Node(value)
        # Set state up if it returns empty queue
        if self.isEmpty() == True:
            self.head = appendingNode
            self.tail = appendingNode
            # Address speciual case where there is only one node in queue
        elif len(self) == 1:
            self.head.next = appendingNode
            self.tail = appendingNode
            # Perscribe general solution to all cases.
        else:
            self.tail.next = appendingNode
            self.tail = appendingNode

    def dequeue(self):
        # write your code here
        # determine if there is anything to be dequeued
        if self.isEmpty() == True:
            return "Queue is empty"
        # Handle specail case of only one item remaining in queue
        elif len(self) == 1:
            topData = self.head.value
            self.head = None
            self.tail = None
            return topData
        # Write genral case to perserve data of old head, and then unhook the node and return old head value and new head
        else:
            topData = self.head.value
            self.head = self.head.next
            return topData


# ----- HW6 Graph code
class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr

    def bfs(self, start):
        # Your code starts here
        mainQueue = Queue()
        vistedNodes = []
        mainQueue.enqueue(start)
        #See if the requested Node is actually in the passed through dictionary as per Pizzas Recommendation
        if start not in self.vertList:
            return 'error BFS: starting Node not in Given Dictionary'
        vistedNodes.append(start)
        while len(mainQueue) != 0:
            dequeuedNode = mainQueue.dequeue()
            for currentNode in sorted(self.vertList[dequeuedNode]):
                if type(currentNode) == tuple:
                    currentNode = currentNode[0]
                if currentNode not in vistedNodes:
                    mainQueue.enqueue(currentNode)
                    vistedNodes.append(currentNode)
        return vistedNodes

    def dfs(self, start):
        # Your code starts here
        # See if the requested Node is actually in the passed through dictionary as per Pizzas Recommendation
        if start not in self.vertList:
            return 'error DFS: starting Node not in Given Dictionary'
        mainStack = Stack()
        visitedNodes = []
        mainStack.push(start)
        while len(mainStack) != 0:
            poppedNode = mainStack.pop()
            if type(poppedNode) == tuple:
                poppedNode = poppedNode[0]
            if poppedNode not in visitedNodes:
                visitedNodes.append(poppedNode)
                # Determine if in tuple form or otherwise
                for currentNode in sorted(self.vertList[poppedNode], reverse=True):
                    if currentNode not in visitedNodes:
                        mainStack.push(currentNode)
        return visitedNodes

    def dijkstra(self, start):
        # Start with Error Handleing, ALA Piazza, Ms. Griselda and TA Larry Lee!
        # See if the requested starting node is even in the instantiated dictionary
        if start not in self.vertList:
            return 'error Dijkstra: starting Node not in Given Dictionary'
        # Instantiate the nextNode, Output Dictionary, and List of Nodes to be visited.
        nextNodeToVisit, dijkstraOutputDict, vistedNodeList = start, {}, []

        # Iterate over all the current keys in the graph dicitonary, and assign new value of infinity.
        for currentKey in self.vertList: dijkstraOutputDict[currentKey] = math.inf
        # Don't forget to reset the current starting Node's value to 0!
        dijkstraOutputDict[start] = 0

        # Continue this process until they are both full
        while len(vistedNodeList) != len(dijkstraOutputDict):
            for currentNode in dijkstraOutputDict:
                if currentNode not in vistedNodeList:
                    nextNodeToVisit = currentNode
                    # Break out and return the output Dict.
                    break

            # Go through all of the nodes in the list again and see weather or not A.) the node has already been visited & B.) determine which cost benefit is best for the next node path.
            for currentNode in dijkstraOutputDict:
                if currentNode not in vistedNodeList:
                    if dijkstraOutputDict[currentNode] < dijkstraOutputDict[nextNodeToVisit]:
                        nextNodeToVisit = currentNode

            # Go through all of the nodes in the output and then run the shortest path comparision.
            for currentNode in self.vertList[nextNodeToVisit]:
                distanceBetweenNext = dijkstraOutputDict[nextNodeToVisit] + currentNode[1]
                # Determine if there are any negatives in the vertList: if so return error!
                if currentNode[1] < 0: return 'error: negative weight is illegal'
                elif distanceBetweenNext < dijkstraOutputDict[currentNode[0]]: dijkstraOutputDict[currentNode[0]] = distanceBetweenNext
            vistedNodeList.append(nextNodeToVisit)

        return dijkstraOutputDict
