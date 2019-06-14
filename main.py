import pygame as pg
import sys
import random

pg.init()

WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
clock = pg.time.Clock()

player_pos = [150, 250]
#posx = 150
#posy = 250
monster_pos = [random.randint(10, 790), random.randint(10,590)]
#mon_posx = random.randint(10, 790)
#mon_posy = random.randint(10, 590)
wall_pos = [random.randint(10, 590), random.randint(10, 590)]
#wall_x = random.randint(10, 590)
#wall_y = random.randint(10, 590)
size = 30
screen = pg.display.set_mode((WIDTH, HEIGHT))
move = 30
game_running = True

def collision_wall(player_pos, wall_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    w_x = wall_pos[0]
    w_y = wall_pos[1]
    if (w_x >= p_x and w_x < p_x+size) or (p_x >= w_x and p_x < w_x+size):
        if (w_y >= p_y and w_y < p_y+size) or (p_y >= w_y and p_y < w_y+size):
            return True
    return False

def collision_monster(player_pos, monster_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    m_x = monster_pos[0]
    m_y = monster_pos[1]
    if (m_x >= p_x and m_x < p_x+size) or (p_x >= m_x and p_x < m_x+size):
        if (m_y >= p_y and m_y < p_y+size) or (p_y >= m_y and p_y < m_y+size):
            return True
    return False

while game_running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]:
        if not collision_wall(player_pos, wall_pos) and not collision_monster(player_pos, monster_pos):
            player_pos[1] -= 10
        else:
            player_pos[1] += 10
    if pressed[pg.K_DOWN]:
        if not collision_wall(player_pos, wall_pos) and not collision_monster(player_pos, monster_pos):
            player_pos[1] += 10
        else:
            player_pos[1] -= 10
    if pressed[pg.K_LEFT]:
        if not collision_wall(player_pos, wall_pos) and not collision_monster(player_pos, monster_pos):
            player_pos[0] -= 10
        else:
            player_pos[0] += 10
    if pressed[pg.K_RIGHT]:
        if not collision_wall(player_pos, wall_pos) and not collision_monster(player_pos, monster_pos):
            player_pos[0] += 10
        else:
            player_pos[0] -= 10

    screen.fill(BLACK)

    player = pg.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], size, size))
    monster = pg.draw.rect(screen, RED, (monster_pos[0], monster_pos[1], size, size))
    wall = pg.draw.rect(screen, BLUE, (wall_pos[0], wall_pos[1], size, size))
    pg.display.flip()
    clock.tick(30)

pg.quit()
