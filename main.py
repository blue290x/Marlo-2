from doctest import master
from faulthandler import disable
import time
import button
import sys
import math
import random
import player
import copy
import os
import json
import math
import hashlib
try:
    import pygame
    #from pygame.locals import*
except ModuleNotFoundError:
    print("pygame library not found. in order to play this game pygame is required.\nfor more information on how to get pygame, visit https://pypi.org/project/pygame/ \n ")
    print("exiting in 10 seconds...")
    time.sleep(10)
    sys.exit()

#from playsound import playsound
#from sys import platform
#import numpy

#####LEVELGRID AND PROCEDURAL GENERATION#####
def buildGrid():
    gameGrid =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    return gameGrid
global modifiedSave
modifiedSave = False
def walker(grid):
    x = 29
    y = 29
    placed = 0
    whatDir = random.randint(1,4)
    while placed <= 400:
        changeDir = random.randint(1,2)
        if changeDir == 2:
            whatDir = random.randint(1,4)
        
        if whatDir ==1:
            if x < 58:
                x += 1
                placed+= 1
            
        if whatDir ==2:
            if x > 1:
                x -= 1
                placed+= 1
        if whatDir ==3:
            if y < 58:
                y += 1
                placed += 1
            
        if whatDir ==4:
            if y > 1:
                y -= 1
                placed += 1
        grid[y][x] = 1

    return grid

def placeWalls(grid):
    for y in range(60):
        for x in range(60):
            if grid[y][x] == 1:
                
                if y != 60:
                    if grid[y+1][x] == 0:
                        grid[y+1][x] = 2
                        
                if y != 0:
                    if grid[y-1][x] ==0:
                       grid[y-1][x] = 2

                if x != 60:
                    if grid[y][x+1]==0:
                       grid[y][x+1] = 2

                if x != 0:
                    if grid[y][x-1] ==0:
                        grid[y][x-1] = 2
    return(grid)

def generateHash():
    with open ("config.json","rb") as f:                #open in binary format for reading
        bytes = f.read()                                #store all data in file as variable
        hashed = hashlib.sha256(bytes).hexdigest();     #hash using sha256
        return hashed                                   #print value, to ensure it's working correctly.

def saveHash(data):
    #write to the file called hash, the data passed to it
    #if the save has been modified then abort
    if modifiedSave is True:
        return -1
    f =  open ("hash","w")
    f.write(data)
    f.close
        
def readHash():
    #read data from the file called hash
    f = open("hash","r")
    data = f.read()
    f.close()
    return data

def generateNewSave():
    data = {'warning': [{'warning': 'editing this file can cause the game to stop working correctly, to recover from this, delete the file and a new one will be generated. you have been warned'}
    ],
    'sounds': [
    {'type': 'master', 'value': 1},
    {'type': 'sound', 'value': 1}, 
    {'type': 'music', 'value': 0.5}
    ], 
    'stats': [
    {'type': 'playTime', 'value': 0}, 
    {'type': 'wins', 'value': 0}, 
    {'type': 'bogosplay', 'value': 0}, 
    {'type': 'marloplay', 'value': 0}
    ]
    }
    with open("config.json","w") as file:
        json.dump(data,file,indent=2)
    saveHash(generateHash())

def convertTime(seconds):
    #if less than 2 minutes, show in seconds
    if seconds // 60 >= 2:
        minutes = seconds/60
    else:
        return str(int(seconds))+" seconds"
    #if less than 2 hours, show in minutes
    if minutes // 60 >= 2:
        hours = minutes/60
    else:
        return str(int(minutes))+" minutes"
    #default to showing in hours
    return str(int(hours))+" hours"

def updatePlayTime(playTime):
    data = json.load(open("config.json"))           #open the file, grab contents
    open("config.json").close()                     #close it
    for i in data["stats"]:                         #look for playtime
        if i["type"] == "playTime":
            playTime += i["value"]
    data["stats"][0]["value"] = playTime            #add the total playtime with the time they just played now
    with open("config.json","w") as file:           #rewrite the entire file with the new contents
        json.dump(data,file,indent=2)
    saveHash(generateHash())



def updateWins():
    #pull all data
    data = json.load(open("config.json"))
    open("config.json").close()
    #increment correct item by 1
    data["stats"][1]["value"] += 1
    #save file
    with open("config.json","w") as file:
        json.dump(data,file,indent=2)
    saveHash(generateHash())



def updateFavCharacter(characterName):
    data = json.load(open("config.json"))
    open("config.json").close()
    character = characterName + "play"
    for i in data["stats"]:
        if i["type"] == character:
            count = i["value"] + 1
    if characterName == "bogos":
        data["stats"][2]["value"] = count
    elif characterName == "marlo":
        data["stats"][3]["value"] = count
    with open("config.json","w") as file:
        json.dump(data,file,indent=2)
    saveHash(generateHash())



def loadSoundConfig():
    data =json.load(open("config.json"))
    open("config.json").close()
    for i in data["sounds"]:
        if i["type"] == "master":
            masterVol = i["value"]
        elif i["type"] == "sound":
            soundVol = i["value"]
        elif i["type"] == "music":
            musicVol = i["value"]
    return masterVol,soundVol,musicVol

