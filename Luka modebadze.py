class Student:
    def __init__(self,name,last_name,private_number,year_born,grades):
        self.name = name
        self.last_name = last_name
        self.private_number = private_number
        self.year_born = year_born
        self.grades = grades
    def __str__(self):
        years_before_18 = 18 - (2025 - self.year_born)
        grades_str = f"math: {self.grades['math']}, English: {self.grades['English']}, programming: {self.grades['programming']}"

        return f"Student: {self.name} {self.last_name}, private Number: {self.private_number}, year Born: {self.year_born}, grades: {grades_str}, Years before 18: {years_before_18}"

exam1 = Student("mirian","Geladze","01525000055",2011,{"math":98,"English":81,"programming":75})
exam2 = Student("gela","paciashvili","01885500099",2008,{"math":80,"English":75,"programming":95})
exam3 = Student("omar","nurmagamedov","01998585400",2010,{"math":100,"English":60,"programming":70})
print(exam1)
print(exam2)
print(exam3)

