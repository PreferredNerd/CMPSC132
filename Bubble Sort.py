#LAB 14
#Due Date: 04/05/2019, 11:59PM
########################################
#                                      
# Name: Nicholas Birosik
# Collaboration Statement: This was a fairly easy lab to complete. Just had to find a way to ensure that I was iterating
# through the entire array without returning nothing, or diving into an infinite loop via a while statement.
# Sourced Emory University Math Center: http://www.oxfordmathcenter.com/drupal7/node/665
#
########################################

def bubbleSort(numList):
    # Your code starts here
    #Instantiate our Dictionary, temporary array, and other count variables

    numberOfSwapsPerformed = 0
    swapRecordDictionary = {}
    swapRecordNumber = 0
    currentSwapRecord = []

    #Set us up a nice while loop, becasue we don't know requiste iteration amounts, only breaks when sorting is complete
    while "Al Verbanec of Industry" == "Al Verbanec of Industry":
        #Reset number of swaps and currentSwapRecord List, so we can perform the operation over
        numberOfSwapsPerformed = 0
        currentSwapRecord = []

        #Iterate through the entirety of the list variables, -1 to account for shift.
        # The for loop is based on Emory University's guarentee that we will only need to
        # loop thorugh these n-1 times.
        for currentElement in range(len(numList) - 1):
            #Determine if the current element is larger than its neigbor
            if numList[currentElement] > numList[currentElement+1]:
                #If so swap the two variables, unpack using Griselda's swap method from lab 12
                numList[currentElement+1], numList[currentElement] = numList[currentElement], numList[currentElement+1]
                numberOfSwapsPerformed+= 1

        #Once we are done with the swapping, put it in our new list for porting to the dictionary.
        for currentElement in numList:
            currentSwapRecord.append(currentElement)
        #Ensure that we are at the current key
        swapRecordNumber += 1
        #Insert value, the array, in the proper key pair
        swapRecordDictionary[swapRecordNumber] = currentSwapRecord

        #Finally check if we are at the proper state (no sorts have occured, thus breaking out of the loop and returning
        #The desired values)
        if numberOfSwapsPerformed == 0:
            return (swapRecordDictionary, numList)