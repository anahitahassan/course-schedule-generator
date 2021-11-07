from bs4 import BeautifulSoup
from time import strptime
import json
def create():
    db = {}
    db['lec'] = {
        'day': [], 
        'time': {},
    }
    db['sec'] = {
        'day': [], 
        'time': {},
    }
    db['title'] = ''
    return db
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
    hr = int(struct[3]) % 12 * 60
    # minutes
    min = int(struct[4])
    time = hr + min + noon
    return time
def getDays(days):
    return [day for day in days]
with open('Bruh.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')
trs = soup.find_all('tr')
prev = None
prevSec = None
EMPTY = '\xa0'
db = {}
for entry in trs:
    if len(entry) == 10:
        childs = list(entry.children)
        course = ''
        if childs[8].string != 'Pittsburgh, Pennsylvania':
            # check if not in Qatar
            continue
        if childs[4].string == 'TBA' or childs[4].string == EMPTY:
            # Do we even have to consider
            # EMPTY if not a course. Just a header
            continue
        elif childs[0].string == EMPTY:
            # Might be listing the sections
            course = prev
        else:
            # New class
            course = childs[0].string
        # First time dealing with this or not
        if course not in db:
            db[course] = create()
        cur = db[course]
        if (title:=childs[1].string) != EMPTY:
            cur['title'] = title.string
        # times of classes in minutes
        beg = toMinutes(childs[5].string)
        end = toMinutes(childs[6].string)
        category = str(childs[3].string)
        if category == EMPTY:
            category = prevSec
        if 'Le' in category:
            cat = cur['lec']
        else:
            cat = cur['sec']
        cat['day'] += getDays(childs[4].string)
        cat['day'] = list(set(cat['day']))
        cat['time'][category] = [beg, end]
        db[course] = cur
        prev = course
        prevSec = category

rep = json.dumps(db)
with open('db.json', 'w') as f:
    json.dump(rep, f)