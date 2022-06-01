import matplotlib.pyplot as plt
import cassiopeia as cass
from cassiopeia import Summoner, Item, Items, Champions, ChampionMasteries, ChampionMastery;
cass.set_riot_api_key("RGAPI-b9188115-dd8d-4469-97b3-6d754e6c6e5c")
me = Summoner(name = "SaiDee", region = "NA")
match = me.match_history[1]
for summoner in match.participants:
    print (summoner.champion.name)