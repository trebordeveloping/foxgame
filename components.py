#-------------------------------------------------------------------------------
# Name:        components
# Purpose:     game components: player, obstacles, etc.
#
# Author:      robert.cormack
#
# Created:     20/04/2021
# Copyright:   (c) robert.cormack 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame

class Player():

    def __init__(self, x, y, jumpHeight, jumpVar, hp, immunity, score, sprites):

        self.x = x
        self.y = y
        self.jumpHeight = jumpHeight
        self.jumpCount = jumpHeight
        self.jumpVar = jumpVar
        self.hp = hp
        self.immunity = immunity
        self.score = score

        for i, sprite in enumerate(sprites):
            
            width, height = sprite.get_size()
            width, height = width // 8, height // 8
            size = (width, height)
            sprites[i] = pygame.transform.scale(sprite, size)

        self.sprites = sprites

    def checkHit(self, obX, obY, obWidth, obHeight):

        if self.immunity > 0:
            self.immunity -= 1

        elif obX <= self.x <= obX + obWidth and obY <= self.y <= obY + obHeight:
            self.hp -= 1
            self.immunity = 40

    def jump(self):

        if self.jumpCount > 0:
            self.y -= self.jumpCount ** 2 * 0.02
            self.jumpCount -= 1
            
        elif self.jumpCount >= -self.jumpHeight:
            self.y += self.jumpCount ** 2 * 0.02
            self.jumpCount -= 1

        elif self.jumpCount == -self.jumpHeight - 1:
            self.jumpVar = False
            self.jumpCount = self.jumpHeight


class Obstacle():

    def __init__(self, x, y, sprite, speed, count):

        self.x = x
        self.y = y
        self.speed = speed
        self.count = count

        self.width, self.height = sprite.get_size()
        self.width, self.height = self.width // 20, self.height // 20
        self.size = (self.width, self.height)

        self.sprite = pygame.transform.scale(sprite, self.size)

    

class Floor():

    def __init__(self, sprite):

        w, h = sprite.get_size()
        self.width, self.height = int(w*((h+30)/h)), int(h*((h+30)/h))
        self.sprite = pygame.transform.scale(sprite, (self.width, self.height))
        

    def draw(self, screen, x, y):
        screen.blit(self.sprite, (x, y))

class Screen():

    def __init__(self, width, height, sprite):

        self.width = width
        self.height = height
        self.dimensions = [width, height]
        w, h = sprite.get_size()
        self.sprW, self.sprH = int(w * (self.width/w)), int(h * (self.width/w))

        self.sprite = pygame.transform.scale(sprite, (self.sprW, self.sprH))
