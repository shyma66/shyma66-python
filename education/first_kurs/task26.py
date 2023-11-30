from random import randint
import pygame

screen_widht = 840
screen_heigt = 600
pygame.init()
screen = pygame.display.set_mode((screen_widht, screen_heigt))
clock = pygame.time.Clock()
pygame.display.set_caption("Randomizer")
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
magenta = (255, 0, 255)
lime = (0, 255, 0)



font = pygame.font.SysFont( ' Castellar (fett) ' , 40 )
start = pygame.font.SysFont('Castellar (fett)', 180)
input_text = ""
main_text = ['Try again.',
            '>>> GUESSING GAME <<<',
            'PRESS "START" TO START!',
            'START',
            'My number is higher!',
            'My number is less!',
            'YOU LOOSE!',
            'YOU WINNER!',
            'Enter number and press "Enter"'
            ]


def message_display():

    screen.fill("purple")

    rect = pygame.draw.rect(screen, lime, (190, 200, 400, 170))
    rect = pygame.draw.rect(screen ,black, rect ,2)
    text01 = font.render(main_text[1],True,magenta )
    screen.blit(text01,( 210 ,100))
    text02 = font.render(main_text[2], True, magenta)
    screen.blit(text02, (200, 150))
    text03 = start.render(main_text[3],True,magenta)
    screen.blit(text03, (190, 230))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    randomizer()
        pygame.display.flip()



def randomizer():
    result_text = ''
    input_text = ''
    r = randint(1, 100)
    attempts = 0

    screen.fill("purple")
    text08 = font.render(main_text[8], True, magenta)
    screen.blit(text08,(150,150) )
    run = True
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(input_text)
                    except ValueError:
                        result_text = "Please enter an integer number."
                    else:
                        attempts += 1
                        if guess == r:
                            result_text = f"You are Winner!You guessed the number {r} after {attempts} attempts."
                            run = True
                        elif attempts >= 10:
                            result_text = f"You have exhausted all attempts. The hidden number was {r}."
                            break


                        else:
                            result_text = "The hidden number is greater." if guess < r else "The hidden number is smaller."
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            screen.fill("purple")

        screen.fill("purple")
        rect = pygame.draw.rect(screen, lime, [285, 300, 200, 50])
        text_surface = font.render("Guess the number from 1 to 100:", True, magenta)
        screen.blit(text_surface, (160, 150))

        result_surface = font.render(result_text, True, magenta)
        screen.blit(result_surface, (10, 220))

        txt_surface = font.render(input_text, True, magenta)
        width = max(200, txt_surface.get_width() + 10)
        rect.w = width
        screen.blit(txt_surface, (  355,  312))
        pygame.draw.rect(screen, black, rect, 2)

        attempts_text = font.render(f"Attempts: {attempts}/10", True, magenta)
        screen.blit(attempts_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

message_display()