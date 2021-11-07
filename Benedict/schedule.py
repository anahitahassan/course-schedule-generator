import json
dotw = {
    "M":  [],
    "T":  [],
    "W":  [],
    "R":  [],
    "F":  [],
    "S":  [],
    "U":  [],
}

with open("db.json") as f:
    db = json.loads(json.load(f))
classes = ["15122", "21127", "21241"]

"""for course in classes:
    for day in db[course]['lec']['day']:
        for lec, starts in db[course]['lec']['time'].items():
            info = (course, lec, starts)
            dotw[day].append(info)
    for day in db[course]['sec']['day']:
        for sec, starts in db[course]['sec']['time'].items():
            info = (course, sec, starts)
            dotw[day].append(info)"""

for course in classes:
    for day in db[course]['lec']['day']:
        dotw[day].append((course, db[course]['lec']['time']))
    for day in db[course]['sec']['day']:
        dotw[day].append((course, db[course]['lec']['time']))
# print(dotw)
def generate(day, dotw):
    for (course, sched) in dotw[day]:
        if "Le" in sched:
            occurs = db[course]['lec']['day']
            for occur in occurs:
                print(occur)
                # dotw[occur].append()
        else:
            occurs = db[course]['sec']['day']
            for occur in occurs:
                print(occur)
                # dotw[occur].append()
generate("M", dotw)
