#Lab #4
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement:             
#  To find index of given object in a list:
#  https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
########################################

def encrypt(message, key):
    # Instantiate List of both lower and upper case letters
    lowerCaseLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperCaseLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    returnString = ""
    #Determine wheather or not the data being passed in is parramaterized in the right format
    if (type(message) == str and type(key) == int):
        #Go through each letter of the input
        for currentLetter in message:
            #Determine type of letter, uppercase, lowercase other charecter
            if currentLetter in lowerCaseLetters:
                # Collab Point, used to find position of letter in list
                currentLetterPosition = lowerCaseLetters.index(currentLetter)
                #Shift the letter by the ammount passed through
                adjustedLetterPosition = currentLetterPosition + key
                # Mod by 26 to ensure it is wrapping around the alphabet!
                returnString += lowerCaseLetters[adjustedLetterPosition % 26]
            elif currentLetter in upperCaseLetters:
                currentLetterPosition = upperCaseLetters.index(currentLetter)
                adjustedLetterPosition = currentLetterPosition + key
                # Mod by 26 to ensure it is wrapping around the alphabet!
                returnString += upperCaseLetters[adjustedLetterPosition % 26]
            else:
                returnString += currentLetter
        return returnString
    else:
        return 'error'


def decrypt(message, key):
    lowerCaseLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperCaseLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    returnString = ""
    if (type(message) == str and type(key) == int):
        for currentLetter in message:
            if currentLetter in lowerCaseLetters:
                # Collab Point, used to find position of letter in list
                currentLetterPosition = lowerCaseLetters.index(currentLetter)
                adjustedLetterPosition = currentLetterPosition - key
                # Mod by 26 to ensure it is wrapping around the alphabet!
                returnString += lowerCaseLetters[adjustedLetterPosition % 26]
            elif currentLetter in upperCaseLetters:
                currentLetterPosition = upperCaseLetters.index(currentLetter)
                adjustedLetterPosition = currentLetterPosition - key
                # Mod by 26 to ensure it is wrapping around the alphabet!
                returnString += upperCaseLetters[adjustedLetterPosition % 26]
            else:
                returnString += currentLetter
        return returnString
    else:
        return 'error'