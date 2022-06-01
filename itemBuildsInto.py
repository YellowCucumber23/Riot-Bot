import cassiopeia as cass
from cassiopeia import Item, Items;
cass.set_riot_api_key("RGAPI-0976708e-d303-40ba-b3a8-ac643f3069de")

# Get what an item builds into + price
itemName = input("Enter Item Name: ")
arr = []
items = Items(region="NA")  #Create list containing item objects
for i in range(len(items)):
    if items[i].name == itemName:
        temp = Item(name = items[i].name, region = "NA")  #Create item object from list
        print("\n" + items[i].name, "Builds into: ")
        for item in temp.builds_into:                     #Cycle through what item builds into to get name and gold
            temp2 = Item(name = item.name, region = "NA")
            print(temp2.name + ":", temp2.gold.total, "g")