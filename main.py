import pygame, sys
from button import Button
from player import Player
from enemy import Enemy
from field import Field
from level1 import level1
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

background_music = pygame.mixer.music.load('assets/background_music.mp3')
pygame.mixer.music.play(-1)

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def music():
    if pygame.mixer.music.get_busy():
       pygame.mixer.music.pause()

    else:
       pygame.mixer.music.unpause()
def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(60).render("MAIN MENU", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 75))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 200),
                             text_input="PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        MUSIC_BUTTON = Button(image=pygame.image.load("assets/Music Rect.png"), pos=(400, 350),
                                text_input="MUSIC", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 500),
                             text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, MUSIC_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level1()
                if MUSIC_BUTTON.checkForInput(MENU_MOUSE_POS):
                    music()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()