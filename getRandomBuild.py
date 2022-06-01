from PIL import Image
import requests
from io import BytesIO
import random
from PIL import Image
import sys

import cassiopeia as cass
from cassiopeia import Summoner, Item, Items, Champions, ChampionMasteries, ChampionMastery;
cass.set_riot_api_key("RGAPI-7a61f82c-b5e3-4492-adbf-fca822e741a1")

items = Items(region="NA")
champions = Champions(region = "NA")

build = []
boots = ["Berserker's Greaves","Boots of Swiftness","Ionian Boots of Lucidity","Mercury's Treads","Mobility Boots","Plated Steelcaps","Sorcerer's Shoes"]
mythicItems = ["Crown of the Shattered Queen","Divine Sunderer","Duskblade of Draktharr","Eclipse","Evenshroud","Everfrost",
"Frostfire Gauntlet","Galeforce","Goredrinker","Hextech Rocketbelt","Immortal Shieldbow","Imperial Mandate","Kraken Slayer",
"Liandry's Anguish","Locket of the Iron Solari","Luden's Tempest","Moonstone Renewer","Night Harvester","Prowler's Claw","Riftmaker",
"Shurelya's Battlesong","Stridebreaker","Sunfire Aegis","Trinity Force","Turbo Chemtank"]
itemImages = []
mythic = True
boot = True

randChamp = random.choice(champions)

# Generate random build
while(len(build) != 6):
    item = random.choice(items)
    if boots:
        if item.name in boots:
            build.append(item.name)
            boot = False
    if mythic:
        if item.name in mythicItems:
            build.append(item.name)
            mythic = False
    if (not boot) and (not mythic):
        if (len(item.builds_into) == 0) and (item.gold.total >= 1100) and (item.name not in build) and (item.name not in mythicItems) and (item.name not in boots):
            build.append(item.name)
print(randChamp.name, "Build: ")
print(build)

print("Champion Images: ")
if ' ' in randChamp.name:
    name = randChamp.name.split()
    champLink = "http://ddragon.leagueoflegends.com/cdn/12.3.1/img/champion/{}{}.png".format(name[0],name[1])
else:
    champLink = "http://ddragon.leagueoflegends.com/cdn/12.3.1/img/champion/{}.png".format(randChamp.name)
print(champLink)

# print("Item Images: ")
# for i in range(len(build)):
#     item = Item(name = build[i], region = "NA")
#     itemImage = ["https://ddragon.leagueoflegends.com/cdn/12.3.1/img/item/",str(item.id),".png"]
#     itemLink = "".join(itemImage)
#     response = requests.get(itemLink)
#     img = Image.open(BytesIO(response.content))
#     itemImages.append(img)

# new_im = Image.new('RGB', (64*6,64))

# x_offset = 0
# for img in itemImages:
#     new_im.paste(img, (x_offset,0))
#     x_offset += img.size[0]

# new_im.save("test.png")