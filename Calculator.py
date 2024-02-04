def add(a,b):
    print("Addition is completed >>>", a+b)

def sub(a,b):
    print("Subtraction is completed >>>", a-b)

def mul(a,b):
    print("Multiplication is completed >>>", a*b)

def div(a,b):
    print("Division is completed >>>", a/b)
    
print("Welcome to calculator by Yu2009") 
print("Currently functions >>")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
a,b  = map(int,input("Numbers type here >> ").split())
d = int(input("Select an operation >> "))
if d == 1:
    add(a,b)
elif d == 2:
    sub(a,b)
elif d == 3:
    mul(a,b)
elif d == 4:
    div(a,b)
else:
    print("Something went wrong :( ")
