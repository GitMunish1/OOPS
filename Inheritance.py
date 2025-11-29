#parent class
class person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"hello, my name is {self.name} and I am {self.age}")
#child class
class employee(person):
    def __init__ (self, name, age, employee_id):
        #person.__init__(self, name, age)
        # use for making the chaild class inherit all the methods and properties from its parent class
        super().__init__(name, age)
        self.employee_id = employee_id
    def work(self):
        print(f"{self.name} is working with employee ID: {self.employee_id}")


x = employee("king", 25, 233523523)
x.work()