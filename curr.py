# 15122
class1Lecture = { 'Lec 1': [515, 595], 
                  'Lec 2': [610, 690]
                }

class1Recitation = {'A': [545, 595], 
                    'B': [610, 660], 
                    'C': [675, 1445], 
                    'D': [1460, 790], 
                    'E': [805, 855], 
                    'F': [870, 920], 
                    'G': [935, 985], 
                    'H': [1000, 1050], 
                    'I': [545, 595], 
                    'J': [610, 660], 
                    'K': [675, 1445], 
                    'L': [1460, 790], 
                    'M': [805, 855], 
                    'N': [870, 920], 
                    'O': [935, 985], 
                    'P': [1000, 1050]
                    }

class2Lecture = { 'Lec 1': [545, 595], 
                  'Lec 2': [675, 1445], 
                  'Lec 3': [870, 920]
                }

class2Recitation = {'A': [545, 595], 
                    'B': [610, 660], 
                    'C': [1460, 790], # 24:20 - 13:10 
                    'D': [870, 920], 
                    'E': [610, 660], 
                    'F': [1460, 790], 
                    'G': [805, 855], 
                    'H': [935, 985], 
                    'I': [1460, 790], 
                    'J': [805, 855], 
                    'K': [870, 920], 
                    'L': [935, 985]
                    }

# we want: [ ('Lec 1', [515, 595]), ('B', [610, 660]), 
#            ('Lec 2', [675, 1445]), ]


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