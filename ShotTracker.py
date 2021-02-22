from Projectile import Projectile
from graphics import Circle, Point

class ShotTracker:
    """A graphical object that acts like a cannon ball, the Projectile
    object does not have graphical properties"""
    def __init__(self, win, angle, velocity, height):
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)
        
    def update(self, t):
        """Move the projectile t seconds farther along its flight"""
        
        # Update the projectile
        self.proj.update(t)
        
        # Move the circle
        center = self.marker.getCenter()
        dx = self.proj.get_x() - center.getX()
        dy = self.proj.get_y() - center.getY()
        self.marker.move(dx, dy)
        
    def get_x(self):
        return self.proj.get_x()
    
    def get_y(self):
        return self.proj.get_y()
    
    def undraw(self):
        """Undraw the shot"""
        self.marker.undraw()