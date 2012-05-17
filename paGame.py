#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, pygame, random
from pygame.locals import *
 
if not pygame.font: print 'estilos y letras desactivadas!'
if not pygame.mixer: print 'sonidos desactivados!'

# variables
WIDTH = 640
HEIGHT = 480
TEXTCOLOR = (255, 255, 255) # color del texto
BGCOLOR = (0,0,0) # color del fondo
ranking = [-100, -100, -100, -100, -100,] # ranking vacío

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('paGame 0.0.2')
pygame.mouse.set_visible(False)

# fuente
font = pygame.font.SysFont(None, 48)

# definimos objeto GNU
class Gnu(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = carga_imagen("gnu.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH - (WIDTH/5)
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
			self.rect.centerx += self.speed[0] * time

# definimos objeto Windos
class Windos(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = carga_imagen("windos.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH - (2 * WIDTH/5)
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
			self.rect.centerx += self.speed[0] * time

# definimos objeto Apple
class Apple(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = carga_imagen("apple.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH - (3*WIDTH/5)
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
			self.rect.centerx += self.speed[0] * time

# definimos objeto FreeBSD
class Freebsd(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = carga_imagen("freebsd.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH - (4*WIDTH/5)
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
			self.rect.centerx += self.speed[0] * time

# definimos jugador Tux
class Tux(pygame.sprite.Sprite):
	def __init__(self, x):
		pygame.sprite.Sprite.__init__(self)
		self.image = carga_imagen("tux.png",-1)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = HEIGHT-50
		self.speed = 0.5

	def mover(self, time, keys):
		if self.rect.left >= 0:
			if keys[K_LEFT]:
				self.rect.centerx -= self.speed * time
		if self.rect.right <= WIDTH:
			if keys[K_RIGHT]:
				self.rect.centerx += self.speed * time

# definimos función presionar cualquier tecla
def waitForPlayerToPressKey():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE: # presionar Esc sale del juego
					terminate()
				return

#definimos terminate para salir del juego
def terminate():
	pygame.quit()
	sys.exit()

# definimos función dibujar texto
def drawText(text, font, surface, x, y):
	textobj = font.render(text, 1, TEXTCOLOR)
	textrect = textobj.get_rect()
	textrect.topleft = (x,y)
	surface.blit(textobj, textrect)

# definimos función cargar imagen
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

# definimos función cargar fondo
def carga_fondo(name, colorkey=None):
	fullname = os.path.join('img', name)
	try:
		image = pygame.image.load(fullname) 
	except pygame.error, message: 
		print 'No se puede cargar la imagen:', name
		raise SystemExit, message
	image = image.convert()
	return image

def main():

	while True:

		screen = pygame.display.set_mode((WIDTH, HEIGHT))

		# mostramos pantalla de inicio
		screen.fill(BGCOLOR)
		drawText('paGame 0.0.2', font, screen, (WIDTH/3), (HEIGHT/3))
		drawText('Presione una tecla para continuar.', font, screen, (WIDTH/3) - 140, (HEIGHT/3) + 50)
		drawText('Esc para salir', font, screen, (WIDTH/3) - 140, (HEIGHT/3) + 260)
		pygame.display.update()
		waitForPlayerToPressKey()

		# cargamos imagen de fondo
		background_image = carga_fondo("fondo.bmp")

		# variables de la partida
		gnu = Gnu()
		windos = Windos()
		apple = Apple()
		freebsd = Freebsd()
		tux = Tux(100)
		clock = pygame.time.Clock()

		SCORE = 0
		vivo = True
		tiempo = 0

		# mientras sigamos vivos...
		while vivo == True:

			# temporizador
			time = clock.tick(40)
			tiempo -= time
			tiempo_real = 60+(tiempo/1000)

			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					sys.exit(0)

			# cargamos los objetos
			gnu.actualizar(time, tux)
			windos.actualizar(time, tux)
			apple.actualizar(time, tux)
			freebsd.actualizar(time, tux)
			tux.mover(time, keys)
			screen.blit(background_image, (0, 0))
			screen.blit(gnu.image, gnu.rect)
			screen.blit(windos.image, windos.rect)
			screen.blit(apple.image, apple.rect)
			screen.blit(freebsd.image, freebsd.rect)
			screen.blit(tux.image, tux.rect)
			pygame.display.flip()

			# definimos los cambios de puntuación según objeto
			if pygame.sprite.collide_rect(gnu, tux):
				SCORE = SCORE + 1

			if pygame.sprite.collide_rect(windos, tux):
				SCORE = SCORE - 1

			if pygame.sprite.collide_rect(apple, tux):
				SCORE = SCORE - 1

			if pygame.sprite.collide_rect(freebsd, tux):
				SCORE = SCORE + 1

			# dibujamos en pantalla el tiempo y la puntuación actuales
			drawText('Libre Level: %s' % (SCORE), font, screen, 10, 10)
			drawText('Tiempo: %s' % (tiempo_real), font, screen, 10, 50)

			pygame.display.update()

			# la partida termina si la puntuación o el tiempo son menores o iguales que -100 y 0
#			if SCORE <= -100 or tiempo_real <= 55:
			if SCORE <= -100 or tiempo_real <= 0:
				vivo = False

		# añadimos la puntuación a la lista, la ordenamos y borramos el valor más bajo
		ranking.append(SCORE)
		ranking.sort(reverse=True)
		del ranking[5]

		# pantalla de Game Over y ranking al finalizar la partida		
		screen.fill(BGCOLOR)
		drawText('GAME OVER', font, screen, (WIDTH/3), (HEIGHT - 470))
		drawText('Su puntuacion ha sido %s' % SCORE, font, screen, (WIDTH/8) - 30, (HEIGHT - 420))
		if SCORE <= 0: # si la puntuación es menor o igual que 0 eres más privativo
			drawText('Eres mas privativo :(', font, screen, (WIDTH/8) - 30, (HEIGHT - 370))
		elif SCORE > 0: # si la puntuación es mayor que 0 eres más libre
			drawText('Eres mas libre :)', font, screen, (WIDTH/8) - 30, (HEIGHT - 370))
		drawText('1. %s' % ranking[0], font, screen, (WIDTH/6) - 30, (HEIGHT/6) + 150)
		drawText('2. %s' % ranking[1], font, screen, (WIDTH/6) - 30, (HEIGHT/6) + 200)
		drawText('3. %s' % ranking[2], font, screen, (WIDTH/6) - 30, (HEIGHT/6) + 250)
		drawText('4. %s' % ranking[3], font, screen, (WIDTH/6) - 30, (HEIGHT/6) + 300)
		drawText('5. %s' % ranking[4], font, screen, (WIDTH/6) - 30, (HEIGHT/6) + 350)
		pygame.display.update()
		waitForPlayerToPressKey()

		# si se reinicia el juego, volvemos a estar vivos
		vivo = True

if __name__ == '__main__':
	pygame.init()
	main()

