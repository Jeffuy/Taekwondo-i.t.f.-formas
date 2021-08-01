from tkinter import *
import random
from tkinter import messagebox
import lists
import patterns

root = Tk()
barramenu = Menu(root)
root.title("Formas Designadas")
root.geometry("+300+100")
root.config(menu=barramenu, bg="white")
root.resizable(0, 0)


def Acerca():
    messagebox.showinfo(
        "Formas", "Versión 2.101 Fecha 24/04/2020.\n(c) Germán Cavani. Todos los derechos reservados.")


AcercaDe = Menu(barramenu, tearoff=0)
AcercaDe.add_command(label="Versión", command=Acerca)

barramenu.add_cascade(label="Acerca de ", menu=AcercaDe)

CuantasFormas = IntVar()
Grado = IntVar()

# -------------ELEGIR------------------------------------------------------------


def elegir():

    # -----------PRIMER DAN-------------------------
    if CuantasFormas.get() == 1 and Grado.get() == 1:
        ResultadoFormas = random.choice(lists.FormasPrimero)
        Resultado.config(text=ResultadoFormas)

    elif CuantasFormas.get() == 2 and Grado.get() == 1:
        ResultadoFormas = random.choice(lists.FormasPrimero)
        ResultadoFormas2 = random.choice(lists.FormasPrimero)

        while ResultadoFormas2 == ResultadoFormas:
            ResultadoFormas2 = random.choice(lists.FormasPrimero)

        Resultado.config(text=ResultadoFormas + " y " + ResultadoFormas2)

    elif CuantasFormas.get() == 3 and Grado.get() == 1:
        ResultadoFormas = random.choice(lists.FormasPrimero)
        ResultadoFormas2 = random.choice(lists.FormasPrimero)
        ResultadoFormas3 = random.choice(lists.FormasPrimero)

        while ResultadoFormas2 == ResultadoFormas:
            ResultadoFormas2 = random.choice(lists.FormasPrimero)

        while ResultadoFormas3 == ResultadoFormas2 or ResultadoFormas3 == ResultadoFormas:
            ResultadoFormas3 = random.choice(lists.FormasPrimero)

        Resultado.config(text=ResultadoFormas + ", " +
                         ResultadoFormas2 + " y " + ResultadoFormas3)

        # -----------SEGUNDO DAN-------------------------

    elif CuantasFormas.get() == 1 and Grado.get() == 2:
        ResultadoFormas = random.choice(lists.FormasSegundo)
        Resultado.config(text=ResultadoFormas)

    elif CuantasFormas.get() == 2 and Grado.get() == 2:
        ResultadoFormas = random.choice(lists.FormasSegundo)
        ResultadoFormas2 = random.choice(lists.FormasSegundo)

        while ResultadoFormas2 == ResultadoFormas:
            ResultadoFormas2 = random.choice(lists.FormasSegundo)

        Resultado.config(text=ResultadoFormas + " y " + ResultadoFormas2)

    elif CuantasFormas.get() == 3 and Grado.get() == 2:
        ResultadoFormas = random.choice(lists.FormasSegundo)
        ResultadoFormas2 = random.choice(lists.FormasSegundo)
        ResultadoFormas3 = random.choice(lists.FormasSegundo)

        while ResultadoFormas2 == ResultadoFormas:
            ResultadoFormas2 = random.choice(lists.FormasSegundo)

        while ResultadoFormas3 == ResultadoFormas2 or ResultadoFormas3 == ResultadoFormas:
            ResultadoFormas3 = random.choice(lists.FormasSegundo)

        Resultado.config(text=ResultadoFormas + ", " +
                         ResultadoFormas2 + " y " + ResultadoFormas3)

        # -----------TERCER DAN-------------------------

    elif CuantasFormas.get() == 1 and Grado.get() == 3:
        ResultadoFormas = random.choice(lists.FormasTercero)
        Resultado.config(text=ResultadoFormas)

    elif CuantasFormas.get() == 2 and Grado.get() == 3:
        ResultadoFormas = random.choice(lists.FormasTercero)
        ResultadoFormas2 = random.choice(lists.FormasTercero)

        while ResultadoFormas2 == ResultadoFormas:
            ResultadoFormas2 = random.choice(lists.FormasTercero)

        Resultado.config(text=ResultadoFormas + " y " + ResultadoFormas2)

    elif CuantasFormas.get() == 3 and Grado.get() == 3:
        ResultadoFormas = random.choice(lists.FormasTercero)
        ResultadoFormas2 = random.choice(lists.FormasTercero)
        ResultadoFormas3 = random.choice(lists.FormasTercero)

        while ResultadoFormas2 == ResultadoFormas:
            ResultadoFormas2 = random.choice(lists.FormasTercero)

        while ResultadoFormas3 == ResultadoFormas2 or ResultadoFormas3 == ResultadoFormas:
            ResultadoFormas3 = random.choice(lists.FormasTercero)

        Resultado.config(text=ResultadoFormas + ", " +
                         ResultadoFormas2 + " y " + ResultadoFormas3)

        # -----------CUARTO DAN-------------------------

    elif CuantasFormas.get() == 1 and Grado.get() == 4:
        ResultadoFormas = random.choice(lists.Formas)
        Resultado.config(text=ResultadoFormas)

    elif CuantasFormas.get() == 2 and Grado.get() == 4:
        ResultadoFormas = random.choice(lists.Formas)
        ResultadoFormas2 = random.choice(lists.Formas)

        while ResultadoFormas2 == ResultadoFormas:
            ResultadoFormas2 = random.choice(lists.Formas)

        Resultado.config(text=ResultadoFormas + " y " + ResultadoFormas2)

    elif CuantasFormas.get() == 3 and Grado.get() == 4:
        ResultadoFormas = random.choice(lists.Formas)
        ResultadoFormas2 = random.choice(lists.Formas)
        ResultadoFormas3 = random.choice(lists.Formas)

        while ResultadoFormas2 == ResultadoFormas:
            ResultadoFormas2 = random.choice(lists.Formas)

        while ResultadoFormas3 == ResultadoFormas2 or ResultadoFormas3 == ResultadoFormas:
            ResultadoFormas3 = random.choice(lists.Formas)

        Resultado.config(text=ResultadoFormas + ", " +
                         ResultadoFormas2 + " y " + ResultadoFormas3)

    else:

        Resultado.config(text="Selecciona grado y cantidad de formas")

