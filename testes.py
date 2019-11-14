import random
from cassiopeia import Champion, Champions
import os
import cassiopeia as cass

cass.set_riot_api_key("RGAPI-ec0f05eb-feb1-487b-9bc9-fd293b54266d")  # This overrides the value set in your configuration/settings.
cass.set_default_region("BR")

# summoner = cass.get_summoner(name='Best Rengar AL')

# print(f"{summoner.name} é level {summoner.level} do servidor {summoner.region}.")

def get_champions():
   # champions = Champions(region='BR')

   # for champion in champions:
   #       print(champion.name, champion.id)



   camp = input('Insira o nome do campeão -> ')
   # annie = Champion(name="Annie", region="NA")
   annie = Champion(name=camp, region="BR")

 
   cls()
   print(f"""
Campeão: {annie.name}

Dano de ataque: {annie.stats.attack_damage} (+{annie.stats.attack_damage_per_level} por nível)
Vida: {annie.stats.health} (+{annie.stats.health_per_level} por nível)
Mana: {annie.stats.mana} (+{annie.stats.mana_per_level} por nível)
Armadura: {annie.stats.armor} (+{annie.stats.armor_per_level} por nível)
Resistência mágica: {annie.stats.magic_resist} (+{annie.stats.magic_resist_per_level} por nível) 

""")
 
   # print(annie.region)
   # print(annie.blurb)
   #nome do champion
   #print(annie.name)
   
   #titulo do champion
   #print(annie.title)

   #dificuldade do champion
   # print(annie.info.difficulty)
   # #nome da passiva
   # print(annie.passive.name)


   # print({item.name: count for item, count in annie.recommended_itemsets[0].item_sets[0].items.items()})
   # print(annie.free_to_play)
   # print(annie._Ghost__all_loaded)

if __name__ == "__main__":
   get_champions()
