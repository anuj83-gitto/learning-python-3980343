# Class example of Departments in College / University
# This code defines a base class `Vehicle` and two derived classes `Car` and `
class Department:
    def __init__(self, name):
        self.name = name
    

class Science_Tech(Department):
    def __init__(self, name, num_labs):
        super().__init__(name)
        self.num_labs = num_labs
    def details(self):
        super()
        self.noTeachers=15
        self.noStudents=200
        print(f"Department for Science and Technology: Number of Labs: {self.num_labs}, Number of Teachers: {self.noTeachers}, Number of Students: {self.noStudents}")

class Arts_Humanities(Department):
    def __init__(self, name, num_workshops):
        super().__init__(name)
        self.num_workshops = num_workshops
    def details(self):
        super()
        self.noTeachers=10
        self.noStudents=150
        print(f"Department for Arts and Humanities: Number of Workshops: {self.num_workshops}, Number of Teachers: {self.noTeachers}, Number of Students: {self.noStudents}")

class Commerce_BusinessStudies(Department):
    def __init__(self, name, num_offices):
        super().__init__(name)
        self.num_offices = num_offices
    def details(self):
        super()
        self.noTeachers=12
        self.noStudents=180
        print(f"Department for Commerce and Business Studies: Number of Offices: {self.num_offices}, Number of Teachers: {self.noTeachers}, Number of Students: {self.noStudents}")

# Example usage
# Creating instances of each department
_science_dept = Science_Tech("Science and Technology", 5)
_arts_dept = Arts_Humanities("Arts and Humanities", 3)
_commerce_dept = Commerce_BusinessStudies("Commerce and Business Studies", 4)
# Displaying details of each department
_science_dept.details()
_arts_dept.details()
_commerce_dept.details() 