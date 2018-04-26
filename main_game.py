import pygame
from classes import playground
from classes import snake as snake_class
from classes import fruit as fruit_class
from pygame.locals import *
import random

pygame.init()

field = playground.PlayGround(32, 32, 10)
cs = field.cell_size
bgc = (255, 255, 255)
snake = snake_class.Snake()

snake_color = (0, 0, 255)
fruit_color = (255, 0, 0)

screen_size = field.size[0] * cs, field.size[1] * cs
screen = pygame.display.set_mode(screen_size)

gameRunning = True

fruit_exist = False

while gameRunning:
    dir_changed = False
    clock = pygame.time.Clock()
    screen.fill(bgc)
    field.clear_field()
    if(fruit_exist == False):
        rand_x = int(random.random() * 1000) % field.height
        rand_y = int(random.random() * 1000) % field.width
        fruit = fruit_class.Fruit(rand_x, rand_y)
        fruit_exist = True

    for event in pygame.event.get():
        print(event)
        if (event.type == pygame.QUIT):
            gameRunning = False
        elif (event.type == pygame.KEYDOWN and dir_changed == False):
            dir_changed = True
            if(event.key == pygame.K_DOWN):
                snake.change_directory('BOT')
            elif(event.key == pygame.K_UP):
                snake.change_directory('TOP')
            elif(event.key == pygame.K_LEFT):
                snake.change_directory('LEFT')
            elif(event.key == pygame.K_RIGHT):
                snake.change_directory('RIGHT')
    try:
        field.field[int(fruit.x)][int(fruit.y)] = 2
    except:
        pass
    # snake.add_head()
    snake.add_head()

    snake.remove_tail()
    print(fruit.x, fruit.y)
    for kek in snake.body:
        if(field.field[kek[0]][kek[1]] == 1):
            quit(0)
        if(field.field[kek[0]][kek[1]] == 2):
            snake.add_head()
            fruit_exist = False
            del fruit
        try:
            field.add_cell(kek, 1)
        except:
            pass

    for i in range(field.height):
        for j in range(field.width):
            if(field.field[i][j] == 1):
                rect = Rect((i * cs, j * cs), (i + cs, j + cs))
                pygame.draw.rect(screen, snake_color,
                                 rect)
            elif(field.field[i][j] == 0):
                rect = Rect((i * cs, j * cs), (i + cs, j + cs))
                pygame.draw.rect(screen, bgc,
                                 rect)
            elif(field.field[i][j] == 2):
                rect = Rect((i * cs, j * cs), (i + cs, j + cs))
                pygame.draw.rect(screen, fruit_color,
                                 rect)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
