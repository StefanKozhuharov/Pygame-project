import pygame
from player3 import Player
from enemy3 import Enemy3
from field import Field
from borders import Border
from level4 import level4
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
def level3():
    is_running = True

    death_sound = pygame.mixer.Sound('assets/death_sound.mp3')

    field_image = pygame.image.load('assets/field3.png')
    field_image = pygame.transform.scale(field_image, (290, 550))

    player = Player(150, 525, 10, 10)
    enemy = Enemy3(120, 200, 5, 5, 15)
    enemy2 = Enemy3(140, 200, 5, 5, -15)
    enemy3 = Enemy3(165, 200, 5, 5, 15)
    enemy4 = Enemy3(185, 200, 5, 5, -15)
    enemy5 = Enemy3(210, 200, 5, 5, 15)
    enemy6 = Enemy3(230, 200, 5, 5, -15)
    enemy7 = Enemy3(260, 200, 5, 5, 15)
    enemy8 = Enemy3(280, 200, 5, 5, -15)
    enemy9 = Enemy3(305, 200, 5, 5, 15)
    enemy10 = Enemy3(320, 200, 5, 5, -15)
    enemy11 = Enemy3(345, 200, 5, 5, 15)
    enemy12 = Enemy3(370, 200, 5, 5, -15)
    level_start = Field(112, 494, 100, 70)
    level_end = Field(278, 38, 100, 70)
    border1 = Border(105, 30, 1, 540)
    border2 = Border(105, 30, 280, 1)
    border3 = Border(385, 30, 1, 540)
    border4 = Border(105, 570, 280, 1)
    borders = [border1, border2, border3, border4]
    font = pygame.font.Font("assets/font.ttf", 32)


    def update_level3():
        keys = pygame.key.get_pressed()
        player.move(keys)
        enemy.move(35, 490)
        enemy2.move(35, 490)
        enemy3.move(35, 490)
        enemy4.move(35, 490)
        enemy5.move(35, 490)
        enemy6.move(35, 570)
        enemy7.move(35, 570)
        enemy8.move(120, 570)
        enemy9.move(120, 570)
        enemy10.move(120, 570)
        enemy11.move(120, 570)
        enemy12.move(120, 570)
        for border in borders:
            if border.hitbox.colliderect(player.draw(screen)):
                player.reset_position()
        if player.draw(screen).collidelist(
                [enemy.draw(screen), enemy2.draw(screen), enemy3.draw(screen), enemy4.draw(screen), enemy5.draw(screen),
                 enemy6.draw(screen), enemy7.draw(screen), enemy8.draw(screen), enemy9.draw(screen),
                 enemy10.draw(screen), enemy11.draw(screen), enemy12.draw(screen)]) != -1:
            death_sound.play()
            player.reset_position()
            player.deaths += 1

        if player.draw(screen).collidelist([level_end.draw(screen)]) != -1:
            level4()

    def draw_level3():
        screen.fill((183, 175, 250))
        screen.blit(field_image, (100, 25))
        level_start.draw(screen)
        level_end.draw(screen)
        player.draw(screen)
        border1.draw(screen)
        border2.draw(screen)
        border3.draw(screen)
        border4.draw(screen)
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
        screen.blit(deathCounter, (500, 350))

        pygame.display.update()

    while is_running:
        pygame.time.delay(35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        update_level3()
        draw_level3 ()
    pygame.quit()