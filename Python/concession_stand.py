menu={"pizza":120.00,
      "fries":55.9,
      "burger":230.87,
      "garlic bread":30.7,
      "coke":70.34}

#print(menu.get("burger"))
#menu.update({"sprite":89.78})
#print(menu.values())
#print(menu.keys())

# for key in menu.keys():
#     print(key)
# for value in menu.values():
#      print(value)

print("      -------Menu-------")


for key,value in menu.items():
     print(f"{key:20}:${value:.2f}")

print("   -------------------------  ")

items=[]
total=0
while True:
    food=input("enter the food you want:('q' to quit): ").lower()
    if food=="q":
        break
    elif food not in menu:
        print("item not available")
    else:
        items.append(food)
        total+=menu[food]

print(f"The items you odered:{items}")
print(f"Your total was {total:.2f}")




