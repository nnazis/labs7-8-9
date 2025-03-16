import pygame
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")
white = (255, 255, 255)
red = (255, 0, 0)
rad = 25
x, y = width // 2, height // 2
step = 20
running = True
while running:
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), rad)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - rad - step >= 0:
                y -= step
            elif event.key == pygame.K_DOWN and y + rad + step <= height:
                y += step
            elif event.key == pygame.K_LEFT and x - rad - step >= 0:
                x -= step
            elif event.key == pygame.K_RIGHT and x + rad + step <= width:
                x += step

pygame.quit()
