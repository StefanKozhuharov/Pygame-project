import pygame
from player import Player
from enemy import Enemy
from field import Field
from borders import Border
pygame.init()

FPS = 30
clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
def level2():
    is_running = True

    death_sound = pygame.mixer.Sound('assets/death_sound.mp3')

    field_image = pygame.image.load('assets/field2.png')
    field_image = pygame.transform.scale(field_image, (550,290))

    player = Player(115, 290, 10, 10, 115, 290)
    enemy = Enemy(500, 280, 6, 6, 10)
    enemy2 = Enemy(350, 280, 6, 6, 10)
    enemy3 = Enemy(350, 310, 6, 6, 10)
    enemy4 = Enemy(500, 310, 6, 6, 10)
    level_start = Field(105, 275, 40, 40)
    level_end = Field(605, 275, 40, 40)
    border1 = Border(100,270, 1, 50)
    border2 = Border(100, 270, 75, 1)
    border3 = Border(175, 247, 1, 23)
    border4 = Border(175, 247, 20, 1)
    border5 = Border(195, 247, 1, 23)
    border6 = Border(195, 270, 168, 1)
    border7 = Border(363, 247, 1, 23)
    border8 = Border(363, 247, 20, 1)
    border9 = Border(383, 247, 1, 23)
    border10 = Border(383, 270, 168, 1)
    border11 = Border(551, 247, 1, 23)
    border12 = Border(551, 247, 20, 1)
    border13 = Border(571, 247, 1, 23)
    border14 = Border(571, 270, 77, 1)
    border15 = Border(648, 270, 1, 50)
    border16 = Border(477, 320, 171, 1)
    border17 = Border(477, 320, 1, 24)
    border18 = Border(457, 344, 20, 1)
    border19 = Border(457, 320, 1, 24)
    border20 = Border(289, 320, 168, 1)
    border21 = Border(289, 320, 1, 24)
    border22 = Border(269, 344, 20, 1)
    border23 = Border(269, 320, 1, 24)
    border24 = Border(100, 320, 169, 1)
    borders = [border1, border2, border3, border4, border5, border6, border7, border8, border9, border10, border11, border12, border13, border14, border15, border16, border17, border18, border19, border20, border21, border22, border23, border24]
    font = pygame.font.Font("assets/font.ttf", 32)

    def update_level2():
        keys = pygame.key.get_pressed()
        player.move(keys)
        enemy.move(170,580)
        enemy2.move(170,580)
        enemy3.move(170,580)
        enemy4.move(170,580)
        for border in borders:
            if border.hitbox.colliderect(player.draw(screen)):
                player.reset_position()
        if player.draw(screen).collidelist([enemy.draw(screen), enemy2.draw(screen), enemy3.draw(screen), enemy4.draw(screen)]) != -1:
            player.reset_position()
        if player.draw(screen).collidelist([level_end.draw(screen)]) != -1:
            print('Finished')
    def draw_level2():
        screen.fill((183, 175, 250))
        screen.blit(field_image, (100,150))
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
        border11.draw(screen)
        border12.draw(screen)
        border13.draw(screen)
        border14.draw(screen)
        border15.draw(screen)
        border16.draw(screen)
        border17.draw(screen)
        border18.draw(screen)
        border19.draw(screen)
        border20.draw(screen)
        border21.draw(screen)
        border22.draw(screen)
        border23.draw(screen)
        border24.draw(screen)
        player.draw(screen)
        enemy.draw(screen)
        enemy2.draw(screen)
        enemy3.draw(screen)
        enemy4.draw(screen)
        deathCounter = font.render("Deaths: " + str(player.deaths), True, (255, 255, 255))
        screen.blit(deathCounter, (250, 50))

        pygame.display.update()

    while is_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        update_level2()
        draw_level2()
    pygame.quit()