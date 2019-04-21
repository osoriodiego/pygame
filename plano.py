# coding=utf-8

# importa la librería Pygame
import pygame

from color import *

width, height = 600, 600
center = (width/2, height/2)



class cartesiano:
    
    def __init__(self):
        # establece el título de la ventana
        pygame.display.set_caption('Plano cartesiano')

        # establece el tamaño de la ventana
        self.screen = pygame.display.set_mode((width, height))

        # pygame.draw.line(Surface, color, start_pos, end_pos, width=1): return Rect
        self.x = pygame.draw.line(self.screen, color.beige, (width/2, 0), (width/2, height), 1)
        self.y = pygame.draw.line(self.screen, color.beige, (0, height/2), (width, height/2), 1)

    def new_pos(self, pos):
        if ((pos[0]>=0) and (pos[1]>=0)): return (((width/2) + pos[0]), (((height/2) - pos[1])))
        if ((pos[0]>=0) and (pos[1]<=0)): return (((width/2) + pos[0]), (((height/2) + pos[1])))
        if ((pos[0]<=0) and (pos[1]<=0)): return (((width/2) - pos[0]), (((height/2) + pos[1])))
        if ((pos[0]<=0) and (pos[1]>=0)): return (((width/2) - pos[0]), (((height/2) - pos[1])))

    def punto(self, pos):
        # pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
        #npos = self.new_pos(pos)
        pygame.draw.circle(self.screen, color.lima, self.new_pos(pos), 3)


    def circulo(self, pos, radio):
        # pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
        pygame.draw.circle(self.screen, color.salmon_suave, self.new_pos(pos), radio, 1)


    def linea(self, inicio, fin):
        pygame.draw.line(self.screen, color.salmon_suave, self.new_pos(inicio), self.new_pos(fin), 1)


    def recta(self, pendiente):
        pass


if __name__ == '__main__':

    # inicializa Pygame
    pygame.init()
    
    plano = cartesiano()

    plano.punto((90,90))
    plano.punto((90,-90))
    plano.punto((-90,-90))
    plano.punto((-90,90))
    plano.punto((0,0))

    plano.linea((100,190), (12,100))
    plano.linea((100,-190), (12,-100))
    plano.linea((-100,-190), (-12,100))
    plano.linea((-100,190), (-12,-100))
    plano.linea((0,0), (300,300))

    plano.circulo((100,100), 30)
    plano.circulo((100,-100), 30)
    plano.circulo((-100,-100), 30)
    plano.circulo((-100,100), 30)
    plano.circulo((0,0), 100)
    plano.circulo((0,300), 100)



    # actualiza la pantalla
    pygame.display.flip()

    # bucle infinito
    while True:
        # retorna un solo evento de la cola de eventos
        event = pygame.event.wait()

        # si se presiona el botón 'cerrar' de la ventana
        if event.type == pygame.QUIT:
            # detiene la aplicación
            break

    # finaliza Pygame
    pygame.quit()