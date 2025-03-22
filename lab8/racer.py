#import
import pygame, sys
from pygame.locals import *
import random, time

# initialization
pygame.init()


FPS = 60
FramePerSec = pygame.time.Clock()

# colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# size of a screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#speed
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0  # new counter

# fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# background
background = pygame.image.load("AnimatedStreet.png")

# screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1  # when new enemy comes, counter increases
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")  
        self.image = pygame.transform.scale(self.image, (30, 30))  # making size of a coin smaller
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-100, 0))  # coin shows up at the top of the screen

    def move(self):
        self.rect.move_ip(0, SPEED // 2)  # coin falss slower than enemy
        if self.rect.top > SCREEN_HEIGHT:  # if coin goes down, it appears at the top again
            self.rect.top = random.randint(-100, 0)
            self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)

# creating objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# sprites group
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# counting time for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# cycle of the game
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # increasing speed
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

   
    DISPLAYSURF.blit(background, (0, 0))

    # showing counter at the top left corner
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # showing number of coins at the top right corner
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

  
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # checks if enemy and player interacts
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    # checks if player and coin interacts
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1 
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(50, 500))  # Перемещение монеты

    # uodating a screen
    pygame.display.update()
    FramePerSec.tick(FPS)
