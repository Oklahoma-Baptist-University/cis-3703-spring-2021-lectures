# This will make all the objects in the graphics package accessible
from graphics import *

def event_loop():
    win = GraphWin("Color Window", 500, 500)
    
    # This is the event loop, it is an infinite loop (the condition is never false). It
    # will exit based on a user action
    while True:
        key = win.getKey()
        
        # Exit the loop when the user selects 'q'
        if key == "q":
            break
            
        # Process the key -change the background color based on a key press
        if key == 'r':
            win.setBackground("pink")
        elif key == 'w':
            win.setBackground("white")
        elif key == 'g':
            win.setBackground("lightgray")
        elif key == 'b':
            win.setBackground("lightblue")
            
    win.close()
    
## A more flexible UI will allow the user to interact in a variety of ways (not just key presses
## as above: keyboard, mouse, menu item, clicking a button, etc

def handle_key(k, win):
    # Process the key -change the background color based on a key press
    if key == 'r':
        win.setBackground("pink")
    elif key == 'w':
        win.setBackground("white")
    elif key == 'g':
        win.setBackground("lightgray")
    elif key == 'b':
        win.setBackground("lightblue")

## Do nothing for now
def do_nothing_click(pt, win):
    pass # Does nothing

def multi_event_loop():
    win = GraphWin("Color Window", 500, 500)
    
    # This is the event loop, it is an infinite loop (the condition is never false). It
    # will exit based on a user action
    while True:
        # This does not wait for the user to do something. If the user has not
        # selected a key, it returns an empty string (interpreted as false)
        key = win.checkKey()
        
        # Exit the loop when the user selects 'q'
        if key == "q":
            break

        if key:
            handle_key(key, win)
            
        # This does not wait for the user to do something. If the user has not
        # clicked the mouse, it returns an empty string (interpreted as false)
        pt = win.checkMouse()
        if pt:
            do_nothing_click(pt, win)

    win.close()
    
## Add some mouse handling
def handle_click(pt, win):
    # Create an empty entry for the user to type in
    entry = Entry(pt, 10)
    entry.draw(win)
    
    # Go modal to wait for the user to type something in the box
    # Modal means that the user can only interact with this control
    while True:
        key = win.getKey()
        if key == "Return": break # aka <Enter> key
            
    # Undraw the entry box
    entry.undraw()
    # Get what the user typed in
    typed = entry.getText()
    # Create a text box with the entered text where the user clicked the mouse
    Text(pt, typed).draw(win)
    
    win.checkMouse() # Ignore any mouse clicks that have queued up
    