# -----------------PREGUNTAS----------------------------------------------------


preguntaGrado = Label(root, text="Elige el grado:",
                      bg="white", fg="blue", font=("null 12 bold"))
preguntaGrado.grid(row=0, column=0, pady=10)

primer = Radiobutton(root, variable=Grado, bg="white",
                     text="Hasta 1er Dan", value=1, font="null 12 bold")
primer.grid(row=0, column=1)

segundo = Radiobutton(root, variable=Grado, bg="white",
                      text="Hasta 2do Dan", value=2, font="null 12 bold")
segundo.grid(row=0, column=2)

tercero = Radiobutton(root, variable=Grado, bg="white",
                      text="Hasta 3er Dan", value=3, font="null 12 bold")
tercero.grid(row=0, column=3)

cuarto = Radiobutton(root, variable=Grado, bg="white",
                     text="Hasta 4to Dan", value=4, font="null 12 bold")
cuarto.grid(row=0, column=4)

pregunta = Label(root, text="Elige la cantidad:", bg="white",
                 fg="blue", font=("null 12 bold"))
pregunta.grid(row=1, column=0, pady=10, columnspan=2)

Cuantas = Radiobutton(root, variable=CuantasFormas,
                      bg="white", text="1 Forma", value=1, font="null 12 bold")
Cuantas.grid(row=1, column=2, stick="w")

Cuantas2 = Radiobutton(root, variable=CuantasFormas,
                       bg="white", text="2 Formas", value=2, font="null 12 bold")
Cuantas2.grid(row=1, column=3, stick="w")

Cuantas3 = Radiobutton(root, variable=CuantasFormas,
                       bg="white", text="3 Formas", value=3, font="null 12 bold")
Cuantas3.grid(row=1, column=4, stick="w")

Elegir = Button(root, text="Formas Designadas", justify="center",
                bg="#C6FFEF", height=1, width=20, command=elegir, font="null 25 bold")
Elegir.grid(row=4, column=0, columnspan=6, pady=10)

Resultado = Label(root, text="Apreta el botón",
                  bg="white", font=("null 25 bold"))
Resultado.grid(row=5, column=0, pady=10, columnspan=5)

# -----------------BOTONES TRIVIA--------------------------------
Linea = Canvas(root, width=800, height=2, bg="black")
Linea.grid(row=7, columnspan=5, pady=20)

