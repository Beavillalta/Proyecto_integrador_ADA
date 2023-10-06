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