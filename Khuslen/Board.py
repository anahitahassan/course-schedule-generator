from cmu_112_graphics import *
import random

# d[15112] = {Lec: , Rec:}
# d[15112][Lec] = {times: , day: }
# 11:30 = 690
# 20:45 = 1245
# d[15112][Lec][times] = (1245, 1305)

#canvas.create_text(app.width/2, app.height/2, fill=app.color, text=app.label, font=f'Arial {s} bold')
'''
d = { 15112: {'lec':
                    {'Lec 1':[690, 810]},
                   'days': ['M','W','F'] },
              'sec':
                  {'time':
                       {'A': [750, 810]},
                   'days' : ['T','TR']},
              'title':'Fundemantels of Programming'},
      21127: {'lec':
                  {'time':
                       {'Lec 2': [1050, 1140]},
                   'days': ['T','TR','S']},
              'sec':
                  {'time':
                       {'B': [480, 540]},
                   'days': ['M','F']},
              'title': 'Concepts of Mathematics'}
      }
'''
#d is the dictionary of classes

def appStarted(app):
    app.cols = 8
    app.rows = 16
    app.empty = ""
    app.board = [([app.empty] * app.cols) for row in range(app.rows + 1) ]
    app.board[0][1] = "Sunday"
    app.board[0][2] = "Monday"
    app.board[0][3] = "Tuesday"
    app.board[0][4] = "Wednesday"
    app.board[0][5] = "Thursday"
    app.board[0][6] = "Friday"
    app.board[0][7] = "Saturday"
    app.board[1][0] = "8:00AM"
    app.board[2][0] = "9:00AM"
    app.board[3][0] = "10:00AM"
    app.board[4][0] = "11:00AM"
    app.board[5][0] = "12:00PM"
    app.board[6][0] = "13:00PM"
    app.board[7][0] = "14:00PM"
    app.board[8][0] = "15:00PM"
    app.board[9][0] = "16:00PM"
    app.board[10][0] = "17:00PM"
    app.board[11][0] = "18:00PM"
    app.board[12][0] = "19:00PM"
    app.board[13][0] = "20:00PM"
    app.board[14][0] = "21:00PM"
    app.board[15][0] = "22:00PM"
    app.courses = []
    app.Colors = [ "red", "yellow", "magenta",
                              "pink", "cyan", "green", "orange" ]
    app.timerDelay = 500



def assignLectureBoard(app, d):
    for course in d:
        week = d[course]['lec']['days']
        for day in week:
            name = ""
            i = None
            print(day)
            for lec in d[course]['lec']['time']:
                name = lec
                i = d[course]['lec']['time'][lec][0]
            j = returnDayIndex(day)
            temp = name
            name = d[course]['title'] +"\n"+ name
            app.board[(i//60)-7][j] = name
            x0, y0, x1, y1 = getCellBounds(app, (i//60)-7, j)
            cy0 = y0+ y0Adjustment(y0, y1, d[course]['lec']['time'][temp])
            cy1 = cy0+y1Adjustment(y0,y1,d[course]['lec']['time'][temp])
            app.courses.append([x0, cy0, x1, cy1, name, "cyan"])

            #canvas.create_rectangle(x0, y0, x1, y1, fill = "blue")
            #canvas.create_text((x0 +x1)//2, (y0+y1)//2, fill = "black", text = app.board[row][col])

def assignRecBoard(app, d):
    for course in d:
        week = d[course]['sec']['days']
        for day in week:
            name = ""
            i = None
            for lec in d[course]['sec']['time']:
                name = lec
                i = d[course]['sec']['time'][lec][0]
            temp = name
            j = returnDayIndex(day)
            name = d[course]['title'] +"\n"+ name
            app.board[(i//60)-7][j] = name
            x0, y0, x1, y1 = getCellBounds(app, (i//60)-7, j)
            cy0 = y0+ y0Adjustment(y0, y1, d[course]['sec']['time'][temp])
            cy1 = cy0+y1Adjustment(y0,y1,d[course]['sec']['time'][temp])
            app.courses.append([x0, cy0, x1, cy1, name, "pink"])


def timerFired(app):
    app.courses = []
    assignLectureBoard(app, d)
    assignRecBoard(app, d)


def drawCourses(app, canvas):
    for x in app.courses:
        x0 = x[0]
        y0 = x[1]
        x1 = x[2]
        y1 = x[3]
        name = x[4]
        col = x[5]
        canvas.create_rectangle(x0, y0, x1, y1, fill = col)
        canvas.create_text((x0+x1)//2, (y0+y1)//2, fill = "black", text = name)

def returnDayIndex(day):
    dict = {'M' : 2, 'T': 3, 'W': 4, 'TR':5, 'F': 6, 'S':7}
    return dict[day]


#add onto y0 to get y0
def y0Adjustment(y0, y1, time):
    t1 = time[0]
    return (((y1-y0)//4)*((t1%60) // 15))

#add onto adjusted y0 to get y1
def y1Adjustment(y0, y1, time):
    t1 = time[0]
    t2 = time[1]
    return ((t2-t1)/60*(y1-y0))


def getCellBounds(app, row, col):
    colwidth = app.width / app.cols
    rowheight = app.height / app.rows
    x0 = col * colwidth
    y0 = row * rowheight
    x1 = (col + 1) * colwidth
    y1 = (row + 1) * rowheight
    return x0, y0, x1, y1

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            x0, y0, x1, y1 = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1)
            if(row == 0 or col ==0):
                canvas.create_text((x0 +x1)//2, (y0+y1)//2, fill = "black", text = app.board[row][col])
            #draw text to indicate course number and section

def redrawAll(app, canvas):
    drawBoard(app, canvas)
    drawCourses(app, canvas)

def drawSchedule():
    runApp(width=1920, height=1080)


drawSchedule()
