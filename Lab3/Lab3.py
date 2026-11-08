import tkinter as tk
import random
from playsound3 import playsound

def click():
    btn.config(state="disabled")
    key = []
    dig = [x for x in "0123456789"]
    let = [x for x in "QWERTYUIOPASDFGHJKLZXCVBNM"]
    for i in range(3):
        a = []
        for i in range(2):
            a.append(random.choice(dig))
        for i in range(3):
            a.append(random.choice(let))
        random.shuffle(a)
        a = "".join(a)
        key.append(a)
    key = "-".join(key)
    print_key(key, 0)

def print_key(key, position):
    if position < len(key):
        position += 1
        lbl2.config(text=key[:position])
        window.after(30, print_key, key, position + 1)
    else:
        btn.config(state="normal")


window = tk.Tk()
window.title("Keygen")
window.geometry("800x500")
img = tk.PhotoImage(file="undertale.png")
lblimg = tk.Label(window, image=img)
lblimg.place(x=0, y=0, relwidth=1, relheight=1)
playsound("Megalovania.mp3", block=False)
lbl1 = tk.Label(window, text="Ключ активации игры", font=("Consolas", 40))
lbl1.place(x=130, y=20)
lbl2 = tk.Label(window, text="XXXXX-XXXXX-XXXXX", font=("Consolas", 50))
lbl2.place(x=90, y=200)
btn = tk.Button(window, text="Генерация", width=20, font=("Consolas", 20), command=click)
btn.place(x=240, y=350)
window.mainloop()