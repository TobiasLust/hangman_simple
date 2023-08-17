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
    # Cipher word
    cipher = cipher_word(word)
    # List letters incorrect
    letters = []
    # Body
    incorrect = []

    print('¡El juego va a comenzar!\n En...')
    # Counter 3 2 1 ...
    counter()
    # Start
    while True:
        print('\n' + ''.join(cipher) + '\n')
        user = input(
            f'{name} Selecciona una opcion (1 - 2)\n1- Decir letra \n2- Adivinar palabra\n').strip()

        # Option 1
        if user == '1':
            letter = input('Letra: ')
            # If input letter is 1
            if len(letter) == 1:
                found = False
                # Search letter
                for i in range(len(word)):
                    if letter == word[i]:
                        cipher[i] = letter
                        found = True
                if not found:
                    # If letter before incorrect
                    if letter in letters:
                        live -= 1
                        incorrect.append(body[live])
                    # Else push letter in list
                    else:
                        letters.append(letter)
                        live -= 1
                        incorrect.append(body[live])
                print(letters, incorrect)
            # If letter not 1
            else:
                print('¡Escribiste mas de una letra o ninguna!')
        # Option 2
        elif user == '2':
            word_guess = input(
                f'¡{name} Te la juegas a todo o nada! ¿Cual es la palabra ?: ')

            if word_guess == word:
                print(f'¡{name} excelente adivinaste la palabra! GANASTE.')
                break
            else:
                print(
                    f'¡{name} incorrecta! La palabra era: {word} . Intentalo nuevamente :(')
                break
        else:
            print('Ingresa una opcion valida... (1 - 2)')

# Level choice


def level_choice(name):
    while True:
        level = input(f'''\n¡{name}! Escribe el numero del nivel que quieres jugar (Sin el punto)...
                      1. Facil
                      2. Medio
                      3. Dificil\n''').strip()  # noqa: E501
        return int(level) if 0 < int(level) <= 3 else print('Por favor escribe un numero valido (Entre 1 - 3).')  # noqa: E501

# Func cipher word


def cipher_word(word):
    cipher_w = list()
    for i in word:
        cipher_w.append('*')
    return cipher_w

# Func correct word

# Func counter


def counter():
    for i in range(3, 0, -1):
        print(f'{i}...')
        ts(0.5)


main()
