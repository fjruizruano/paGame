#!/usr/bin/env python
# -*- coding: utf-8; tab-width: 4; mode: python -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: t -*-
# vi: set ft=python sts=4 ts=4 sw=4 noet 

import pygame
from constants import HEIGHT, WIDTH
from loader import Loader

class Player(pygame.sprite.Sprite):
    def __init__(self, x_position = 0, sprite = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = Loader().load(name = sprite, color_key = True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x_position
        self.rect.centery = HEIGHT - 50
        self.speed = 0.5

    def move(self, time, keys):
        print pygame.K_LEFT, pygame.K_RIGHT, keys[pygame.K_LEFT], keys[pygame.K_RIGHT]
        if self.rect.left >= 0:
            
            if keys[pygame.K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right <= WIDTH:
            if keys[pygame.K_RIGHT]:
                self.rect.centerx += self.speed * time
                
class Tux(Player):
    def __init__(self, x_position):
        Player.__init__(self, x_position, 'tux.png')