import pygame
pygame.init()
width, height = 500, 500
rad = 25
ball_color = (255, 0, 0)  
bg_color = (255, 255, 255)  
STEP = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball")
x, y = width // 2, height // 2
running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - rad - STEP >= 0:
        x -= STEP
    if keys[pygame.K_RIGHT] and x + rad + STEP <= width:
        x += STEP
    if keys[pygame.K_UP] and y - rad - STEP >= 0:
        y -= STEP
    if keys[pygame.K_DOWN] and y + rad + STEP <= height:
        y += STEP
        screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color, (x, y), rad)
    pygame.display.update()
pygame.quit()
