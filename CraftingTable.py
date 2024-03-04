#The crafting system from Minecraft 
# 0 - Void
# 1 - Wood
# 2 - Stick
# 3 - Iron
# 4 - Iron Block
# 5 - Stone 
print("Enter the ingredients")
a1,a2,a3 = map(int,input().split())
a4,a5,a6 = map(int,input().split())
a7,a8,a9 = map(int,input().split())

if (a1 == 1) and (a2 == 1) and (a3 == 1) and (a4 == 0) and (a5 == 2) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0):  #Recipe example
    print("Result : Wooden Pickaxe")

elif (a1 == 1) and (a2 == 1) and (a3 == 0) and (a4 == 0) and (a5 == 2) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0): #Another recipe example
    print("Result : Wooden Hoe")

elif (a1 == 1) and (a2 == 1) and (a3 == 0) and (a4 == 1) and (a5 == 2) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0): 
    print("Result : Wooden Axe")

elif (a1 == 0) and (a2 == 1) and (a3 == 0) and (a4 == 0) and (a5 == 1) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0): 
    print("Result : Wooden Sword")

elif (a1 == 0) and (a2 == 1) and (a3 == 0) and (a4 == 0) and (a5 == 2) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0): 
    print("Result : Wooden Shovel")

elif ((a1 == 3) and (a2 == 3) and (a3 == 3) and (a4 == 3) and (a5 == 0) and (a6 == 3) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 3) and (a5 == 3) and (a6 == 3) and (a7 == 3) and (a8 == 0) and (a9 == 3)):
    print("Result : Iron Helm")

elif ((a1 == 3) and (a2 == 3) and (a3 == 3) and (a4 == 3) and (a5 == 0) and (a6 == 3) and (a7 == 3) and (a8 == 0) and (a9 == 3)):
    print("Result : Iron Leggins")

elif ((a1 == 3) and (a2 == 0) and (a3 == 3) and (a4 == 3) and (a5 == 3) and (a6 == 3) and (a7 == 3) and (a8 == 3) and (a9 == 3)):
    print("Result : Iron Chestplate")

elif ((a1 == 3) and (a2 == 0) and (a3 == 3) and (a4 == 3) and (a5 == 0) and (a6 == 3) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 3) and (a5 == 0) and (a6 == 3) and (a7 == 3) and (a8 == 0) and (a9 == 3)):
    print("Result : Iron Boots")
    
elif ((a1 == 3) and (a2 == 0) and (a3 == 3) and (a4 == 3) and (a5 == 0) and (a6 == 3) and (a7 == 3) and (a8 == 3) and (a9 == 3)):
    print("Result : Calduron")
    
elif (a1 == 3) and (a2 == 3) and (a3 == 3) and (a4 == 0) and (a5 == 2) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0):  #Recipe example
    print("Result : Iron Pickaxe")

elif (a1 == 3) and (a2 == 3) and (a3 == 0) and (a4 == 0) and (a5 == 2) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0): #Another recipe example
    print("Result : Iron Hoe")

elif (a1 == 3) and (a2 == 3) and (a3 == 0) and (a4 == 3) and (a5 == 2) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0): 
    print("Result : Iron Axe")

elif (a1 == 0) and (a2 == 3) and (a3 == 0) and (a4 == 0) and (a5 == 3) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0): 
    print("Result : Iron Sword")

elif (a1 == 0) and (a2 == 3) and (a3 == 0) and (a4 == 0) and (a5 == 2) and (a6 == 0) and (a7 == 0) and (a8 == 2) and (a9 == 0): 
    print("Result : Iron Shovel")

elif (a1 == 1) and (a2 == 1) and (a3 == 1) and (a4 == 1) and (a5 == 0) and (a6 == 1) and (a7 == 1) and (a8 == 1) and (a9 == 1): 
    print("Result : Chest")

elif (a1 == 3) and (a2 == 3) and (a3 == 3) and (a4 == 3) and (a5 == 3) and (a6 == 3) and (a7 == 3) and (a8 == 3) and (a9 == 3): 
    print("Result : Iron Block")

elif (a1 == 4) and (a2 == 4) and (a3 == 4) and (a4 == 0) and (a5 == 3) and (a6 == 0) and (a7 == 3) and (a8 == 3) and (a9 == 3): 
    print("Result : Anvil")

elif ((a1 == 1) and (a2 == 1) and (a3 == 0) and (a4 == 1) and (a5 == 1) and (a6 == 0) and (a7 == 1) and (a8 == 1) and (a9 == 0)) or ((a1 == 0) and (a2 == 1) and (a3 == 1) and (a4 == 0) and (a5 == 1) and (a6 == 1) and (a7 == 0) and (a8 == 1) and (a9 == 1)):
    print("Result : Wooden Door")

elif ((a1 == 3) and (a2 == 3) and (a3 == 0) and (a4 == 3) and (a5 == 3) and (a6 == 0) and (a7 == 3) and (a8 == 3) and (a9 == 0)) or ((a1 == 0) and (a2 == 3) and (a3 == 3) and (a4 == 0) and (a5 == 3) and (a6 == 3) and (a7 == 0) and (a8 == 3) and (a9 == 3)):
    print("Result : Iron Door")

