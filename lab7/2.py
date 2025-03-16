import pygame
import os
pygame.init()
pygame.mixer.init()
music = "music/"
tracks = [f for f in os.listdir(music) if f.endswith(".mp3")]
current_track = 0
def play_music():
    pygame.mixer.music.load(os.path.join(music, tracks[current_track]))
    pygame.mixer.music.play()
    print(f"Playing: {tracks[current_track]}")
if tracks:
    play_music()
else:
    print("No music found in the folder!")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  
                current_track = (current_track + 1) % len(tracks)
                play_music()
            elif event.key == pygame.K_p:  
                current_track = (current_track - 1) % len(tracks)
                play_music()
pygame.quit()