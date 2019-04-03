#Lab #10
#Due Date: 03/15/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: Course materials: the videos on the website were crucial to my completion of this task.
#  
########################################

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
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        #write your code here\
        if len(self) == 0:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty() == True:
            return "Stack is empty"
        else:
            return self.top.value

    def push(self,value):
        #write your code here
        #Create a new node and add it to the top of the stack, point to the next value in the stack at that point
        appendingNode = Node(value)
        appendingNode.next = self.top
        self.top = appendingNode

    def pop(self):
        #Determine weather or not there is anything to pop!
        if self.isEmpty() == True:
            return "Stack is empty"
        else:
            #Hold old value, unchain old vlaue, return old value
            topValue = self.top.value
            valueUnderTop = self.top.next
            self.top = valueUnderTop
            return topValue

    def __len__(self):
    # write your code here
    #Find length by determining the amount of objects in the Stack using a while loop looking for no further connections.
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