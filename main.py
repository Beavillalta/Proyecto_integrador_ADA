
import random
"""
laberinto =  [P, '#', '#' ,'#', '#',.
             .,. ,. ,'#', '#','#', .,
             '#' . . . . . . '#'
             '#' '#' '#' . . . .
             . . . . . . . . '#'
             '#' '#' . '#' . '#'
             . . . . . . '#' '#'
             . . . . '#' '#' '#'
             '#' . . . . '#' '#'
             '#' . '#' . '#' '#'
             . . . '#' '#' . '#'
             . '#' '#' . . . '#'
             . '#' . . . '#' '#'
             . . . . . . . . x ]  """

"""posicion_jugador = [1, 1]

def imprimir_laberinto ():
   for fila in laberinto:
      print(''.join(fila)) 

def mover_jugador(direccion)
   if direccion == 'arriba': [posicion_jugador[0]- 1, posicion_jugador]
     nueva_posicion = [posicion_jugador[0]- 1, posicion_jugador[1]]
   elif direccion == 'abajo':
     nueva_posicion = [posicion_jugador[0], + 1, posicion_jugador[1]]
   elif direccion == 'izquierda':
     nueva_posicion = [posicion_jugador[0], posicion_jugador[1] - 1]
   elif direccion == 'drecha':
     nueva_posicion = [posicion_jugador[0], posicion_jugador[1] + 1]

   if laberinto[nueva_posicion[0]][nueva_posicion[1]] != '#':
     posicion_jugador[0], posicion_jugador[1] = nueva_posicion

while True:
  imprimir_laberinto()
  print("usar las teclas W (arriba), S (abajo), A (izquierda), D (derecha) para moverte.")"""

nombre =input("escriba su nombre: ")
print(f"""
 ##         ##     #####    ######   #####     ####    ##  ##   ######    ####
 ##        ####    ##  ##   ##       ##  ##     ##     ### ##     ##     ##  ##
 ##       ##  ##   ##  ##   ##       ##  ##     ##     ######     ##     ##  ##
 ##       ######   #####    ####     #####      ##     ######     ##     ##  ##
 ##       ##  ##   ##  ##   ##       ####       ##     ## ###     ##     ##  ##
 ##       ##  ##   ##  ##   ##       ## ##      ##     ##  ##     ##     ##  ##
 ######   ##  ##   #####    ######   ##  ##    ####    ##  ##     ##      ####


      bienvenido {nombre} 

""")

# Parte 2 proyecto integrador #

import  readchar

while True:
    k = readchar.readkey()
    if k != readchar.key.UP:
        print(k)
    else:
        print("bye")
        break
  
# proyecto integrador parte 3
import os

def clear_terminal():
    # Esta función borra la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    numero = 0
    while numero <= 50:
        clear_terminal()
        print(numero)
        input("Presiona 'n' y Enter para continuar...")
        numero += 1

if __name__ == "__main__":
    main()
