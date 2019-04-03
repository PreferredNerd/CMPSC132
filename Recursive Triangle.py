#Lab #7
#Due Date: 02/22/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: Just Me, and my day off in this Happy Valley!
#
########################################



#### DO NOT modify the triangle(n) function in any way! 
def triangle(n):
    return recursive_triangle(n, n)

###################

def recursive_triangle(k, n):
    if n > 0 and k > 0:
        if k <= n:
            #Define the base case, which is we are reducing the problem to the k = 1
            if k == 1:
                returnString = ""
                for numberOfSpaces in range(n-1):
                    returnString += " "
                returnString += "*"
                return returnString
            #If it has not reduced to this point then we wiull reduce it further to the number of spaces and asteriks and continue to amend the return string.
            else:
                returnString = ""
                for numberOfSpaces in range(n-k):
                    returnString += " "
                for numberofAsterisks in range(k):
                    returnString += "*"
                returnString+="\n"
                #Take what we have added onto what is at each deeper iteration
                return returnString + recursive_triangle(k-1, n)
        else:
            return "Error invalid dimensions"
    else:
        return "Error Please submit a valid psoitive non-zero entry"