def saveSoundConfig(master,sound,music):
    data = json.load(open("config.json"))
    data["sounds"][0]["value"] = master
    data["sounds"][1]["value"] = sound
    data["sounds"][2]["value"] = music
    with open("config.json","w") as file:
        json.dump(data,file,indent=2)
    saveHash(generateHash())


def loadStatsConfig():
    #pull all data from the file, then close it
    data =json.load(open("config.json"))
    open("config.json").close()    
    #go through all the stats related things, assign variables as appropriate
    for i in data["stats"]:
        if i["type"] == "playTime":
            playTime = i["value"]
        elif i["type"] == "wins":
            wins = i["value"]
        elif i["type"] == "bogosplay":
            bogoscount = i["value"]
        elif i["type"] == "marloplay":
            marlocount = i["value"]
    #choose who's the most played character based on this
    if bogoscount > marlocount:
        mostPlayed = "bogos"
    elif marlocount > bogoscount:
        mostPlayed = "marlo"
    else:
        mostPlayed = "none"
    #return the values
    return playTime,wins,mostPlayed

def updateStatsText(highScore,playTime,mostPlayed):
    winsText = menuFont.render("wins: {}".format(highScore),False,(255,255,255))
    playTimeText = menuFont.render("play time: {}".format(convertTime(playTime)),False,(255,255,255))
    mostPlayedText = menuFont.render("most played character: {}".format(mostPlayed),False,(255,255,255))
    return winsText,playTimeText,mostPlayedText

#initialise the pygame module
pygame.init()
pygame.mixer.pre_init()
pygame.font.init()
#loading the icon file
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
#setting up text font to be used and size:
menuFont = pygame.font.SysFont("comic sans MS",30)
warningFont = pygame.font.SysFont("comic sans MS",18)

mainMenuText = menuFont.render("main menu",False,(255,255,255))
optionsMenuText = menuFont.render("options",False,(255,255,255))
characterSelectText = menuFont.render("choose your character",False,(255,255,255))

statsText = menuFont.render("stats",False,(255,255,255))
if not(os.path.isfile("config.json")):
    generateNewSave()

masterVol,soundVol,musicVol = loadSoundConfig()
playTime,wins,mostPlayed = loadStatsConfig()
winsText,playTimeText,mostPlayedText = updateStatsText(wins,playTime,mostPlayed)

#text for stats stuff:

#these are placeholders to show that it works, in a future version this values will be read from a config file.

#wins = 500
#playTime = "60 hours"
#mostPlayed = "example"
#highScoreText = menuFont.render("high score: {}".format(highScore),False,(255,255,255))
#playTimeText = menuFont.render("play time: {}".format(playTime),False,(255,255,255))
#mostPlayedText = menuFont.render("most played character: {}".format(mostPlayed),False,(255,255,255))
highScoreTextPos = winsText.get_rect()
playTimeTextPos = playTimeText.get_rect()
mostPlayedTextPos = mostPlayedText.get_rect()

mainMenuTextPos = mainMenuText.get_rect()
optionsMenuTextPos = optionsMenuText.get_rect()
characterSelectTextPos = characterSelectText.get_rect()
statsTextPos = statsText.get_rect()

#define the width and height of the window
displayWidth = 800
displayHeight = 600

#variable for the framerate object
clock = pygame.time.Clock()

#draw the screen + change the caption
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight),pygame.RESIZABLE)
pygame.display.set_caption("Marlo 2")
backgroundImage = pygame.image.load("bg.jpg").convert()

#creating play button object
playButtonImage = pygame.image.load("buttons/PlayButton.png").convert()
playButton = button.Button(20,200,playButtonImage,0.25)
play2 = button.Button(20,200,playButtonImage,0.25)

#creating exit button object
exitButtonImage = pygame.image.load("buttons/ExitButton.png").convert()
exitButton = button.Button(20,500,exitButtonImage,0.25)

#creating stats button object
statsButtonImg = pygame.image.load("buttons/Stats.png").convert()
statsButton = button.Button(20,300,statsButtonImg,0.25)

#creating options button
optionsButtonImg = pygame.image.load("buttons/Options.png").convert()
optionsButton = button.Button(20,400,optionsButtonImg,0.25)

#go back (for the select character menu
goBackButtonImg = pygame.image.load("buttons/goBack.png").convert()
goBackButton = button.Button(20,300,goBackButtonImg,0.25)

#same but for options and stats (they will do the same thing and be in same place so the same object can be used)
goBackButtonImg = pygame.image.load("buttons/goBack.png").convert()
goBackButton2 = button.Button(600,500,goBackButtonImg,0.25)

#save warning related
ignoreWarnButton = pygame.image.load("buttons/ignoreWarning.png").convert()
ignoreButton = button.Button(500,400,ignoreWarnButton,0.25)

makeNewSaveButton = pygame.image.load("buttons/makeNewSave.png").convert()
makeNewSave = button.Button(500,300,makeNewSaveButton,0.25)

disableWarningimg = pygame.image.load("buttons/disableWarning.png").convert()
disableWarning = button.Button(500,500,disableWarningimg,0.25)

