#!/usr/bin/env python
# -*- coding: utf-8; tab-width: 4; mode: python -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: t -*-
# vi: set ft=python sts=4 ts=4 sw=4 noet 

import sys

try:
	import pygame
except ImportError, e:
	print 'Error: no pygame library found'
	sys.exit(1)
	
from pygame.locals import *

if not pygame.font: 
	print 'Warning: fonts disabled'
	
if not pygame.mixer: 
	print 'Warning: sound disabled'

from loader import Loader
from constants import WIDTH, HEIGHT, TEXTCOLOR, BGCOLOR
from system import Gnu, Windows, Apple, Freebsd
from player import Tux

class Game:
	def __init__(self):
		''' Init pygame configuration and game initial config '''
		
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption('paGame 0.0.2')
		pygame.mouse.set_visible(False)
		
		self.font = pygame.font.SysFont(None, 48)
		self.ranking = [-100, -100, -100, -100, -100,]
		self.score = 0
		self.running = True
		
		self.background_image = Loader().load('bg.jpg')
		
		self.gnu = Gnu()
		self.windows = Windows()
		self.apple = Apple()
		self.freebsd = Freebsd()
		self.tux = Tux(x_position = 100)
			
		self.systems = [self.gnu, self.windows, self.apple, self.freebsd, self.tux]
	
	def terminate(self):
		''' Quit the game '''
		
		pygame.quit()
		sys.exit()
		
	def drawText(self, text, font, surface, x, y):
		''' Draw a text on screen '''
		
		textobj = font.render(text, 1, TEXTCOLOR)
		textrect = textobj.get_rect()
		textrect.topleft = (x,y)
		surface.blit(textobj, textrect)
	
	def main(self):
		''' Run the game main loop '''
		
		while self.running:
			clock = pygame.time.Clock()
			self.events = pygame.event.get()
			time = 0

			self.show_initial_screen()
			
			while self.running:
	
				time -= clock.tick(40)
				self.real_time = 60 + (time / 1000)
	
				# Update system objects
				for system in self.systems:
					system.update(time, self.tux)
				
				self.keys = pygame.key.get_pressed()
				self.tux.move(time, self.keys)
				
				self.screen.blit(self.background_image, (0, 0))
				
				for system in self.systems:
					self.screen.blit(system.image, system.rect)
				
				pygame.display.flip()
	
				self.check_collide()
				self.draw_hud()
				self.check_finished_game()

	
			self.update_scores()
			self.draw_game_over()
	
			# Restart the game
			self.running = True
	
	def show_initial_screen(self):
		''' Show the initial welcome screen '''
		
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
	
		# Show initial screen
		self.screen.fill(BGCOLOR)
		self.drawText('paGame 0.0.2', self.font, self.screen, (WIDTH/3), (HEIGHT/3))
		self.drawText('Press a key to continue.', self.font, self.screen, (WIDTH/3) - 140, (HEIGHT/3) + 50)
		self.drawText('Esc to exit', self.font, self.screen, (WIDTH/3) - 140, (HEIGHT/3) + 260)
		pygame.display.update()
		self.wait_key()
	
	def check_collide(self):
		''' Check collide for every system object '''
		
		if pygame.sprite.collide_rect(self.gnu, self.tux):
			self.score = self.score + 1
	
		if pygame.sprite.collide_rect(self.windows, self.tux):
			self.score = self.score - 1
	
		if pygame.sprite.collide_rect(self.apple, self.tux):
			self.score = self.score - 1
	
		if pygame.sprite.collide_rect(self.freebsd, self.tux):
			self.score = self.score + 1
	
	def draw_hud(self):
		''' Draw current time and score on screen (HUD: Head Up Display) '''

		self.drawText('Free level: %s' % (self.score), self.font, self.screen, 10, 10)
		self.drawText('Time: %s' % (self.real_time), self.font, self.screen, 10, 50)
	
		pygame.display.update()

	def check_finished_game(self):
		''' The game finish if score or time are -100 or 0 '''
		
		if self.score <= -100 or self.real_time <= 0:
			self.running = False
		
	def update_scores(self):
		''' Add the score ordered to list and delete the most oldest value '''
		
		self.ranking.append(self.score)
		self.ranking.sort(reverse=True)
		del self.ranking[5]
		
	def draw_game_over(self):
		''' Show the game over screen '''
		
		self.screen.fill(BGCOLOR)
		self.drawText('GAME OVER', self.font, self.screen, (WIDTH/3), (HEIGHT - 470))
		self.drawText('You score are %s' % self.score, self.font, self.screen, (WIDTH/8) - 30, (HEIGHT - 420))
			
		result_game_text = ('You are more free :)', 'You are more privative :(')[self.score <= 0]

		self.drawText(result_game_text, self.font, self.screen, (WIDTH/8) - 30, (HEIGHT - 370))

		for n in xrange(0, 5):
			self.drawText('{0}. {1}'.format(n + 1, self.ranking[n]), self.font, self.screen, (WIDTH / 6) - 30, (HEIGHT / 6) + 150 + 50 * n)

			
		pygame.display.update()
		self.wait_key()
	
	def check_exit(self):
		''' Check if the user wants exit '''
		
		for event in self.events:
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				sys.exit(0)
				
	def wait_key(self):
		''' Wait to user for press a key '''
		
		while True:
			for event in self.events:
				if event.type == pygame.QUIT or ():
					self.terminate()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.terminate()
					else:
						return

if __name__ == '__main__':
	Game().main()