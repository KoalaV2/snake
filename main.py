#!/usr/bin/env python3

import pygame
import time

pygame.init()

white = (255,255,255)
font_style = pygame.font.SysFont(None, 50)
class Map:
   def __init__(self):
        self.W = 800
        self.H = 800
        self.foreground = (235, 219, 178)
        self.background = (39, 39, 39)

        self.display = pygame.display.set_mode((self.W,self.H))
        self.display.fill(self.background)
        pygame.display.set_caption('Snääääk')
class Snake:
    def __init__(self,x,y):
        self.x = x / 2
        self.y = y / 2

        self.x_tmp = 0
        self.y_tmp = 0
        self.dead = False

def main():
    clock = pygame.time.Clock()
    game_map = Map()
    snake = Snake(800,800)
    while snake.dead == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                snake.dead = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.x_tmp = -10
                    snake.y_tmp = 0
                elif event.key == pygame.K_RIGHT:
                    snake.x_tmp = 10
                    snake.y_tmp = 0
                elif event.key == pygame.K_UP:
                    snake.y_tmp = -10
                    snake.x_tmp = 0
                elif event.key == pygame.K_DOWN:
                    snake.y_tmp = 10
                    snake.x_tmp = 0
        print(event)
        if snake.x >= game_map.W or snake.x < 0 or snake.y >= game_map.H or snake.y < 0:
            snake.dead = True
        snake.x += snake.x_tmp
        snake.y += snake.y_tmp
        pygame.draw.rect(game_map.display, white, [snake.x, snake.y, 10, 10])

        pygame.display.update()
        clock.tick(10)
    time.sleep(2)
    pygame.quit()


if __name__ == "__main__":
    main()
