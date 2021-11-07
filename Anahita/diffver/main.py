import json
dotw = {
    "M":  [],
    "T":  [],
    "W":  [],
    "TR": [],
    "F":  [],
    "S":  [],
}

with open("db.json") as f:
    db = json.loads(json.load(f))
classes = ["15122", "21127", "21241"]

for course in classes:
    for day in db[course]['lec']['day']:
        for lec, starts in db[course]['lec']['time'].items():
            info = (course, lec, starts)
            dotw[day].append(info)
    for day in db[course]['sec']['day']:
        for sec, starts in db[course]['sec']['time'].items():
            info = (course, sec, starts)
            dotw[day].append(info)

# for elem in dotw:
#     print(elem, dotw[elem])

# what we want: [ ('15122', 'A', [545, 595]),
                  
# 
# 
# ]

monday = (dotw['M'])

def f(monday):
    class1 = []
    class2 = []
    class3 = []
    for elem in monday:
        if elem[0] == '15122':
            class1.append(elem)
        if elem[0] == '21127':
            class2.append(elem)
        if elem[0] == '21241':
            class3.append(elem)
    result = [class1, class2, class3]
    return result

final = f(monday)
# where final[0] and final[1] and so on are different classes
# print(final[0])
# print(final[1])
# print(final[2])

result = []
def backtrack(final, result, index=0):
    if len(result) == len(final):
        return result
    for classData in final[index]:
        for elem in monday:
            if elem[0] == classData[0][0]:
                result.append(elem)
                if isLegalTime(result):
                    solution = backtrack(monday, result, index + 1)
                    if solution != None:
                        return solution
                    # backtrack
                    result.remove(elem)
    return None

def isLegalTime(result):
    if len(result) <= 1: return True
    for firstElem in result:
        for comparisonElem in result:
            if firstElem != comparisonElem:
                time1a = firstElem[2][0]
                time1b = firstElem[2][1]
                time2a = comparisonElem[2][0]
                time2b = comparisonElem[2][1]

                if ((time1a < time2a < time1b) or (time2a < time1b < time2b) or
                   (time1a < time2b < time1b) or (time2a < time1a < time2b)):
                   return False
    return True

print(backtrack(monday, result))