exdict = {
    "phone": "Tablet",
    "laptop": "Desktop",
    "leaf": "Bush",
    "knife": "Sword",
    "sapling": "Tree",
    "room": "House"
}

print("See the code")
a = str(input("Choose an item to upgrade : "))
a = a.lower()
print("Item Upgraded :",exdict[a])
