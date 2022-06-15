import pygame
from player4 import Player
from enemy3 import Enemy3
from enemy import Enemy
from field import Field
from borders import Border
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
def level4():
    is_running = True

    death_sound = pygame.mixer.Sound('assets/death_sound.mp3')

    field_image = pygame.image.load('assets/field4.png')
    field_image = pygame.transform.scale(field_image, (742, 324))

    player = Player(66, 477, 10, 10)
    enemy = Enemy(39, 300, 15, 15, 15)
    enemy2 = Enemy(337, 300, 15, 15, 15)
    enemy3 = Enemy(39, 415, 15, 15, 15)
    enemy4 = Enemy(337, 415, 15, 15, 15)
    enemy5 = Enemy(135, 490, 30, 30, 5)
    enemy6 = Enemy(230, 240, 30, 30, 8)
    enemy7 = Enemy(760, 415, 15, 15, 15)
    enemy8 = Enemy(460, 415, 15, 15, 15)
    enemy9 = Enemy(760, 300, 15, 15, 15)
    enemy10 = Enemy(460, 300, 15, 15, 15)
    level_start = Field(41, 452, 60, 60)
    level_end = Field(699, 452, 60, 60)
    border1 = Border(102, 272, 54, 252)
    border2 = Border(102, 272, 178, 60)
    border3 = Border(339, 200, 120, 252)
    border4 = Border(219, 392, 360, 60)
    border5 = Border(637, 272, 58, 252)
    border6 = Border(517, 272, 178, 60)
    border7 = Border(39, 200, 1, 324)
    border8 = Border(39, 210, 742, 1)
    border9 = Border(39, 515, 742, 1)
    border10 = Border(760, 200, 1, 324)
    borders = [border1, border2, border3, border4, border5, border6, border7, border8, border9, border10]
    font = pygame.font.Font("assets/font.ttf", 32)


    def update_level4():
        keys = pygame.key.get_pressed()
        player.move(keys)
        enemy.move(39, 337)
        enemy2.move(39, 337)
        enemy3.move(39, 337)
        enemy4.move(39, 337)
        enemy5.move(130, 675)
        enemy6.move(90, 720)
        enemy7.move(460, 760)
        enemy8.move(460, 760)
        enemy9.move(460, 760)
        enemy10.move(460, 760)
        for border in borders:
            if border.hitbox.colliderect(player.draw(screen)):
                player.reset_position()
        if player.draw(screen).collidelist(
                [enemy.draw(screen), enemy2.draw(screen), enemy3.draw(screen), enemy4.draw(screen), enemy5.draw(screen),
                 enemy6.draw(screen), enemy7.draw(screen), enemy8.draw(screen), enemy9.draw(screen),
                 enemy10.draw(screen)]) != -1:
            death_sound.play()
            player.reset_position()
            player.deaths += 1

        if player.draw(screen).collidelist([level_end.draw(screen)]) != -1:
            print('Finished')

    def draw_level4():
        screen.fill((183, 175, 250))
        screen.blit(field_image, (29, 200))
        level_start.draw(screen)
        level_end.draw(screen)
        border1.draw(screen)
        border2.draw(screen)
        border3.draw(screen)
        border4.draw(screen)
        border5.draw(screen)
        border6.draw(screen)
        border7.draw(screen)
        border8.draw(screen)
        border9.draw(screen)
        border10.draw(screen)
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
        deathCounter = font.render("Deaths: " + str(player.deaths), True, (255, 255, 255))
        screen.blit(deathCounter, (250, 80))

        pygame.display.update()

    while is_running:
        pygame.time.delay(35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        update_level4()
        draw_level4()
    pygame.quit()