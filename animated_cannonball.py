from graphics import *
from input_dialog import InputDialog
from ShotTracker import ShotTracker

def main():
    # Autoflush - do not update the object anytime the object is asked to change,
    # We will explicitly ask for this
    win = GraphWin("Projectile Animation", 640, 480, autoflush=True)
    win.setCoords(-10, -10, 210, 155)
    
    # Draw baseline
    Line(Point(-10, 0), Point(210, 0)).draw(win)
    
    # Draw labeled ticks
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)
        
    angle, vel, height = 45.0, 40.0, 2.0
    while True:
        inputwin = InputDialog(angle, vel, height)
        choice = inputwin.interact()
        inputwin.close()
        
        if choice == "Quit":
            break
            
        angle, vel, height = inputwin.get_values()
        shot = ShotTracker(win, angle, vel, height)
        
        while 0 <= shot.get_y() and -10 <= shot.get_x() <= 210:
            shot.update(1/50)
            ## This is the force flush
            update(50)
            
    win.close()