"""
Crea un programa en Python llamado Conversor.py que cree una ventana con Tkinter para convertir valores
monetarios entre divisas Euro–Dólar y viceversa.
"""
import tkinter
from tkinter import *

win = Tk()
win.title("Conversor Euro-Dólar USA")
win.geometry("600x400")
win.resizable(False, False)

img = PhotoImage(file="venv/resource/wise.png")
img = img.subsample(2, 2)
img_label = Label(win, image=img, width=300, height=100)
img_label.pack()
img_label.place(x=600, y=10, anchor="ne")

label = Label(win, text="Conversión de divisas Euro - Dólar USA", font=("Arial", 20))
label.pack()
label.place(x=100, y=100)

label = Label(win, text="Cantidad a convertir", font=("Arial", 15))
label.pack()
label.place(x=100, y=150)

entry = Entry(win, font=("Arial", 15))
entry.pack()
entry.place(x=300, y=150)

label = Label(win, text="Conversión", font=("Arial", 15))
label.pack()
label.place(x=100, y=200)

radioBtn = IntVar()
radioBtn.set(1)
radio1 = Radiobutton(win, text="Euro a Dólar USA", variable=radioBtn, value=1, font=("Arial", 15))
radio1.pack()
radio1.place(x=300, y=200)

radio2 = Radiobutton(win, text="Dólar USA a Euro", variable=radioBtn, value=2, font=("Arial", 15))
radio2.pack()
radio2.place(x=300, y=230)

label = Label(win, text="Resultado", font=("Arial", 15))
label.pack()
label.place(x=100, y=350)

result_label = Label(win, text="", font=("Arial", 15))
result_label.pack()
result_label.place(x=300, y=350)


def convert():
    cantidad = float(entry.get())
    result = radioBtn.get()

    if result == 1:
        resultado = cantidad / 1.054883
        resultado_texto = "{:.2f} dólares USA".format(resultado)
    elif result == 2:
        resultado = cantidad / 0.947983
        resultado_texto = "{:.2f} euros".format(resultado)

    result_label.config(text=resultado_texto)


button = Button(win, text="Convertir", font=("Arial", 15))
button.config(command=convert)
button.pack()
button.place(x=100, y=300)

win.mainloop()
