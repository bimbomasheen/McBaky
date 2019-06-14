import pygame as pg
import sys

pg.init()

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
clock = pg.time.Clock()


posx = 150
posy = 250
player_size = 10
screen = pg.display.set_mode((WIDTH, HEIGHT))
move = 5
Game_running = True

while Game_running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]: posy -= 3
    if pressed[pg.K_DOWN]: posy += 3
    if pressed[pg.K_LEFT]: posx -= 3
    if pressed[pg.K_RIGHT]: posx += 3



    screen.fill(BLACK)
    player = pg.draw.circle(screen, GREEN, (posx, posy), player_size, 0)

    pg.display.flip()
    clock.tick(60)

pg.quit()