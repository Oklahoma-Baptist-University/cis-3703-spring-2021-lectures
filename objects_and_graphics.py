# This will make all the objects in the graphics package accessible
from graphics import *

# This is a simple window creation. You provide the title and dimensions. The GraphWin function
# creates  a new window on the screen
def create_window(title, width, height):
    win = GraphWin(title, width, height)
    # We will return the object so that users can manipulate it
    return win

# This is a simple function that just closes the window, but we will create small functions in the spirit of
# object-oriented programming
def close_window(win):
    win.close()
    
def draw_some_points():
    p1 = Point(50, 60)
    print("The x position of the point is ", p1.getX())
    print("The y position of the point is ", p1.getY())
    win = create_window("Simple Window", 200, 200)
    # Draw the point in the window
    p1.draw(win)
    # Make another point
    p2 = Point(140, 100)
    p2.draw(win)
    return win

def draw_some_shapes():
    win = create_window("Shapes", 500, 500)
    
    # Create a circle by first creating an object that is the center of the circle
    # then create a Circle object with center defined by the point and radius 30 and
    # then fill it red
    center = Point(100, 100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)
    
    # Put some text in the center of the circle
    label = Text(center, "Red Circle")
    label.draw(win)
    
    # Draw a square - the first argument is the upper right position of the
    # rectangle and the second argument is the lower right position of the
    # rectangle
    rect = Rectangle(Point(30, 30), Point(70, 70))
    rect.draw(win)
    
    # Draw a line segment - the first argument is the start point and the
    # second argument is the end point
    line = Line(Point(20, 30), Point(180, 165))
    line.draw(win)
    
    # Now draw an oval
    oval = Oval(Point(20, 150), Point(180, 199))
    oval.draw(win)
    
    return win

## Using Graphical Objects
## GraphWin, Point, Circle, etc are examples of classes
## Every object is an instance of some class; the class describes the properties that the instance will have
## A Point instance has a specific X and Y value, but support the same operations (getX, draw, etc)

## A constructor is a special type of method that creates a brand-new object:
##   <class-name>(<param1>, <param2>, ...)
## The number and type of paramters depend on the class

## Figure 4.4

##
## To perform an operation on an instance, we send the instance a message via a method (functions
## that live inside the instance
##   <object>.<method-name(<param1>, <param2>, ...)
## An accessor is a method that access information from the instance
## A mutator is a method that change the values of an instance variables
## Methods can take complex objects as parameters

## Figure 4.5

## It is possible for two different variables to refer to the same instance: changes made to one will also be 
## made to the other
def incorrect_object_references():
    win = create_window("Incorrect Object References", 200, 200)
    left = Circle(Point(80, 50), 5)
    left.setFill('yellow')
    left.setOutline('red')
    right = left # Right is now pointing to left. It is not a different object
    right.move(20, 0)
    left.draw(win)
    right.draw(win)
    return win

def correct_object_references():
    win = create_window("Correct Object References", 200, 200)
    left = Circle(Point(80, 50), 5)
    left.setFill('yellow')
    left.setOutline('red')
    right = Circle(Point(100, 50), 5) # Right is now its own object
    right.setFill('yellow')
    right.setOutline('red')
    left.draw(win)
    right.draw(win)
    return win

def clone_circles():
    win = create_window("Correct Object References", 200, 200)
    left = Circle(Point(80, 50), 5)
    left.setFill('yellow')
    left.setOutline('red')
    
    right = left.clone()
    right.move(20, 0)
    
    left.draw(win)
    right.draw(win)
    return win

## Programming with graphics requires careful planning
##   What the program will do
##   The size of the window
##   The position of the graphic elements
##   Colors, line widths, fonts, etc.
def future_value():
    principal = float(input("Enter the initial principal "))
    apr = float(input("Enter the annualized interest rate "))
    
    win = create_window("Investment Growth Chart", 320, 240)
    win.setBackground('white')
    ## ***** NEW NOTATION
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)
    
    # Bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)
    
    # Bar for successive years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11 + 25, 230 - height))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)
        
    input("Press <Enter> to quit") 
    win.close()
    
## Operating at the pixel level can become tedious
def coordinates():
    win = GraphWin("TTT")
    # Defines a 3x3 grid - objects are placed in this grid (instead of the pixels)
    # Defines the lower left and upper right corners
    # This has the additional advantage of scaling with the screen size
    win.setCoords(0.0, 0.0, 3.0, 3.0)
    
    # Draw the lines on the board
    Line(Point(1, 0), Point(1, 3)).draw(win)
    Line(Point(2, 0), Point(2, 3)).draw(win)
    Line(Point(0, 1), Point(3, 1)).draw(win)
    Line(Point(0, 2), Point(3, 2)).draw(win)
    
def future_value_with_coords():
    principal = float(input("Enter the initial principal "))
    apr = float(input("Enter the annualized interest rate "))
    
    win = create_window("Investment Growth Chart", 320, 240)
    win.setBackground('white')
    win.setCoords(-1.75, -200, 11.5, 10400)
    ## ***** NEW NOTATION
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)
    
    # Bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)
    
    # Bar for successive years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)
        
    input("Press <Enter> to quit") 
    win.close()

## Interactive graphics - accept user input
## Widgets - buttons, menus, text boxes, etc.
## Event-driven programming - widgets are drawn on the screen and then the app waits for something
##    When the user moves a mouse, clicks a button - an event is generated
def click():
    win = GraphWin("Click the Mouse")
    for i in range(10):
        p = win.getMouse()
        print("Clicked at ", p.getX(), ", ", p.getY())
    win.close()

def draw_triangle():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    
    # Provides prompts
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)
    
    p1 = win.getMouse()
    p1.draw(win)
    
    p2 = win.getMouse()
    p2.draw(win)
    
    p3 = win.getMouse()
    p3.draw(win)
    
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)
    
    # Change the text that is displayed
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()
    
## Handling text input
def text_input():
    win = GraphWin("Text Input")
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)
    win.close()
    
def temp_converter():
    win = GraphWin("Text Entry", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    Text(Point(1, 3), "   Celsius temperature:").draw(win)
    Text(Point(1, 1), "Fahrenheit temperature:").draw(win)
    
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    
    outputText = Text(Point(2.25, 1), "")
    outputText.draw(win)
    
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
    
    win.getMouse()
    
    celsius = float(inputText.getText())
    fahrenheit = 9.0 / 5.0 * celsius * 32
    
    outputText.setText(round(fahrenheit, 2))
    button.setText("Quit")
    
    win.getMouse()
    win.close()