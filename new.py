import json
with open("db.json") as f:
    db = json.loads(json.load(f))

monday21127Lectures = []
monday21127Sections = []

listOfClassCodes = ['21127', '15122']

for classCode in listOfClassCodes:
    lecDict = db[classCode]['lec']
    if 'M' in lecDict['day']:
        timeDict = lecDict['time']
        for key in timeDict:
            miniTuple = (key, timeDict[key])
            monday21127Lectures.append(miniTuple)
        print(monday21127Lectures)

    secDict = db[classCode]['sec']
    if 'M' in secDict['day']:
        timeDict = secDict['time']
        for key in timeDict:
            miniTuple = (key, timeDict[key])
            monday21127Sections.append(miniTuple)
        print(monday21127Sections)

# print(db['15122'])
# print(db['21127'])

# {
#     'lec': 
#         {
#             'day': ['M', 'F', 'W'], 
#             'time':     
#                 {
#                     'Lec 1': [545, 595], 
#                     'Lec 2': [675, 725], 
#                     'Lec 3': [870, 920]
#                 }
#         }, 
#     'sec': 
#         {
#             'day': ['TR'], 
#             'time': 
#                 {
#                     'A': [545, 595], 
#                     'B': [610, 660], 
#                     'C': [740, 790], 
#                     'D': [870, 920], 
#                     'E': [610, 660], 
#                     'F': [740, 790], 
#                     'G': [805, 855], 
#                     'H': [935, 985], 
#                     'I': [740, 790], 
#                     'J': [805, 855], 
#                     'K': [870, 920], 
#                     'L': [935, 985]
#                 }
#         }, 
#     'title': 'Concepts of Mathematics'
# }