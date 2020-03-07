class Student:
    def __init__(self, name, lastname, year_of_entrance, department):
        self.name = name
        self.lastname = lastname
        self.year_of_entrance = year_of_entrance
        self.department = department
    
    def get_studen_info(self):
        return f"{self.name} {self.lastname} entered {self.year_of_entrance} the faculty {self.department} "
        
uchenik = Student('Emir', 'Beishen',  2017, 'maschine learning')
# print(uchenik.name, uchenik.lastname, "in", uchenik.year_of_entrance, "entered the faculty", uchenik.department)
print(uchenik.get_studen_info())