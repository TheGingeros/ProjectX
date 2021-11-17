import pygame

pygame.init()

screen_w, screen_h = 1280, 720
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Fialka's Adventures")
menu_background = pygame.image.load('menu_background.png')
icon = pygame.image.load('fialka_hlava.png')
pygame.display.set_icon(icon)


def refresh ():
    pygame.display.update()
#Main_Loop
main_loop = True
while main_loop:
    screen.blit(menu_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False
            pygame.quit()
    refresh()