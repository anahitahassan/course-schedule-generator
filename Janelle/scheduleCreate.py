from dataclasses import make_dataclass
from cmu_112_graphics import *


#creating three main screens
#first screen: running the app, gives title and asks user for class user input
#first screen button - leads to second
#second screen: asks user for preference user input
#second screen button - leads to third screen
#intermission: asks for confirmation, then a loading screen (getting data or whatever)
#third screen: gives user their schedule(s) and stats


#first screen
def appStarted(app): 
    app.rects = []
    app.allclasses = []
    app.mode = 'addScheduleMode'
    app.firstclass = 'Click here to enter first class'
    app.secondclass = 'Click here to enter second class'
    app.thirdclass = 'Click here to enter third class'
    app.fourthclass = 'Click here to enter fourth class'
    app.fifthclass = 'Click here to enter fifth class'


def addScheduleMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'white')
    canvas.create_text(app.width/2, 80, text = 'Generate Your Course Schedule :D', 
    font = "Arial 17", fill = "black")

    canvas.create_rectangle(app.width - 540, app.height - 445, app.width - 300, app.height - 380, fill='white')
    canvas.create_text(app.width - 420,  app.height - 412,
                       text=app.firstclass, font='Arial 12', fill = 'black')
                
    canvas.create_rectangle(app.width - 540, app.height - 345, app.width - 300, app.height - 280, fill='white')    
    canvas.create_text(app.width - 420,  app.height - 312,
                       text=app.secondclass, font='Arial 12', fill = 'black')

    canvas.create_rectangle(app.width - 540, app.height - 245, app.width - 300, app.height - 180, fill='white')    
    canvas.create_text(app.width - 420,  app.height - 212,
                       text=app.thirdclass, font='Arial 12', fill = 'black')

    canvas.create_rectangle(app.width - 280, app.height - 445, app.width - 40, app.height - 380, fill='white')
    canvas.create_text(app.width - 160,  app.height - 412,
                       text=app.fourthclass, font='Arial 12', fill = 'black')

    canvas.create_rectangle(app.width - 280, app.height - 345, app.width - 40, app.height - 280, fill='white')
    canvas.create_text(app.width - 160,  app.height - 312,
                       text=app.fifthclass, font='Arial 12', fill = 'black')

    canvas.create_text(app.width/2, app.height - 50, text = 'Hit enter to generate your course schedule !',
                        font = 'Arial 11', fill = 'black')


def addScheduleMode_keyPressed(app,event):
    #pressing enter generates schedule
    if (event.key == 'Enter'):
        app.mode = 'generatedSchedulesMode'


#after user inputs class, store somewhere
#compare user input to key in data dictionary 
#another dataclass (??)
def addScheduleMode_mousePressed(app,event):
#boundaries for first class mouse pressed
    if ((event.x > app.width - 540) and (event.x < app.width - 300)  and
    (event.y > app.height - 445) and (event.y < app.height - 380)):
        cmuclass1 = app.getUserInput('What is your first class?')
        if (cmuclass1 == None):
            return app.firstclass
        else:
            app.showMessage('You entered: ' + cmuclass1)
            app.firstclass = f'Class 1: {cmuclass1}'
            app.allclasses.append(cmuclass1)
            print(app.allclasses)

#boundaries for second class mouse pressed
    if ((event.x > app.width - 540) and (event.x < app.width - 300)  and
    (event.y > app.height - 345) and (event.y < app.height - 280)):
        cmuclass2 = app.getUserInput('What is your second class?')
        if (cmuclass2 == None):
            return app.secondclassclass
        else:
            app.showMessage('You entered: ' + cmuclass2)
            app.secondclass = f'Class 2: {cmuclass2}'  
            app.allclasses.append(cmuclass2)
            print(app.allclasses)
    
#boundaries for third class mouse pressed
    if ((event.x > app.width - 540) and (event.x < app.width - 300)  and
    (event.y > app.height - 245) and (event.y < app.height - 180)):
        cmuclass3 = app.getUserInput('What is your third class?')
        if (cmuclass3 == None):
            return app.thirdclassclass
        else:
            app.showMessage('You entered: ' + cmuclass3)
            app.thirdclass = f'Class 3: {cmuclass3}'  
            app.allclasses.append(cmuclass3)
            print(app.allclasses)

#boundaries for fourth class mouse pressed
    if ((event.x > app.width - 280) and (event.x < app.width - 40)  and
    (event.y > app.height - 445) and (event.y < app.height - 380)):
        cmuclass4 = app.getUserInput('What is your third class?')
        if (cmuclass4 == None):
            return app.fourthclassclass
        else:
            app.showMessage('You entered: ' + cmuclass4)
            app.fourthclass = f'Class 4: {cmuclass4}'  
            app.allclasses.append(cmuclass4)
            print(app.allclasses)

#boundaries for fifth class mouse pressed
    if ((event.x > app.width - 280) and (event.x < app.width - 40)  and
    (event.y > app.height - 345) and (event.y < app.height - 280)):
        cmuclass5 = app.getUserInput('What is your fifth class?')
        if (cmuclass5 == None):
            return app.fifthclassclass
        else:
            app.showMessage('You entered: ' + cmuclass5)
            app.fifthclass = f'Class 3: {cmuclass5}'  
            app.allclasses.append(cmuclass5)
            print(app.allclasses)


def generatedSchedulesMode_redrawAll(app,canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'white')
    canvas.create_text(app.width/2, 80, text = 'Your Schedule', 
    font = 'Arial 17', fill = 'black')


def createSchedule():
    runApp(width=600, height=600)

def main():
    createSchedule()

if __name__ == '__main__':
    main()

