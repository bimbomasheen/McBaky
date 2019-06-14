import pygame as pg
import sys
import random

pg.init()

WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
clock = pg.time.Clock()


posx = 150
posy = 250
mon_posx = random.randint(10, 790)
mon_posy = random.randint(10, 590)
player_size = 10
screen = pg.display.set_mode((WIDTH, HEIGHT))
move = 5
Game_running = True

while Game_running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]: posy -= 10
    if pressed[pg.K_DOWN]: posy += 10
    if pressed[pg.K_LEFT]: posx -= 10
    if pressed[pg.K_RIGHT]: posx += 10

    screen.fill(BLACK)
    player = pg.draw.circle(screen, GREEN, (posx, posy), player_size, 0)
    monster = pg.draw.rect(screen, RED, (mon_posx, mon_posy, 20, 35))
    pg.display.flip()
    clock.tick(10)

pg.quit()