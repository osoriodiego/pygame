#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, pygame
pygame.init()


width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("baseball")

speed = [1, 1]
white = 255, 255, 255

# Crea un objeto imagen pelota y obtengo su rectángulo
ball = pygame.image.load("img/colorBall.png")
ballrect = ball.get_rect()

# Crea un objeto imagen bate y obtengo su rectángulo
bate = pygame.image.load("img/bate64.png")
baterect = bate.get_rect()
baterect.move_ip((width/2, height/2))	#Ubicar el bate


run=True
while run:
	pygame.time.delay(0)
	# Capturamos los eventos que se han producido
	for event in pygame.event.get():
		#Si el evento es salir de la ventana, terminamos
		if event.type == pygame.QUIT: run = False
	# Compruebo si se ha pulsado alguna tecla
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		baterect=baterect.move(0, -1)
	if keys[pygame.K_RIGHT]:
		baterect=baterect.move(1, 0)
	if keys[pygame.K_DOWN]:
		baterect=baterect.move(0, 1)
	if keys[pygame.K_LEFT]:
		baterect=baterect.move(-1, 0)
	# Compruebo si hay colisión
	if baterect.colliderect(ballrect):
		speed[0] = - speed[0]
	# Muevo la pelota
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	screen.fill(white)			#"colorear" la pantalla
	screen.blit(ball, ballrect)	#dibujar los elementos - pelota
	screen.blit(bate, baterect)	#dibujar los elementos - bate
	pygame.display.flip()		#actualizar la pantalla
# Salgo de pygame
pygame.quit()