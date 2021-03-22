class Student:
    def __init__(self, name, hours, grade_points):
        self.name = name
        # Make the type float - explicitly
        self.hours = float(hours)
        self.grade_points = float(grade_points)
        
    # Accessor methods
    def get_name(self):
        return self.name
    
    def get_hours(self):
        return self.hours
    
    def get_grade_points(self):
        return self.grade_points
    
    def gpa(self):
        return self.grade_points / self.hours