import pygame
from player import Player
from enemy import Enemy
from field import Field
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
def level1():
    is_running = True

    death_sound = pygame.mixer.Sound('assets/death_sound.mp3')
    background_music = pygame.mixer.music.load('assets/background_music.mp3')

    pygame.mixer.music.play(-1)

    field_image = pygame.image.load('assets/field.png')
    field_image = pygame.transform.scale(field_image, (550,290))

    player = Player(150, 390, 10, 10)
    enemy = Enemy(350,200,5,5,15)
    enemy2 = Enemy(350,250,5,5,15)
    enemy3 = Enemy(300,300,5,5,15)
    enemy4 = Enemy(150,170,5,5,15)
    enemy5 = Enemy(150,220,5,5,15)
    enemy6 = Enemy(150,280,5,5,15)
    enemy7 = Enemy(150,320,5,5,15)
    enemy8 = Enemy(270,360,5,5,15)
    enemy9 = Enemy(270,400,5,5,15)
    enemy10 = Enemy(410,380,5,5,15)
    enemy11 = Enemy(350,340,5,5,15)
    enemy12 = Enemy(410,420,5,5,15)
    level_start = Field(113, 359, 100, 70)
    level_end = Field(540, 160, 100, 70)
    font = pygame.font.Font("assets/font.ttf", 32)


    def update_level1():
        keys = pygame.key.get_pressed()
        player.move(keys)
        enemy.move (125, 520)
        enemy2.move(125, 520)
        enemy3.move(125, 620)
        enemy4.move(125, 520)
        enemy5.move(125, 520)
        enemy6.move(125, 620)
        enemy7.move(125, 620)
        enemy8.move(225, 620)
        enemy9.move(225, 620)
        enemy10.move(225, 620)
        enemy11.move(125, 620)
        enemy12.move(225, 620)
        if player.draw(screen).collidelist([enemy.draw(screen),enemy2.draw(screen), enemy3.draw(screen), enemy4.draw(screen), enemy5.draw(screen), enemy6.draw(screen), enemy7.draw(screen), enemy8.draw(screen), enemy9.draw(screen), enemy10.draw(screen), enemy11.draw(screen), enemy12.draw(screen)]) != -1:
            death_sound.play()
            player.reset_position()
            player.deaths += 1

        if player.draw(screen).collidelist([level_end.draw(screen)]) != -1:
            print('Finished')

    def draw_level1():
        screen.fill((183, 175, 250))
        screen.blit(field_image, (100,150))
        level_start.draw(screen)
        level_end.draw(screen)
        player.draw(screen)
        enemy.draw(screen)
        enemy2.draw(screen)
        enemy3.draw(screen)
        enemy4.draw(screen)
        enemy5.draw(screen)
        enemy6.draw(screen)
        enemy7.draw(screen)
        enemy8.draw(screen)
        enemy9.draw(screen)
        enemy10.draw(screen)
        enemy11.draw(screen)
        enemy12.draw(screen)
        deathCounter = font.render("Deaths: " + str(player.deaths), True, (255, 255, 255))
        screen.blit(deathCounter, (250, 50))

        pygame.display.update()

    while is_running:
        pygame.time.delay(35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        update_level1()
        draw_level1()
    pygame.quit()