#play button menu objects:
#characters and difficulty buttons
c2Img = pygame.image.load("buttons/Bogos.png").convert()
c1Img = pygame.image.load("buttons/Marlo.png").convert()
character2Button = button.Button(200,500,c2Img,0.25)
character1Button = button.Button(10,500,c1Img,0.25)


easy = pygame.image.load("buttons/Easy.png").convert()
easyButton = button.Button(600,200,easy,0.25)
hard = pygame.image.load("buttons/Hard.png").convert()
hardButton = button.Button(600,300,hard,0.25)

#textures for the tiles
wall = pygame.image.load("textures/TestWall.png").convert()
floor = pygame.image.load("textures/TestFloor.png").convert()

#character image
character1 = pygame.image.load("sprites/tooCool.png").convert()
character2 = pygame.image.load("sprites/Character2.png").convert()
character1.set_colorkey((255,255,255))
character2.set_colorkey((255,255,255))

#loading item pickup images
healthImage = pygame.image.load("sprites/life.png").convert()
healthImage.set_colorkey((255,255,255))

#ghosts sprite
ghostImage = pygame.image.load("sprites/ghost.png").convert()
ghostImage.set_colorkey((255,255,255))


#volume slider related stuff
barX = 20                   #x offset of bar
barY = 300                  #y offset of middle bar
xscrollMaster = barX        #set the default values to 0
xscrollSoundfx = barX
xscrollMusic = barX
barWidth = 400              #set the length to 400
barHeight = 5               #height to 5

def slider(x,y,width,height,action=None):
    global xscrollMaster,xscrollSoundfx,xscrollMusic                    #make these variables available to the rest of the program
    cur = pygame.mouse.get_pos()                                        #get the position of the cursor
    click = pygame.mouse.get_pressed()                                  #check if the mouse button is pressed
    if x + width > cur[0] > x and y + height + 12 > cur[1] > y-12:      #check if the cursr is in bounds
        pygame.draw.rect(gameDisplay,(255,255,255), (x,y,width,height)) #draw to the display the bar if it's possible
        if click[0] == 1 and action != None:                            #if the bar is clicked and it has an action
            if action == "master":                                      #if the action is for the master volume
                xscrollMaster = cur[0]                                  #change the x coordinate of the rectangle appropriately
            elif action == "soundfx":                                   #same for others
                xscrollSoundfx = cur[0]
            elif action == "music":
                xscrollMusic = cur[0]
    else:
        pygame.draw.rect(gameDisplay,(255,255,255),(x,y,width,height))

##### MENU functions #####
whatMenu = int(0)

#function for the main menu:
def mainMenu():
    gameDisplay.blit(backgroundImage,(0,0))
    gameDisplay.blit(mainMenuText,(340,0))
    whatMenu = 0
    if optionsButton.draw(gameDisplay) == True:
        whatMenu = int(3)
        
    if statsButton.draw(gameDisplay)==True:
        whatMenu = int(2)
        
    if playButton.draw(gameDisplay) == True:
        whatMenu = int(1)

    if exitButton.draw(gameDisplay) == True:
        pygame.quit()
        sys.exit()
    return whatMenu

#options menu
def optionsMenu(firstTime):
    global masterVol,soundVol,musicVol
    if firstTime:
        masterVol,soundVol,musicVol = loadSoundConfig()
        global xscrollMaster,xscrollSoundfx,xscrollMusic
        xscrollMaster = (masterVol)*barWidth + barX
        xscrollSoundfx = (soundVol)*barWidth + barX
        xscrollMusic = (musicVol)*barWidth + barX
        
    whatMenu = 5

    #rendering text for each volume
    masterText = menuFont.render("Master Volume:",False,(255,255,255))
    soundText = menuFont.render("Sound Effect Volume:",False,(255,255,255))
    musicText = menuFont.render("Music Volume:",False,(255,255,255))

    #drawing background, all drawings must be done after this or it won't show up.
    gameDisplay.blit(backgroundImage,(0,0))
    gameDisplay.blit(masterText,(barX,90))
    gameDisplay.blit(optionsMenuText,(340,0))
    gameDisplay.blit(soundText,(barX,240))
    gameDisplay.blit(musicText,(barX,390))

    #master volume
    slider(barX,barY-150, barWidth,barHeight,action="master")
    pygame.draw.rect(gameDisplay,(255,255,255),[xscrollMaster- barHeight,barY-150 -12,10,24])
    masterVol = (1/barWidth)*(xscrollMaster-barX)

    #soundfx volume
    slider(barX,barY, barWidth,barHeight,action="soundfx")
    pygame.draw.rect(gameDisplay,(255,255,255),[xscrollSoundfx -barHeight,barY - 12,10,24])
    soundVol = (1/barWidth)*(xscrollSoundfx-barX)

    #music volume
    slider(barX,barY+150, barWidth,barHeight,action="music")
    pygame.draw.rect(gameDisplay,(255,255,255),[xscrollMusic -barHeight,barY+150 - 12,10,24])
    musicVol = (1/barWidth)*(xscrollMusic-barX)

    if goBackButton2.draw(gameDisplay) == True:
        whatMenu = 0
        saveSoundConfig(masterVol,soundVol,musicVol)
    return whatMenu

