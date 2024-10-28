from characters import *
from random import randint
from constant import *
from control import *

# INICIO EL EQUIPO PLAYER 1
player_team = [Goku(), Vegeta(), Piccolo()]

# MUESTRO MENSAJE DE BIENVENIDA IMPORTADO DESDE CONSTANT.PY
print(WELCOME)

# INICIO EL NIVEL 1
current_level = 1

# FUNCIÓN PARA GENERAR EQUIPO ENEMIGO POR NIVEL
def generate_enemy_team(level):
    if level == 1:
        print(GAP)
        print(GINYULVL1)
        return [Recoome(randint(0, 2)), Burter(randint(0, 2)), CapGinyu(randint(0, 2))]
    elif level == 2:
        print(GAP)
        print(ANDROIDLVL2)
        return [Androide16(randint(0, 2)), Androide17(randint(0, 2)), Androide18(randint(0, 2))]
    elif level == 3:
        print(GAP)
        print(BOSSLVL3)
        return [Raditz(randint(0, 2)), Cell(randint(0, 2)), Freezer(randint(0, 2))]
    return None

# FUNCIÓN PARA PASAR AL SIGUIENTE NIVEL
def next_level(player_team, current_level):
    current_level += 1
    if current_level <= 3:
        enemy_team = generate_enemy_team(current_level)
        if enemy_team:
            print("Iniciando nivel " + str(current_level))
            fight(player_team, enemy_team)
    else:
        print(FINISHGAME)
        for hero in player_team:
            loot(hero)
    return current_level

# FUNCIÓN DEL COMBATE
def fight(player_team, enemy_team):
    print(NEWFIGHT)
    print(BATTLEBEGINS)
    print(GAP)

    turn = 1  # COMIENZAN LOS HEROES

    # WHILE PARA CONTROLAR ENEMIGOS Y HEROES VIVOS
    while any(hero.alive for hero in player_team) and any(enemy.alive for enemy in enemy_team):
        
        if turn == 1:  # TURNO DE LOS HEROES
            print(PLAYERTURN)
            for hero in player_team:    
                if hero.alive:
                    print("Héroe: " + hero.name + ", Vida: " + str(hero.health) + ", Energía: " + str(hero.energy))
                    respuesta = input("Turno de " + hero.name + ". ¿Qué deseas hacer? 1-Atacar / 2-Curar: ")

                    # ATAQUE HEROES
                    if respuesta == "1": 
                        # SELECCIONO ENEMIGO
                        while True:
                            print(SELECTENEMY)
                            if enemy_team[0].alive:
                                print("a: " + enemy_team[0].name + " - Vida: " + str(enemy_team[0].health))
                            if enemy_team[1].alive:
                                print("b: " + enemy_team[1].name + " - Vida: " + str(enemy_team[1].health))
                            if enemy_team[2].alive:
                                print("c: " + enemy_team[2].name + " - Vida: " + str(enemy_team[2].health))

                            choice = input(SELECTENEMY).lower()
                            if choice in ['a', 'b', 'c']:
                                break
                            else:
                                print(INVALIDOPTION)

                        # SELECCIONO ATAQUE
                        while True:
                            attack_choice = input(CHOOSEATTACK).lower()
                            damage, energy_cost = 0, 0
                            if choice in ['a', 'b', 'c']:
                                if attack_choice == "a":
                                    damage, energy_cost = 25, 20 #a) KAMEHAMEHA (daño, costoenergía)
                                elif attack_choice == "b":
                                    damage, energy_cost = 15, 10 #b) KAOIKEN
                                elif attack_choice == "c":
                                    damage, energy_cost = 100, 75 #c) GENKIDAMA
                                break
                            else:
                                print(INVALIDOPTION)

                        # MUETRA ATAQUE
                        if hero.energy >= energy_cost:
                            target_enemy = enemy_team[ord(choice) - ord('a')]
                            if target_enemy.alive:
                                hero.energy -= energy_cost
                                target_enemy.health -= damage
                                print(hero.name + "  usó " + str(attack_choice) + "contra " + str(target_enemy.name) + ", causando " + str(damage) + " de daño.")
                                print("La vida de " + str(target_enemy.name) + " es ahora " + str(target_enemy.health) + ".")
                                if target_enemy.health <= 0:
                                    target_enemy.alive = False
                                    print(target_enemy.name + " ha sido derrotado!")
                            else:
                                print(ENEMYDEFEATED)
                        else:
                            print("Energía insuficiente para realizar este ataque.")
                    
                    # CUANDO ME CURO
                    elif respuesta == "2" and hero.energy >= hero.energyCost:  
                        print(hero.name + " se ha curado.")
                        hero.healing()
                    else:
                        print(NOTENERGY)

        else:  # TURNO DE LOS ENEMIGOS
            print(GAP)
            print(ENEMYTURN)
            for enemy in enemy_team:
                if enemy.alive:
                    heros_alive = [hero for hero in player_team if hero.alive]
                    if heros_alive:
                        target = heros_alive[randint(0, len(heros_alive) - 1)]
                        print(enemy.name + " ataca a " + target.name + "!")
                        target.injureHero(enemy.attack)
                        print("La vida de " + target.name + " es ahora " + str(target.health) + ".")
                        if not target.alive:
                            print(target.name + " ha sido derrotado!")

        # CAMBIO DE TURNO
        turn = 1 if turn == 2 else 2

    # SI GANO O PIERDO
    if all(not enemy.alive for enemy in enemy_team):
        print(ALLENEMYDEFEATED)
        if current_level < 3:        
            for hero in player_team:
                loot(hero)
                hero.lvlcheck()
            return True
        else:
            print(FINISHGAME)
    if not any(hero.alive for hero in player_team):
        print(LOSTBATTLE)
        return False

# INICIO DESDE EL NIVEL 1
enemy_team = generate_enemy_team(current_level)
if enemy_team:
    success = fight(player_team, enemy_team)

# PASO A LA SIGUIENTE BATALLA SI EL COMBATE FUE EXITOSO
while success and current_level <= 3:
    current_level = next_level(player_team, current_level)


#5° REORDENO EL CÓDIGO PARA SUMAR MAS ENEMIGOS - SIGUIENTE CÓDIGO
#6° CREO LA FUNCIÓN DEL COMBATE
#7° ARREGLO EL BUG DE QUE SIGUE ATACANDO CUANDO MUERE EL ENEMIGO
#8° AÑADO LOOT(LA FUNCION DE COMBATE LA SACAMOS AL ARCHIVO APARTE)
#9° AGREGAMOS FUNCION PARA COMPRAR
#10° CREO LISTA PARA ENEMIGOS Y NIVELES(DE PLANTA EN PLANTA)
#11° EXPERIENCIA PARA SUBIR EL NIVEL
#12° CREO CLASE HIJA PARA SECUACES DE LOS ENEMIGOS
#13° CREO AUMENTO DE PODERES PARA LOS ENEMIGOS POR CADA NIVEL
#26/10/24 
#14° SISTEMA DE ATAQUE MODIFICADO
#15° LAS CONSTANTES -VAN EN MAYUSCULA - BUENAS PRÁCTICAS-