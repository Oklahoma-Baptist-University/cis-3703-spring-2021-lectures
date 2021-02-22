import graphics

def do_something():
    win = graphics.GraphWin("DEMO", 200, 200)
    p1 = graphics.Point(20, 30)
    p2 = graphics.Point(30, 40)
    p1.draw(win)
    p2.draw(win)

def something_with_mice():
    win = graphics.GraphWin("MOUSE")
    for i in range(5):
        print("Waiting for mouse click #", i)
        p = win.getMouse()
        print(p.getX(), ", ", p.getY())
  

def draw_triangle():
    win = graphics.GraphWin()
    
    message1 = graphics.Text(graphics.Point(100, 20), "Some text")
    message1.setStyle("bold")
    message1.setSize(12)
    message1.setFace("courier")
    message1.draw(win)
    
    message2 = graphics.Text(graphics.Point(100, 100), "Some more text")
    message2.setStyle("italic")
    message2.setFace("times roman")
    message2.setSize(24)
    message2.draw(win)
    
    p1 = win.getMouse()
    p1.draw(win)
    
    p2 = win.getMouse()
    p2.draw(win)
    
##    line1 = graphics.Line(p1, p2)
##    line1.draw(win)
    
    p3 = win.getMouse()
    p3.draw(win)
    
##    line2 = graphics.Line(p2, p3)
##    line2.draw(win)
    
##    line3 = graphics.Line(p3, p1)
##    line3.draw(win)

    poly = graphics.Polygon(p1, p2, p3)
    poly.setFill("green")
    poly.setOutline("blue")
    poly.draw(win)