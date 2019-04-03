#Lab #1
#Due Date: 01/11/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: By myself and with the help of the course materials including LAs.            
#
########################################


def sumSquares(aList):
    sumOfTheSquares = 0.0
    if type(aList) != list:
        return 'error'
    else:
        for currentElement in range(len(aList)):
            currentTestElement = aList[currentElement]
            if type(currentTestElement) == str and currentTestElement.lstrip('-').isdigit():
                aList[currentElement] = float(aList[currentElement])
            if type(aList[currentElement]) == int or type(aList[currentElement]) == float:
                sumOfTheSquares += (aList[currentElement] ** 2)
        return sumOfTheSquares

