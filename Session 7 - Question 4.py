ShoppingList= []
while True:
    item = input("Enter an item for the shopping list: ")
    if len(item) == 0:
        break
ShoppingList.append(item)

print(ShoppingList)
    
