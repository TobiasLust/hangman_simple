from random import choice as ch
from time import sleep as ts

# Main function


def main():
    # Lives
    LIVES = 6
    BODY = ['Pierna der', 'Pierna izq', 'Brazo der',
            'Brazo izq', 'Cuerpo', 'Cabeza']

    # Define words for levels
    EASY = ['gato', 'nube', 'tierra', 'arbol', 'silla', 'plato', 'mesa']
    MEDIUM = ['cuchara', 'planeta', 'elefante', 'universidad', 'zafari']
    HARD = ['zanahoria', 'interplanetario', 'futurista',
            'esdrujula', 'cosmopolitan', 'otorrinolaringolo']

    # Welcome and request name
    print('¡Bienvenidos al Ahorcado!')
    ts(0.5)
    name = input('¿Cual es tu nombre? ').strip()
    # Choice level
    ts(0.5)
    level = level_choice(name)
    print(level)

    # Start game


# Functions

# Level choice
def level_choice(name):
    while True:
        level = input(f'''\n¡{name}! Escribe el numero del nivel que quieres jugar (Sin el punto)...
                      1. Facil
                      2. Medio
                      3. Dificil\n''')
        return int(level) if 0 < int(level) <= 3 else print('Por favor escribe un numero valido (Entre 1 - 3).')

# Func game

# Func cipher word

# Func correct word


main()
