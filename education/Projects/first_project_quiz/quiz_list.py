import sys
import pygame
import time
# size of window
screen_width = 840
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("QUIZ")
# usually
font = pygame.font.SysFont('Castellar (fett)', 35)
# Quiz
quiz = pygame.font.SysFont('Castellar (fett)', 100)
score = 0
total = 6
score_questions = 0



main_text = [
    '>>> QUIZ GAME <<<',
    'TRUE',
    'FALSE']
def answer_true():
    answer_true = pygame.draw.rect(screen, "gray", (screen_width / 2 - 320, screen_height / 2 - 200, 650, 380))
    answer_true = pygame.draw.rect(screen, "black", answer_true, 2)
    text_true = pygame.font.SysFont('Castellar (fett)', 250).render(main_text[1], True, "green")
    screen.blit(text_true, (screen_width / 2 - 240, screen_height / 2 - 100))
    pygame.display.flip()

def answer_false():
    answer_false = pygame.draw.rect(screen, "gray", (screen_width / 2 - 320, screen_height / 2 - 200, 650, 380))
    answer_false = pygame.draw.rect(screen, "black", answer_false, 2)
    text_false = pygame.font.SysFont('Castellar (fett)', 250).render(main_text[2], True, "red")
    screen.blit(text_false, (screen_width / 2 - 270, screen_height / 2 - 100))

    pygame.display.flip()

def window():            # makes the window with buttons
    screen.fill("purple")
    text_quiz_game = quiz.render(main_text[0], True, "magenta")
    screen.blit(text_quiz_game, (screen_width / 2 - 340, screen_height / 2 - 270))

    rect_question = pygame.draw.rect(screen, "gray", (screen_width / 2 -320, screen_height / 2 -200, 650, 380))
    rect_question = pygame.draw.rect(screen, "black", rect_question, 2)

    rect_a = pygame.draw.rect(screen, "red", (screen_width / 2 - 300, screen_height / 2 - 65, 300, 110))
    rect_a = pygame.draw.rect(screen, "black", rect_a, 2)

    rect_b = pygame.draw.rect(screen, "green", (screen_width / 2 + 10, screen_height / 2 - 65, 300, 110))
    rect_b = pygame.draw.rect(screen, "black", rect_b, 2)

    rect_c = pygame.draw.rect(screen, "blue", (screen_width / 2 - 300, screen_height / 2 + 50, 300, 110))
    rect_c = pygame.draw.rect(screen, "black", rect_c, 2)

    rect_d = pygame.draw.rect(screen, "yellow", (screen_width / 2 + 10, screen_height / 2 + 50, 300, 110))
    rect_d = pygame.draw.rect(screen, "black", rect_d, 2)

    return rect_a, rect_b, rect_c, rect_d , rect_question
def score_text():      # makes a test counter
    global  total , score_questions
    score_questions +=1
    score_text = pygame.font.SysFont('Castellar (fett)', 60).render(f" {score_questions}/{total}", True,
                                                                    "white")
    screen.blit(score_text, (screen_width / 2 + 240, screen_height / 2 - 180))


    # all the Quiz code are almost identical, the only difference is another number of list
    #
    # (quiz_01)
    #           \/                                   \/
    # quiz_list_01_answer_01 = font.render(quiz_list_01[1], True, "black")
    #                       \/
    # screen.blit(quiz_list_01_answer_01, (rect_a.centerx - 140, rect_a.centery - 10))
    #
    # (quiz_02)
    #           \/                                   \/
    # quiz_list_02_answer_01 = font.render(quiz_list_02[1], True, "black")
    #                       \/
    # screen.blit(quiz_list_02_answer_01, (rect_a.centerx - 140, rect_a.centery - 10))
quiz_list_01 = [        #list of question and answers
    "Badge :",
    "(a) die Anstecknadel", #True
    "(b) die Form/Gestalt",
    "(c) der Antrag",
    "(d) die Träne"]
