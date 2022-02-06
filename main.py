import pygame, sys


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))
man_pic = pygame.image.load("man.gif")
man_rect = man_pic.get_rect(topleft=[200, 300])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(man_pic, man_rect)
    if man_rect.right <= 500:
        man_rect.right += 2
    else:
        man_rect.bottom += 2
    pygame.display.flip()
    clock.tick(60)