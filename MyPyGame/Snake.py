import pygame
import random

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("Mickey.mp3")
pygame.mixer.music.play(-1) 


WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


SNAKE_SIZE = 20
SNAKE_SPEED = 10
FOOD_SIZE = 20


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


snake_x, snake_y = WIDTH // 2, HEIGHT // 2
snake_x_change, snake_y_change = 0, 0


food_x, food_y = random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE, random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE

snake_length = 1
snake_list = [(snake_x, snake_y)]

game_over = False


def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -SNAKE_SIZE
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = SNAKE_SIZE
                snake_x_change = 0


    snake_x += snake_x_change
    snake_y += snake_y_change

    
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE, random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE
        snake_length += 1

    
    screen.fill(WHITE)

   
    pygame.draw.rect(screen, GREEN, [food_x, food_y, FOOD_SIZE, FOOD_SIZE])

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]


    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        game_over = True


    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    draw_snake(snake_list)

    pygame.display.update()

    clock.tick(SNAKE_SPEED)

pygame.quit()