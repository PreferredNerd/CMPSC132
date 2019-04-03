#HW 3
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: Just me, my restless nights, and dream like solutions (In all actuallity, though, the solution came to me in my dreams!).
#
########################################


def findNextOpr(txt):
    currentPosition = 0
    #Check each charecter to determine if it is an arethmetic operator or not
    for currentCharecter in txt:
        if currentCharecter == '*' or currentCharecter == '+' or currentCharecter == '-' or currentCharecter == '/' or currentCharecter == '^':
            #If so, return the current position of it
            return currentPosition
        currentPosition += 1
    # If it is not, return -1, designating an arthmetic operator is not present in the string
    return (-1)

def isNumber(txt):
    if not isinstance(txt, str) or len(txt)==0:
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
    updatedString = ""
    returnString = ""

    #Create a string that hold on the information that we care about.
    testString = ""
    for currentCharecter in range(len(expr)-pos):
        updatedString += str(expr[currentCharecter + pos])

    #Get position of first operator using the function as explicated above
    firstOperatorPosition = findNextOpr(updatedString)

    #Splice string check into in front of operator. Set initial states of the machine.
    beforeOperator = updatedString[:firstOperatorPosition]
    returnOne = 0.0
    hasChanged = False
    isNegative = False

    # if inFrontOfOperator;
    # If it is a number than first Return Value = floatThatNumber
    try:
        float(beforeOperator)
        returnOne = float(beforeOperator)
        hasChanged = True
    # If it is not check if the operator is a - else return first Return Value = None
    except ValueError:
        # If -, bool is negative true, splice away the operator, find next operator, splice to that point
        if updatedString[firstOperatorPosition] == '-':
            #Calls the isNumber Function as defined above
            if isNumber(updatedString[firstOperatorPosition+1]):
                isNegative = True
                updatedString = updatedString[firstOperatorPosition+1:]
                #Get Position of next operator, try again
                beforeOperator = updatedString[:firstOperatorPosition]
                try:
                    float(beforeOperator)
                    returnOne = float(beforeOperator)
                    hasChanged = True
                except ValueError:
                    returnOne = None
    if hasChanged == False:
        returnOne = None

    returnOperatorPosition = firstOperatorPosition

    # Else return operator, plus the position of +1 depending on if negative
    # Create a return negative value instance of that number
    if isNegative:
        #Add one to account for the difference of splicing away the negative operator
        returnOperatorPosition += 1
        #Self explanitory...
        returnOne *= -1

    #Prepare a consolidated return value for position of the new charecter
    returnOperatorPosition += pos

    #Ensure that there exists and instance of the operators position that is real, and lies within the string (Accounts
    # for the -1 return from the find operator function (designating that there does not exist a operator in substring))
    try:
        return returnOne, updatedString[firstOperatorPosition], returnOperatorPosition
    #Accounting for the negative one in the firstOperatorPosition!
    except IndexError:
        return returnOne, None, None