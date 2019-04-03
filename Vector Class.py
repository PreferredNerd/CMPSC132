#Lab #6
#Due Date: 02/08/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: All me and TA Lawrence Lee
#
########################################



class Vector:
    #Initialize the Vector object with a list.
    def __init__(self, vector_list):
        self.vector = vector_list

    #Overide the + operator so that we may interact with vecotr addition
    def __add__(self, other):
        #Ensure that the other parameter is in fact a Vector object otherwise throw an Error
        if type(other) == Vector:
            #Ensure that the other Vector object's list property is in fact of the same demension, else throw an error
            if len(self.vector) == len(other.vector):
                #Instantiate a return list that is empty.
                returnVector = []
                #Run through each element in the list and add them together, append the vector output.
                for currentRow in range(len(self.vector)):
                    returnVector.append(self.vector[currentRow] + other.vector[currentRow])
                #Create a new Vector object and prepare it for return
                newVector = Vector(returnVector)
                #Return the new Vector object
                return newVector
            else:
                return "Error - Invalid dimensions"
        else:
            return "Error - Invalid operation"

    def __mul__ (self, other):
        if type(other) == Vector:
            #Handle multiplication of two Vector objects take list and follow procedure as explicated above
            if len(self.vector) == len(other.vector):
                returnVector = []
                for currentRow in range(len(self.vector)):
                    returnVector.append(self.vector[currentRow] * other.vector[currentRow])
                returnNumber = 0
                for currentIndex in range(len(returnVector)):
                    returnNumber += returnVector[currentIndex]
                return returnNumber
        #Handel issues resulting from scalar mulitplication
        elif type(other) == int or type(other) == float:
            returnVector = []
            for currentRow in range(len(self.vector)):
                returnVector.append(self.vector[currentRow] * other)
            newVector = Vector(returnVector)
            return newVector
        else:
            return 'Error - Invalid operation'

    #Override and define equality.
    def __eq__(self, other):
        if type(other) == Vector:
            #Conduct simple list comparision and return weather the property of the two Vector objects are equivalent
            if len(self.vector) == len(other.vector):
                if self.vector == other.vector:
                    return True
                else:
                    return False

    def __sub__(self, other):
        #Follow the same methodology as described in the addition section
        if type(other) == Vector:
            returnVector = []
            if len(self.vector) == len(other.vector):
                for currentNumber in range(len(self.vector)):
                    returnVector.append(self.vector[currentNumber]-other.vector[currentNumber])
                newVector = Vector(returnVector)
                return newVector
            else:
                return "Error - Invalid dimensions"
        else:
            return "Error - Invalid operation"

    #Define the string (human readable) represetnation of our object
    def __str__(self):
        return "Vector("+str(self.vector)+")"
    #Set the representation of our object: the objects representaiton (unambigious)
    __repr__ = __str__

    #Ensure that the first failure of operations performed on Vectors can be handled
    def __rsub__(self, other):
        return "Error - Invalid operation"

    def __radd__(self, other):
        return "Error - Invalid operation"
    #Special error handeling with regards to multiplication in the reverse order. handles this error by sending the
    #multiplication in the proper order back to the __mul__ override.
    def __rmul__(self, other):
        return self * other