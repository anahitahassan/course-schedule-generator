
# 15122
class1Lecture = { 'Lec 1': [515, 595], 
                  'Lec 2': [610, 690]
                }

class1Recitation = {'A': [545, 595], 
                    'B': [610, 660], 
                    'C': [740, 790], 
                    'D': [870, 920], 
                    'E': [610, 660], 
                    'F': [740, 790], 
                    'G': [805, 855], 
                    'H': [935, 985], 
                    'I': [740, 790], 
                    'J': [805, 855], 
                    'K': [870, 920], 
                    'L': [935, 985]
                   }

# we want: [ ('Lec 1', [515, 595]), ('B', [610, 660])]

def bestClassAndTime(allClassData, result, index = 0):
    if index >= len(allClassData):
        if noTimeConflicts(result):
            return result
        else:
            return None
    else:
        classData = allClassData[index]
        for key in classData:
            #print(index, result)
            if noTimeConflicts(result):
                #print(index, result)
                value = classData[key]
                miniTuple = (key, value)
                result.append(miniTuple)
                # print(result)
                solution = bestClassAndTime(allClassData, result, index + 1)
                if solution != None:
                    return solution
                # backtracking: remove it from result. 
                result.remove(miniTuple)
        return 'None'

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
    allClassData = [class1Data, class2Data, class3Data]
    result = []
    print(bestClassAndTime(allClassData, result))

testBestClassAndTime()