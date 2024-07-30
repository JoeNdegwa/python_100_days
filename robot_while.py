def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_up():
    turn_left()
    move()
    
def turn_down():
    turn_right()
    move()
def repeat():
    move()
    turn_up()
    turn_right()
    move()
    turn_down()
    turn_left()
hurdles = 6
while hurdles > 0:
    repeat()
    hurdles -= 1
    if at_goal():
        break
