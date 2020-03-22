from tkinter import *
import datetime
import locale

root= Tk()
root.geometry("420x400")
root.config(bd=20)



def calcular():
    date = datetime.date(anio.get(),mes.get(),dia.get())
    resultado.set(date.strftime("%A"))

    dia.set("")
    mes.set("")
    anio.set("")

locale.setlocale(locale.LC_ALL, '')

dia = IntVar()
mes = IntVar()
anio = IntVar()
resultado = StringVar()

dia.set("")
mes.set("")
anio.set("")

Label(root, text="Adivino el dia", font=("Helvetica",30)).pack()

Label(root, text="Ingrese el día,por ejemplo 3: ").pack()
Entry(root, justify="center", textvariable=dia).pack()

Label(root, text="Ingrese el mes, por ejemplo 4: ").pack()
Entry(root, justify="center", textvariable=mes).pack()

Label(root, text="Ingrese el año, por ejemplo 1990: ").pack()
Entry(root, justify="center", textvariable=anio).pack()

Button(root, text="Calcular", command=calcular).pack()

Label(root, justify="center",textvariable=resultado).pack()

Entry(root, )
root.mainloop()