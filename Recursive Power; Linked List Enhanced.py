#Quiz 2 - Coding Part
#March 28th, 2019
#NICHOLAS C. BIROSIK
#######################


## QUESTION 1
def power(x,n):
    #Base Case is zero
    if n == 0: return 1
    #Standard Case returning and subtracting one from the exponent
    if n > 1: return x * power(x,n-1)


## QUESTION 2
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 

    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__
                          
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        current=self.head
        out=[]
        while current:
            out.append(str(current.value))
            current=current.next
        out=' '.join(out)
        return 'Head:{}, Tail:{}\nList:{}'.format(self.head, self.tail,out)

    __repr__=__str__

    def __len__(self):
        return self.count

    def append(self, value):
        #If it is not a linked list that we are appending
        if type(value) != type(LinkedList()):
            new_node=Node(value)
            if self.head is None:
                self.head=new_node
                self.tail=new_node
            else:
                self.tail.next=new_node
                self.tail=new_node
            self.count+=1
        else:
        #Iterate through the linked list values that were passed in
            while value.head != None:
                #Create a new node based on the current value of the current position in second list
                currentNode = value.head
                #Determine if the first is empty or not.
                if self.head is None:
                #If it is then set the current lsit head and tail equal to the current value in the second
                    self.head = currentNode
                    self.tail = currentNode
                    #Move the value along by settign the current head position equal to the next position in the second list
                    value.head = value.head.next
                    # Add to the count of Nodes!
                    self.count += 1
                else:
                    #Set the end of the current list = to the new node,
                    self.tail.next = currentNode
                    #Set the end of the current tail to this new node as the new end
                    self.tail = currentNode
                    #Update the value current position in the new list to be the next in the sequence
                    value.head = value.head.next
                    #Add to the count of Nodes!
                    self.count += 1