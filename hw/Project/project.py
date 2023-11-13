
from quiz_list import *

start = pygame.font.SysFont('Castellar (fett)', 180)
first = pygame.font.SysFont('Castellar (fett)', 45)
main_text = [
    '>>> QUIZ GAME <<<',
    'PRESS "START" TO START!',
    'START'
]
def message_display():  #first window

    screen.fill("purple")

    rect = pygame.draw.rect(screen, "lime", (screen_width / 2 - 230, screen_height / 2 - 100, 400, 170))
    rect = pygame.draw.rect(screen, "black", rect, 2)
    text01 = first.render(main_text[0],True,"magenta")
    screen.blit(text01, (screen_width / 2 - 180, screen_height/2 - 200))
    text02 = first.render(main_text[1], True, "magenta")
    screen.blit(text02, (screen_width / 2 - 230, screen_height/2 - 150))
    text03 = start.render(main_text[2], True, "magenta")
    screen.blit(text03, (screen_width / 2 - 230, screen_height/2 - 70))

    run = True
    while run:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    quiz_01()

        pygame.display.flip()



if __name__ == "__main__":
    message_display()
