from random import choice as ch
from time import sleep as ts

# Main function


def main():
    # Lives
    LIVES = 6
    PART_BODY = ['Pierna der', 'Pierna izq', 'Brazo der',
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

    if level == 1:
        level = EASY
    elif level == 2:
        level = MEDIUM
    else:
        level = HARD

    # Start game
    hangman(LIVES, PART_BODY, level, name)


# Functions

# Func game

def hangman(live, body, list, name):
    # Random choice word in list
    word = ch(list)
    
    print('¡El juego va a comenzar!\n En...')
    
    # Counter 3 2 1 ...
    counter()
    
    # Start
    while True:
            
        
            
    


# Level choice


def level_choice(name):
    while True:
        level = input(f'''\n¡{name}! Escribe el numero del nivel que quieres jugar (Sin el punto)...
                      1. Facil
                      2. Medio
                      3. Dificil\n''').strip()
        return int(level) if 0 < int(level) <= 3 else print('Por favor escribe un numero valido (Entre 1 - 3).')

# Func cipher word

# Func correct word

# Func counter


def counter():
    for i in range(3, 0, -1):
        print(f'{i}...')
        ts(0.5)


main()
