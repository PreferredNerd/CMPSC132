#Lab #8
#Due Date: 02/22/2019, 11:59PM
########################################
#                                      
# Name: Nicholas Birosik
# Collaboration Statement: Actually only me, TA Lee.
#
########################################

import sys

def isPrime(n, userDefinedNumber = 0):
    if n>=1:
        try:
            # Checking if this is the first run, meaning we need to set our instantiation cases
            if userDefinedNumber == 0:
                userDefinedNumber = n
                if n >= 1000:
                    sys.setrecursionlimit(n)
                n = n-1


            #Determine if there is an illegal entry
            if n <= 1:
                return False
            #Determine if the number has reached the lower modular division point, and return a success to all the higher calls
            elif n == 2:
                return True
            else:
                #Use modular division with the original userDefinedNumber to determine if there does exist another valid divisior
                if userDefinedNumber % n != 0:
                    #If not, pass along the current number in the call to our same function as well as the original number passed
                    return isPrime(n - 1, userDefinedNumber)
                else:
                    return False
        except MemoryError:
            return "You entered a number which has caused a memory error, attempt the operation again with a smaller number!"
    else:
        return "Try entering a positive non zero number next time: ERROR"
