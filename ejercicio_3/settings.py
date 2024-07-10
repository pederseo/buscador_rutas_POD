import pygame
from matriz import Mapa


#datos de la matriz
MAPA_AUTO = Mapa.mapa_auto
MAPA = Mapa.mapa
FILAS = len(MAPA)
COLUMNAS = len(MAPA[0])


# Dimensiones de la pantalla y las celdas
TAMANO_VENTANA = 800
TAMANO_CELDA = TAMANO_VENTANA // len(MAPA)

#personas en el tablero
CANTIDAD_PERSONAS = 10

#elementos del tablero

FONDO = 'ejercicio_3/TEMPLATES/city2.png'
EDIFICIO = (128, 128, 128)#                     '#'
CAMINO = (255, 255, 255) #                      ' '
EMPEDRADO = 'ejercicio_3/TEMPLATES/b.png'#      '+'
OBSTACULO = 'ejercicio_3/TEMPLATES/cono.png'#   'o'
PERSONAS = 'ejercicio_3/TEMPLATES/p.png'#       'p'

AUTO_UP = 'ejercicio_3/TEMPLATES/u.png'
AUTO_DOWN = 'ejercicio_3/TEMPLATES/d.png'
AUTO_LEFT = 'ejercicio_3/TEMPLATES/l.png'
AUTO_DIGHT = 'ejercicio_3/TEMPLATES/r.png'


