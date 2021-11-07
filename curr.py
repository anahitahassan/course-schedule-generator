import json
with open("db.json") as f:
    db = json.loads(json.load(f))

# This takes in a class code and 
# returns a list containing the days of that lecture/section.  

listOfClassCodes = ['21127', '15122', '36200', '80100', '76101']

s = ""
def getDays(listOfClassCodes, s):
    for classCode in listOfClassCodes:
        lectures = db[classCode]['lec']['day']
        section = db[classCode]['sec']['day']
        s += f"{classCode} lec: {lectures} \n"
        s += f"{classCode} sec: {section} \n"
    return s

s = getDays(listOfClassCodes, s)
#print(s)

# This function takes in s and 
# returns all the lec/sec on Monday, Tuesday, so on. 
def getClassesOnDays(s):
    monday = []
    for line in s.splitlines():
        if 'M' in line:
            monday.append(line[:9])
    tuesday = []
    for line in s.splitlines():
        if 'T' in line:
            tuesday.append(line[:9])
    wednesday = []
    for line in s.splitlines():
        if 'W' in line:
            wednesday.append(line[:9])
    thursday = []
    for line in s.splitlines():
        if 'TR' in line:
            thursday.append(line[:9])
    friday = []
    for line in s.splitlines():
        if 'F' in line:
            friday.append(line[:9])
    dayClasses = [monday, tuesday, wednesday, thursday, friday]
    return dayClasses

dayClasses = getClassesOnDays(s)
# for elem in dayClasses:
#     print(elem)

# ['21127 lec', '15122 sec', '36200 lec', '80100 lec', '76101 sec']
# ['21127 sec', '15122 lec', '76101 sec']
# ['21127 lec', '36200 lec', '80100 lec', '76101 sec']
# ['21127 sec', '15122 lec', '76101 sec']
# ['21127 lec', '15122 sec', '36200 lec', '36200 sec', '80100 sec', '76101 sec']

###############################################################################

###############################################################################

# day = "M", or "T" and so on. 
def getTimes(day, dayClasses, classCode):
    lst = []
    classLecOrSec = ''
    if day == "M":
        lst = dayClasses[0]
    if day == "T":
        lst = dayClasses[1]
    if day == "W":
        lst = dayClasses[2]
    if day == "TR":
        lst = dayClasses[3]
    if day == "F":
        lst = dayClasses[4]
    for elem in lst:
        if classCode in elem:
            classLecOrSec = elem[6:]
    # so we've got classCode (21127) and classLecOrSec(lec in our case)
    possibleTimes = db[classCode][classLecOrSec]['time']
    return possibleTimes

#print(getTimes("M", dayClasses, '21127'))
# {'Lec 1': [545, 595], 'Lec 2': [675, 725], 'Lec 3': [870, 920]}

def main(dayClasses):
    d = {}
    lst = []
    dayResult = []
    for day in ["M", "T", "W", "TR", "F"]:
        if day == "M":
            lst = dayClasses[0]
        if day == "T":
            lst = dayClasses[1]
        if day == "W":
            lst = dayClasses[2]
        if day == "TR":
            lst = dayClasses[3]
        if day == "F":
            lst = dayClasses[4]
        # we need dayResult to essentially keep track of all the classes and times. 
        # we just need lst to keep track of the number of classes we need (that when we'll know when to stop)
        dayResult = bestClassAndTime(day, dayClasses, dayResult, lst)
        # should return something like: 
        # d = [ ('21127 lec', sometime), ('15122 sec', sometime) ...
        #   ]
        d[day] = dayResult
    return d

def bestClassAndTime(day, dayClasses, dayResult, lst, depth = 0):
    if len(dayResult) == len(lst):
        if isLegalTime(dayResult):
            return dayResult
    else:
        print(depth)
        for classLecOrSec in lst: # '21127 lec' or '15122 sec'
            # think of these as possible solutions
            possibleSolutions = getTimes(day, dayClasses, classLecOrSec[:5]) # this should be a disctionary
            for key in possibleSolutions: # 'Lec 1': [545, 595]
                possibleLecOrSec = key
                time = possibleSolutions[key]
                miniTuple = (possibleLecOrSec, time)
                dayResult.append(miniTuple)
                # with altered dayResult
                solution = bestClassAndTime(day, dayClasses, dayResult, lst)
                if solution != None:
                    return solution
                # backtracking:
                dayResult.remove(miniTuple)
        return None

# say that dayResult = [('21127 lec', [545, 595]), ('15122 sec', [675, 725])]
def isLegalTime(dayResult):
    for firstElem in dayResult:
        for comparisonElem in dayResult:
            if firstElem != comparisonElem:
                time1a = firstElem[1][0]
                time1b = firstElem[1][1]
                time2a = comparisonElem[1][0]
                time2b = comparisonElem[1][1]

                if ((time1a < time2a < time1b) or (time2a < time1b < time2b) or
                   (time1a < time2b < time1b) or (time2a < time1a < time2b)):
                   return False
    return True

print(main(dayClasses))


# # allClassData = {'Lec 1': [545, 595], 'Lec 2': [675, 725], 'Lec 3': [870, 920]}
# # result = [ ('Lec 1', [545, 595]) ]
# def bestClassAndTime(allClassData, result, index = 0):
#     if index >= len(allClassData):
#         if noTimeConflicts(result):
#             return result
#         else:
#             return None
#     else:
#         classData = allClassData[index]
#         for key in classData:
#             #print(index, result)
#             if noTimeConflicts(result):
#                 #print(index, result)
#                 value = classData[key]
#                 miniTuple = (key, value)
#                 result.append(miniTuple)
#                 # print(result)
#                 solution = bestClassAndTime(allClassData, result, index + 1)
#                 if solution != None:
#                     return solution
#                 # backtracking: remove it from result. 
#                 result.remove(miniTuple)
#         return 'None'