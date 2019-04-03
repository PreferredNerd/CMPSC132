#Lab #12
#Due Date: 03/24/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: None, just me and TA Larry.
#  
########################################


class MaxHeapPriorityQueue:
    def __init__(self):
        self.heap=[]
        self.size = 0

    def __len__(self):
        return len(self.heap)

    def parent(self,index):
        #Take the supplied index and ensure that it is not the root or smaller and that it is not larger than the size
        #of the heap array itself
        if index <= 1 or index > len(self): return None
        else: return self.heap[(index // 2)-1]

    def swap(self, index1, index2):
        self.heap[index1 - 1], self.heap[index2 - 1] = self.heap[index2 - 1], self.heap[index1 - 1]

    def leftChild(self,index):
        #Determine weather or not the requested child is out of the bounds of the array, if so return None.
        if 2*index < len(self): return self.heap[(2 * index) - 1]
        else: return None

    def rightChild(self,index):
        # Determine weather or not the requested child is out of the bounds of the array, if so return None.
        if (2*index) - 1 < len(self): return self.heap[(2 * index)]
        else: return None


    def insert(self,x):
        # Determine how long the size of the list is; if zero, start off by just appending it
        if self.size == 0:
            self.heap.append(x)
            self.size += 1
        else:
            #Insert and start the sorting methodology
            self.heap.append(x)
            newNodeIndex = self.heap.index(x)
            if newNodeIndex == 1:
                newNodeParentIndex = 1
                parentNode = self.heap[0]
            else:
                # Otherwise, utilze floor division calculations to find where parent is.
                newNodeParentIndex = ((newNodeIndex + 1) // 2)
                parentNode = self.heap[newNodeParentIndex - 1]
            while parentNode < x:
                # Commece the switching operations between parents and children until the condition for MAX heap is satisfied
                self.swap(newNodeParentIndex, newNodeIndex + 1)
                newNodeIndex = self.heap.index(x)
                # Determine if it lies at the root and terminate the while loop -- Beware infinte looping
                if newNodeIndex == 0: break
                # Update Parent indec
                newNodeParentIndex = ((newNodeIndex + 1) // 2)
                parentNode = self.heap[newNodeParentIndex - 1]
            self.size += 1


    def deleteMax(self):
        # Determine if there is actually anything to delete
        if self.size <= 0:
            return None
        # Determine if there is 1 element and address special case
        elif self.size == 1:
            self.size = 0
            maximumValue = self.heap[0]
            self.heap = []
            return maximumValue
        # Work with general case or 2 or more elements
        else:
            # Swap first and last element, pop last element, grab return value into max value
            heapLength = len(self.heap)
            childValue = self.heap[heapLength - 1]
            childIndex = self.heap.index(childValue) + 1
            self.swap(1, childIndex)
            maximumValue = self.heap.pop(heapLength - 1)
            # decrease the size of the heap by one, Becasue we just got rid of the maximum number.
            self.size -= 1
            #Set Left and right childrens popstions in terms of their list positions.
            leftChild = 1
            rightChild = 2
            # Lets check if there even are right and left children to begin with!
            if leftChild and rightChild in range(len(self.heap)):
                currentRight = self.heap[leftChild]
                currentLeft = self.heap[rightChild]
                #Determine with sibling is the largest.
                if currentRight > currentLeft:
                    currentMax = currentRight
                    # Handle Empty Heap condition
                else:
                    currentMax = currentLeft
                    # Compare children to root, if they exist
            elif leftChild and not rightChild in range(len(self.heap)): currentMax = self.heap[rightChild]
            elif rightChild and not leftChild in range(len(self.heap)): currentMax = self.heap[rightChild]
            else:
                self.size = 0
                self.heap = []
                return maximumValue
            # I don't know about you but this whole working with an appended list +1 for the trees is hard, store list positons for clarity
            currentIndex = self.heap.index(currentMax)

            while currentMax > childValue:
                self.swap(currentIndex + 1, self.heap.index(childValue) + 1)
                #Again for clarity purposes
                newIndex = currentIndex + 1
                #update right and left child for current swapping iteration
                rightChild = newIndex * 2
                leftChild = newIndex * 2 - 1
                #Are we actually holding the child, like Mrs. Griselda and her kid, or is the variable holding type(None); if so define it as such...
                if leftChild in range(len(self.heap)): currentRight = self.heap[leftChild]
                else: currentRight = None
                if rightChild in range(len(self.heap)): currentLeft = self.heap[rightChild]
                else: currentLeft = None
                if currentRight and currentLeft is not None:
                    if currentRight > currentLeft:
                        currentMax = currentRight
                    else:
                        currentMax = currentLeft
                # Ensure that any sibling that contains something and the other none, returns the other by default
                elif currentRight and not currentLeft is None: currentMax = currentLeft
                elif currentRight and not currentLeft is not None: currentMax = currentRight
                elif currentRight is None and currentLeft is None: break
                currentIndex = self.heap.index(currentMax)
            return maximumValue