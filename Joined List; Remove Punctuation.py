#Lab #2
#Due Date: 01/25/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement:  Access of course materials and resources. Personal Knowledge.
#
########################################


def joinedList(n):
    outputArray = []
    if type(n) == int:
        if n > 0:
            for currentNumber in range(n):
                outputArray.append(currentNumber+1)
            for currentNumber in range(n):
                outputArray.append(n-currentNumber)
        elif n < 0:
            for currentNumber in range(n*-1):
                outputArray.append(n+currentNumber)
            for currentNumber in range(n*-1):
                outputArray.append(-1*(currentNumber)-1)
        return outputArray
    else:
        return "error"

def removePunctuation(txt):
    # --- YOU CODE STARTS HERE
    returnString = ""
    if type(txt) == str:
        for letter in txt:
            if letter.isalpha():
                returnString += letter
            else:
                returnString += ' '
        return returnString
    else:
        return "error"