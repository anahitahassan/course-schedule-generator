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
        s += f"{classCode} Lec: {lectures} \n"
        s += f"{classCode} Sec: {section} \n"
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
for elem in dayClasses:
    print(elem)
