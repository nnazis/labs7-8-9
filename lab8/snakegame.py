import pygame
import random
import sys
#initialization
pygame.init()
pygame.mixer.init()
# music
pygame.mixer.music.load('scatman.mp3')
pygame.mixer.music.play(-1)
# screen 
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with levels")
clock = pygame.time.Clock()
#Game Font
font = pygame.font.Font(None,30)
# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
# Snake Settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 10
# first parameters of food
def spawn_food():
    while True:
        food = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        if food not in snake_body: # check if food is not in snake
            return food
food_pos = spawn_food()
game_score = 0
level = 1
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"
    # move the snake
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10
    # add new head
    snake_body.insert(0, list(snake_pos))
    # checking if food was eaten
    if snake_pos == food_pos:
        game_score += 1
        food_pos = spawn_food()
            # increasing the level every 4 points
        if game_score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake_body.pop()
# checking interaction with the wall
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False
# checking interaction with itself
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False
# game rendering
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
# showing the score and level
    score_text = font.render(f"Score: {game_score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))
    screen.blit(level_text, (20, 50))
    pygame.display.update()
    clock.tick(speed)
# game over
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
screen.fill(BLACK)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(3000) # delay before quiting