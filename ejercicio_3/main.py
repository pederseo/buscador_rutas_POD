
import pygame
from tablero import dibujar_tablero, dibujar_elementos
from eventos import detectar_evento, agregar_elementos, mover_auto
from settings import MAPA, MAPA_AUTO, TAMANO_VENTANA,FONDO
from algoritmo import Algoritmo

class Juego():

    def __init__(self):
        '''Iniciar PYGAME y declaracion de variables'''

        pygame.init()

        self.clock = pygame.time.Clock()  # Crear un objeto Clock

        self.ventana = pygame.display.set_mode((TAMANO_VENTANA, TAMANO_VENTANA))

        self.game_name = pygame.display.set_caption("UBER TRIP")

        self.mapa = MAPA

        self.auto = (0,0)

        self.objetivo = (0,0)

        self.camino = [(0,0)]

        self.pos_anterior = (0,0)

        self.agregar_elementos = agregar_elementos(self.mapa,self.auto)

        self.img_fondo = pygame.image.load(FONDO).convert()
        self.img_fondo = pygame.transform.scale(self.img_fondo, (TAMANO_VENTANA, TAMANO_VENTANA))

    def ejecutar(self):
        '''Bucle principal PYGAME'''

        while True:
            # detecta el evento click dentro de la ventana
            new_objetivo = detectar_evento(self.mapa)

            # si se detecta las coordenadas del objetivo
            if new_objetivo:
                algoritmo = Algoritmo(self.mapa, self.auto, new_objetivo)
                self.camino = algoritmo.a_star()
                self.objetivo = new_objetivo

            # si el auto alcanza a la persona
            elif self.auto == self.objetivo:
                MAPA[self.objetivo[0]][self.objetivo[1]] = ' '            

            # se tenemos camino el auto se mueve
            elif self.camino:
                self.pos_anterior = self.auto
                self.auto = mover_auto(self.camino)
            
            # actualiza los elementos del tablero
            self.ventana.fill((0, 0, 0))
            self.ventana.blit(self.img_fondo, (0, 0))  # Dibuja el fondo

            # self.tablero = dibujar_tablero(self.ventana, self.mapa)

            self.elementos = dibujar_elementos(self.pos_anterior,self.auto, self.ventana, self.mapa)
            pygame.display.flip()

            # cuadros por segundo (FPS)
            self.clock.tick(10)  


if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()