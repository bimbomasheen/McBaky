import pygame as pg
import sys

pg.init()

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
clock = pg.time.Clock()

player_pos = [int(WIDTH/2), int(HEIGHT/2)]
player_size = 10
screen = pg.display.set_mode((WIDTH, HEIGHT))
move = 5
Game_running = True

while Game_running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if pg.key == pg.K_LEFT:
                player_pos = player_pos-move
            if pg.key == pg.K_RIGHT:
                player_pos = player_pos+move


    screen.fill(BLACK)
    pg.draw.circle(screen, GREEN, (player_pos[0], player_pos[1]), player_size)

    pg.display.update()