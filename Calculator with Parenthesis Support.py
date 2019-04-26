# HW 5
# Due Date: 04/16/2019, 11:59PM
########################################
#
# Name: Nicholas C. Birosik
# Collaboration Statement: Just me, my previous code, Griselda's helpful homework intructions, TA Larry Lee.
#
########################################
#NODE AND STACK IMPLEMENTATION
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
    if not isinstance(txt, str) or len(txt)==0:
        return "error: isNumber"
    # --- YOU CODE STARTS HERE
    try:
        float(txt.replace(')', '').replace('(', '')) #Updated with the parenthetical requirements of this assiignment
        return (True)
    except:
        return (False)


def getNextNumber(expr, pos):
    if not isinstance(expr, str) or not isinstance(pos, int) or len(expr)==0 or pos<0 or pos>=len(expr):
        return None, None, "error: getNextNumber"
    # --- YOU CODE STARTS HERE
    #Instantiate variables
    stripParenthesis, nextOprerator, nextNumber, currentOpreratorPosition = expr.replace(')', ' ').replace('(', ' ') ,"","", 0
    weCareString = stripParenthesis[pos:].strip() #Parsed string with no parenthesis, after the given position: ie the stuff we actually care about; get rid of white space before

    #Take into consideration that we may start with a - sign (usuaually not allowed as operator predecencing number, make exception)
    if weCareString[0] == '-':
        positionOfMinus = findNextOpr(stripParenthesis[pos:]) + pos #Find where the minus position is
        currentOpreratorPosition = findNextOpr(stripParenthesis[positionOfMinus + 1:]) # Get the position of the next operator past the minus sign operator
        if currentOpreratorPosition != -1: #Address if there is another operator in this expresion
            currentOpreratorPosition = currentOpreratorPosition + positionOfMinus + 1 #Update the current operator position one beyond minus sign
            nextOprerator = stripParenthesis[currentOpreratorPosition] #Get the next operators value (+_*,etc.)
            nextNumber = stripParenthesis[pos:currentOpreratorPosition] #Find the number that lies between the given pos input and the next operator
        else:#Address concern of there not being another operator position in string
            nextOprerator,currentOpreratorPosition = None, None #Set to type none for it is not in the expression. Further, We cannot say there is a current operaator position if there indeed is not another operator!
            nextNumber = stripParenthesis[pos:] #Next number is going to be the nuimber beyond the user defined position input.
    else: #Ok, so lets adress not starting with a negative number.
        currentOpreratorPosition = findNextOpr(stripParenthesis[pos:]) #Update pos, with next operator pos
        if currentOpreratorPosition != -1: #Assuming that it exists, continue
            currentOpreratorPosition = currentOpreratorPosition + pos
            nextOprerator = stripParenthesis[currentOpreratorPosition]#Get the next operators value (+_*,etc.)
            nextNumber = stripParenthesis[pos:currentOpreratorPosition]#Find the number that lies between the minus sign and the next operator
        else: #set to same variables as above.
            nextOprerator, currentOpreratorPosition = None, None  # Set to type none for it is not in the expression. Further, We cannot say there is a current operaator position if there indeed is not another operator!
            nextNumber = stripParenthesis[pos:]  # Next number is going to be the nuimber beyond the user defined position input.

    if isNumber(nextNumber):return float(nextNumber.replace('(', '').replace(')', '').strip()), nextOprerator, currentOpreratorPosition #Return as adequate
    else: return None, nextOprerator, currentOpreratorPosition

