#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
pygame.init()

width, height = 400, 800

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("PlayBall")

speed = [1,1]
white = 255, 255, 255
black = 0, 0, 0

ball = pygame.image.load("img/colorBall.png")
ballRect = ball.get_rect()

runApp = True
while runApp:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit(0) 

	pygame.time.delay(2)
	ballRect = ballRect.move(speed)
	#limites de la ventana
	if ballRect.left < 0 or ballRect.right > width:
		speed[0] = -speed[0]
	if ballRect.top < 0 or ballRect.bottom > height:
		speed[1] = -speed[1]

	screen.fill(black)			#"colorear" la pantalla
	screen.blit(ball, ballRect)	#dibujar la pelota
	pygame.display.flip()		#actualizar la ppantalla

pygame.quit()