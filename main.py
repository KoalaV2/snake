#!/usr/bin/env python3

import pygame
import time
import random

pygame.init()

white = (255,255,255)
font_style = pygame.font.SysFont(None, 50)
class Map:
   def __init__(self):
        self.W = 800
        self.H = 800
        self.foreground = (235, 219, 178)
        self.background = (39, 39, 39)
        self.snake_block = 10

        self.foodx = round(random.randrange(0, self.W - self.snake_block))
        self.foody = round(random.randrange(0, self.H - self.snake_block))

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
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                snake.dead = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    snake.x_tmp = -10
                    snake.y_tmp = 0
                elif event.key == pygame.K_l:
                    snake.x_tmp = 10
                    snake.y_tmp = 0
                elif event.key == pygame.K_k:
                    snake.y_tmp = -10
                    snake.x_tmp = 0
                elif event.key == pygame.K_j:
                    snake.y_tmp = 10
                    snake.x_tmp = 0
        print(event)
        if snake.x >= game_map.W or snake.x < 0 or snake.y >= game_map.H or snake.y < 0:
            snake.dead = True
        snake.x += snake.x_tmp
        snake.y += snake.y_tmp
        pygame.draw.rect(game_map.display, game_map.foreground, [snake.x, snake.y, 10, 10])
        pygame.draw.rect(game_map.display, game_map.foreground, [game_map.foodx, game_map.foodx, game_map.snake_block, game_map.snake_block])
        print(round(snake.x))
        print(round(game_map.foodx))
        if round(snake.x) == game_map.foodx and round(snake.y) == game_map.foody:
            print("Eaten")

        pygame.display.update()
        clock.tick(10)
    time.sleep(2)
    pygame.quit()


if __name__ == "__main__":
    main()
