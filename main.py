nombre =input("escriba su nombre:")
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

# Parte 2 proyecto integrador 

from readchar import readkey , key

"""while True:
    k = readchar.readkey()
    if k != readchar.key.UP:
        print(k)
    else:
        print("bye")
        break"""
  
# proyecto integrador parte 3
import os

"""def clear_terminal():
    # Esta función borra la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    numero = 0
    while numero <= 50:
        clear_terminal()
        print("Presiona 'n' y Enter para continuar...")
        print(numero)
        llave = readkey()

        if llave == "n":
         numero  += 1  
        else: 
           break

main()"""
 
 #parte 4 

from readchar import readkey, key
import os
import time

# Mapa del laberinto
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Función para convertir el mapa en una matriz de caracteres
def crear_laberinto(laberinto_str):
    filas = laberinto_str.split("\n")
    matriz = [list(fila) for fila in filas]
    return matriz

# Función para limpiar la pantalla y mostrar el laberinto
def mostrar_laberinto(matriz):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla

    for fila in matriz:
        print("".join(fila))  # Imprime cada fila del laberinto

# Función principal del juego
def main_loop(laberinto_mapa, posicion_inicial, posicion_final):
    laberinto_matriz = crear_laberinto(laberinto_mapa)
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        mostrar_laberinto(laberinto_matriz)
        laberinto_matriz[py][px] = 'P'
        
        
        # Leer entrada del usuario
        print("Presiona una tecla de flecha para mover al jugador (q para salir): ")
        movimiento = readkey()

        if movimiento == "q":
            break
        elif movimiento == "w":
            if py - 1 >= 0 and laberinto_matriz[py - 1][px] != '#':
                laberinto_matriz[py][px] = '.'
                laberinto_matriz[py - 1][px] = 'P'
                py -= 1
        elif movimiento == "s":
            if py + 1 < len(laberinto_matriz) and laberinto_matriz[py + 1][px] != '#':
                laberinto_matriz[py][px] = '.'
                laberinto_matriz[py + 1][px] = 'P'
                py += 1
        elif movimiento == "a":
            if px - 1 >= 0 and laberinto_matriz[py][px - 1] != '#':
                laberinto_matriz[py][px] = '.'
                laberinto_matriz[py][px - 1] = 'P'
                px -= 1
        elif movimiento == "d":
            if px + 1 < len(laberinto_matriz[0]) and laberinto_matriz[py][px + 1] != '#':
                laberinto_matriz[py][px] = '.'
                laberinto_matriz[py][px + 1] = 'P'
                px += 1


    mostrar_laberinto(laberinto_matriz)

    if (px, py) == posicion_final: # mensaje de felicitacion de juego completado
        print("\n¡Felicidades! Has superado el juego del laberinto.\n")

# Coordenadas iniciales y finales
posicion_inicial = (0, 0)
posicion_final = (len(laberinto.split('\n')[0]) - 1, len(laberinto.split('\n')) - 1)

# Iniciar el juego
main_loop(laberinto, posicion_inicial, posicion_final)

# Parte 5 del Proyecto
import random
class Juego:
  def __init__ (self, laberinto, posicion_inicial, posicion_final):
      self.laberinto = laberinto
      self.posicion_inicial = posicion_inicial
      self.posicion_final = posicion_final
  
    # Función para convertir el mapa en una matriz de caracteres
  def crear_laberinto(self):
    filas = self.laberinto
    matriz = [list(fila) for fila in filas]
    return matriz

# Función para limpiar la pantalla y mostrar el laberinto
  def mostrar_laberinto(self, matriz):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla

    for fila in matriz:
        print("".join(fila))  # Imprime cada fila del laberinto

# Función principal del juego
  def main_loop(self):
    laberinto_matriz = self.crear_laberinto()
    px, py = self.posicion_inicial

    while (px, py) != self.posicion_final:
        self.mostrar_laberinto(laberinto_matriz)
        laberinto_matriz[py][px] = 'P'
        
        
        # Leer entrada del usuario
        print("Presiona una tecla de flecha para mover al jugador (q para salir): ")
        movimiento = readkey()

        if movimiento == "q":
            break
        elif movimiento == "w":
            if py - 1 >= 0 and laberinto_matriz[py - 1][px] != '#':
                laberinto_matriz[py][px] = '.'
                laberinto_matriz[py - 1][px] = 'P'
                py -= 1
        elif movimiento == "s":
            if py + 1 < len(laberinto_matriz) and laberinto_matriz[py + 1][px] != '#':
                laberinto_matriz[py][px] = '.'
                laberinto_matriz[py + 1][px] = 'P'
                py += 1
        elif movimiento == "a":
            if px - 1 >= 0 and laberinto_matriz[py][px - 1] != '#':
                laberinto_matriz[py][px] = '.'
                laberinto_matriz[py][px - 1] = 'P'
                px -= 1
        elif movimiento == "d":
            if px + 1 < len(laberinto_matriz[0]) and laberinto_matriz[py][px + 1] != '#':
                laberinto_matriz[py][px] = '.'
                laberinto_matriz[py][px + 1] = 'P'
                px += 1


    self.mostrar_laberinto(laberinto_matriz)

    if (px, py) == self.posicion_final: # mensaje de felicitacion de juego completado
        print("\n¡Felicidades! Has superado el juego del laberinto.\n")

class JuegoArchivo(Juego):
     def __init__(self, path_mapas):
         archivos_mapas = os.listdir(path_mapas)
         nombre_archivo = random.choice(archivos_mapas)
         path_completo = f"{path_mapas}/{nombre_archivo}"

         with open(path_completo, 'r') as archivo:
             contenido = archivo.read()

         lineas = contenido.split("\n")
         inicio_x, inicio_y, fin_x, fin_y = map(int, lineas[0].split())
         posicion_inicial =(inicio_x, inicio_y)
         posicion_final = (fin_x, fin_y)

         super().__init__(lineas[1:22], posicion_inicial, posicion_final)

ejecutar_juego = JuegoArchivo("mapas")
ejecutar_juego.main_loop()

 

