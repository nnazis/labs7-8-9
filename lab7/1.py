import pygame
import time
import os
from datetime import datetime
pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")
background = pygame.image.load("clock")  
minute = pygame.image.load("rightarm")   
second = pygame.image.load("leftarm")    
music = "music"  
music_files = [f for f in os.listdir(music) if f.endswith(".mp3")]
current_track = 0
pygame.mixer.init()
if music_files:
    pygame.mixer.music.load(os.path.join(music, music_files[current_track]))
def clock():
    now = datetime.now()
    minutes = now.minute * 6   
    seconds = now.second * 6   
    screen.blit(background, (0, 0))
    minute = pygame.transform.rotate(minute, -minutes)
    second = pygame.transform.rotate(second, -seconds)
    m_rect = minute.get_rect(center=(width//2, height//2))
    s_rect = second.get_rect(center=(width//2, height//2))
    screen.blit(minute, m_rect.topleft)
    screen.blit(second, s_rect.topleft)
def play():
    if music_files:
        pygame.mixer.music.load(os.path.join(music, music_files[current_track]))
        pygame.mixer.music.play()
def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    play()
def track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    play()
def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    elif keys[pygame.K_s]:
        pygame.mixer.music.stop()
    elif keys[pygame.K_RIGHT]:
        next_track()
    elif keys[pygame.K_LEFT]:
        track()
running = True
while running:
    screen.fill((255, 255, 255))
    clock()
    handle_keys()
    pygame.display.update()
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()