#stats menu
def statsMenu():
    playTime,wins,mostPlayed = loadStatsConfig()
    winsText,playTimeText,mostPlayedText = updateStatsText(wins,playTime,mostPlayed)
    whatMenu = 2
    gameDisplay.blit(backgroundImage,(0,0))
    gameDisplay.blit(statsText,(340,0))
    gameDisplay.blit(winsText,(20,200))
    gameDisplay.blit(playTimeText,(20,300))
    gameDisplay.blit(mostPlayedText,(20,400))
    if goBackButton2.draw(gameDisplay) == True:
        whatMenu = 0
        
    return whatMenu

#play menu
character = 0
difficulty = 0

#whatMenu is already known and doesn't change until the player hits a button so this doesn't need to be passed
#character and difficulty must be passed

def saveWarning():
    #make sure it stays on this menu
    whatMenu = -1                   
    #render and display all the text                                                                                                                        
    warnText1 = menuFont.render("Warning: save file modified!!",False,(255,255,255))
    warnText2 = warningFont.render("modifying the save file may cause the game to cease functioning and/or cause loss of save data.",False,(255,255,255))
    warnText3 = warningFont.render("it is recommended that you generate a new save file to avoid these issues.",False,(255,255,255))
    warnText4 = warningFont.render("if you are aware of the risks, you can choose to ignore this warning.",False,(255,255,255))
    gameDisplay.blit(warnText1,(0,0))
    gameDisplay.blit(warnText2,(0,100))
    gameDisplay.blit(warnText3,(0,150))
    gameDisplay.blit(warnText4,(0,200))

    #if the button to ignore the error is pressed then ignore it but flag the save as modified
    if ignoreButton.draw(gameDisplay) == True:
        global modifiedSave
        modifiedSave = True
        whatMenu = 0
    #if the button to generate a new save is pressed then generate a new save and load the new config
    if makeNewSave.draw(gameDisplay) == True:
        generateNewSave()
        loadSoundConfig()
        whatMenu = 0
    #if disable the warning is pressed then just generate a new hash for the file
    if disableWarning.draw(gameDisplay) == True:
        saveHash(generateHash())
        whatMenu = 0

    return whatMenu

def playMenu(character,difficulty):
    whatMenu = int(1)
    
    #draw background and text    
    gameDisplay.blit(backgroundImage,(0,0))
    gameDisplay.blit(characterSelectText,(280,0))

    #go back button
    if goBackButton.draw(gameDisplay) ==True:
        whatMenu= int(0)
        
    #button for playing    
    if play2.draw(gameDisplay) == True:
        if character != 0 and difficulty != 0:
            whatMenu = 4
            
    #characters and difficulty       
    if character1Button.draw(gameDisplay) == True:
        #print("character 1 selected")
        character = player.Marlo(character1,1,200,150,8,4)

    if character2Button.draw(gameDisplay) == True:
        #print("character 2 selected")
        character = player.Bogos(character2,1,200,150,1,12)

    if hardButton.draw(gameDisplay) == True:
        #print("hard selected")
        difficulty = 2
    if easyButton.draw(gameDisplay) == True:
        #print("easy selected")
        difficulty = 1

    #returns a tuple for character state, difficulty state and where in the menu the player is.
    return (whatMenu,character,difficulty)

#main menu loop
def Menu(whatMenu=0):

    whatMenu = whatMenu
    menuLoop = 1
    while menuLoop == 1:

    #listens for close clicked 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if whatMenu == -1:              #if the stored hash does not match the hash of the config file
            whatMenu = saveWarning()
            character = 0
            difficulty = 0

        if whatMenu == 0:
            whatMenu = mainMenu()
            character = 0
            difficulty = 0
        
        if whatMenu == 1:
            playMenuTuple = playMenu(character,difficulty)
            whatMenu = playMenuTuple[0]
            character = playMenuTuple[1]
            difficulty = playMenuTuple[2]
        
        if whatMenu == 2:
            whatMenu = statsMenu()

        if whatMenu == 3:
            whatMenu = optionsMenu(True)
        if whatMenu == 5:
            whatMenu = optionsMenu(False)
        if whatMenu == 4:
            break
#set clockspeed to 60fps and update screen
        pygame.display.update()
        clock.tick(60)
    return (1,character,difficulty)

#function for checking if the player is hitting wall:
def collideTest(rect,tiles):
    collisions = []
    for tile in tiles:
        if tile.colliderect(rect):
            collisions.append(tile)
    return collisions

#handles the bullet collisions with the wall tiles, for each bullet which has been fired.
def bulletCollide(bullets,tiles,cameraOffset):
        collisions = []
    #having a weird bug which happens when it intercepts 2 tiles at once 
    # it deletes the entry twice which isn't good
    # for now putting it in a try except stops the program from crashing but this needs to be fixed later
    #try:
        for bullet in bullets[:]:
                collisionCount = 0
                bullet.update(cameraOffset)
                for tile in tiles:
                    if bullet.rect.colliderect(tile):
                        if collisionCount == 0:
                            collisions.append(bullet)
                            collisionCount += 1
        for bullet in collisions:
            bullets.remove(bullet)
    #except:
       # return 0

