import pygame
import sys
import random
import pygame_menu
pygame.init()

colors = {
    "box_1": (255,255,255),
    "box_2": (160,32,240),
    "background": (85,26,139),
    "header_color": (154,50,205),
    "snake_color": (255,52,179),
    "apple_color": (0,255,127),
    "score": (255,255,255),
    "background_menu": (138, 43, 226)
}

size_block = 20
count_blocks = 20
header_margin = 70
margin = 1
size = [size_block * count_blocks + 2 * size_block + margin * count_blocks,
        size_block * count_blocks + 2 * size_block + margin * count_blocks + header_margin]
print(size)

pygame.display.set_caption("Snake 2")
screen = pygame.display.set_mode(size)
timer = pygame.time.Clock()

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < size_block and 0 <= self.y < size_block

    def __eq__(self, other):
        return isinstance(other,SnakeBlock) and self.x == other.x and self.y == other.y


def draw_block(color,row,column):
    pygame.draw.rect(screen, color, [size_block + column * size_block + margin * (column + 1),
                                     header_margin + size_block + row * size_block + margin * (row + 1),
                                     size_block,
                                     size_block])





def start_the_game():
    def get_rando_empty_block():
        x = random.randint(0, count_blocks - 1)
        y = random.randint(0, count_blocks - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, count_blocks - 1)
            empty_block.y = random.randint(0, count_blocks - 1)
        return empty_block

    snake_blocks = [SnakeBlock(9,8),SnakeBlock(9,9), SnakeBlock(9,10)]
    apple = get_rando_empty_block()
    d_row =  0
    d_col =  1
    speed = 1
    score = 0
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exit")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_s and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_a and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == pygame.K_d and d_row != 0:
                    d_row = 0
                    d_col = 1


        screen.fill(colors["background"])
        pygame.draw.rect(screen, colors["header_color"], [0,0,size[0], header_margin])



        text_score = pygame.font.SysFont('courier', 36).render(f" Score: {score}", True, colors["score"])
        screen.blit(text_score, (size_block * 0.1, size_block))
        text_speed = pygame.font.SysFont('courier', 36).render(f" Speed: {speed}", True, colors["score"])
        screen.blit(text_speed, (size_block * 0.1 + 220, size_block))

        for row in range(count_blocks):
            for column in range(count_blocks):
                if (row + column) % 2 == 0:
                    color = colors["box_2"]
                else:
                    color = colors["box_1"]

                draw_block(color,row,column)

        head = snake_blocks[-1]
        if not head.is_inside():
            print("Crash")
            break
        draw_block(colors["apple_color"], apple.x,apple.y)
        for block in snake_blocks:
            draw_block(colors["snake_color"], block.x, block.y)

        if apple == head:
            score += 1
            speed = score // 4 + 1
            snake_blocks.append(apple)
            apple = get_rando_empty_block()

        for block in snake_blocks:
            draw_block(colors["snake_color"], block.x, block.y)


        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            print("Crash yourself")
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        pygame.display.flip()
        timer.tick(4+speed)


main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.7)
menu = pygame_menu.Menu('', 300, 300,
                        theme=main_theme)
menu.add.text_input('Name :', default='User 1')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


while True:
    screen.fill(colors["background_menu"])

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()
