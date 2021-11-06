# backtracking algo:

# helper functions we need:
    # isLegalAddition : returns True if a certain class's times works with current schedule.


# storing our classes + their times
    # where listOfClasses is a dictionary. class/lec/recitation is the key. 
    # ex: listOfClasses['15112-Lecture2'] = '3:05-4:25 PM'

# say this is the dictionary containing ALL the data for ALL LECTURES/RECITATIONS FOR A CLASS
classData = { '15112-Lecture1': '9:05AM-9:55AM', # 
      "15112-Lecture2": '3:05PM-4:25PM'
    }

# result is the dictionary that holds the result result['className'] = 'time'

# cmu 112 course notes website
def backtracker(classData, result):
    # we are trying to build result up. 
    if len(result) == 5:
        return result
        # now the graphics does it thing
    else:
        for posClass in classData:
            result.append(posClass)
            if noTimeConflicts(result):
                solution = backtracker(classData, result)
                if solution != None:
                    return solution
                # backtracking: remove it from result. 
                result.remove(posClass)
        return None