import json
with open("db.json") as f:
    db = json.loads(json.load(f))

print(db['21127']["lec"])
# 'Lec 1': [545, 595], 'Lec 2': [675, 725], 'Lec 3': [870, 920]}