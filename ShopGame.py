import time as t

# Made with heart

shop = {
    
    "Apple": 100, "Orange": 250, "Banana": 150,
    "Grapes": 200, "Lime": 300, "Lemon": 250,
    "Plum": 100, "Chocolate": 150, "Soda": 400,
    "Cherry": 50, "Lemonade": 500, "Lolipop": 10,
    "Gum": 50, "Chips": 100, "Sandwich": 200
    
}

money = 5000

box = []

print("Welcome to our shop!")
print("See the list before starting!", shop)

while True:
    
    a = str(input("Choose item to buy : "))
    if shop[a] < money:
        box.append(a)
        print("You just bought :",a)
        print("List :", box)
        money = money - shop[a]
        print("Money :", money)
        print()
        print("####################")
        print()
        t.sleep(3)
        continue

    elif len(box) >= 15:
        print("You have full box, See you later! ;)")
        t.sleep(5)
        break
    
    else:
        print("You havent enough money (((")
        t.sleep(5)
        break
    
        