elif ((a1 == 3) and (a2 == 3) and (a3 == 0) and (a4 == 1) and (a5 == 1) and (a6 == 0) and (a7 == 1) and (a8 == 1) and (a9 == 0)) or ((a1 == 0) and (a2 == 3) and (a3 == 3) and (a4 == 0) and (a5 == 1) and (a6 == 1) and (a7 == 0) and (a8 == 1) and (a9 == 1)):
    print("Result : Smithing Table")

elif ((a1 == 5) and (a2 == 0) and (a3 == 0) and (a4 == 5) and (a5 == 5) and (a6 == 0) and (a7 == 5) and (a8 == 5) and (a9 == 5)) or ((a1 == 0) and (a2 == 0) and (a3 == 5) and (a4 == 0) and (a5 == 5) and (a6 == 5) and (a7 == 5) and (a8 == 5) and (a9 == 5)):
    print("Result : Stone Stairs")

elif ((a1 == 1) and (a2 == 0) and (a3 == 0) and (a4 == 1) and (a5 == 1) and (a6 == 0) and (a7 == 1) and (a8 == 1) and (a9 == 1)) or ((a1 == 0) and (a2 == 0) and (a3 == 1) and (a4 == 0) and (a5 == 1) and (a6 == 1) and (a7 == 1) and (a8 == 1) and (a9 == 1)):
    print("Result : Wooden Stairs")

elif ((a1 == 1) and (a2 == 1) and (a3 == 0) and (a4 == 1) and (a5 == 1) and (a6 == 0) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 1) and (a3 == 1) and (a4 == 0) and (a5 == 1) and (a6 == 1) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 1) and (a5 == 1) and (a6 == 0) and (a7 == 1) and (a8 == 1) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 0) and (a5 == 1) and (a6 == 1) and (a7 == 0) and (a8 == 1) and (a9 == 1)):
    print("Result : Crafting Table")

elif (a1 == 5) and (a2 == 5) and (a3 == 5) and (a4 == 5) and (a5 == 0) and (a6 == 5) and (a7 == 5) and (a8 == 5) and (a9 == 5): 
    print("Result : Furnace")

elif ((a1 == 1) and (a2 == 1) and (a3 == 1) and (a4 == 0) and (a5 == 0) and (a6 == 0) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 1) and (a5 == 1) and (a6 == 1) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 0) and (a5 == 0) and (a6 == 0) and (a7 == 1) and (a8 == 1) and (a9 == 1)):
    print("Result : Wooden Slab")

elif ((a1 == 3) and (a2 == 3) and (a3 == 0) and (a4 == 3) and (a5 == 3) and (a6 == 0) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 3) and (a3 == 3) and (a4 == 0) and (a5 == 3) and (a6 == 3) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 3) and (a5 == 3) and (a6 == 0) and (a7 == 3) and (a8 == 3) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 0) and (a5 == 3) and (a6 == 3) and (a7 == 0) and (a8 == 3) and (a9 == 3)):
    print("Result : Iron Trapdoor")

elif ((a1 == 1) and (a2 == 2) and (a3 == 1) and (a4 == 1) and (a5 == 2) and (a6 == 1) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 1) and (a5 == 2) and (a6 == 1) and (a7 == 1) and (a8 == 2) and (a9 == 1)):
    print("Result : Wooden Fence")

elif ((a1 == 2) and (a2 == 1) and (a3 == 2) and (a4 == 2) and (a5 == 1) and (a6 == 2) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 2) and (a5 == 1) and (a6 == 2) and (a7 == 2) and (a8 == 1) and (a9 == 2)):
    print("Result : Wooden Gate")

elif ((a1 == 5) and (a2 == 5) and (a3 == 5) and (a4 == 5) and (a5 == 5) and (a6 == 5) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 5) and (a5 == 5) and (a6 == 5) and (a7 == 5) and (a8 == 5) and (a9 == 5)):
    print("Result : Stone Wall")

elif ((a1 == 1) and (a2 == 0) and (a3 == 1) and (a4 == 1) and (a5 == 1) and (a6 == 1) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 1) and (a5 == 0) and (a6 == 1) and (a7 == 1) and (a8 == 1) and (a9 == 1)):
    print("Result : Boat")

elif ((a1 == 3) and (a2 == 0) and (a3 == 3) and (a4 == 0) and (a5 == 3) and (a6 == 0) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 3) and (a5 == 0) and (a6 == 3) and (a7 == 0) and (a8 == 3) and (a9 == 0)):
    print("Result : Bucket")

elif ((a1 == 1) and (a2 == 0) and (a3 == 1) and (a4 == 0) and (a5 == 1) and (a6 == 0) and (a7 == 0) and (a8 == 0) and (a9 == 0)) or ((a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 1) and (a5 == 0) and (a6 == 1) and (a7 == 0) and (a8 == 1) and (a9 == 0)):
    print("Result : Bowl")

else:
    print("None")
