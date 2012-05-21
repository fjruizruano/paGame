#!/usr/bin/env python
# -*- coding: utf-8; tab-width: 4; mode: python -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: t -*-
# vi: set ft=python sts=4 ts=4 sw=4 noet 

import os
import pygame

class Loader:
    def load(self, name = None, color_key = None):
        self.image_path = os.path.join('img', name)
        
        try:
            self.image = pygame.image.load(self.image_path) 
        except pygame.error, message: 
            print 'Could not load the image:', name
            raise SystemExit, message
        
        self.image = self.image.convert()
        
        if color_key: 
            color_key = self.image.get_at((0,0))
            self.image.set_colorkey(color_key, pygame.RLEACCEL)
        
        return self.image