def quiz_01():
    global score
    rect_a, rect_b, rect_c, rect_d , rect_question= window()
    print("quiz_01")
    quiz_list_01_question = pygame.font.SysFont('Castellar (fett)', 70).render(quiz_list_01[0], True, "black")
    screen.blit(quiz_list_01_question, (rect_question.centerx - 100, rect_question.centery - 150))
    quiz_list_01_answer_01 = font.render(quiz_list_01[1], True, "black")
    screen.blit(quiz_list_01_answer_01, (rect_a.centerx - 140 , rect_a.centery - 10))
    quiz_list_01_answer_02 = font.render(quiz_list_01[2], True, "black")
    screen.blit(quiz_list_01_answer_02, (rect_b.centerx - 140 , rect_b.centery - 10))
    quiz_list_01_answer_03 = font.render(quiz_list_01[3], True, "black")
    screen.blit(quiz_list_01_answer_03, (rect_c.centerx - 140 , rect_c.centery - 10))
    quiz_list_01_answer_04 = font.render(quiz_list_01[4], True, "black")
    screen.blit(quiz_list_01_answer_04, (rect_d.centerx - 140 , rect_d.centery - 10))
    score_text()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if rect_a.collidepoint(event.pos):  # correct answer
                    print("Your answer: A\n True")
                    score += 1
                    answer_true()
                    time.sleep(0.5)
                    quiz_02()
                    run = False
                elif rect_b.collidepoint(event.pos) :   #other answer
                    print("Your answer: B\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_02()
                    run = False
                elif rect_c.collidepoint(event.pos):    #other answer
                    print("Your answer: C\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_02()
                    run = False
                elif rect_d.collidepoint(event.pos):    #other answer
                    print("Your answer: D\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_02()
                    run = False
        pygame.display.flip()
quiz_list_02 = [
    "Invention :",
    "(a) die Auszeihnung",
    "(b) das Geschlecht",
    "(c) die Erfindung", #True
    "(d) die Wahrheit"]
def quiz_02():
    global score
    print("quiz_02")
    rect_a, rect_b, rect_c, rect_d, rect_question = window()
    quiz_list_02_question = pygame.font.SysFont('Castellar (fett)', 70).render(quiz_list_02[0], True, "black")
    screen.blit(quiz_list_02_question, (rect_question.centerx - 100, rect_question.centery - 150))
    quiz_list_02_answer_01 = font.render(quiz_list_02[1], True, "black")
    screen.blit(quiz_list_02_answer_01, (rect_a.centerx - 140, rect_a.centery - 10))
    quiz_list_02_answer_02 = font.render(quiz_list_02[2], True, "black")
    screen.blit(quiz_list_02_answer_02, (rect_b.centerx - 140, rect_b.centery - 10))
    quiz_list_02_answer_03 = font.render(quiz_list_02[3], True, "black")
    screen.blit(quiz_list_02_answer_03, (rect_c.centerx - 140, rect_c.centery - 10))
    quiz_list_02_answer_04 = font.render(quiz_list_02[4], True, "black")
    screen.blit(quiz_list_02_answer_04, (rect_d.centerx - 140, rect_d.centery - 10))
    score_text()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_c.collidepoint(event.pos):  # correct answer
                    print(("Your answer: C\n True"))
                    score += 1
                    answer_true()
                    time.sleep(0.5)
                    quiz_03()
                    run = False
                elif rect_a.collidepoint(event.pos):    #other answer
                    print("Your answer: A\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_03()
                    run = False
                elif rect_b.collidepoint(event.pos):    #other answer
                    print("Your answer: B\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_03()
                    run = False
                elif rect_d.collidepoint(event.pos):    #other answer
                    print("Your answer: D\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_03()
                    run = False
        pygame.display.flip()
quiz_list_03 = [
    "Realize :",
    "(a) erstellen",
    "(b) überfallen",
    "(c) gehören",
    "(d) etwas erkennen"] #True
def quiz_03():
    global score
    print("quiz_03")
    rect_a, rect_b, rect_c, rect_d, rect_question = window()
    quiz_list_03_question = pygame.font.SysFont('Castellar (fett)', 70).render(quiz_list_03[0], True, "black")
    screen.blit(quiz_list_03_question, (rect_question.centerx - 100, rect_question.centery - 150))
    quiz_list_03_answer_01 = font.render(quiz_list_03[1], True, "black")
    screen.blit(quiz_list_03_answer_01, (rect_a.centerx - 140, rect_a.centery - 10))
    quiz_list_03_answer_02 = font.render(quiz_list_03[2], True, "black")
    screen.blit(quiz_list_03_answer_02, (rect_b.centerx - 140, rect_b.centery - 10))
    quiz_list_03_answer_03 = font.render(quiz_list_03[3], True, "black")
    screen.blit(quiz_list_03_answer_03, (rect_c.centerx - 140, rect_c.centery - 10))
    quiz_list_03_answer_04 = font.render(quiz_list_03[4], True, "black")
    screen.blit(quiz_list_03_answer_04, (rect_d.centerx - 140, rect_d.centery - 10))
    score_text()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_d.collidepoint(event.pos):  # correct answer
                    print("Your answer: D\n True")
                    score += 1
                    answer_true()
                    time.sleep(0.5)
                    quiz_04()
                    run = False
                elif rect_b.collidepoint(event.pos):    #other answer
                    print("Your answer: B\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_04()
                    run = False
                elif rect_c.collidepoint(event.pos):    #other answer
                    print("Your answer: C\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_04()
                    run = False
                elif rect_a.collidepoint(event.pos):    #other answer
                    print("Your answer: A\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_04()
                    run = False
        pygame.display.flip()

quiz_list_04 = [
    "To claim :",
    "(a) behaupten", #True
    "(b) lösen",
    "(c) hochladen",
    "(d) durchführen"]
def quiz_04():
    global score
    print("quiz_04")
    rect_a, rect_b, rect_c, rect_d , rect_question= window()
    quiz_list_04_question = pygame.font.SysFont('Castellar (fett)', 70).render(quiz_list_04[0], True, "black")
    screen.blit(quiz_list_04_question, (rect_question.centerx - 100, rect_question.centery - 150))
    quiz_list_04_answer_01 = font.render(quiz_list_04[1], True, "black")
    screen.blit(quiz_list_04_answer_01, (rect_a.centerx - 140, rect_a.centery - 10))
    quiz_list_04_answer_02 = font.render(quiz_list_04[2], True, "black")
    screen.blit(quiz_list_04_answer_02, (rect_b.centerx - 140, rect_b.centery - 10))
    quiz_list_04_answer_03 = font.render(quiz_list_04[3], True, "black")
    screen.blit(quiz_list_04_answer_03, (rect_c.centerx - 140, rect_c.centery - 10))
    quiz_list_04_answer_04 = font.render(quiz_list_04[4], True, "black")
    screen.blit(quiz_list_04_answer_04, (rect_d.centerx - 140, rect_d.centery - 10))
    score_text()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_a.collidepoint(event.pos):  # correct answer
                    print("Your answer: A\n True")
                    score += 1
                    answer_true()
                    time.sleep(0.5)
                    quiz_05()
                    run = False
                elif rect_b.collidepoint(event.pos):    #other answer
                    print("Your answer: B\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_05()
                    run = False
                elif rect_c.collidepoint(event.pos):    #other answer
                    print("Your answer: C\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_05()
                    run = False
                elif rect_d.collidepoint(event.pos):    #other answer
                    print("Your answer: D\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_05()
                    run = False

        pygame.display.flip()
quiz_list_05 = [
    "Fact :",
    "(a) die Periode",
    "(b) der Gegenstand",
    "(c) die Tatsache",  #True
    "(d) der Zusammenhang"]
def quiz_05():
    global score
    print("quiz_05")
    rect_a, rect_b, rect_c, rect_d , rect_question = window()
    quiz_list_05_question = pygame.font.SysFont('Castellar (fett)', 70).render(quiz_list_05[0], True, "black")
    screen.blit(quiz_list_05_question, (rect_question.centerx - 100, rect_question.centery - 150))
    quiz_list_05_answer_01 = font.render(quiz_list_05[1], True, "black")
    screen.blit(quiz_list_05_answer_01, (rect_a.centerx - 140, rect_a.centery - 10))
    quiz_list_05_answer_02 = font.render(quiz_list_05[2], True, "black")
    screen.blit(quiz_list_05_answer_02, (rect_b.centerx - 140, rect_b.centery - 10))
    quiz_list_05_answer_03 = font.render(quiz_list_05[3], True, "black")
    screen.blit(quiz_list_05_answer_03, (rect_c.centerx - 140, rect_c.centery - 10))
    quiz_list_05_answer_04 = font.render(quiz_list_05[4], True, "black")
    screen.blit(quiz_list_05_answer_04, (rect_d.centerx - 140, rect_d.centery - 10))
    score_text()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_c.collidepoint(event.pos):
                    print("Your answer: C\nTrue")   # correct answer
                    score += 1
                    answer_true()
                    time.sleep(0.5)
                    quiz_06()
                    run = False
                elif rect_b.collidepoint(event.pos):    #other answer
                    print("Your answer: B\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_06()
                    run = False
                elif rect_a.collidepoint(event.pos):    #other answer
                    print("Your answer: A\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_06()
                    run = False
                elif rect_d.collidepoint(event.pos):    #other answer
                    print("Your answer: D\n False")
                    answer_false()
                    time.sleep(0.5)
                    quiz_06()
                    run = False
        pygame.display.flip()
quiz_list_06 = [
    "To consider :",
    "(a) lösen",
    "(b) erwägen",  #True
    "(c) streiten",
    "(d) sich einsetzen"]
def quiz_06():
    global score
    print("quiz_05")
    rect_a, rect_b, rect_c, rect_d , rect_question = window()
    quiz_list_06_question = pygame.font.SysFont('Castellar (fett)', 70).render(quiz_list_06[0], True, "black")
    screen.blit(quiz_list_06_question, (rect_question.centerx - 100, rect_question.centery - 150))
    quiz_list_06_answer_01 = font.render(quiz_list_06[1], True, "black")
    screen.blit(quiz_list_06_answer_01, (rect_a.centerx - 140, rect_a.centery - 10))
    quiz_list_06_answer_02 = font.render(quiz_list_06[2], True, "black")
    screen.blit(quiz_list_06_answer_02, (rect_b.centerx - 140, rect_b.centery - 10))
    quiz_list_06_answer_03 = font.render(quiz_list_06[3], True, "black")
    screen.blit(quiz_list_06_answer_03, (rect_c.centerx - 140, rect_c.centery - 10))
    quiz_list_06_answer_04 = font.render(quiz_list_06[4], True, "black")
    screen.blit(quiz_list_06_answer_04, (rect_d.centerx - 140, rect_d.centery - 10))
    score_text()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_b.collidepoint(event.pos): # correct answer
                    print("Your answer: B\n True")
                    answer_true()
                    time.sleep(0.5)
                    score += 1
                    display_score()
                    run = False
                elif rect_d.collidepoint(event.pos):    #other answer
                    print("Your answer: D\n False")
                    answer_false()
                    time.sleep(0.5)
                    display_score()
                    run = False
                elif rect_a.collidepoint(event.pos):    #other answer
                    print("Your answer: A\n False")
                    answer_false()
                    time.sleep(0.5)
                    display_score()
                    run = False
                elif rect_c.collidepoint(event.pos):    #other answer
                    print("Your answer: C\n False")
                    answer_false()
                    time.sleep(0.5)
                    display_score()
                    run = False
        pygame.display.flip()

def display_score(): #shows the score at the end
    global score, total
    print(f"Finish\nYour score: {score}/{total} ")
    screen.fill("purple")
    score_text = pygame.font.SysFont('Castellar (fett)', 70).render(f"Your Score: {score}/{total}", True, "white")
    screen.blit(score_text, (screen_width / 2 - 200, screen_height / 2 - 50))
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    pygame.quit()
    sys.exit()



