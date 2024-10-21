# EMPIEZO IMPORTANDO CLASES Y FUNCIONES
from characters import *
from random import randint
from constant import *
from control import *

# INICIO EL EQUIPO PLAYER 1
player_team = [Goku(), Vegeta(), Piccolo()]
# MUESTRO MENSAJE DE BIENVENIDA IMPORTADO DESDE CONSTANT.PY
print(welcome)

# INICIO EL NIVEL 1
current_level = 1

# 2° LA FUNCIÓN GENERAR EQUIPO ENEMIGO ME TRAE LOS ENEMIGOS POR NIVEL 1,2 Y 3 Y VERIFICA EL NIVEL(LEVEL) DESDE CHARACTER.PY
def generate_enemy_team(level):
    if level == 1:
        print(gap)
        print("¡Las Fuerzas Especiales Ginyu llegan al planeta Namek! Prepárate para luchar.")
        return [Recoome(randint(0, 2)), Burter(randint(0, 2)), CapGinyu(randint(0, 2))]
    elif level == 2:
        print(gap)
        print("¡Los Androides han llegado a la Tierra! Prepárate para luchar.")
        return [Androide16(randint(0, 2)), Androide17(randint(0, 2)), Androide18(randint(0, 2))]
    elif level == 3:
        print(gap)
        print("¡Prepárate para luchar contra los Jefes!")
        return [Raditz(randint(0, 2)), Cell(randint(0, 2)), Freezer(randint(0, 2))]
    return None

# HAGO UNA FUNCIÓNPARA PASAR AL SIGUIENTE NIVEL
def next_level(player_team, current_level):
    # VOY A IR INCREMENTANDO EN 1 EL NIVEL CUANDO LO TERMINE
    current_level += 1

    # NO SE VA A PASAR DE NIVEL 3(QUE ES EL MAXIMO QUE TENGO
    if current_level <= 3:
        enemy_team = generate_enemy_team(current_level)
        if enemy_team:
            print("Iniciando nivel " + str(current_level))
            fight(player_team, enemy_team)
    else:
        print("¡Felicidades, has completado el juego!")
        #LLAMO A LOOT PARA LAS RECOMPENSAS
        for hero in player_team:
            loot(hero)
    # DEVUELVO EL NUEVO NIVEL ACTUALIZADO
    return current_level

# DEFINO LA FUNCIÓN DEL COMBATE
def fight(player_team, enemy_team):
    #HAGO PRINT CON LAS ENTRADAS
    print(newfight)
    print(battlebegins)
    print(gap)

    turn = 1  #VOY A IR ALTERNANDO EL TURNO DE LOS HÉROES SI ES 1 Y DE LOS ENEMIGOS SI ES 2

    # ESTO SE VA A EJECTUTAR MIENTRAS LOS HÉROES Y ENEMIGOS ESTEN VIVOS
    while any(hero.alive for hero in player_team) and any(enemy.alive for enemy in enemy_team):
        
        if turn == 1:  # ARRANCAN LOS HÉROES
            print(playerturn)
            for hero in player_team:    
                if hero.alive:
                    print("Héroe: " + hero.name + ", Vida: " + str(hero.health) + ", Energía: " + str(hero.energy))
                    respuesta = input("Turno de " + hero.name + ". ¿Qué deseas hacer? 1-Atacar / 2-Curar: ")
                    #EL ATAQUE
                    if respuesta == "1": 
                        print("Elige a qué enemigo atacar:")
                        if enemy_team[0].alive:
                            print("a: " + enemy_team[0].name + " - Vida: " + str(enemy_team[0].health))
                        if enemy_team[1].alive:
                            print("b: " + enemy_team[1].name + " - Vida: " + str(enemy_team[1].health))
                        if enemy_team[2].alive:
                            print("c: " + enemy_team[2].name + " - Vida: " + str(enemy_team[2].health))

                        # AHORA SELECCIONO A QUE ENEMIGO ATACAR
                        choice = input("Selecciona el enemigo a atacar (a, b, c): ").lower() #LOWERCASE PARA EL CONTROL DE ERRORES CON MINUSCULAS Y MAYUSCULAS
                        if choice == 'a' and enemy_team[0].alive:
                            print(hero.name + " ataca a " + enemy_team[0].name + "!")
                            enemy_team[0].injureEnemy(hero.attack)
                            print("La vida de " + enemy_team[0].name + " es ahora " + str(enemy_team[0].health) + ".")
                            if not enemy_team[0].alive:
                                print(enemy_team[0].name + " ha sido derrotado!")
                        elif choice == 'b' and enemy_team[1].alive:
                            print(hero.name + " ataca a " + enemy_team[1].name + "!")
                            enemy_team[1].injureEnemy(hero.attack)
                            print("La vida de " + enemy_team[1].name + " es ahora " + str(enemy_team[1].health) + ".")
                            if not enemy_team[1].alive:
                                print(enemy_team[1].name + " ha sido derrotado!")
                        elif choice == 'c' and enemy_team[2].alive:
                            print(hero.name + " ataca a " + enemy_team[2].name + "!")
                            enemy_team[2].injureEnemy(hero.attack)
                            print("La vida de " + enemy_team[2].name + " es ahora " + str(enemy_team[2].health) + ".")
                            if not enemy_team[2].alive:
                                print(enemy_team[2].name + " ha sido derrotado!")
                        else:
                            print("Opción inválida o enemigo ya está derrotado.")
                    
                    elif respuesta == "2" and hero.energy >= hero.energyCost:  # CUANDO ME CURO
                        print(hero.name + " se ha curado.")
                        hero.healing()
                    else:
                        print("Acción inválida o energía insuficiente.")

        else:  # CUANDO ES EL TURNO DE LOS ENEMIGOS
            print(gap)
            print("Es el turno de los enemigos.")
            for enemy in enemy_team:
                if enemy.alive:
                    heros_alive = [hero for hero in player_team if hero.alive]
                    if heros_alive:
                        target = heros_alive[randint(0, len(heros_alive) - 1)] #DESDE 0 HASTA LEN QUE ES LA TOTALIDAD DE LOS HÉROES VIVOS, 1,2 O 3
                        print(enemy.name + " ataca a " + target.name + "!")
                        target.injureHero(enemy.attack)
                        print("La vida de " + target.name + " es ahora " + str(target.health) + ".")
                        if not target.alive:
                            print(target.name + " ha sido derrotado!")

        # ES LO MISMO QUE HACER UN WHILE CON UN CONTADOR
        turn = 1 if turn == 2 else 2

    # CHECKEO DE CONTADORES 
    if all(not enemy.alive for enemy in enemy_team):
        print("¡Todos los enemigos han sido derrotados!")
        for hero in player_team:
            loot(hero)
            hero.lvlcheck()
        return True

    if not any(hero.alive for hero in player_team):
        print("¡Has perdido la batalla!")
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