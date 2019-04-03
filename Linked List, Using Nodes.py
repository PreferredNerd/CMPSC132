#Lab #9
#Due Date: 03/01/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: Just me and, TA LL
#  
########################################


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        

                          
class OrderedLinkedList:
    #Initialize a new Ordered Linked List with behaviour no node and no head nor tail
    def __init__(self):
    	#You can add a count attribute for len
        self.head=None
        self.tail=None
        self.count=0

    #Define a striung representation of the object
    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    # Transform the is empty boolean to be a property rather than a method. Makes it more accessable.
    @property
    def isEmpty(self):
        #write your code here
        #Determine if the head opbject is instantiated. If not return so.
        if self.head is None:
            return True
        else:
            return False

    def __len__(self):
        #write your code here
        #Iterate uyntil there is no longer a head object (meaning you hit the tail) Count through the amount of iteratioms
        #I suppose this could have been delt with a strait while (while is not = self.tail but whatever) Dont mind my
        #Worthless digressions.
        curentPosition = self.head
        self.count = 0
        while curentPosition != None:
            self.count += 1
            curentPosition = curentPosition.next
        return self.count


    def add(self, value):
        #write your code here
        #Create the node with the passed in parameter
        appendingNode = Node(value)
        #If it is empty, use the appending node to set both the head and tail to the appending node object
        if self.isEmpty:
            self.head = appendingNode
            self.tail = appendingNode
        #Handle special case of length one, and determine weather or not the value of the new node being passed in is
        #Greater than or less than the current head object, place it appropriatley, and link the new head and tail resp.
        elif len(self) == 1:
            if appendingNode.value <= self.head.value:
                 self.head.next = appendingNode
                 self.tail = appendingNode
            else:
                self.tail = self.head
                self.head = appendingNode
                self.head.next = self.tail
        #Explicate a general case of list length greater than 1
        else:

            #Accounting for it being the new head, i.e. the Largest Number
            if self.head.value < appendingNode.value:
                oldHead = self.head
                self.head = appendingNode
                appendingNode.next = oldHead

            #Account for it being the end, new tail;
            if self.tail.value > appendingNode.value:
                oldTail = self.tail
                self.tail = appendingNode
                oldTail.next = self.tail
                print(self.tail.next)

            #Account for it being somewhere in the middle of the chain
            current = self.head
            previous = self.head

            #Find the position at which to insert the new object
            while current:
                if appendingNode.value <= current.value:
                    previous = current
                    current = current.next
                else:
                    break

            #Link the new node appropriatley, old head points to the new node object and the new node's tail point to the
            #Following one
            oldTo = current
            previous.next = appendingNode
            appendingNode.next = oldTo

    def pop(self):
        #write your code here
        #Detrmine if the chain is empty and warn the user than they are performing an illegal operation
        if self.isEmpty:
            return "List is empty"
        #Handle special case of length one. Set the head and tail = to nothing. And return the previous #'s Value
        elif len(self) == 1:
            oldTailValue = self.head.value
            self.head = None
            self.tail = None
            return oldTailValue
        #Handle General case of len > 1.
        else:
            current = self.head
            previous = self.head
            #Iterate through the chain until you reach the position of current = tailObject; meaning that the previous
            # object will be at the proper position to become the next Chain Tail.
            for currentIteration in range(len(self)):
                if (current is self.tail):
                    break
                else:
                    previous = current
                    current = current.next
            #update Old Tail appropriate; Handle return values.
            oldTailValue = self.tail.value
            self.tail = previous
            self.tail.next = None
            return oldTailValue