#!/usr/bin/env python
# -*- coding: utf-8; tab-width: 4; mode: python -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: t -*-
# vi: set ft=python sts=4 ts=4 sw=4 noet 

import pygame
from constants import HEIGHT, WIDTH
from loader import Loader

class System(pygame.sprite.Sprite):
    def __init__(self, sprite = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = Loader().load(name = sprite, color_key = True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - (WIDTH/5)
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]

    def update(self, time, pala_jug):
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
            
class Gnu(System):
    def __init__(self):
        System.__init__(self, 'gnu.png')

class Windows(System):
    def __init__(self):
        System.__init__(self, 'windows.png')

class Apple(System):
    def __init__(self):
        System.__init__(self, 'apple.png')

class Freebsd(System):
    def __init__(self):
        System.__init__(self, 'freebsd.png')