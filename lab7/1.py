import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1480, 1090))
clock = pygame.time.Clock()
background = pygame.image.load("clock.png")
min_hand = pygame.image.load("rightarm.png")
sec_hand = pygame.image.load("leftarm.png")
s_sec = pygame.transform.scale(sec_hand, (sec_hand.get_width()*0.9, sec_hand.get_height()*0.9))
s_min = pygame.transform.scale(min_hand, (min_hand.get_width()*1, min_hand.get_height()*1))
p = (700, 525)
angle_sec = 0
angle_min = 0
def rotate(image, angle, p):
    r_image = pygame.transform.rotate(image, -angle)
    r_rect = r_image.get_rect(center=p)
    return r_image, r_rect
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    current_time = time.localtime()
    seconds = time.time() % 60
    minutes = (time.time() // 60) % 60
    angle_sec = (seconds*6 - 90)
    angle_min = ((minutes*6 + seconds * 0.1) - 90)
    r_sec, r_sec_rect = rotate(s_sec, angle_sec, p)
    r_min, r_min_rect = rotate(s_min, angle_min, p)
    screen.fill((255, 255, 255))
    screen.blit(background, (6, 11))
    screen.blit(r_sec, r_sec_rect.topleft)
    screen.blit(r_min, r_min_rect.topleft)
    pygame.display.flip()
    clock.tick(60)
    pygame.time.delay(10)
pygame.quit()