def bulletEnemy(bullets,enemyList):
    collisions = []
    for bullet in bullets[:]:                           #loop through all lists
        collisionCount = 0
        for enemy in enemyList:
            if bullet.rect.colliderect(enemy):          #check every possible collision
                if collisionCount == 0:
                    collisions.append(bullet)           #add the bullet to the list if it's collided
                    collisionCount += 1

                if enemy.takeDamage(bullet.getDamage()):#run the method on the enemy to take damage
                    enemyList.remove(enemy)             #if it's true the enemy died, so it is removed from the list

    for bullet in collisions:                           #remove all collided bullets
        bullet.takeDamage()
        if bullet.getHealth() == 0:
            bullets.remove(bullet)

#handles the movement of the player and camera when 
def move(rect, movement, tiles):
    hit_list = collideTest(rect,tiles)
    for tile in hit_list:
        if (rect.right - tile.left) < 4:
            movement[0] += (tile.left - rect.right)
             #these are the same for collisions on that side, perhaps use this to decide where to move the player.
        elif (tile.right - rect.left)<4:
            movement[0] += (tile.right - rect.left)

        elif (rect.bottom -tile.top) <4:
            movement[1] += (tile.top - rect.bottom)

        elif (tile.bottom - rect.top) < 4:
            movement[1] -= (rect.top - tile.bottom)
            
    return movement[0],movement[1]

def playSound(path,masterV,soundV):
    sound = pygame.mixer.Sound(path)
    sound.set_volume((masterV*soundV)**1.5)
    sound.play()

def enemyWallCollide(rect, movement, tiles):
    hit_list = collideTest(rect,tiles)
    for tile in hit_list:
        if (rect.right - tile.left) < 4:
            movement[0] += (tile.left - rect.right)
             #these are the same for collisions on that side, perhaps use this to decide where to move the player.
        elif (tile.right - rect.left)<4:
            movement[0] += (tile.right - rect.left)

        elif (rect.bottom -tile.top) <4:
            movement[1] += (tile.top - rect.bottom)

        elif (tile.bottom - rect.top) < 4:
            movement[1] -= (rect.top - tile.bottom)
            
    return movement[0],movement[1]

def playerHit(character,enemyList):
    for enemy in enemyList:
        if character.rect.colliderect(enemy):
            if character.takeDamage(enemy.damage) ==1:
                playSound("sounds/damage.mp3",masterVol,soundVol)

def abilityPickup(character,lifeList):                    
    if character.fullSpecial():                             #check if max special
        return 0
    else:
        for life in lifeList:                               #loop through the list of ability pickups
            if character.rect.colliderect(life):            #if colliding
                character.increaseSpecial(life.getHeal())   #increase character's special + kill the pickup
                #character.heal(life.getHeal())
                lifeList.remove(life)                       #remove from the list

def upgradePickup(character,upgradelist):
    for upgrade in upgradelist:                         #check all items in the list of upgrades against the player
        if character.rect.colliderect(upgrade):         #if they're touching
            upgradeType = upgrade.getType()             #get the type of upgrade
            
            #get the appropraite upgrade depending on the upgrade type
            #remove the upgrade from the list afterwards
            if upgradeType == 1:                        
                character.increaseMaxHealth()
            elif upgradeType == 2:
                character.increaseFireRate()
            elif upgradeType == 3:
                character.increaseDamage()
            elif upgradeType == 4:
                character.increaseMaxSpecial()
            upgradelist.remove(upgrade)

def doorLocation(grid):
    notPicked = True
    while notPicked is True:
        #generate random index for x and y
        x = random.randint(0,(len(grid)-2))
        y = random.randint(0,(len(grid)-2))

        #2 corresponds to a Wall tile
        #if a wall tile is picked out then replace it with a door tile
        if grid[y][x] ==2:
            grid[y][x]= 3
            #exit the loop 
            notPicked = False
            
def findFloors(gameMap):
    floorList = [] #a list that stores a tuple for each location of floor tile, index 0 is x and index y is 1
    for x in range(0,len(gameMap)-1): #loop through each tile
        for y in range(0,len(gameMap)-1):
            if gameMap[y][x] == 1: #if the tile is a floordd
                floorCoordinates = (y,x)
                floorList.append(floorCoordinates)
    return floorList

def shootSound():
    shootSound = pygame.mixer.Sound("sounds/gun"+str(random.randint(0,4))+".mp3")
    shootSound.set_volume(math.log(1+masterVol * soundVol,2))
    shootSound.play()

def placeAngryDudes(gameMap,image,scale,difficulty,howMany):
    floors = findFloors(gameMap)
    #if more enemies than floor tiles then equate them
    if howMany > len(floors)-1:
        howMany = (len(floors) -1)
    enemyList = []
    for i in range(howMany):#len(floors)-1):
        floor = random.randint(0,len(floors)-1) #pick a random index24
        coordinates = floors[floor] #coordinates of the floor tile
        floors.pop(floor)
        y,x = coordinates[0],coordinates[1]
        enemy =  player.angrydude(image,scale,difficulty,x,y,gameMap,i,howMany)
        enemyList.append(enemy)
    return (enemyList)

