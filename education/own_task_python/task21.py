from colorama import Fore
from pyfiglet import Figlet
import time
def display_text_animation(text, delay=1.0):
    fig = Figlet(font='slant')
    for line in text.splitlines():
        print(Fore.GREEN + fig.renderText(line))
        time.sleep(delay)

display_text_animation("Hallo world", delay=1)