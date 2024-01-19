import pygame
import random

width = 720
height = 540
pygame.init()
display = pygame.display.set_mode((width,height))

pygame.display.update()
pygame.display.set_caption("Snake game")
colors = {
    "snake_head": ("green"),
    "snake_tail": (0,200,0),
    "apple": ("red")
}
snake_position = {
    "x": width/2-10,
    "y": height/2-10,
    "x_change": 0,
    "y_change": 0,
}
snake_size = (10,10)

snake_speed = 10

snake_tails = []



food_position = {
    "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10
}
food_size = (10,10)
food_eaten = 0

score = 0
def score_text():      # makes a test counter
    score_text = pygame.font.SysFont('Castellar (fett)', 60).render(f" score: {food_eaten}", True, "white")
    display.blit(score_text, (width / 2 * 0.05, height /2 * 0.1))
    pygame.display.update()
run = True
clock = pygame.time.Clock()

while run:
    score_text()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and snake_position["x_change"] == 0:
                snake_position["x_change"] = -snake_speed
                snake_position["y_change"] = 0
            elif event.key == pygame.K_d and snake_position["x_change"] == 0:
                snake_position["x_change"] = snake_speed
                snake_position["y_change"] = 0

            elif event.key == pygame.K_w and snake_position["y_change"] == 0:
                snake_position["x_change"] = 0
                snake_position["y_change"] = -snake_speed
            elif event.key == pygame.K_s and snake_position["y_change"] == 0:
                snake_position["x_change"] = 0
                snake_position["y_change"] = snake_speed

    display.fill("purple")

    ltx = snake_position["x"]
    lty = snake_position["y"]

    for i ,v in enumerate(snake_tails):
        _ltx = snake_tails[i][0]
        _lty = snake_tails[i][1]

        snake_tails[i][0] = ltx
        snake_tails[i][1] = lty

        ltx = _ltx
        lty = _lty

    for t in snake_tails:
        pygame.draw.rect(display, colors["snake_tail"], [
            t[0],
            t[1],
            snake_size[0],
            snake_size[1]])

    snake_position["x"] += snake_position["x_change"]
    snake_position["y"] += snake_position["y_change"]

    if(snake_position["x"] < -snake_size[0]):
        snake_position["x"] = width

    elif(snake_position["x"] > width):
        snake_position["x"] = 0

    elif(snake_position["y"] < -snake_size[1]):
        snake_position["y"] = height

    elif(snake_position["y"] > height):
        snake_position["y"] = 0

    pygame.draw.rect(display,colors["snake_head"],[
        snake_position["x"],
        snake_position["y"],
        snake_size[0],
        snake_size[1]] )

    pygame.draw.rect(display, colors["apple"],[
        food_position["x"],
        food_position["y"],
        food_size[0],
        food_size[1]])

    if(snake_position["x"] == food_position["x"]
        and snake_position["y"] == food_position["y"]):
        food_eaten += 1

        snake_tails.append([food_position["x"], food_position["y"]])

        food_position = {
            "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
            "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10
        }
    for i,v in enumerate(snake_tails):
        if(snake_position["x"]+ snake_position["x_change"] == snake_tails[i][0]
            and snake_position["y"]+ snake_position["y_change"] == snake_tails[i][1]):
            snake_tails = snake_tails[:i]
            break


    clock.tick(30)
pygame.quit()
quit()