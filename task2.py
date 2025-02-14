class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

student1 = Student("Josh", 19, "Information Technology\n")
student2 = Student("Rodolfo", 22, "Computer Engineering\n")
student3 = Student("Brent", 21, "Education\n")

student1.introduce()
student2.introduce()
student3.introduce()
