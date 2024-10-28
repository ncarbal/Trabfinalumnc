from random import randint  # PARA LOOT ALEATORIO
from constant import * 
from characters import *

def next_level(player_team):
    print(LEVELCLEAR)
    level_up = min(hero.level for hero in player_team) + 1

    if level_up == 2:
        androide16 = Androide16(randint(0, 2))
        androide17 = Androide17(randint(0, 2))
        androide18 = Androide18(randint(0, 2))
        enemy_team = [androide16, androide17, androide18]
    elif level_up == 3:
        raditz_lvl3 = Raditz(randint(1, 3))
        cell_lvl3 = Cell(randint(1, 3))
        freezer_lvl3 = Freezer(randint(1, 3))
        enemy_team = [raditz_lvl3, cell_lvl3, freezer_lvl3]
        return
    elif level_up == 4:
        print(FINISHGAME)
        return
    
def loot(player1):
    print(EXPPOINT)
    player1.experience += 100

    # HAGO EL SISTEMA DE LOOT RECOMPENSAS
    prob = randint(1, 3)
    if prob == 1:
        print(LOOTERMIT)
        player1.health += 100
    elif prob == 2:
        print(HEALTHLOOT)
        player1.energy += 100
    elif prob == 3:
        print(SSJ1LOOT)
        player1.attack += 100