TriviasLabel = Label(root, text="Trivias: ", fg="blue",
                     bg="white", font=("null 14 bold"))
TriviasLabel.grid(row=8, column=0, pady=20)

BotonChonJi = Button(root, text="Chon Ji", font="null 12 bold",
                     command=patterns.ChonJi, height=1, width=15)
BotonChonJi.grid(row=8, column=1, pady=20)

BotonDangun = Button(root, text="Dangun", font="null 12 bold",
                     command=patterns.Dangun, height=1, width=15)
BotonDangun.grid(row=8, column=2, pady=20)

BotonDosan = Button(root, text="Dosan", font="null 12 bold",
                    command=patterns.Dosan, height=1, width=15)
BotonDosan.grid(row=8, column=3, pady=20)

BotonWonhyo = Button(root, text="Won Hyo", font="null 12 bold",
                     command=patterns.Wonhyo, height=1, width=15)
BotonWonhyo.grid(row=8, column=4, pady=20)

BotonYulgok = Button(root, text="Yulgok", font="null 12 bold",
                     command=patterns.Yulgok, height=1, width=15)
BotonYulgok.grid(row=9, column=0, pady=10)

BotonJoonGun = Button(root, text="Joon Gun", font="null 12 bold",
                      command=patterns.JoonGun, height=1, width=15)
BotonJoonGun.grid(row=9, column=1, pady=10)

BotonToiGye = Button(root, text="Toi Gye", font="null 12 bold",
                     command=patterns.ToiGye, height=1, width=15)
BotonToiGye.grid(row=9, column=2, pady=10)

BotonHwarang = Button(root, text="Hwarang", font="null 12 bold",
                      command=patterns.Hwarang, height=1, width=15)
BotonHwarang.grid(row=9, column=3, pady=10)

BotonChoongMoo = Button(root, text="Choong Moo", font="null 12 bold",
                        command=patterns.ChoongMoo, height=1, width=15)
BotonChoongMoo.grid(row=9, column=4, pady=10)

TriviasLabel = Label(root, text="Trivias: ", fg="blue",
                     bg="white", font=("null 14 bold"))
TriviasLabel.grid(row=8, column=0, pady=10)

Linea2 = Canvas(root, width=800, height=2, bg="black")
Linea2.grid(row=11, columnspan=5, pady=30)


#PuntajeTotal=Label(root,text=("Tu puntaje hasta el momento es de " + str(Puntaje1) + " puntos"), fg="black", bg="white", font=("null 14 bold"))
#PuntajeTotal.grid(row=10, column=0, columnspan=5, pady=20)

"""BotonKwangGae=Button(root, text="(próximamente)", font="null 12 bold", height=1, width=15)
BotonKwangGae.grid(row=9, column=4, pady=10)

BotonPoEun=Button(root, text="Po Eun", font="null 12 bold", command=Poeun)
BotonPoEun.grid(row=10, column=0, pady=10)

BotonGaeBaek=Button(root, text="Gae Baek", font="null 12 bold", command=GaeBaek)
BotonGaeBaek.grid(row=10, column=1, pady=10)

BotonEuIam=Button(root, text="Eu Iam", font="null 12 bold")
BotonEuIam.grid(row=10, column=2, pady=10)

BotonJuche=Button(root, text="Juche", font="null 12 bold")
BotonJuche.grid(row=10, column=3, pady=10)

BotonChoongJang=Button(root, text="Choong Jang", font="null 12 bold")
BotonChoongJang.grid(row=10, column=4, pady=10)

BotonSamIl=Button(root, text="Sam Il", font="null 12 bold")
BotonSamIl.grid(row=11, column=0, pady=10)

BotonYooSin=Button(root, text="Yoo Sin", font="null 12 bold")
BotonYooSin.grid(row=11, column=1, pady=10)

BotonChoiJong=Button(root, text="Choi Jong", font="null 12 bold")
BotonChoiJong.grid(row=11, column=2, pady=10)

BotonMoonMoo=Button(root, text="Moon Moo", font="null 12 bold")
BotonMoonMoo.grid(row=11, column=3, pady=10)

BotonUlJi=Button(root, text="Ul Ji", font="null 12 bold")
BotonUlJi.grid(row=11, column=4, pady=10)

BotonYonGae=Button(root, text="Yon Gae", font="null 12 bold")
BotonYonGae.grid(row=12, column=0, pady=10)"""
