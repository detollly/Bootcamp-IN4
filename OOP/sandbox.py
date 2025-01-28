class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        
    # Add a method to show the details of an instance of the Employee class       
    def show_details(self):
        print(f"name: {self.name}\ndepartment: {self.department}\nage: {self.age}")
        
employee = Employee("John", 30, "IT")
employee.show_details()

# Create a class called Programmer that inherits from the Employee class
# Inherit from the Employee class
class Programmer(Employee):
    def __init__(self, name, age, department, salary, languages):
        super().__init__(name, age, department)
        self.salary = salary
        self.languages = languages
        
    # Add a method to show details of the Programmer class
    def show_details(self):
        super().show_details()
        
    # Add getters & setters to the Programmer class
    def get_name(self):
        return self.name
            
    def set_name(self, name):
        self.name = name      
        
# Use the G&S methods to update the information of your Programmer       
# Display the updated information
programmer = Programmer("John", 30, "IT", 20000, ["Python", "Java"])
programmer.set_name("Faye")
programmer.show_details()
print(f"The new name is: {programmer.get_name()}")









