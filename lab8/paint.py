import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    draw_mode = 'line'  # Default drawing mode
    points = []
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Color selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    draw_mode = 'eraser'
                elif event.key == pygame.K_c:
                    draw_mode = 'circle'
                elif event.key == pygame.K_t:
                    draw_mode = 'rectangle'
                elif event.key == pygame.K_l:
                    draw_mode = 'line'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # Right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append((position, draw_mode))
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        for i in range(len(points) - 1):
            drawShape(screen, i, points[i][0], points[i + 1][0], radius, mode, points[i][1])
        pygame.display.flip()
        clock.tick(60)
def drawShape(screen, index, start, end, width, color_mode, draw_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    else:
        color = (255, 255, 255)  # Default to white
    
    if draw_mode == 'eraser':
        color = (0, 0, 0)  # Eraser mode
    
    if draw_mode == 'line':
        pygame.draw.line(screen, color, start, end, width)
    elif draw_mode == 'circle':
        pygame.draw.circle(screen, color, start, width)
    elif draw_mode == 'rectangle':
        rect = pygame.Rect(start[0] - width, start[1] - width, width * 2, width * 2)
        pygame.draw.rect(screen, color, rect)

main()
