import pygame
from settings import *

def direcciones(pos_anterior, siguiente_pos):
    dx = siguiente_pos[1] - pos_anterior[1]
    dy = siguiente_pos[0] - pos_anterior[0]
    
    if dx > 0:
        return 'right'
    elif dx < 0:
        return 'left'
    elif dy > 0:
        return 'down'
    elif dy < 0:
        return 'up'
    return 'up'

def dibujar_tablero(ventana,mapa):
    '''verificacion de los elementos y cre el tablero en la ventana principal'''
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            
            x = col * TAMANO_CELDA
            y = fila * TAMANO_CELDA                
            
            if mapa[fila][col] == ' ':
                pygame.draw.rect(ventana, CAMINO,( x, y, TAMANO_CELDA, TAMANO_CELDA))

            elif mapa[fila][col] == '#':
                pygame.draw.rect(ventana, EDIFICIO,( x, y, TAMANO_CELDA, TAMANO_CELDA))

def dibujar_elementos(pos_anterior, siguiente_pos, ventana, mapa):
    '''dibuja los elementos en el tablero
    'a' = auto    'p' = personas      '#' = obstaculos'''

    dx = siguiente_pos[1] - pos_anterior[1]
    dy = siguiente_pos[0] - pos_anterior[0]
    
    img_auto = AUTO_DOWN

    if dx > 0:
        img_auto = AUTO_DIGHT
    elif dx < 0:
        img_auto = AUTO_LEFT
    elif dy > 0:
        img_auto = AUTO_DOWN
    elif dy < 0:
        img_auto = AUTO_UP

    for fila in range(FILAS):
        for col in range(COLUMNAS):

            x = col * TAMANO_CELDA
            y = fila * TAMANO_CELDA

            if MAPA_AUTO[fila][col] == 'a':    
                img = pygame.image.load(img_auto).convert_alpha()
                img = pygame.transform.scale(img, (TAMANO_CELDA, TAMANO_CELDA))
                ventana.blit(img, (x, y))

            elif mapa[fila][col] == 'p':
                img = pygame.image.load(PERSONAS).convert_alpha()
                img = pygame.transform.scale(img, (TAMANO_CELDA, TAMANO_CELDA))
                ventana.blit(img, (x, y))

            elif mapa[fila][col] == 'o':
                img = pygame.image.load(OBSTACULO).convert_alpha()
                img = pygame.transform.scale(img, (TAMANO_CELDA, TAMANO_CELDA))
                ventana.blit(img, (x, y))


            elif mapa[fila][col] == '+':
                img = pygame.image.load(EMPEDRADO).convert_alpha()
                img = pygame.transform.scale(img, (TAMANO_CELDA, TAMANO_CELDA))
                ventana.blit(img, (x, y))
