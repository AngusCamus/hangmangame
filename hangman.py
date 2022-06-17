
import time
import os
from algoritm import select_word
from algoritm import refresh_word

#global vars
letters_list = []
player_points = 100
fresh_word = ""

#Screen and algoritm calls
def visual_screen(player_points):
    print("""
**  **    ***    **   **  *******   **      **    ***    **   **  
**  **   ** **   ***  **  **        ***    ***   ** **   ***  **  
******   *****   **** **  **  ***   ****  ****   *****   **** **  
**  **  **   **  ** ****  **   **   ** **** **  **   **  ** ****  
**  **  **   **  **  ***  *******   **  **  **  **   **  **  ***
Created by __Pole__""")
    print("Bienvenido al juego del ahorcado. Intenta adivinar la siguiente palabra: ")
    print(f"Tu puntaje actual es: '{player_points}'")

refresh = lambda: os.system("cls")

def refresh_screen(random_word,letters_list):
    global player_points
    global fresh_word
    
    while True:
        list_word = list(random_word)
        visual_screen(player_points)
        fresh_word = refresh_word(list_word, letters_list).upper()
        print(fresh_word)

        #Defeat o victory check
        if player_points == 0:
            refresh()
            user_input = input("Lo siento, perdiste!! Pulsa 'E' para volver a jugar o cualquier otra tecla + 'Enter' para salir ").upper()
            if user_input == 'E': 
                refresh()
                run()
            else: break
        elif '-' not in fresh_word:
            refresh()
            user_input = input("Felicidades, has ganado! Pulsa 'E' y luego 'Enter' para volver a jugar o cualquier otra tecla + 'Enter' para salir ").upper()
            if user_input == 'E': 
                refresh()
                run()
            else: break
        else: user_letter = input("Ingresa una letra y luego presiona 'Enter': ")

        #assert or not assert letter
        if user_letter in letters_list:
            player_points -=10
            fresh_word = refresh_word(list_word, letters_list).upper()
            print("Ya elegiste esa letra antes, se restaran 10 puntos")
            time.sleep(1.5)
            refresh()
            continue
        elif user_letter in list_word:
            letters_list.append(user_letter)
            fresh_word = refresh_word(list_word, letters_list).upper()
            print("Acertaste!")
            time.sleep(1)
            refresh()
            continue
        else:
            letters_list.append(user_letter)
            player_points -=10
            fresh_word = refresh_word(list_word, letters_list).upper()
            print("La letra no esta dentro de la palabra, se restaran 10 puntos")
            time.sleep(1.5)
            refresh()
            continue

        refresh()


def run():
    #Reset global vars
    global player_points
    global letters_list
    global fresh_word
    letters_list = []
    player_points = 100
    fresh_word = ""

    #select new word
    random_word = select_word()

    #play the game
    refresh_screen(random_word, letters_list)
    





if __name__ =='__main__': run()