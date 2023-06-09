import pygame
import time

class Narco:
    def __init__(self, player, x, y, data, spriteSheet, animationSteps):
        self._player = player
        self._size = data[0]
        self._imageScale = data[1]
        self._offset = data[2]
        self._animationList = self.loadImages(spriteSheet, animationSteps)
        self._action = 0
        self._frameIndex = 0
        self._image = self._animationList[self._action][self._frameIndex]
        self._updateTime = pygame.time.get_ticks()
        self._rect = pygame.Rect((x, y, 60, 150))
        self._sy = 0
        self._run = False
        self._jump = False
        self._attacking = False
        self._attackType = 0
        self._attackCD = 0
        self.health = 100
        self._alive = True

    def loadImages(self, spriteSheet, animationSteps):
        animationList = []
        for i, animation in enumerate(animationSteps):
            tempImg = []
            for e in range(animation):
                temp = spriteSheet.subsurface(e * self._size, i * self._size, self._size, self._size)
                tempImg.append(pygame.transform.scale(temp, (self._size * self._imageScale, self._size * self._imageScale)))
            animationList.append(tempImg)
        return animationList


    def update(self):
        if self.health <= 0:
            self.health = 0
            self._alive = False
            self.updateAction(5)
        elif self._attacking == True:
            if self._player == 1:
                if self._attackType == 1:
                    self.updateAction(1)
                elif self._attackType == 2:
                    self.updateAction(4)
                elif self._attackType == 3:
                    self.updateAction(0)
                elif self._attackType == 4:
                    self.updateAction(3)
            elif self._player == 2:
                if self._attackType == 1:
                    self.updateAction(4)
                elif self._attackType == 2:
                    self.updateAction(1)
                elif self._attackType == 3:
                    self.updateAction(0)
                elif self._attackType == 4:
                    self.updateAction(3)
        elif self._run == True:
            self.updateAction(2)
        else:
            self.updateAction(6)
        cd = 30
        self._image = self._animationList[self._action][self._frameIndex]
        if pygame.time.get_ticks() - self._updateTime > cd:
            self._frameIndex += 1
            self._updateTime = pygame.time.get_ticks()
        if self._frameIndex >= len(self._animationList[self._action]):
            if self._alive == False:
                self._frameIndex = len(self._animationList[self._action]) - 1
            else:
                self._frameIndex = 0
                if self._action == 0 or self._action == 1 or self._action == 3 or self._action == 4:
                    self._attacking = False
                    self._attackCD = 20

    def attack1(self, sf, target):
        if self._attackCD == 0:
            self._attacking = True
            attacking = pygame.Rect(self._rect.centerx, self._rect.y, 1.75 * self._rect.width, self._rect.height)
            if attacking.colliderect(target._rect):
                target.health -= 1
            #pygame.draw.rect(sf, "green", attacking)


    def attack2(self, sf, target):
        if self._attackCD == 0:
            self._attacking = True
            attacking = pygame.Rect(self._rect.centerx-100, self._rect.y, 1.75 * self._rect.width, self._rect.height)
            if attacking.colliderect(target._rect):
                target.health -= 1
            #pygame.draw.rect(sf, "green", attacking)


    def attack3(self, sf, target):
        if self._attackCD == 0:
            self._attacking = True
            attacking = pygame.Rect(self._rect.centerx-30, self._rect.y-75, self._rect.width, self._rect.height-75)
            if attacking.colliderect(target._rect):
                target.health -= 2
            #pygame.draw.rect(sf, "green", attacking)


    def attack4(self, sf, target):
        if self._attackCD == 0:
            self._attacking = True
            if self._player == 1:
                attacking = pygame.Rect(self._rect.centerx, self._rect.y+100, 7*self._rect.width, self._rect.height-145)
                if attacking.colliderect(target._rect):
                    target.health -= 0.5
                pygame.draw.rect(sf, "green", attacking)
            elif self._player == 2:
                attacking = pygame.Rect(self._rect.centerx-450, self._rect.y+100, 7 * self._rect.width, self._rect.height-145)
                if attacking.colliderect(target._rect):
                    target.health -= 0.5
                pygame.draw.rect(sf, "green", attacking)

    def updateAction(self, newAction):
        if newAction != self._action:
            self._action = newAction
            self._frameIndex = 0
            self._updateTime = pygame.time.get_ticks()

    def show(self, sf):
        #pygame.draw.rect(sf, "blue", self._rect)
        sf.blit(self._image, (self._rect.x - (self._offset[0] * self._imageScale), self._rect.y - (self._offset[1] * self._imageScale)))


    def move(self, screenWidth, screenHeight, sf, target):
        speed = 10
        dx = 0
        dy = 0
        g = 2
        self._run = False
        self._attackType = 0

        key = pygame.key.get_pressed()

        if self._alive == True:
            if self._player == 1:
                if key[pygame.K_a]:
                    dx = -speed
                    self._run = True
                if key[pygame.K_d]:
                    dx = speed
                    self._run = True
                #Jump
                if key[pygame.K_w] and self._jump == False:
                    self._sy = -30
                    self._jump = True
                #Attack
                if key[pygame.K_e] and key[pygame.K_q] == False and key[pygame.K_f] == False and key[pygame.K_r] == False:
                    self.attack1(sf, target)
                    self._attackType = 1
                if key[pygame.K_q] and key[pygame.K_e] == False and key[pygame.K_f] == False and key[pygame.K_r] == False:
                    self.attack2(sf, target)
                    self._attackType = 2
                if key[pygame.K_f] and key[pygame.K_q] == False and key[pygame.K_e] == False and key[pygame.K_r] == False:
                    self.attack3(sf, target)
                    self._attackType = 3
                if key[pygame.K_r] and key[pygame.K_q] == False and key[pygame.K_f] == False and key[pygame.K_e] == False:
                    self.attack4(sf, target)
                    self._attackType = 4

            if self._player == 2:
                if key[pygame.K_LEFT]:
                    dx = -speed
                    self._run = True
                if key[pygame.K_RIGHT]:
                    dx = speed
                    self._run = True
                if key[pygame.K_UP] and self._jump == False:
                    self._sy = -30
                    self._jump = True

                if key[pygame.K_DOWN] and key[pygame.K_RSHIFT] == False and key[pygame.K_l] == False and key[pygame.K_RALT] == False:
                    self.attack1(sf, target)
                    self._attackType = 1
                if key[pygame.K_RSHIFT] and key[pygame.K_DOWN] == False and key[pygame.K_l] == False and key[pygame.K_RALT] == False:
                    self.attack2(sf, target)
                    self._attackType = 2
                if key[pygame.K_l] and key[pygame.K_DOWN] == False and key[pygame.K_RSHIFT] == False and key[pygame.K_RALT] == False:
                    self.attack3(sf, target)
                    self._attackType = 3
                if key[pygame.K_RALT] and key[pygame.K_DOWN] == False and key[pygame.K_RSHIFT] == False and key[pygame.K_l] == False:
                    self.attack4(sf, target)
                    self._attackType = 4


        self._sy += g
        dy += self._sy

        if self._rect.left + dx < 0:
            dx = 0 - self._rect.left
        if self._rect.right + dx > screenWidth:
            dx = screenWidth - self._rect.right
        if self._rect.bottom + dy > screenHeight - 110:
            self._sy = 0
            self._jump = False
            dy = screenHeight - 110 - self._rect.bottom

        if self._attackCD > 0:
            self._attackCD -= 1

        self._rect.x += dx
        self._rect.y += dy






