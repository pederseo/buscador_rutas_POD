# import pygame
# import sys
# from algoritmo import Algoritmo
# import heapq

# # Clase del jugador
# class Jugador:
#     def __init__(self, posicion):
#         self.posicion = posicion

#     def mover(self, nuevo_camino):
#         if nuevo_camino:
#             self.posicion = nuevo_camino.pop(0)
#             return nuevo_camino
#         return None

# # Inicialización de pygame
# pygame.init()

# # Configuración de colores
# COLOR_CAMINO = (255, 255, 255)  # Blanco
# COLOR_OBSTACULO = (0, 0, 0)     # Negro
# COLOR_INICIO = (0, 255, 0)      # Verde
# COLOR_OBJETIVO = (255, 0, 0)    # Rojo
# COLOR_JUGADOR = (0, 0, 255)     # Azul

# # Tamaño del tablero
# ANCHO_CELDA = 40
# ALTO_CELDA = 40

# filas = 10
# columnas = 10

# ancho_ventana = columnas * ANCHO_CELDA
# alto_ventana = filas * ALTO_CELDA

# # Configuración de la pantalla
# pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
# pygame.display.set_caption("algoritmo A*")

# # Matriz del mapa
# mapa = [
#     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#     [' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' '],
#     [' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' '],
#     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#     [' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' '],
#     [' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' '],
#     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#     [' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' '],
#     [' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' '],
#     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# ]

# inicio = (0, 0)
# objetivo = (9, 9)

# def dibujar_tablero():
#     for fila in range(filas):
#         for columna in range(columnas):
#             color = COLOR_CAMINO if mapa[fila][columna] == ' ' else COLOR_OBSTACULO

#             pygame.draw.rect(pantalla, color, (columna * ANCHO_CELDA,
#                                                 fila * ALTO_CELDA, 
#                                                 ANCHO_CELDA, 
#                                                 ALTO_CELDA))
                
#     pygame.draw.rect(pantalla, COLOR_INICIO, (inicio[1] * ANCHO_CELDA, 
#                                               inicio[0] * ALTO_CELDA, 
#                                               ANCHO_CELDA, 
#                                               ALTO_CELDA))
    
#     pygame.draw.rect(pantalla, COLOR_OBJETIVO, (objetivo[1] * ANCHO_CELDA, 
#                                                 objetivo[0] * ALTO_CELDA, 
#                                                 ANCHO_CELDA, 
#                                                 ALTO_CELDA))

# algoritmo = Algoritmo(mapa, inicio, objetivo)
# jugador = Jugador(inicio)
# camino = algoritmo.a_star()

# # ____________________________________________________Bucle principal del juego_____________________________________________
# corriendo = True
# while corriendo:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             corriendo = False

#         if evento.type == pygame.MOUSEBUTTONDOWN:
#             x, y = evento.pos
#             fila = y // ALTO_CELDA
#             columna = x // ANCHO_CELDA
            
#             if mapa[fila][columna] == ' ':  # Solo permite poner obstáculos en caminos
#                 mapa[fila][columna] = '#'
#                 algoritmo = Algoritmo(mapa, jugador.posicion, objetivo)
#                 camino = algoritmo.a_star()  # Recalcular el camino si se añaden obstáculos

#     if camino:
#         camino = jugador.mover(camino)

#     pantalla.fill((0, 0, 0))
#     dibujar_tablero()
#     pygame.draw.rect(pantalla, COLOR_JUGADOR, (jugador.posicion[1] * ANCHO_CELDA, jugador.posicion[0] * ALTO_CELDA, ANCHO_CELDA, ALTO_CELDA))
#     pygame.display.flip()
#     pygame.time.wait(500)  # Espera de 500ms entre movimientos

# pygame.quit()
# sys.exit()


import pygame
import sys
import time

# Inicializa Pygame
pygame.init()

# Configura la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UBER TRIP")

# Define los colores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define el tamaño de cada celda del tablero
CELL_SIZE = 40

# Matriz del tablero
board = [
    [' ', ' ', '#', ' ', 'p'],
    ['+', ' ', '#', ' ', ' '],
    [' ', '+', '#', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', 'a', ' ', ' ', ' ']
]

# Lista de coordenadas del camino
path = [(4, 1), (3, 1), (2, 1), (1, 1), (1, 0), (0, 0)]

def draw_board(screen, board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            cell_value = board[row][col]
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if cell_value == ' ':
                color = WHITE
            elif cell_value == '+':
                color = GRAY
            elif cell_value == '#':
                color = DARK_GRAY
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

def add_entities(screen, board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            cell_value = board[row][col]
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if cell_value == 'a':
                pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))
            elif cell_value == 'p':
                pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))

def move_auto(board, path):
    if path:
        # Obtener la siguiente coordenada del camino
        next_pos = path.pop(0)
        # Buscar la posición actual del auto
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'a':
                    # Limpiar la posición actual del auto
                    board[row][col] = ' '
                    # Colocar el auto en la nueva posición
                    board[next_pos[0]][next_pos[1]] = 'a'
                    return

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover el auto
    move_auto(board, path)
    
    screen.fill((0, 0, 0))  # Limpia la pantalla
    draw_board(screen, board)
    add_entities(screen, board)
    
    pygame.display.flip()
    
    # Pausa para controlar la velocidad del movimiento
    time.sleep(0.5)

pygame.quit()
sys.exit()
