import math

class Projectile:
    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistence. Tracking is done in two
    dimensions, height (x) and distance (y)."""
    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial velocity and height."""
        self.xpos = 0.0
        self.ypos = height
        # Not an instance variable
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)
        
    def get_x(self):
        """Returns the x position of the projectile."""
        return self.xpos
    
    def get_y(self):
        return self.ypos
    
    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1