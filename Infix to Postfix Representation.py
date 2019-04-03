# HW 4
# Due Date: 02/01/2019, 11:59PM
########################################
#
# Name: Nicholas C. Birosik
# Collaboration Statement: Just me, my previous code, Griselda's helpful homework intructions, TA Larry Lee,
# http://condor.depaul.edu/ichu/csc415/notes/notes9/Infix.htm; for general discussion on how I should be pushing
# items to stacks, http://csis.pace.edu/~wolf/CS122/infix-postfix.htm; further diving into how to iterate through.
#
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

def findNextOpr(txt):
    currentPosition = 0
    # Check each charecter to determine if it is an arethmetic operator or not
    for currentCharecter in txt:
        if currentCharecter == '*' or currentCharecter == '+' or currentCharecter == '-' or currentCharecter == '/' or currentCharecter == '^':
            # If so, return the current position of it
            return currentPosition
        currentPosition += 1
    # If it is not, return -1, designating an arthmetic operator is not present in the string
    return (-1)


def isNumber(txt):
    if not isinstance(txt, str) or len(txt) == 0:
        return "error: isNumber"
    # --- YOU CODE STARTS HERE
    try:
        float(txt)
        return (True)
    except ValueError:
        return (False)

def getNextNumber(expr, pos):

    if not isinstance(expr, str) or not isinstance(pos, int) or len(expr)==0 or pos<0 or pos>=len(expr):
        return None, None, "error: getNextNumber"
    # --- YOU CODE STARTS HERE
    newNum = None
    #We will take in the expression and trim it straight off the bat because we only care about what is after index(pos)
    expr = expr[pos:]
    spacesBeforeFirstIncident = 0
    #Next we will strip all of the white space off of the expression before our next operator or operand
    #Use try except block to determine if the passed in values are legitimate / return 'error' to throw flag to calling methods
    try:
        while expr[spacesBeforeFirstIncident] == " ": spacesBeforeFirstIncident += 1
    except IndexError:
        return "error, illegal expression"
    #Remove all of these white spaces, by updating the expression based on first non-space index value
    expr = expr[spacesBeforeFirstIncident:]
    #Set operator position to the index of the next operaor in our expression expr, using our written function findNextOpr
    oprPos = findNextOpr(expr)
    #Programmed to return a -1 if their is no operator found in our expression, handle return variable setting
    #If there exists something handle getting the value of the operator at position [oprPos]
    if oprPos != -1:
        nextOpr = expr[oprPos]
        #Handle the envent that it is a negative number
        if nextOpr == "-" and oprPos == 0:
            #Use our favorite: recursion! to call this function again to obtain return tuple of values after -.
            numberAfterNegativeSign, nextOpr, oprPos = getNextNumber(expr,1)
            #Cast the returned value to a flaot, multiply by -1 to get the actual next number in the neagtive sequence
            newNum = -1* float(numberAfterNegativeSign)
            #If the finNextOpr in our recursion call returns a -1, meaning there is not another opr, return what we have established
            if nextOpr is None:
                return newNum, nextOpr, oprPos
            #Otherwise, return the next num, the next operator, and position amended with the predecesing whitespace
            return newNum, nextOpr, oprPos + spacesBeforeFirstIncident + pos
        #Determine if what we found before the current operator housed a number, cut expr = itself until the current scanning point
        elif isNumber(expr[:oprPos]):
            #If it evasluates to be, make that stroip a permanent modification, by performing the same splice as above.
            expr = expr[:oprPos]
            #Save the float value of this string so it may be returned later.
            newNum = float(expr)
    #Otherwise handle return value handeling if there were no operators in the expression.
    else:
        oprPos = None
        nextOpr = None
    #Determine if there are any hanging numbers at the end of the string; may be the case even though there are no operators
    #For example think of either a single number -- account for recursion
    if oprPos is None:
        # Save the float value of this string so it may be returned later.
        if isNumber(expr): newNum = float(expr)
    #Handle Special return case where there is no operator, to mitigate foreseeable problems with None type addition
    #No overrides for type none in this code!
    if oprPos is None: return newNum, nextOpr, oprPos
    #Otherwise return the completed tuple!
    else: return newNum, nextOpr, oprPos + pos + spacesBeforeFirstIncident + 1




def postfix(expr):
    #Determine if the expression is illegal by setting up counting variables
    numberOfNumbers = 0
    numberOfOperands = 0
    nextNumber = 0
    nextOperator = 0
    nextOperatorPosition = 0
    postfixString = ''
    operatorStack = Stack()
    precendenceDictionary = {'^':3, '*':2, '/':2, '+':1, '-':1}

    #Try block to acount for errors arising from two operators next to each other
    try:
        # Continue the loop until there is no more operators
        while nextOperator != None:
            #Set using tuple operation.
            nextNumber, nextOperator, nextOperatorPosition = getNextNumber(expr,nextOperatorPosition)
            #Account for the illegal cases by keeping record of how many numbers and operator total
            if nextNumber != None: numberOfNumbers += 1
            if nextOperator != None: numberOfOperands += 1
            #Add the number to the output string
            postfixString += str(nextNumber) + " "
            #Push to stack if empty, determine precedence otherwise
            if len(operatorStack) == 0:
                operatorStack.push(nextOperator)
            else:
                #Remeber states can change before they are put back into the while loop; dfetermine if the opr is none!
                if nextOperator != None:
                    try:
                        #Check precedence level of PEMDAS; and iterate through until lower precendece found
                        while precendenceDictionary[operatorStack.peek()] >= precendenceDictionary[nextOperator]:
                            postfixString += str(operatorStack.pop()) + " "
                        operatorStack.push(nextOperator)
                    #Meaning we hit the end of all operators in that list. Time to push the other.
                    except KeyError:
                        operatorStack.push(nextOperator)
                else:
                    #Push the remaining valuies of teh stack to the end of the postfix expression
                    while len(operatorStack) > 0:
                        postfixString += str(operatorStack.pop())

    except ValueError:
        return 'error, invalid expression'
    #Amend the return stastement to determine weather or not there are no operancds, or it operands are more than numbers,
    #  or if numbers are two more than operands
    #Use the try except block to determine if it is only a single number or not.
    try:
        return str(float(postfixString)) #Honestly used to strip to end white space...
    except:
        if numberOfNumbers - numberOfOperands != 1:
            return "error, invalid expression"
        return postfixString