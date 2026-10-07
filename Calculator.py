# This is a mini project made by using Python

# Calculator
#Concepts covered:
    # 1.variables
    # 2.Input and Output
    # 3.Arithmatic Operators
    # 4.Data types
    # Conditional Statements

# Project Features:
    #  1.It takes a value and then arithmetic operator from user as input
    #  2. Then it permforms arithmetic operations and show result as output
# Logic Flow
    # Start the programme
    # Enter the value and operator
    # Press enter and see results
print("=== MINI CALCULATOR ===")
a=float(input("Enter First Number:"))
b=input("Enter Operator:")
c=float(input("Enter Second Number:"))
if b == "+":
    result = round(a + c)
elif b == "-":
    result = round(a - c)
elif b == "*":
    result = round(a * c)
elif b == "**":
    result = round(a**c)
elif b == "%":
    result = round(a%c)
elif b == "/":
    if c == 0:
        result = "Not Defined"
    else:
        result = round(a/c)
elif b == "//":
    result = round(a//c)
else:
    result="Invalid Operator"

print(f"Result: {result:,}")
