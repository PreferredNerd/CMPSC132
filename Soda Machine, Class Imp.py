#Lab #5
#Due Date: 02/08/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: TA Lawerence Lee!
#
########################################
import math

class SodaMachine:
    def __init__(self, product, price):
        #-- start code here ---
        #Set the initial state fo the program
        #Define errors for setting up the machine wrong
        if price < 0:
            return "error, invalid price"
        self.product = product
        self.price = price
        self.quantity = 0
        self.amountDeposited = 0


    def purchase(self):
    #-- start code here ---
    #Self explanatory casing to ensure adequate resutlts
        if self.quantity == 0 and self.amountDeposited > 0:
            changeToTender = self.amountDeposited
            self.amountDeposited = 0
            return ('Sorry, out of stock. Take your' + changeToTender + 'back')
        elif self.quantity == 0 and self.amountDeposited == 0:
            return "Product out of stock"
        elif self.amountDeposited == self.price:
            self.amountDeposited = 0
            self.quantity -= 1
            return str(self.product) + " dispensed"
        elif self.amountDeposited < self.price:
            return "Please deposit $" + str(self.price - self.amountDeposited)
        elif self.amountDeposited > self.price:
            changeToTender = self.amountDeposited - self.price
            self.amountDeposited = 0
            self.quantity -= 1
            return  str(self.product) + " dispensed, take your $" + str(changeToTender)


    def deposit(self, amount):
        #-- start code here ---
        if self.quantity != 0:
            if amount < 0:
                return "error, you cant steal from the machine. Put money in!"
            else:
                self.amountDeposited += amount
                return "Balance: $" + str(self.amountDeposited)
        else:
            return "Sorry, out of stock. Take your $" + str(amount) + " back"


    def restock(self, amount):
        #-- start code here ---
        if amount < 0:
            return "error, invalid restock number"
        else:
            self.quantity += amount
            return "Current soda stock: " + str(self.quantity)



class Line:
    """
         Creates objects of the class Line, takes 2 tuples. Class must have 2 PROPERTY methods
         >>> line1=Line((-7,-9),(1,5.6))
         >>> line1.distance
         16.648
         >>> line1.slope
         1.825
         >>> line2=Line((2,4),(2,3))
         >>> line2.distance
         22
         >>> line2.slope
         'Infinity'
     """
    def __init__(self, coord1, coord2):
        #-- start code here ---
        # Ensure that we are recieveing info that this expected, two tuples of length two and two ints or floats
        if type(coord1) == tuple and type(coord2) == tuple:
            if len(coord1) == 2 and len(coord2) == 2:
                self.xCoordinateFirstPair, self.yCoordinateFirstPair = coord1
                self.xCoordinateSecondPair, self.yCoordinateSecondPair = coord2
                if not ((type(self.xCoordinateFirstPair) == int or type(self.xCoordinateFirstPair) == float) and (type(self.yCoordinateFirstPair) == int or type(self.yCoordinateFirstPair) == float) and (type(self.xCoordinateSecondPair) == int or type(self.xCoordinateSecondPair) == float) and (type(self.yCoordinateSecondPair) == int or type(self.yCoordinateSecondPair) == float)):
                    return "Error! Tuple does not hold either int or float variable for either or poth coordinate pair!"
            else:
                return "Tuple size error! Ensure the tuple you pass in has two components exactly!"
        else:
            return "Type Error, ensure you are passing in a tuple!"

    @property
    def distance(self):
        #-- start code here ---
        #Use pythogreans identity to solve for the distance between these two points.
        return round(math.sqrt((self.yCoordinateSecondPair-self.yCoordinateFirstPair)**2+(self.xCoordinateSecondPair-self.xCoordinateFirstPair)**2), 3)
        #-- ends here ---

    # Make it a property of the object rather than a method
    @property
    def slope(self):
        #-- start code here ---
        #Account for the possibility of a divide by zero error
        try:
            return round(((self.yCoordinateSecondPair-self.yCoordinateFirstPair) / (self.xCoordinateSecondPair-self.xCoordinateFirstPair)), 3)
        except ZeroDivisionError:
            return "Infinity"
        #-- ends here ---