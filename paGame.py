#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, pygame, random
import time as tiempo
from pygame.locals import *
 
if not pygame.font: print 'estilos y letras desactivadas!'
if not pygame.mixer: print 'sonidos desactivados!'

WIDTH = 640
HEIGHT = 480
TEXTCOLOR = (255, 255, 255)
BGCOLOR = (0,0,0)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# set up font
font = pygame.font.SysFont(None, 48)

class Gnu(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = carga_imagen("gnu.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		self.speed = [0.5, -0.5]

	def actualizar(self, time, pala_jug):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time

		if pygame.sprite.collide_rect(self, pala_jug):
#			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time

class Windos(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = carga_imagen("windos.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 3
		self.rect.centery = HEIGHT / 3
		self.speed = [0.5, -0.5]

	def actualizar(self, time, pala_jug):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time

		if pygame.sprite.collide_rect(self, pala_jug):
#			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time


class Apple(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = carga_imagen("apple.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 4
		self.rect.centery = HEIGHT / 4
		self.speed = [0.5, -0.5]

	def actualizar(self, time, pala_jug):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time

		if pygame.sprite.collide_rect(self, pala_jug):
#			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time


class Logo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
#		self.image = carga_imagen("gnu.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		self.speed = [0.5, -0.5]

	def actualizar(self, time, pala_jug):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time

		if pygame.sprite.collide_rect(self, pala_jug):
#			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time


class Logo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
#		self.image = carga_imagen("gnu.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		self.speed = [0.5, -0.5]

	def actualizar(self, time, pala_jug):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time

		if pygame.sprite.collide_rect(self, pala_jug):
#			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time


class Logo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
#		self.image = carga_imagen("gnu.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		self.speed = [0.5, -0.5]

	def actualizar(self, time, pala_jug):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time

		if pygame.sprite.collide_rect(self, pala_jug):
#			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time


class Tux(pygame.sprite.Sprite):
	def __init__(self, x):
		pygame.sprite.Sprite.__init__(self)
		self.image = carga_imagen("tux.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = HEIGHT-50 # / 2
		self.speed = 0.5

	def mover(self, time, keys):
		if self.rect.left >= 0:
			if keys[K_LEFT]:
				self.rect.centerx -= self.speed * time
		if self.rect.right <= WIDTH:
			if keys[K_RIGHT]:
				self.rect.centerx += self.speed * time

def waitForPlayerToPressKey():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE: # pressing escape quits
					terminate()
				return

def drawText(text, font, surface, x, y):
	textobj = font.render(text, 1, TEXTCOLOR)
	textrect = textobj.get_rect()
	textrect.topleft = (x,y)
	surface.blit(textobj, textrect)

def carga_imagen(name, colorkey=None):
	fullname = os.path.join('img', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'No se puede cargar la imagen:', name
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None: 
		if colorkey is -1: 
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image

def carga_fondo(name, colorkey=None):
	fullname = os.path.join('img', name)
	try:
		image = pygame.image.load(fullname) 
	except pygame.error, message: 
		print 'No se puede cargar la imagen:', name
		raise SystemExit, message
	image = image.convert()
	return image

countdown = 60
def main():

	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	# show the start screen
	screen.fill(BGCOLOR)
	drawText('Dodger', font, screen, (WIDTH/3), (HEIGHT/3))
	drawText('Press a key to start.', font, screen, (WIDTH/3) - 30, (HEIGHT/3) + 50)
	pygame.display.update()
	waitForPlayerToPressKey()

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Colisiones Pygame")

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	background_image = carga_fondo("fondo.bmp")

	gnu = Gnu()
	windos = Windos()
	apple = Apple()
	tux = Tux(100)
	clock = pygame.time.Clock()

	SCORE = 0


	while True:
		time = clock.tick(40)
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				sys.exit(0)

		gnu.actualizar(time, tux)
		windos.actualizar(time, tux)
		apple.actualizar(time, tux)
		tux.mover(time, keys)
		screen.blit(background_image, (0, 0))
		screen.blit(gnu.image, gnu.rect)
		screen.blit(windos.image, windos.rect)
		screen.blit(apple.image, apple.rect)
		screen.blit(tux.image, tux.rect)
		pygame.display.flip()

		if pygame.sprite.collide_rect(gnu, tux):
			SCORE = SCORE + 1

		if pygame.sprite.collide_rect(windos, tux):
			SCORE = SCORE - 1

		if pygame.sprite.collide_rect(apple, tux):
			SCORE = SCORE - 1



		#puntuacion
		drawText('Score: %s' % (SCORE), font, screen, 10, 0)
		drawText('Time: %s' % (countdown), font, screen, 10, 40)
		pygame.display.update()

	return 0

if __name__ == '__main__':
	pygame.init()
	main()

