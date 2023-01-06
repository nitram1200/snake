from screeninfo import get_monitors
import pygame
import random
import numpy

pygame.init()

# Getting the screen size for the monitors in pixels
snake_size = 25
info = str(get_monitors()).split(',')
width = int((round((int(info[2][7:])) // snake_size) * snake_size))
height = int((round(((int(info[3][8:])) - snake_size - 50) // snake_size) * snake_size))
if width + snake_size > int(info[2][7:]):
    width -= snake_size
if height + snake_size > int(info[3][8:]):
    height -= snake_size

# Colours
BLACK = (0, 0, 0)  # RGB code for black, the background
WHITE = (255, 255, 255)  # RGB code for white, text
GREEN = (57, 255, 20)  # RGB code for neo green, the snake
RED = (255, 49, 49)  # RGB code for neon red, the borders

# Display and font
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake by Nitram_20')
font_style = pygame.font.SysFont("microsoftsansserif", 25)

# How fast does the snake move - in one frame the snake moves one block
clock = pygame.time.Clock()
FPS = 15  # Recommended


def pathfiner(snake_list):
    grid = numpy.zeros((round(width / snake_size), round(height / snake_size)))
    for x in snake_list:
        print(x)


# Displays the starting and end messages
def message(msg, color):
    dis.fill(BLACK)
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])
    pygame.display.update()


# Main loop for the game itself - playable with human controls
def game():
    game_over = False
    game_close = False

    headx = round(width / 2 / snake_size) * snake_size  # Places the head of the snake at the centre of the screen
    heady = round(height / 2 / snake_size) * snake_size
    headx_change = 0
    heady_change = 0

    snake_list = []  # Location values for the snake
    len_snake = 1  # Len of snake

    foodx = round(random.randrange(0, width-snake_size)/snake_size) * snake_size  # Location of the food on the x-axis
    foody = round(random.randrange(0, height-snake_size)/snake_size) * snake_size  # Location of the food on the y-axis

    while not game_close:

        while game_over:

            message("You Lost! Press R-Restart to try again or Q-Quit", RED)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                    game_over = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_r:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
                game_over = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_close = True
                    game_over = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    headx_change = -snake_size
                    heady_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    headx_change = snake_size
                    heady_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    heady_change = -snake_size
                    headx_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    heady_change = snake_size
                    headx_change = 0

        headx += headx_change
        heady += heady_change

        snake_head = [headx, heady]
        snake_list.append(snake_head)

        if len(snake_list) > len_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        if headx + snake_size > width or headx < 0 or heady + snake_size > height or heady < 0:
            game_over = True

        dis.fill('white')  # Makes the screen white
        pygame.draw.rect(dis, 'black', [0, 0, width+snake_size, height+snake_size])  # Creates a black playing field,
        # leaving white borders for outside of bounds
        pygame.draw.rect(dis, RED, [foodx, foody, snake_size, snake_size])  # Displays food

        for x in snake_list:
            pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_size, snake_size])

        pygame.display.update()

        if headx == foodx and heady == foody:
            len_snake += 5

            food = False
            while not food:
                foodx = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
                foody = round(random.randrange(0, height - snake_size) / snake_size) * snake_size
                if [foodx, foody] not in snake_list:
                    print(f'New food added at {foodx, foody}')
                    food = True
                else:
                    print('Finding a new location for food')

        print(snake_list)
        print(foodx, foody)

        clock.tick(FPS)


if __name__ == '__main__':
    start = False
    while not start:
        message('Press any key to begin, press Q-Quit to close', 'white')

        for y in pygame.event.get():
            if y.type == pygame.QUIT:
                start = True
            if y.type == pygame.KEYDOWN:
                if y.key == pygame.K_q:
                    start = True
                else:
                    start = True
                    game()

    pygame.quit()
    quit()
