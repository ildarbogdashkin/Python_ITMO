import time

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'

def draw_flag():
    height = 3
    length = 12
    line = length // 3
    for i in range(height):
        print(f"{BLUE}{' ' * line}{WHITE}{' ' * line}{RED}{' ' * line}{RESET}")

def pattern():
    size = 12
    colors = [101, 102, 103, 104]
    for j in colors:
        for i in range(size):
            if size // 3 <= i < size // 3 * 2:
                print(f"{'  ' * (size // 3)}\u001b[{j}m{'  ' * (size // 3)}{RESET}{'  ' * (size // 3)}", flush=True)
            else:
                print(f"\u001b[{j}m{'  ' * (size // 3)}{RESET}{'  ' * (size // 3)}\u001b[{j}m{'  ' * (size // 3)}{RESET}", flush=True)
        time.sleep(1)
        print(f"\u001b[{size}A", end="") # возврат в начало

def sequence():
    f = open("sequence.txt", "r")
    more0 = 0
    less0 = 0
    for i in f:          # считаем количество чисел больше и меньше 0
        if float(i) > 0:
            more0 += 1
        else:
            less0 += 1
    f.close()
    print(f"{BLUE}{" " * more0}{RESET} {more0 / (more0 + less0) * 100}% больше 0")
    print(f"{RED}{" " * less0}{RESET} {less0 / (more0 + less0) * 100}% меньше 0")

def graph():
    height = 9
    for i in range(height + 1): # вывожу ось Y и соответствующую точку
        print(f"{height - i}\u001b[{round(2 + (height - i)**0.5)}G{RED} {RESET}")
    print(" ", end="") # отступ вправо для оси X
    for i in range(round(height**0.5) + 1): # вывожу ось X
        print(i, end="")


# запускать по отдельности

# draw_flag()
# pattern()
# sequence()
# graph()