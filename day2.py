name = "Ria" 
age = "23"

print("The girl over there is " +name+ " ,\n She is "+age+ " years old.")
print("***********************************************************************************")

a = 12
b = 234

print("")
print("Addition: ", (a+b))
print("Subtraction: ",(a-b))
print("Multiplication: ",(a*b))
print("Reminder: ",(a%b))

print("***************************************************************")
print(" ")

colour = ["Blue", "Yellow", "Indigo", "Lavender"]
print(colour[2])
colour.insert(1, "Pink")
print(colour)

print("***************************************************************")
print(" ")

axis = (0,3)
print(axis)

print("***************************************************************")
print(" ")

def employee_details():
    emp_id = input("Enter your empolyee id: ")
    emp_age = input("Enter your age: ")
    print("Employee details: ")
    print(emp_id)
    print(emp_age)

employee_details()