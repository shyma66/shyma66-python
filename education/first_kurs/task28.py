import pygame

FPS = 60

WIDTH_DISPLAY = 800
HEIGHT_DISPLAY = 700

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 260
HEIGHT_RECTANGLE = 250
DELTA_STEP = 50

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first_kurs game")


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and COORD_X > 0:
        COORD_X = COORD_X - DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X < WIDTH_DISPLAY - WIDTH_RECTANGLE:
        COORD_X = COORD_X + DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y > 0 :
        COORD_Y = COORD_Y - DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y < HEIGHT_DISPLAY - HEIGHT_RECTANGLE:
        COORD_Y = COORD_Y + DELTA_STEP

    gameDisplay.fill(BLACK_COLOR)

    # pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
    #                                           COORD_Y,
    #                                           WIDTH_RECTANGLE,
    #                                           HEIGHT_RECTANGLE])

    spider_img = pygame.image.load("./3508010.png")
    gameDisplay.blit(spider_img , (COORD_X,COORD_Y))
    pygame.display.update()
    clock.tick(FPS)