def placeGhosts(gameMap,image,scale,difficulty,howMany,enemyList):
    floors = findFloors(gameMap)
    #if more enemies than floor tiles then equate them
    if howMany > len(floors)-1:
        howMany = (len(floors) -1)
    for i in range(howMany):#len(floors)-1):
        floor = random.randint(0,len(floors)-1) #pick a random index24
        coordinates = floors[floor] #coordinates of the floor tile
        floors.pop(floor)
        y,x = coordinates[0],coordinates[1]
        enemy =  player.Ghost(image,scale,difficulty,x,y,gameMap,i,howMany)
        enemyList.append(enemy)
    return (enemyList)

def placeLife(gameMap,image,scale,howMany):
    floors = findFloors(gameMap)
    if howMany > len(floors) - 1:
        howMany = len(floors) - 1
    lifeList = []
    for i in range(howMany):
        floor = random.randint(0,len(floors)-1)
        coordinates = floors[floor]
        floors.pop(floor)
        y,x = coordinates[0],coordinates[1]
        life = player.life(image,scale,x,y)
        lifeList.append(life)
    return lifeList

def placeUpgradeBoxes(gameMap,image,scale,howMany):
    floors = findFloors(gameMap)                        #find valid floors
    if howMany > len(floors) - 1:                       #make sure a valid number are being placed
        howMany = len(floors) - 1                       
    upgradeBoxList = []                                 #make a list of them
    for i in range(howMany):
        floor = random.randint(0,len(floors)-1)
        coordinates = floors[floor]
        floors.pop(floor)                               #ensure only 1 is placed per tile
        y,x = coordinates[0],coordinates[1]             
        upgrade = player.upgrade(image,scale,x,y)       #build the upgrades
        upgradeBoxList.append(upgrade)                  #add them to a list

    return (upgradeBoxList)                             #return the list

def createMatrix(gameMap):
    matrix = gameMap
    for y in range(len(matrix)-1):      #loop through the grid
        for x in range(len(matrix)-1):
            if matrix[y][x] != 1:       #if it's not a floor tile
                matrix[y][x] = 0        #make it an obsticle. 
    return matrix

def placePlayer(floors,resolution):
    cameraOffset = [0,0]
    floor = floors[random.randint(0,len(floors)-1)]
    cameraOffset[1] = 32*floor[0] +8 - resolution[1]/4
    cameraOffset[0] = 32*floor[1] +8 - resolution[0]/4
    return cameraOffset


def game(gameMap,character,difficulty,room):
    enemyConstant = 5
    currentRes = gameDisplay.get_size()
    previousRes = currentRes

    floors = findFloors(gameMap)

    #variable which gets returned
    room += 1
    #setting up text for the HUD
    pygame.font.init()
    gameFont = pygame.font.SysFont("arial",15)

    #sprite group for the character, this is needed for the character to be drawn on screen.
    characterSpriteGroup = pygame.sprite.Group()
    characterSpriteGroup.add(character)

    #loading door and game textures 
    door = pygame.image.load("textures/door.png").convert()
    angrydudeimg = pygame.image.load("sprites/angry.png").convert()
    angrydudeimg.set_colorkey((255,255,255))

    #setting up the character's gun sprite:

    pistolImg = pygame.image.load("sprites/pistol.png").convert()
    pistolImg.set_colorkey((255,255,255))


    #setting up some variables required for the game
    tileWidth = 32
    cameraOffset = placePlayer(floors,currentRes)
    #cameraOffset = [24*tileWidth,26*tileWidth]
    gameLoop = 1

    #adding a door to the game
    doorLocation(gameMap)

    #create a list for the hitbox for walls, as well as bullets. declare the shootdelay to be 20 which allows the gun to be instantly fired. 
    tilesRects = []
    bullets = []
    shootDelay = 20

    #setting the player's invincibility frames to 0, when it's 30 or above they can take damage
    gunSpriteGroup = pygame.sprite.Group()
    gun = player.gun(400,300,pistolImg,1,0,cameraOffset)
    gunSpriteGroup.add(gun)

    #AngryDudes being placed and added to the srite group
    enemySpriteGroup = pygame.sprite.Group()
    enemyList = placeAngryDudes(gameMap,angrydudeimg,1,difficulty,enemyConstant*(room-1))
    enemyList = placeGhosts(gameMap,ghostImage,1,difficulty,random.randint(0,room),enemyList)
    for i in range(len(enemyList)):
        enemySpriteGroup.add(enemyList[i])

    #placing life tings
    lifeSpriteGroup = pygame.sprite.Group()
    if difficulty ==2:
        howMany = 1
    else:
        howMany = 2
    lifeList = placeLife(gameMap,healthImage,1,howMany)

    for life in lifeList:
        lifeSpriteGroup.add(life)

    #place the upgrade boxes
    upgradeImage = pygame.image.load("sprites/upgrade.png").convert()
    upgradeImage.set_colorkey((255,255,255))
    upgradeBoxList = placeUpgradeBoxes(gameMap,upgradeImage,1,1)
    upgradeSpriteGroup = pygame.sprite.Group()
    for upgrade in upgradeBoxList:
        upgradeSpriteGroup.add(upgrade)

    #generate the matrix for the map, used for pathfinding
    gameMap2 = copy.deepcopy(gameMap)
    matrix = createMatrix(gameMap2)

    distanceFromDoor = (0,0)
    if os.path.isfile("SUPERMARLO"):
        character.SUPERMARLO()

    character.newLevel()

    #GAME LOOP
    while gameLoop == 1:
        #display scaling things
        screenSizeX,screenSizeY = gameDisplay.get_size()

        currentRes = gameDisplay.get_size()                 #get the current size of the window
        changeInX = currentRes[0] - previousRes[0]          #calculate the change in x and y from the previous res to this res
        changeInY = currentRes[1] - previousRes[1]
        cameraOffset[0] -= changeInX/4                      #change the camera offset accordingly to prevent the player moving
        cameraOffset[1] -= changeInY/4
        previousRes = currentRes
        character.updateScreenPosition(screenSizeX/4,screenSizeY/4)

        display = pygame.Surface((screenSizeX/2,screenSizeY/2))


        healthText = gameFont.render("HP: {} / {}".format(character.health,character.maxHealth),False,(255,255,255))
        roomNumberText = gameFont.render("room: {}/10".format(room-1),False,(255,255,255))
        enemyText = gameFont.render("enemies: {}".format(len(enemyList)),False,(255,255,255))
        distanceText = gameFont.render("{},{}".format(distanceFromDoor[0],distanceFromDoor[1]),False,(255,255,255))
        specialText = gameFont.render("special: {}/{}".format(character.getSpecial(),character.getMaxSpecial()),False,(255,255,255))
        movement = [0,0]
        gameDisplay.fill((0,0,0))
        display.fill((32,36,78))

        #print(character.getTile(cameraOffset,(screenSizeX,screenSizeY)))
        #for badguy in enemyList:
            #print(badguy.getTile(character,cameraOffset,(screenSizeX,screenSizeY)))


