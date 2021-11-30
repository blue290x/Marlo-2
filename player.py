import pygame
import math
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
#import numpy

class Person(pygame.sprite.Sprite):
  def __init__(self,image,scale,x,y):
    super().__init__()
    width = image.get_width()
    height = image.get_height()
    self.image = image
    self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.maxHealth = 8
    self.health = self.maxHealth
    self.invincibilityFrames = 30
  
  def getTile(self,cameraOffset,resolution):
    self.tile = cameraOffset[0]//32 + resolution[0]//128, cameraOffset[1]//32  + resolution[1]//128 #formula for calculating currentTile
    return self.tile

  def updateScreenPosition(self,x,y):
    self.rect.x = x
    self.rect.y = y
  
  def fullHealth(self):
    if self.maxHealth == self.health:
      return 1
    else:
      return 0
  def moveright(self, pixels):
    self.rect.x += pixels

  def moveleft(self, pixels):
    self.rect.x -= pixels

  def moveup(self,pixels):
    self.rect.y -= pixels
  
  def movedown(self,pixels):
    self.rect.y += pixels
  
  def takeDamage(self,damage):
    if self.invincibilityFrames >= 30:
      self.health -= damage
      self.invincibilityFrames = 0

  def heal(self,heal):
    self.health += heal
    if self.health > self.maxHealth:
      self.health = self.maxHealth
    
class life(pygame.sprite.Sprite):
  def __init__(self,image,scale,tilex,tiley):
    super().__init__()
    width = image.get_width()
    height = image.get_height()
    self.originalImage = image
    self.image = image
    self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    self.rect = self.image.get_rect()
    self.rect.x = tilex*32
    self.rect.y = tiley*32
    self.startx = tilex
    self.starty = tiley
    self.heal = 4
  
  def updatePosition(self,cameraOffset):

    self.rect.x = (self.startx)*32 - cameraOffset[0]
    self.rect.y = (self.starty)*32 - cameraOffset[1]
  
  def getHeal(self):
    self.kill()
    return self.heal
  

class angrydude(pygame.sprite.Sprite):
  def __init__(self,image,scale,difficulty,tilex,tiley,map,number):
    super().__init__()
    width = image.get_width()
    height = image.get_height()
    self.map = map
    self.originalImage = image
    self.image = image
    self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    self.rect = self.image.get_rect()
    self.rect.x = tilex*32
    self.rect.y = tiley*32
    self.tilex = tilex
    self.tiley = tilex
    self.startx = tilex
    self.starty = tiley
    self.ticks = number
    if difficulty == 2:
      self.health = 12
      self.damage = 4
    else:
      self.health = 6
      self.damage = 2

    
    #pathfinding setup
    #self.currentTileX = tilex
    #self.currentTileY = tiley
  
  def getTile(self,player,cameraOffset,resolution):
    playerTile = player.getTile(cameraOffset,resolution)
    tileDistance = self.rect.x//32 - resolution[0]//128, self.rect.y//32 - resolution[1]//128
    self.tile = (playerTile[0] + tileDistance[0],playerTile[1]+ tileDistance[1])
    return self.tile
  
  def updateTicks(self):
    self.ticks += 1

  def pathfind(self,playerTile,matrix):
    searching = False
    if self.ticks == 60:
      self.ticks = 0
      searching = True
    while searching:
      y,x = int(playerTile[0]),int(playerTile[1])
      self.grid = Grid(matrix=matrix)
      self.start = self.grid.node(self.tilex,self.tiley)
      self.end = self.grid.node(y,x)
      finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
      self.pathIndex = 0
      self.path, runs = finder.find_path(self.start,self.end,self.grid)
      print(self.grid.grid_str(path=self.path, start=self.start, end=self.end))
      searching = False
  
  def updatePath(self):
    now = pygame.time.get_ticks()
    if now - self.moveTimer > 1000:
      new = self.path[self.pathIndex]


  def updatePosition(self,cameraOffset,direction):
    x,y=direction[0],direction[1]                     # x,y representing the x and y distances that the bad dudes move by
    self.startx -= x/32                               
    self.starty -= y/32
    self.rect.x = (self.startx)*32 - cameraOffset[0]  
    self.rect.y = (self.starty)*32 - cameraOffset[1]
  
  def chasePlayer(self,player):
    distance = (player.rect.x - self.rect.x, player.rect.y - self.rect.y) #calculate the length of each component of the vector
    length = math.hypot(*distance)                                        #calculate the length of the vector
    if length == 0.0:
      direction = (0, -1)                                                 #avoid divide by 0 exception
    else:
      direction = (distance[0]/length,distance[1]/length)                 #calculate the direction

    newX = -(2*direction[0])                                              #the multiplier represents the speed
    newY = -(2*direction[1])
    return (newX,newY)
    #would be used for rotation but it's not working well so i disabled it.
    #angle = math.degrees(math.atan2(direction[1],direction[0]))
    #self.image = pygame.transform.rotate(self.originalImage, -angle)
    #print(angle)
  def takeDamage(self,damage):
    self.health -= damage
    if self.health <= 0:
      self.kill()
      return True
    else:
      return False
    
#weapons
  
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pos = (x/2, y/2)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((10, 4)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 25
        self.rect = self.bullet.get_rect(center = self.pos)
        self.rect.x = x
        self.rect.y = y
        self.bulletDamage = 3
    
    def bulletDamage(self):
      return self.bulletDamage

    def update(self):  
        self.pos = (self.pos[0]+(self.dir[0]*self.speed), 
                    self.pos[1]+(self.dir[1]*self.speed))
        self.rect = self.bullet.get_rect(center = self.pos)

    def draw(self, surf,camera):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, (bullet_rect))

class gun(Bullet):
  def __init__(self,x, y,image,scale):
        super().__init__(x,y)
        self.originalImage = image
        width = image.get_width()
        height = image.get_height()
        self.originalImage = pygame.transform.scale(image,(int(width*scale),int(height*scale)))

        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.image = pygame.transform.rotate(self.originalImage, angle)
        self.rect = self.bullet.get_rect(center = self.pos)
        self.rect.x = x
        self.rect.y = y
        self.bulletDamage = 3
  
  def update(self,x,y,image,scale):
    #width,height = image.get_width,image.get_height
    #self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))

    self.imageCopy = image
    w,h = self.imageCopy.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    self.pos = (x,y)
    self.rect.x = x - 10
    self.rect.y = y - 10
    mx, my = pygame.mouse.get_pos()
    self.dir = (mx - x*2, my - y*2)
    length = math.hypot(*self.dir)
    if length == 0.0:
      self.dir = (0, -1)
    else:
      self.dir = (self.dir[0]/length, self.dir[1]/length)
    angle = math.degrees(math.atan2(self.dir[1], -self.dir[0]))
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    boxRotate = [p.rotate(angle) for p in box]

    minBox = (min(boxRotate, key=lambda p: p[0])[0], min(boxRotate, key=lambda p: p[1])[1])
    maxBox = (max(boxRotate, key=lambda p: p[0])[0], max(boxRotate, key=lambda p: p[1])[1])
    self.image = pygame.transform.rotate(self.imageCopy, angle)