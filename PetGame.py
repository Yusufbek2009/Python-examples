p = 0
print("Type like this with no problems")
print("apple |X|", "Apple |V|")

while True:
    a = str(input())
    if a == "Apple":
        p += 10
        print("Calories : ",p)
        print()
        if p >= 5000:
            print("Your pet is dead because it ate too much :( ")
        elif p < 0:
            print("You're hungry")
            p = 0
        else:
            continue
        
        
    elif a == "Banana":
        p += 15
        print("Calories : ",p)
        print()
        if p >= 5000:
            print("Your pet is dead because it ate too much :( ")
        elif p < 0:
            print("You're hungry")
            p = 0
        else:
            continue
    
    elif a == "Cucumber":
        p -= 15
        print("Calories : ",p)
        print()
        if p >= 5000:
            print("Your pet is dead because it ate too much :( ")
        elif p < 0:
            print("You're hungry")
            print()
            p = 0
        else:
            continue
    
    elif a == "Bread":
        p += 30
        print("Calories : ",p)
        print()
        if p >= 5000:
            print("Your pet is dead because it ate too much :( ")
        elif p < 0:
            print("You're hungry")
            print()
            p = 0
        else:
            continue
    
    elif a == "Soup":
        p += 70
        print("Calories : ",p)
        print()
        if p >= 5000:
            print("Your pet is dead because it ate too much :( ")
        elif p < 0:
            print("You're hungry")
            print()
            p = 0
        else:
            continue
    
    elif a == "Pancake":
        p += 5
        print("Calories : ",p)
        print()
        if p >= 5000:
            print("Your pet is dead because it ate too much :( ")
        elif p < 0:
            print("You're hungry")
            print()
            p = 0
        else:
            continue
    
    elif a == "Onion":
        p -= 10
        print("Calories : ",p)
        print()
        if p >= 5000:
            print("Your pet is dead because it ate too much :( ")
        elif p < 0:
            print("You're hungry")
            print()
            p = 0
        else:
            continue
    
    elif a == "Bread":
        p += 30
        print("Calories : ",p)
        print()
        if p >= 5000:
            print("Your pet is dead because it ate too much :( ")
        elif p < 0:
            print("You're hungry")
            print()
            p = 0
        else:
            continue
    
    else:
        print()
        print("No Food found")
        print()
        continue