#####  _                   _         
##### (_)                 | |      
#####  _ _ __  _ __  _   _| |_ ___
##### | | '_ \| '_ \| | | | __/ __|  
##### | | | | | |_) | |_| | |_\__ \
##### |_|_| |_| .__/ \__,_|\__|___/
#####         | |                    
#####         |_|              
        character.updateShootFrames()

        mousePressed = pygame.mouse.get_pressed()
        if mousePressed[0]:                                                                         #when the mouse button is pressed
            if character.getShootCooldown()>=character.getShootFrames():                            #if the bullet is ready to be fired
                playSound("sounds/gun"+str(random.randint(0,4))+".mp3",masterVol,soundVol)
                bullet = player.Bullet(screenSizeX/2,screenSizeY/2,character.damage,cameraOffset,character.getPen())   #create a bullet object and put it in a list
                bullets.append(bullet)
                character.resetShootDelay()                                                         #reset it so its not ready to fire.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if mousePressed[2]:
                if character.getName() == "marlo":
                    character.ability()
                elif character.getName() == "bogos":
                    cameraOffset,activated = character.ability(cameraOffset,currentRes,floors)
                    if activated == 1:
                        playSound("sounds/bogos.mp3",masterVol,soundVol)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            movement[0]-=(3)

        if keys[pygame.K_d]:
            movement[0]+=(3)
    
        if keys[pygame.K_w]:
            movement[1]-=(3)
            
        if keys[pygame.K_s]:
            movement[1]+=(3)
            
        display.fill((0,0,0))

        #temporary, press p to take damage, in order to test that the health system works
        if keys[pygame.K_p]:
            character.takeDamage(1)
