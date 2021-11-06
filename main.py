# backtracking algo:

# helper functions we need:
    # isLegalAddition : returns True if a certain class's times works with current schedule.

# storing our classes + their times
    # where listOfClasses is a dictionary. class/lec/recitation is the key. 
    # ex: listOfClasses['15112-Lecture2'] = '3:05-4:25 PM'

# say this is just Monday. 
# say this is the dictionary containing ALL the data for ALL LECTURES/RECITATIONS FOR A CLASS

class1Data = { '15122-Lecture1': '08:35AM to 09:55AM', # (1080, 1100)
               '15122-Lecture2': '10:10AM to 11:30AM'
             }
class2Data = { '21127-Lecture1': '09:05AM to 09:55AM', # (1080, 1100)
               '21127-Lecture2': '11:15AM to 12:05PM'
             }
# answer should be ['15122-Lecture1': '08:35AM to 09:55AM' 
#                   '21127-Lecture2': '11:15AM to 12:05PM']

allClassData = [class1Data, class2Data]
result = []

# result is the dictionary that holds the result result['className'] = 'time'

def stuff(allClassData):
    final = []
    for classData in allClassData:
        final += backtracker(classData, result)
    return final

# cmu 112 course notes website
# classData is a dictionary. 
def backtracker(classData, result):
    # we are trying to build result up. 
    if len(result) == 2:
        return result
        # now the graphics does it thing
    else:
        for key in classData:
            print(f'Key: {key}')
            value = classData[key]
            miniTuple = (key, value)
            result.append(miniTuple)
            if noTimeConflicts(result):
                solution = backtracker(allClassData, result)
                if solution != None:
                    return solution
                # backtracking: remove it from result. 
                result.remove(miniTuple)
        return None

# L = [ (key, classData[key]) , (key, classData[key]) ]
def noTimeConflicts(L):
    for elem in L:
        for comparisonElem in L:
            if elem != comparisonElem:
                # we want to compare their times. 
                # '08:35AM to 09:55AM'
                time1a = convertTimeStringToInt(elem[1][:5]) # '08:35'
                time1b = convertTimeStringToInt(elem[1][11:16]) # '09:55'
                time2a = convertTimeStringToInt(comparisonElem[1][:5])
                time2b = convertTimeStringToInt(comparisonElem[1][11:16])

                if ((time1a < time2a < time1b) or (time2a < time1a < time2b) or
                    (time1a < time2b < time1b) or (time2a < time1b < time2b)):
                    return False
    return True

# s = '08'
# i = int(s)
# print(i*2)
# takes in '08:35' and returns 8*60 + 35
def convertTimeStringToInt(s):
    return int(s[1:2])*60 + int(s[3:])
    
print(stuff(allClassData))