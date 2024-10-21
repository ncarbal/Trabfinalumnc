from constant import *

# 5°) CREAMOS CLASE PARA EL ENEMIGO
class Enemy:  # CLASE QUE ENGLOBA A TODOS LOS ENEMIGOS
    def __init__(self, name, health, attack, level):  # LA FUNCION QUE SE VA A EJECUTAR CUANDO CREEMOS ESTA CLASE
        self.name = name
        self.health = health + 10 * level  # LE SUMO 10 POR NIVEL 
        self.attack = attack + 10 * level
        self.alive = True  # 7°)
        self.level = level

    # METODO PARA PERDER VIDA
    def injureEnemy(self, amount):
        if self.alive:  # SOLO ME QUITA VIDA SI ESTA VIVO
            self.health -= amount
            if self.health <= 0:
                self.alive = False

# 6°) UN ENEMIGO PUEDE ATACAR CURARSE, VAMOS A DARLE METODOS, A LAS FUNCIONES DE LAS CLASES
# 7°) CREAMOS CLASE PARA NUESTRO PERSONAJE
class Hero:  # CLASE QUE ENGLOBA A TODOS LOS ENEMIGOS
    def __init__(self, name, health, attack, energy, energyCost, heal): 
        self.name = name
        self.health = health
        self.attack = attack
        self.energy = energy
        self.energyCost = energyCost
        self.heal = heal
        self.alive = True  # 7°) 
        self.experience = 0  # 8°)
        self.level = 1
        self.gold = 50
        self.lvlexp = 150
    
    # METODO PARA PERDER VIDA
    def lvlcheck(self):
        if self.experience >= self.lvlexp:
            self.level += 1
            self.lvlexp = 550
            self.health += 50
            self.attack += 50
            self.energy += 50
        """
            # Definimos los mensajes de texto que queremos mostrar al subir de nivel
            newlvl = "Nuevo nivel alcanzado:"
            newhealth = "Nueva salud:"
            newattack = "Nuevo ataque:"
            newenergy = "Nueva energía:"
            
            # Mostramos los mensajes con los valores correspondientes
            print(f"{newlvl} {self.level}")
            print(f"{newhealth} {self.health}")
            print(f"{newattack} {self.attack}")
            print(f"{newenergy} {self.energy}")
            """

    # METODO PARA PERDER VIDA
    def injureHero(self, amount):
        if self.alive:  # SOLO ME QUITA VIDA SI ESTA VIVO
            self.health -= amount
            if self.health <= 0:
                self.alive = False
    
    # METODO PARA CURARSE
    def healing(self):
        self.health += self.heal
        self.energy -= self.energyCost

    def print_level(self):
        print("Nivel:", self.level)

class Goku(Hero):
    def __init__(self):
        super().__init__("Goku", 100, 25, 100, 25, 30)

class Vegeta(Hero):
    def __init__(self):
        super().__init__("Vegeta", 100, 25, 100, 25, 30)

class Piccolo(Hero):
    def __init__(self):
        super().__init__("Piccolo", 100, 25, 100, 25, 30)

# HAGO CON SUPER UNA CLASE HIJA PARA QUE SEA MAS FACIL AÑADIR MAS PERSONAJES
class Raditz(Enemy):
    def __init__(self, level):
        super().__init__("Raditz", 20, 6, level)

class Cell(Enemy):
    def __init__(self, level):
        super().__init__("Cell", 20, 10, level)

class Freezer(Enemy):
    def __init__(self, level):
        super().__init__("Freezer", 20, 10, level)

class Androide16(Enemy):
    def __init__(self, level):
        super().__init__("Androide16", 20, 6, level)

class Androide17(Enemy):
    def __init__(self, level):
        super().__init__("Androide17", 20, 6, level)

class Androide18(Enemy):
    def __init__(self, level):
        super().__init__("Androide18", 20, 6, level)

class Burter(Enemy):
    def __init__(self, level):
        super().__init__("Burter", 20, 6, level)

class Recoome(Enemy):
    def __init__(self, level):
        super().__init__("Recoome", 20, 6, level)

class CapGinyu(Enemy):
    def __init__(self, level):
        super().__init__("CapGinyu", 20, 6, level)

