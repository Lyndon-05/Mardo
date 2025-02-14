class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s salary has been increased by ${amount}.")

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")
        print()
        
employee1 = Employee("John Wick", "Hitman", 750000)
employee1.display_employee()
employee1.give_raise(50000)
employee1.display_employee()
