#LAB 15
#Due Date: 04/05/2019, 11:59PM
########################################
#
# Name: Nicholas C. Birosik
# Collaboration Statement: Just me and Larry Lee. I also consulted Arron for help with the floor division aspect of the
# Second part of the assignment. I thought I had seen this concept dealt with in the heap sorting algorithm!
#
########################################


def merge(list1, list2):
    # write your code here
    # Explicate (instantiate) our variables, first index, second index, current count and our output merged array
    indexOne, indexTwo, currentCount = 0,0,0
    outputList = []

    #Control the number of iterations bassed on the length of the two lists as a maximum number of iterations
    #Better to use a while statement than a for loop with a break statement!
    while currentCount < len(list1) + len(list2):
        #Ensure that the input that we are given is within the bounds of the passed in parameters
        if indexOne < len(list1) and indexTwo < len(list2):
            #Determine the values at the current index of each of the lists and append the smaller of the two.
            if list1[indexOne] < list2[indexTwo]:
                outputList.append(list1[indexOne])
                indexOne += 1
            #Take appropriate action if value of list one at the current index is greater than that of list two
            else:
                outputList.append(list2[indexTwo])
                indexTwo += 1
            #Advance the current count of the output list by one
            currentCount += 1
        #Now, if we passed through the entierty of the list, take specific action to merege the two halves.
        else:
            #Take care of having passed through all of list1 and add list2 to it
            if indexOne >= len(list1):
                #Operate between current value fo indexTwo and the len(of the list)
                for x in range(indexTwo, len(list2)):
                    outputList.append(list2[x])
                    currentCount += 1
            #Otherwise, add list one to list 2
            elif indexTwo >= len(list2):
                # Operate between current value fo indexTwo and the len(of the list)
                for x in range(indexOne, len(list1)):
                    outputList.append(list1[x])
                    currentCount += 1
    #return the compounded list as the completed list.
    return outputList

def mergeSort(numList):
    # write your code here
    #Find the middle of the input array; so that we can send half of it into the mergeSort again.
    middleOfInput = len(numList) // 2

    #Create a base case so we can work down to the bottom of our expression
    if len(numList) == 1: return numList
    elif len(numList) < 1: return "An error occurred"

    #Call mergeSort function repeatedly scanning and selecting the first half the list after each iteration
    firstComponent = mergeSort(numList[:middleOfInput])
    # Call mergeSort function repeatedly scanning and selecting the second half the list after each iteration
    secondComponent = mergeSort(numList[middleOfInput:])

    #Return a sorted list to each iteration call, until it reaches the base case where there is only one element left
    return merge(firstComponent, secondComponent)