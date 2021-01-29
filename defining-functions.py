# This will make all the objects in the graphics package accessible
from graphics import *

# Create a generic function for drawing a bar
# If we need to change anything (bar color, width, etc), we only
# need to make the change here
def draw_bar(window, year, height):
    bar = Rectangle(Point(year, 0), Point(year + 1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

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
    draw_bar(win, 0, principal)
#    bar = Rectangle(Point(0, 0), Point(1, principal))
#    bar.setFill('green')
#    bar.setWidth(2)
#    bar.draw(win)
    
    # Bar for successive years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        draw_bar(win, year, principal)
#        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
#        bar.setFill('green')
#        bar.setWidth(2)
#        bar.draw(win)
        
    input("Press <Enter> to quit") 
    win.close()

##
## MODULAR VERSION
##
def create_labeled_window():
    win = create_window("Investment Growth Chart", 320, 240)
    win.setBackground('white')
    win.setCoords(-1.75, -200, 11.5, 10400)
    ## ***** NEW NOTATION
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)
    return win
    
def future_value_with_coords():
    principal = float(input("Enter the initial principal "))
    apr = float(input("Enter the annualized interest rate "))
    
    win = create_labeled_window()
    
    # Bar for initial principal
    draw_bar(win, 0, principal)
    
    # Bar for successive years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        draw_bar(win, year, principal)
        
    input("Press <Enter> to quit") 
    win.close()

