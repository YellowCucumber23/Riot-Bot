import asyncio
import discord
import os
from PIL import Image
import requests
from io import BytesIO
from discord.ext import commands
import cassiopeia as cass
from cassiopeia import Summoner, Item, Items, Champions, ChampionMasteries, ChampionMastery;
import random
cass.set_riot_api_key("RGAPI-b9188115-dd8d-4469-97b3-6d754e6c6e5c")


def getBuild():
    items = Items(region="NA")
    champions = Champions(region = "NA")

    build = []
    boots = ["Berserker's Greaves","Boots of Swiftness","Ionian Boots of Lucidity","Mercury's Treads","Mobility Boots","Plated Steelcaps","Sorcerer's Shoes"]
    mythicItems = ["Crown of the Shattered Queen","Divine Sunderer","Duskblade of Draktharr","Eclipse","Evenshroud","Everfrost",
    "Frostfire Gauntlet","Galeforce","Goredrinker","Hextech Rocketbelt","Immortal Shieldbow","Imperial Mandate","Kraken Slayer",
    "Liandry's Anguish","Locket of the Iron Solari","Luden's Tempest","Moonstone Renewer","Night Harvester","Prowler's Claw","Riftmaker",
    "Shurelya's Battlesong","Stridebreaker","Sunfire Aegis","Trinity Force","Turbo Chemtank"]
    mythic = True
    boot = True

    randChamp = random.choice(champions)

    # Generate random build
    while(len(build) != 6):
        item = random.choice(items)
        if boot:
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
    
    # Get the champ images
    if " " in randChamp.name:
        temp = "".join(randChamp.name.split())
    elif "." in randChamp.name:
        temp = "".join(randChamp.name.split("."))
    elif "'" in randChamp.name:
        temp = "".join(randChamp.name.split("'"))
    else:
        temp = randChamp.name
    champLink = "http://ddragon.leagueoflegends.com/cdn/12.2.1/img/champion/" + temp +".png"

    # Get item images
    itemImages = []
    for i in range(len(build)):
        item = Item(name = build[i], region = "NA")
        itemImage = ["https://ddragon.leagueoflegends.com/cdn/12.2.1/img/item/",str(item.id),".png"]
        itemLink = "".join(itemImage)
        response = requests.get(itemLink)
        img = Image.open(BytesIO(response.content))
        itemImages.append(img)

        new_im = Image.new('RGB', (64*6,64))

    x_offset = 0
    for img in itemImages:
        new_im.paste(img, (x_offset,0))
        x_offset += img.size[0]

    new_im.save("test.png")

    return randChamp.name, build, champLink, itemImages


client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def build(ctx):
    champ, build, champLink, buildImg = getBuild()
    embed=discord.Embed(title= champ + " Build",description= '\n'.join('{}'.format(k) for k in build), color=0xFF5733)
    file = discord.File("test.png", filename="image.png")
    embed.set_thumbnail(url = champLink)
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)


client.run("OTM3NDUzNjI2MTk5MjY5Mzg3.Yfb9uQ.mkpzmfHLrKE8-09mc-7jz8YAEG0")
