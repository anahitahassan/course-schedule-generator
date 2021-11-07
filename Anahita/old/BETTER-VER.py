# class1Data = { 1: 8, 
#                2: 10
#              }
# class2Data = { 3: 8,  
#                4: 9
#              }

class1Data = { '15122-Lecture1': '08:35AM to 09:55AM', # (1080, 1100)
               '15122-Lecture2': '10:10AM to 11:30AM'
             }
class2Data = { '21127-Lecture1': '09:05AM to 09:55AM', # (1080, 1100)
               '21127-Lecture2': '11:15AM to 12:05PM'
             }

# what we want: [(1, 8), (4, 11)] since (1, 8) and (3, 8) conflict

def bestClassAndTime(allClassData, result, index = 0):
    if index >= len(allClassData):
        if noTimeConflicts(result):
            return result
        else:
            return None
    else:
        classData = allClassData[index]
        for key in classData:
            if noTimeConflicts(result):
                value = classData[key]
                miniTuple = (key, value)
                result.append(miniTuple)

                solution = bestClassAndTime(allClassData, result, index + 1)
                if solution != None:
                    return solution
                # backtracking: remove it from result. 
                result.remove(miniTuple)
        return 'None'

# we only are about index 1 of the tuple 
# def noTimeConflicts(L):
#     if len(L) <= 1: return True
#     newL = []
#     for tupleElem in L:
#         newL.append(tupleElem[1])
#     seen = []
#     for elem in newL:
#         if elem not in seen:
#             seen.append(elem)
#         else:
#             return False
#     return True

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

def convertTimeStringToInt(s):
    return int(s[1:2])*60 + int(s[3:])


def testBestClassAndTime():
    allClassData = [class1Data, class2Data]
    result = []
    print(bestClassAndTime(allClassData, result))

testBestClassAndTime()