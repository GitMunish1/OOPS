# this is only for practice methodology in oops
class me:
    def __init__(ji, name, age):
        ji.name = name
        ji.age = age
    def aap(ji):
        print("name:" + ji.name)
        print(f"age:{ji.age}")

p1=me("Munish", 19)
p1.aap()

# calculator using the parameter method
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print("***********************\n")
print("***********************")
n = int(input("enter first number:"))
m = int(input("enter second number:"))
print("Calculator results:")
print(calc.add(n, m))
print(calc.multiply(n, m))