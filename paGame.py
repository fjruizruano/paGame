#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, pygame
from pygame.locals import *
 
if not pygame.font: print 'estilos y letras desactivadas!'
if not pygame.mixer: print 'sonidos desactivados!'

WIDTH = 640
HEIGHT = 480

def carga_fondo (name, colorkey=None):
	fullname = os.path.join("img", name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print "No se puede cargar la imagen", name
		raise SystemExit, message
	image = image.convert()
	return image, image.get_rect()

def main():

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("¡Hola pyGame!")
	background_image = carga_fondo("fondo.bmp")
	screen.blit(background_image[0], (0, 0))
	pygame.display.flip()	
	while True:
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
#		screen.blit(background_image, (0, 0))
#		pygame.display.flip()	
	return 0

if __name__ == '__main__':
	pygame.init()
	main()