def postfix(expr):
    #Instansitate all of the required variables including the stacks. Precedence stacks by squares (LOL).
    precedenceDictionary = {"^" : 25, "*" : 16, "/" : 16, "+" : 9, "-" : 9, "(" : 4}
    #Tuples for Life!!!!!!!
    outputPostFixExpression, opratorStack, parenthesisStack, endPositionIndex, currentPosition, splitExpressionString = "", Stack(), Stack(), 0, 0, expr.split()

    #Determine if the whole expression it self is a number or otherwise -- start by stripping the parenteticals to handle cases like-->(4)
    if isNumber(expr):
        return str(float(expr.replace('(', '').replace(')', '')))

    try:
        if splitExpressionString[0] in precedenceDictionary and precedenceDictionary[splitExpressionString[0]] > 4: raise parentheticalError

        #Shout out to TA Lee for the balanced parenthesis implementation idea!
        for currenCharecter in expr:
            if currenCharecter == "(":
                parenthesisStack.push(currenCharecter)
            elif currenCharecter == ")":
                if parenthesisStack.peek() == "(":
                    parenthesisStack.pop()
                else:
                    raise parenthesisError

        #Now that preliminary parentheticals / lone number issues are teaken care of, lets look thorugh and put in postfix order!
        while len(expr) > currentPosition:
            #Update the startPosition and endPosition with last iteration through this loop; set new end based on next number
            startPositionIndex = endPositionIndex
            number, nextOpr, oprPosition = getNextNumber(expr, currentPosition)
            endPositionIndex = oprPosition
            outputPostFixExpression += (str(number) + " ")

            #Use Griselda's methodology, as indecated in the home work packet to push open parenthesis and pop unitl open upon close contact.
            for currentOperator in expr[startPositionIndex:endPositionIndex]:
                if currentOperator == "(": opratorStack.push(currentOperator) #Push becasue of the open parenthesis
                elif currentOperator == ")":
                    while opratorStack.peek() != "(":
                        outputPostFixExpression += (str(opratorStack.pop()) + " ") #Otherwise pop and add to the output expression all the way down unitl the next top is an open parenthesis:
                    opratorStack.pop() # Finally pop that last pesky open parenthesis without adding to the postfix expression output

            #Now that parentesis iomplemntation is taken care of, go bakc to HW4 implementation
            #If it a number and the stack is empty push it through without bias.
            if isNumber(oprPosition) and opratorStack.isEmpty(): opratorStack.push(nextOpr)
            #Handle final case of if there is not another operator
            elif nextOpr is None:
                while len(opratorStack) != 0: #Continue until there the stack remains filled with at least one object
                    outputPostFixExpression += (str(opratorStack.pop()) + " ") #Add to the output string with the space!
                return outputPostFixExpression.rstrip() # We have hit the end of our operator input therefore we are ready to return the postfix string - the last " " that way added ala our while statement
            elif precedenceDictionary[nextOpr] > precedenceDictionary[opratorStack.peek()]: opratorStack.push(nextOpr)#Then compare wheater or not the precedence of the latter item in the stack is of less precedednce than current, if so push it!
            else:
                while len(opratorStack) != 0 and precedenceDictionary[nextOpr] <= precedenceDictionary[opratorStack.peek()]: outputPostFixExpression += (opratorStack.pop() + " ") #Handlke general case where the next operator is of lower or the same PEMDAS precendecne, push accoridngingly
                opratorStack.push(nextOpr)
            #We may have edited the stack during our prevoiuos handling. Ensure one last time to make sure that we have another oprator to use with the next iteration / else errors will occurr
            if nextOpr is None: return outputPostFixExpression.rstrip() #Again get rid of that last end space
            currentPosition = oprPosition + 1 #Continue the current position along form the index jsut past that of our last found operator.
        return outputPostFixExpression.rstrip()
    except:
        return "error, invalid expression"

def calculator(expression):
    precendenceDictionary = {'^': 5, '*': 4, '/': 3, '+': 2, '-': 1}
    postfixString = postfix(expression)
    print (postfixString)
    operandStack = Stack()
    #Run until there are no additional items in our postfix string
    while postfixString != "":
        firstWhiteSpace = postfixString.find(" ")
        #Meaning we are not yet at the end
        if firstWhiteSpace != -1:
            currentOperator = postfixString[:firstWhiteSpace]
        else:
            currentOperator = postfixString
        #Determine if what we have is a number or an operator
        if isNumber(currentOperator):
            operandStack.push(float(postfixString[:firstWhiteSpace]))
        #Its an operator so calculate it
        else:
            secondOperand, firstOperand, evalStatement = operandStack.pop(), operandStack.pop(), "" #They are put in backwards Remember!
            if precendenceDictionary[currentOperator] == 1:
                evalStatement = float(firstOperand) - float(secondOperand)
            elif precendenceDictionary[currentOperator] == 2:
                evalStatement = float(firstOperand) + float(secondOperand)
            elif precendenceDictionary[currentOperator] == 3:
                if secondOperand == 0: return "error: illegal division by 0!" #Catch illegal division error before proceding to division by zero!
                evalStatement = float(firstOperand) / float(secondOperand)
            elif precendenceDictionary[currentOperator] == 4:
                evalStatement = float(firstOperand) * float(secondOperand)
            elif precendenceDictionary[currentOperator] == 5:
                evalStatement = float(firstOperand) ** float(secondOperand)
            operandStack.push(evalStatement)

        if firstWhiteSpace != -1: postfixString = postfixString[firstWhiteSpace + 1:] # Continue on if there is whitespace left
        else:postfixString = "" #Else ensure that it is caught before next iteration!

    return (float(operandStack.pop()))



