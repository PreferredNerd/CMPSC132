#Lab #3
#Due Date: 01/25/2019, 11:59PM
########################################
#                                      
# Name: Nicholas C. Birosik
# Collaboration Statement: By myself
#
########################################



def countWords(document):
    if type(document) == str:
        myDictionary = {}
        stripedString = ""
        for letter in document:
            if letter == '\'':
                stripedString += "'"
            elif letter.isalpha():
                stripedString += str(letter)
            elif letter == ' ':
                stripedString += " "
            elif letter == '\n':
                stripedString += " "
        for currentWord in stripedString.split():
            if currentWord.lower() in myDictionary:
                myDictionary[currentWord.lower()] += 1
            else:
                myDictionary[currentWord.lower()] = 1
        print (myDictionary)
        return myDictionary
    else:
        return 'error'

def studentGrades(gradeList):
    studentGradeOutput = []
    if type(gradeList) == list:
        for currentRow in range(len(gradeList)):
            studentTotal = 0
            totalCount = 0
            for currentColumn in range(len(gradeList[0])):
                if type(gradeList[currentRow][currentColumn]) == int:
                    studentTotal += gradeList[currentRow][currentColumn]
                    totalCount += 1
            if totalCount != 0:
                studentGradeOutput.append(int(studentTotal/totalCount))
        return (studentGradeOutput)
    else:
        return ("error")