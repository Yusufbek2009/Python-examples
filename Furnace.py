import time
print("Correct : Apple Juice | Not correct : apple juice")
print("To exit give furnace void")
while True:
    a = str(input("Insert item to smelt : "))
    if a == "Wood": 
        time.sleep(5)
        print("Result : Charcoal")
        print()
        print()
        
    elif a == "Cobblestone":
        time.sleep(5)
        print("Result : Stone")
        print()
        print()

    elif a == "Stone":
        time.sleep(5)
        print("Result : Smooth Stone")
        print()
        print()

    elif a == "Clay":
        time.sleep(5)
        print("Result : Brick")
        print()
        print()

    elif a == "Void":
        time.sleep(5)
        break
    
    else:
        print("None")
        print()
        print()
