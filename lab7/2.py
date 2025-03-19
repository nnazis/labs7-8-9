import pygame
import os
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Music Player")
mus_files = ["music1.mp3", "music2.mp3"]  
for mus_file in mus_files:
    if not os.path.exists(mus_file):
        print(f"Ошибка: Файл '{mus_file}' не найден!")
        exit()
track_index = 0
def play_music():
    pygame.mixer.music.load(mus_files[track_index])
    pygame.mixer.music.play()
    print(f"Playing: {mus_files[track_index]}")
def stop_music():
    pygame.mixer.music.stop()
    print("Music Stopped")
def next_track():
    global track_index
    track_index = (track_index + 1) % len(mus_files)  
    play_music()
def previous_track():
    global track_index
    track_index = (track_index - 1) % len(mus_files) 
    play_music()
is_playing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  #p play
                if not is_playing:
                    play_music()
                    is_playing = True
            elif event.key == pygame.K_m:  #m stop
                stop_music()
                is_playing = False
            elif event.key == pygame.K_n:  #n next 
                next_track()
            elif event.key == pygame.K_l:  #l previous 
                previous_track()

    pygame.display.flip()

pygame.quit()