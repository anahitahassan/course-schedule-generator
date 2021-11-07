class1Data = { '36202-Lecture1': '04:40PM to 05:30PM'}
#class1DataRecitation = { '36202-Recit': '04:40PM to 05:30PM'}

class2Data = { '15122-Lecture1': '08:35AM to 09:55AM', 
               '15122-Lecture2': '10:10AM to 11:30AM'
             }
class3Data = { '21127-Lecture1': '09:05AM to 09:55AM', 
               '21127-Lecture2': '11:15AM to 12:05PM'
             }

# NOTES:
    # this program only works for some reason when we have class1Data, 
    # class2Data, class3Data go in order from lowest number of elements to 
    # highest. 
    # see how class1Data has 1 element and class2Data has 2: if we had it 
    # switched (class1Data has 2 elements and class2Data has 1), thent he 
    # program doesn't work properly. 

    # I didn't take AM and PM time into consideration yet. 

# we want: [(15122-Lecture1', '08:35AM to 09:55AM'), (21127-Lecture2, '11:15AM to 12:05PM')] 
# since [(15122-Lecture1', '08:35AM to 09:55AM'), (21127-Lecture1, '09:05AM to 09:55AM')] has time conflict

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