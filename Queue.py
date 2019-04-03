#Lab #11
#Due Date: 03/15/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: Class Materials.
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    def __init__(self): 
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def __len__(self):
        #write your code here
        if self.head == None:
            return 0
        elif self.head == self.tail:
            return 1
        else:
            #Count starts at one to account for the head node starting it off
            count = 1
            currentQueuePosition = self.head
            while currentQueuePosition != self.tail:
                count += 1
                currentQueuePosition = currentQueuePosition.next
            return count


    def enqueue(self, value):
        #write your code here
        #Factor a quanity of appendingNode out of all functions to stop resuing code.
        appendingNode = Node(value)
        #Set state up if it returns empty queue
        if self.isEmpty() == True:
            self.head = appendingNode
            self.tail = appendingNode
            #Address speciual case where there is only one node in queue
        elif len(self) == 1:
            self.head.next = appendingNode
            self.tail = appendingNode
            #Perscribe general solution to all cases.
        else:
            self.tail.next = appendingNode
            self.tail = appendingNode



    def dequeue(self):
    #write your code here
    #determine if there is anything to be dequeued
        if self.isEmpty() == True:
            return "Queue is empty"
        #Handle specail case of only one item remaining in queue
        elif len(self) == 1:
            topData = self.head.value
            self.head = None
            self.tail = None
            return topData
        #Write genral case to perserve data of old head, and then unhook the node and return old head value and new head
        else:
            topData = self.head.value
            self.head = self.head.next
            return topData
