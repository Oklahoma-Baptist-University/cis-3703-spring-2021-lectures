from graphics import *
from random import randrange

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside
    it."""
    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button."""
        w,h = width / 2.0, height / 2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
        
    def get_label():
        """Accessor to get the label"""
        return self.label.getText()
    
    def activate(self):
        """Sets the button to 'active"""
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
        
    def deactivate(self):
        """Sets the button to 'inactive"""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        
    def clicked(self, p):
        """Returns true of button is active and p is inside"""
        return(self.active and 
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)
    
class DieView:
    def __init__(self, win, center, size):
        self.win = win
        # This allows us to tweak the appearance if needed
        self.background = "white"
        self.foreground = "black"  # Color of the pips
        self.psize = 0.1 * size # radius of each pip
        hsize = size / 2.0 # Half the die size
        offset = 0.6 * hsize
        
        # Create the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)
        
        # Pip circles
        self.pip1 = self.__make_pip(cx - offset, cy - offset)
        self.pip2 = self.__make_pip(cx - offset, cy)
        self.pip3 = self.__make_pip(cx - offset, cy + offset)
        self.pip4 = self.__make_pip(cx, cy)
        self.pip5 = self.__make_pip(cx + offset, cy - offset)
        self.pip6 = self.__make_pip(cx + offset, cy)
        self.pip7 = self.__make_pip(cx + offset, cy + offset)
        
        self.set_value(1)
        
    ## Leading underscores are a notation that these are to be
    ## private
    def __make_pip(self, x, y):
        """Internal helper method to draw a pip at (x, y)"""
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip
    
    def set_value(self, value):
        # Turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)
        
        # Turn correct pips on
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif (value == 2):
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif (value == 3):
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif (value == 4):
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif (value == 5):
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
    
def main():
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")
    
    # Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    
    roll_button = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    roll_button.activate()
    quit_button = Button(win, Point(5, 1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quit_button.clicked(pt):
        if roll_button.clicked(pt):
            value1 = randrange(1, 7)
            die1.set_value(value1)
            value2 = randrange(1, 7)
            die2.set_value(value2)
            quit_button.activate()
        pt = win.getMouse()
        
    win.close()