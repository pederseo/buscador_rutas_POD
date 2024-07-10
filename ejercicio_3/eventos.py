import pygame
import random
from settings import *

#__________________________________________________________________________________________________
def mover_auto(camino):
    '''recorre el camino encontrado por A* y actualiza las posiciones'''
    # Obtener la siguiente coordenada del camino
    next_x,next_y = camino.pop(0)
    
    # Buscar la posición actual del auto
    x,y = encontrar_posicion(MAPA_AUTO,'a')

    # Limpiar la posición actual del auto
    MAPA_AUTO[x][y] = ' '

    # Colocar el auto en la nueva posición
    MAPA_AUTO[next_x][next_y] = 'a'

    return (next_x,next_y)

#__________________________________________________________________________________________________
def encontrar_posicion(mapa,elemento):
    '''Encuentra la posición inicial del auto en la matriz'''

    for fila in range(len(mapa)):
        for col in range(len(mapa[fila])):
            if mapa[fila][col] == elemento:
                return (fila, col)
            
#__________________________________________________________________________________________________
def click_persona(mapa):
    '''click izquierdo sobre persona'''

    x, y = pygame.mouse.get_pos()
    col = x // (TAMANO_VENTANA // len(mapa[0]))
    fila = y // (TAMANO_VENTANA // len(mapa))
    if mapa[fila][col] == 'p':  # Si se hace click en una persona
        # print(f'persona {fila,col}')
        return (fila, col)  # Devolver las coordenadas de la persona
    
#__________________________________________________________________________________________________
def click_obstaculo(mapa):
    '''click derecho para agregar obstaculos'''

    x, y = pygame.mouse.get_pos()
    col = x // (TAMANO_VENTANA // len(mapa[0]))
    fila = y // (TAMANO_VENTANA // len(mapa))

    obs_exist = encontrar_posicion(MAPA,'o')

    if mapa[fila][col] == ' ' or mapa[fila][col] == '+':  # Si se hace click en el camino
        mapa[fila][col] = "o"
        # print(f'obstaculos {fila,col}')

        if obs_exist:
            MAPA[obs_exist[0]][obs_exist[1]] = ' '

#__________________________________________________________________________________________________
def detectar_evento(mapa):
    '''detecta los eventos click dentro de la ventana PYGAME'''

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT: # detecta el boton de salir
            pygame.quit()
            quit()
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:  # Detectar click izquierdo
               return click_persona(mapa)
                
            elif pygame.mouse.get_pressed()[2]:  # Detectar click derecho
                click_obstaculo(mapa)
                
#__________________________________________________________________________________________________
def agregar_elementos(mapa,auto):
    '''agrega el auto y las personas de forma aleatoria al mapa'''

    mapa[0][0] = '+'

    MAPA_AUTO[auto[0]][auto[1]] = 'a'

    caminos = []
    for x in range(len(mapa)):
        for y in range(len(mapa[x])):
            if mapa[x][y] == ' ':
                caminos.append((x, y))

    posicion_personas = random.sample(caminos, CANTIDAD_PERSONAS)

    for p in posicion_personas:
        if mapa[p[0]][p[1]] == ' ':
            mapa[p[0]][p[1]] = 'p'

