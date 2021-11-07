from time import strptime
def toMinutes(time):
    time = str(time)
    try:
        # AM
        struct = strptime(time, '%H:%MAM')
        noon = 0
    except:
        # PM
        struct = strptime(time, '%H:%MPM')
        noon = 12 * 60
    # hr
    hr = int(struct[3])* 60
    # minutes
    min = int(struct[4])
    time = hr + min + noon
    return time

import json
with open("db.json") as f:
    db = json.loads(json.load(f))
print(db["15122"])

{'lec': 
    {'day': ['TR'], 
    'time': {'Lec 1': [515, 595], 'Lec 2': [610, 690]}}, 
'sec': 
    {'day': ['M', 'F'], 
    'time': 
        {'A': [545, 595], 'B': [610, 660], 'C': [675, 725], 'D': [740, 790], 'E': [805, 855], 'F': [870, 920], 'G': [935, 985], 'H': [1000, 1050], 'I': [545, 595], 'J': [610, 660], 'K': [675, 725], 'L': [740, 790], 'M': [805, 855], 'N': [870, 920], 'O': [935, 985], 'P': [1000, 1050]}}, 
'title': 'Principles of Imperative Computation'}