#####  _                   _                        _ 
##### (_)                 | |                      | |
#####  _ _ __  _ __  _   _| |_ ___    ___ _ __   __| |
##### | | '_ \| '_ \| | | | __/ __|  / _ \ '_ \ / _` |
##### | | | | | |_) | |_| | |_\__ \ |  __/ | | | (_| |
##### |_|_| |_| .__/ \__,_|\__|___/  \___|_| |_|\__,_|
#####         | |                                     
#####         |_| 
        #enemy logic and stuff
        enemyCount = len(enemyList)

        #gun rotation and updating position and such
        gun.update(screenSizeX/4,screenSizeY/4,pistolImg,1)

        #draw the tiles onto the surface
        for y in range(60):
            for x in range(60):
                #draw floors
                if gameMap[y][x] ==1:
                    display.blit(floor,(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1]))
                #draw walls
                if gameMap[y][x] ==2:    
                    display.blit(wall,(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1]))
                    tilesRects.append(pygame.Rect(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1],tileWidth,tileWidth))
                #draw door
                if gameMap[y][x] ==3:
                    doorX,doorY = x,y
                    display.blit(door,(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1]))
                    doorHitbox = (pygame.Rect(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1],tileWidth,tileWidth))
                    if enemyCount:
                        tilesRects.append(pygame.Rect(x*tileWidth-cameraOffset[0],y*tileWidth-cameraOffset[1],tileWidth,tileWidth))

        distanceFromDoor = (-doorX*32 + cameraOffset[0]+screenSizeX/4 ,doorY*32-cameraOffset[1]-screenSizeY/4)
        #put the enemy in the correct place

        #for enemy in enemyList:
            #enemy.updatePosition(cameraOffset,(enemy.chasePlayer(character)))
        
        #putting items in the correct places:
        for life in lifeList:
            life.updatePosition(cameraOffset)

        for upgrade in upgradeBoxList:
            upgrade.updatePosition(cameraOffset)

        #bullet interactions and logic in main loop
        bulletCollide(bullets,tilesRects,cameraOffset)
        bulletEnemy(bullets,enemyList)
        playerHit(character,enemyList)
        abilityPickup(character,lifeList)
        upgradePickup(character,upgradeBoxList)

        #pathfinding
        for badguy in enemyList:
            if badguy.getType() == "angrydude":
                badguy.updateTicks()
                badguy.pathfind(character.getTile(cameraOffset,(screenSizeX,screenSizeY)),matrix,badguy.getTile(character,cameraOffset,(screenSizeX,screenSizeY)))
                if badguy.updatePath() == 0:
                    badguy.updatePosition(cameraOffset,(badguy.chasePlayer(character)))
                elif badguy.updatePath() == 1:
                    badguy.updatePosition(cameraOffset,(badguy.movex,badguy.movey))

            elif badguy.getType() == "ghost":
                badguy.updatePosition(cameraOffset,(badguy.chasePlayer(character)))

        #
        for bullet in bullets:
            bullet.draw(display,cameraOffset)
        
        #drawing the HUD text onto the screen
        display.blit(healthText,(0,0))
        display.blit(roomNumberText,(0,15))
        display.blit(enemyText,(screenSizeX/2 - 100 ,0))
        display.blit(distanceText, (screenSizeX/2 - 100,15))
        display.blit(specialText,(0,30))
        
        movement[0],movement[1] = move(character.rect,movement,tilesRects)
        cameraOffset[0] +=movement[0]
        cameraOffset[1] += movement[1]

        #drawing sprite groups            
        #characterSpriteGroup.update()
        characterSpriteGroup.draw(display)
        enemySpriteGroup.draw(display)
        lifeSpriteGroup.draw(display)
        upgradeSpriteGroup.draw(display)
        #gunSpriteGroup.draw(display)
        character.increment()
#break loop conditions
        #collisions between the door and player when the door is unlocked:
        if doorHitbox.colliderect(character.rect) and enemyCount == 0:
            break
        if character.health <= 0:
            break
#break loop condition end

        surf = pygame.transform.scale(display,(screenSizeX,screenSizeY))
        tilesRects = []
        gameDisplay.blit(surf,(0,0))
        pygame.display.update()
        character.invincibilityFrames += 1
        clock.tick(60)
    #terminate all health that hasn't been used by the player
    for life in lifeList:
        life.kill()
    #return the room number if they survive
    if character.health > 0:
        return room
    #return 99 if they died.
    else:
        return 99


def levelGeneration(Array):
    grid = Array
    grid = walker(grid)
    grid = walker(grid)
    grid = walker(grid)
    grid = walker(grid)
    grid = walker(grid)
    grid = placeWalls(grid)

    return grid
if (os.path.isfile("hash")):
    if readHash() == generateHash():
        gameOrMenu = 0
    else:
        gameOrMenu = -1
else:
    gameOrMenu = -1

start = float(0)
done = False
while True:
    #if you're in the menu this functions are ran.
    if gameOrMenu == -1:
        returnTuple = Menu(-1)
        gameOrMenu = returnTuple[0]
        character = returnTuple[1]
        difficulty = returnTuple[2]
    if gameOrMenu == 0:
        returnTuple = Menu()
        gameOrMenu = returnTuple[0]
        character = returnTuple[1]
        difficulty = returnTuple[2]
    
    #the functions below are for the game itself.
    #if the game is won
    if gameOrMenu == 11:
        gameOrMenu = 0
        print("you win!")
        pygame.mixer.music.stop()
        playSound("sounds/win.mp3",masterVol,soundVol)
        end = time.time()
        #calculate time taken
        playTime = end-start
        updatePlayTime(playTime)
        #increment win count
        updateWins()
        #reload stats
        playTime,wins,mostPlayed = loadStatsConfig()
        winsText,playTimeText,mostPlayedText = updateStatsText(wins,playTime,mostPlayed)


    #if the character's health drops to 0 or below
    if gameOrMenu ==99:
        gameOrMenu = 0
        print("you died :(")
        pygame.mixer.music.stop()
        playSound("sounds/lose.mp3",masterVol,soundVol)
        end = time.time()
        #calculate time taken
        playTime = end - start
        updatePlayTime(playTime)
        #reload stats
        playTime,wins,mostPlayed = loadStatsConfig()
        winsText,playTimeText,mostPlayedText = updateStatsText(wins,playTime,mostPlayed)

    if gameOrMenu == 1:
        pygame.mixer.music.load("sounds/gameMusic.mp3")
        pygame.mixer.music.set_volume((masterVol*musicVol)**1.5)
        pygame.mixer.music.play(-1)
        updateFavCharacter(character.getName())
        start = time.time()

    # every time a room number is returned, this code is ran in order to generate a new grid.
    if gameOrMenu >= 1 and done == False:
        gameGrid = buildGrid()
        gameMap = levelGeneration(gameGrid)
        gameDisplay.fill((0,0,0))
    #running the game itself. 
    if gameOrMenu >=1:
        gameOrMenu = game(gameMap,character,difficulty,gameOrMenu)

pygame.quit()
sys.exit()
