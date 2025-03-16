import pygame
import time
import math
pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")
background = pygame.image.load("clock.png")  
right_hand = pygame.image.load("rightarm.png")  
left_hand = pygame.image.load("leftarm.png") 
background = pygame.transform.scale(background, (width, height))
right_hand = pygame.transform.scale(right_hand, (20, 150))
left_hand = pygame.transform.scale(left_hand, (15, 120))
center = (width // 2, height // 2)
def rotate_hand(image, angle, offset):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=(center[0] + offset[0], center[1] + offset[1]))
    return rotated_image, rect
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    minute_angle = -(minutes * 6) 
    second_angle = -(seconds * 6)     
    r_hand, r_rect = rotate_hand(right_hand, minute_angle, (0, -75))
    l_hand, l_rect = rotate_hand(left_hand, second_angle, (0, -60))    
    screen.blit(r_hand, r_rect.topleft)
    screen.blit(l_hand, l_rect.topleft)    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.time.delay(1000)  
pygame.quit()
