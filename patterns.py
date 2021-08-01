import window
from tkinter import *
from tkinter import messagebox

Count1 = 0
Count2 = 0
Count3 = 0
Count4 = 0
Count5 = 0
Count6 = 0
Count7 = 0
Count8 = 0
Count9 = 0
Count10 = 0
Count11 = 0
Count12 = 0
Count13 = 0
Count14 = 0
Count15 = 0
Count16 = 0
Intentos1 = 0
Intentos2 = 0
Intentos3 = 0
Intentos4 = 0
Intentos5 = 0
Intentos6 = 0
Intentos7 = 0
Intentos8 = 0
Intentos9 = 0
Intentos10 = 0
Intentos11 = 0
Intentos12 = 0
Intentos13 = 0
Intentos14 = 0
Puntaje1 = 0


def ChonJi():

    global Intentos1
    Intentos1 = Intentos1+1
    if Intentos1 >= 2:
        messagebox.showinfo("Error", "Ya has realizado la trivia de Chon Ji")

    else:
        root1 = Toplevel()
        root1.resizable(0, 1)
        root1.geometry("470x500+400+25")
        root1.title("Trivia: Chon-Ji")
        scrollbar = Scrollbar(root1)
        c = Canvas(root1, bg="white", yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        elFrame = Frame(c, bg="white", padx=10)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=elFrame, anchor="nw")

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                c.xview_scroll(scroll, "units")
            else:
                c.yview_scroll(scroll, "units")
        c.bind_all("<MouseWheel>", on_mousewheel)

        Chon1 = IntVar()
        Chon2 = IntVar()
        Chon3 = IntVar()
        Chon4 = IntVar()
        Chon5 = IntVar()
        Chon6 = IntVar()
        Chon7 = IntVar()
        Chon8 = IntVar()
        Chon9 = IntVar()
        Chon10 = IntVar()

        def Ya():
            global Puntaje1
            global Count1
            if Chon1.get() == 1:
                Count1 = Count1+1

            if Chon2.get() == 2:
                Count1 = Count1+1

            if Chon3.get() == 3:
                Count1 = Count1+1

            if Chon4.get() == 3:
                Count1 = Count1+1

            if Chon5.get() == 3:
                Count1 = Count1+1

            if Chon6.get() == 1:
                Count1 = Count1+1

            if Chon7.get() == 3:
                Count1 = Count1+1

            if Chon8.get() == 3:
                Count1 = Count1+1

            if Chon9.get() == 3:
                Count1 = Count1+1

            if Chon10.get() == 2:
                Count1 = Count1+1

            messagebox.showinfo("Resultado", ("Tienes " + str(Count1) +
                                              "/10 respuestas correctas en la trivia sobre Chon-Ji"))
            window.BotonChonJi.config(
                text=("Chon Ji: " + str(Count1) + "/10"), font="null 12 bold")
            Puntaje1 = Puntaje1+Count1
            root1.destroy()

        p1 = Label(elFrame, text="1) ¿Cuantos movimientos tiene Chon Ji?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p11 = Radiobutton(elFrame, variable=Chon1, bg="white", text="19",
                          value=1, font="null 10 bold", justify="center").pack()

        p12 = Radiobutton(elFrame, variable=Chon1, bg="white", text="20",
                          value=2, font="null 10 bold", justify="center").pack()

        p13 = Radiobutton(elFrame, variable=Chon1, bg="white", text="17",
                          value=3, font="null 10 bold", justify="center").pack()

        p2 = Label(elFrame, text="\n2) ¿De qué cinto es Chon Ji?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p21 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Blanco",
                          value=1, font="null 10 bold", justify="center").pack()

        p22 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Blanco punta amarilla",
                          value=2, font="null 10 bold", justify="center").pack()

        p23 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Verde",
                          value=3, font="null 10 bold", justify="center").pack()

        p3 = Label(elFrame, text="\n3) ¿Para qué lado arranca?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p31 = Radiobutton(elFrame, variable=Chon3, bg="white", text="Hacia la derecha",
                          value=1, font="null 10 bold", justify="center").pack()

        p32 = Radiobutton(elFrame, variable=Chon3, bg="white", text="Hacia adelante",
                          value=2, font="null 10 bold", justify="center").pack()

        p33 = Radiobutton(elFrame, variable=Chon3, bg="white", text="Hacia la izquierda",
                          value=3, font="null 10 bold", justify="center").pack()

        p4 = Label(elFrame, text="\n4) ¿Cuántos puños tiene Chon Ji?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p41 = Radiobutton(elFrame, variable=Chon4, bg="white", text="12",
                          value=1, font="null 10 bold", justify="center").pack()

        p42 = Radiobutton(elFrame, variable=Chon4, bg="white", text="15",
                          value=2, font="null 10 bold", justify="center").pack()

        p43 = Radiobutton(elFrame, variable=Chon4, bg="white", text="11",
                          value=3, font="null 10 bold", justify="center").pack()

        p5 = Label(elFrame, text="\n5) ¿Qué significa Chon Ji?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p51 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Mar y Cielo",
                          value=1, font="null 10 bold", justify="center").pack()

        p52 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Tierra y Mente",
                          value=2, font="null 10 bold", justify="center").pack()

        p53 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Cielo y Tierra",
                          value=3, font="null 10 bold", justify="center").pack()

        p6 = Label(elFrame, text="\n6) ¿Qué forma tiene el diagrama?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p61 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Una cruz",
                          value=1, font="null 10 bold", justify="center").pack()

        p62 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Una hache",
                          value=2, font="null 10 bold", justify="center").pack()

        p63 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Una ele",
                          value=3, font="null 10 bold", justify="center").pack()

        p7 = Label(elFrame, text="\n7) ¿Qué posiciones hay en Chon Ji?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p71 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Niunja Sogui y Annun Sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p72 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Gunnun Sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p73 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Gunnun Sogui y Niunja Sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p8 = Label(elFrame, text="\n8) ¿A qué se debe la cantidad de movimientos?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p81 = Radiobutton(elFrame, variable=Chon8, bg="white", text="A la edad del General Choi",
                          value=1, font="null 10 bold", justify="center").pack()

        p82 = Radiobutton(elFrame, variable=Chon8, bg="white", text="A la latitud de Corea",
                          value=2, font="null 10 bold", justify="center").pack()

        p83 = Radiobutton(elFrame, variable=Chon8, bg="white", text="A la cantidad de grados en Taekwon-Do",
                          value=3, font="null 10 bold", justify="center").pack()

        p9 = Label(elFrame, text="\n9) ¿Dónde debe terminar la forma?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p91 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Depende de la altura de la persona",
                          value=1, font="null 10 bold", justify="center").pack()

        p92 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Un paso más adelante",
                          value=2, font="null 10 bold", justify="center").pack()

        p93 = Radiobutton(elFrame, variable=Chon9, bg="white", text="En el lugar de comienzo",
                          value=3, font="null 10 bold", justify="center").pack()

        p10 = Label(elFrame, text="\n10) ¿Qué movimiento se dirige a zona alta?\n",
                    bg="white", fg="blue", font=("null 14 bold")).pack()

        p101 = Radiobutton(elFrame, variable=Chon10, bg="white", text="El número 15",
                           value=1, font="null 10 bold", justify="center").pack()

        p102 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Ninguno",
                           value=2, font="null 10 bold", justify="center").pack()

        p103 = Radiobutton(elFrame, variable=Chon10, bg="white", text="El número 9",
                           value=3, font="null 10 bold", justify="center").pack()

        ResultadoP = Button(elFrame, text="RESULTADO",
                            command=Ya, font="null 25 bold").pack(pady=15)

        root1.update()

        c.config(scrollregion=c.bbox("all"))

        root1.mainloop()

# ----------------------DANGUN----------------------------------------


def Dangun():

    global Puntaje1
    global Intentos2
    Intentos2 = Intentos2+1
    if Intentos2 >= 2:
        messagebox.showinfo("Error", "Ya has realizado la trivia de Dangun")

    else:
        root1 = Toplevel()
        root1.resizable(1, 1)
        root1.geometry("650x600+400+25")
        root1.title("Trivia: Dangun")
        scrollbar = Scrollbar(root1)
        c = Canvas(root1, bg="white", yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        elFrame = Frame(c, bg="white", padx=10)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=elFrame, anchor="nw")

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                c.xview_scroll(scroll, "units")
            else:
                c.yview_scroll(scroll, "units")
        c.bind_all("<MouseWheel>", on_mousewheel)

        Chon1 = IntVar()
        Chon2 = IntVar()
        Chon3 = IntVar()
        Chon4 = IntVar()
        Chon5 = IntVar()
        Chon6 = IntVar()
        Chon7 = IntVar()
        Chon8 = IntVar()
        Chon9 = IntVar()
        Chon10 = IntVar()

        def Ya():
            global Count2
            if Chon1.get() == 1:
                Count2 = Count2+1

            if Chon2.get() == 1:
                Count2 = Count2+1

            if Chon3.get() == 2:
                Count2 = Count2+1

            if Chon4.get() == 3:
                Count2 = Count2+1

            if Chon5.get() == 3:
                Count2 = Count2+1

            if Chon6.get() == 3:
                Count2 = Count2+1

            if Chon7.get() == 3:
                Count2 = Count2+1

            if Chon8.get() == 1:
                Count2 = Count2+1

            if Chon9.get() == 3:
                Count2 = Count2+1

            if Chon10.get() == 3:
                Count2 = Count2+1

            messagebox.showinfo("Resultado", ("Tienes " + str(Count2) +
                                              "/10 respuestas correctas en la trivia sobre Dangun"))
            window.BotonDangun.config(
                text=("Dangun: " + str(Count2) + "/10"), font="null 12 bold")

            root1.destroy()

        p1 = Label(elFrame, text="1) ¿Cuantos movimientos tiene Dangun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p11 = Radiobutton(elFrame, variable=Chon1, bg="white", text="21",
                          value=1, font="null 10 bold", justify="center").pack()

        p12 = Radiobutton(elFrame, variable=Chon1, bg="white", text="19",
                          value=2, font="null 10 bold", justify="center").pack()

        p13 = Radiobutton(elFrame, variable=Chon1, bg="white", text="24",
                          value=3, font="null 10 bold", justify="center").pack()

        p2 = Label(elFrame, text="\n2) ¿A qué altura se dirigen los puños en Dangun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p21 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Alta",
                          value=1, font="null 10 bold", justify="center").pack()

        p22 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Media",
                          value=2, font="null 10 bold", justify="center").pack()

        p23 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Alta y media",
                          value=3, font="null 10 bold", justify="center").pack()

        p3 = Label(elFrame, text="\n3) ¿Con qué pierna se vuelve al inicio al finalizar?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p31 = Radiobutton(elFrame, variable=Chon3, bg="white", text="Con la pierna derecha",
                          value=1, font="null 10 bold", justify="center").pack()

        p32 = Radiobutton(elFrame, variable=Chon3, bg="white", text="Con la pierna izquierda",
                          value=2, font="null 10 bold", justify="center").pack()

        p33 = Radiobutton(elFrame, variable=Chon3, bg="white", text="Con cualquiera",
                          value=3, font="null 10 bold", justify="center").pack()

        p4 = Label(elFrame, text="\n4) ¿Quién era Dangun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p41 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Un militar con honor",
                          value=1, font="null 10 bold", justify="center").pack()

        p42 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Un maestro de Corea",
                          value=2, font="null 10 bold", justify="center").pack()

        p43 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Un santo legendario",
                          value=3, font="null 10 bold", justify="center").pack()

        p5 = Label(elFrame, text="\n5) ¿En que año se fundó Corea según el significado de Dangun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p51 = Radiobutton(elFrame, variable=Chon5, bg="white", text="3.222 a.C.",
                          value=1, font="null 10 bold", justify="center").pack()

        p52 = Radiobutton(elFrame, variable=Chon5, bg="white", text="2.323 a.C.",
                          value=2, font="null 10 bold", justify="center").pack()

        p53 = Radiobutton(elFrame, variable=Chon5, bg="white", text="2.333 a.C.",
                          value=3, font="null 10 bold", justify="center").pack()

        p6 = Label(elFrame, text="\n6) ¿Para cuántos oponentes es el movimiento número 9?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p61 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Ninguno",
                          value=1, font="null 10 bold", justify="center").pack()

        p62 = Radiobutton(elFrame, variable=Chon6, bg="white", text="1",
                          value=2, font="null 10 bold", justify="center").pack()

        p63 = Radiobutton(elFrame, variable=Chon6, bg="white", text="2",
                          value=3, font="null 10 bold", justify="center").pack()

        p7 = Label(elFrame, text="\n7) ¿Qué posiciones hay en Dangun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p71 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Niunja Sogui y Annun Sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p72 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Gunnun Sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p73 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Gunnun Sogui y Niunja Sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p8 = Label(elFrame, text="\n8) ¿En que moción se ejecutan los movimientos número 13 y 14?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p81 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Continua",
                          value=1, font="null 10 bold", justify="center").pack()

        p82 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Rápida",
                          value=2, font="null 10 bold", justify="center").pack()

        p83 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Normal",
                          value=3, font="null 10 bold", justify="center").pack()

        p9 = Label(elFrame, text="\n9) ¿En que moción se ejecuta el movimiento número 21?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p91 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Continua",
                          value=1, font="null 10 bold", justify="center").pack()

        p92 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Rápida",
                          value=2, font="null 10 bold", justify="center").pack()

        p93 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Normal",
                          value=3, font="null 10 bold", justify="center").pack()

        p10 = Label(elFrame, text="\n10) ¿Qué representa la altura de los puños en Dangun?\n",
                    bg="white", fg="blue", font=("null 14 bold")).pack()

        p101 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Elevar la energía",
                           value=1, font="null 10 bold", justify="center").pack()

        p102 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Elevar las técnicas",
                           value=2, font="null 10 bold", justify="center").pack()

        p103 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Subir la montaña",
                           value=3, font="null 10 bold", justify="center").pack()

        ResultadoP = Button(elFrame, text="RESULTADO",
                            command=Ya, font="null 25 bold").pack(pady=15)

        root1.update()

        c.config(scrollregion=c.bbox("all"))

        root1.mainloop()


# ----------------------DOSAN----------------------------------------

def Dosan():
    global Puntaje1
    global Intentos3
    Intentos3 = Intentos3+1
    if Intentos3 >= 2:
        messagebox.showinfo("Error", "Ya has realizado la trivia de Dosan")

    else:
        root1 = Toplevel()
        root1.resizable(0, 1)
        root1.geometry("710x500+400+25")
        root1.title("Trivia: Dosan")
        scrollbar = Scrollbar(root1)
        c = Canvas(root1, bg="white", yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        elFrame = Frame(c, bg="white", padx=10)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=elFrame, anchor="nw")

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                c.xview_scroll(scroll, "units")
            else:
                c.yview_scroll(scroll, "units")
        c.bind_all("<MouseWheel>", on_mousewheel)

        Chon1 = IntVar()
        Chon2 = IntVar()
        Chon3 = IntVar()
        Chon4 = IntVar()
        Chon5 = IntVar()
        Chon6 = IntVar()
        Chon7 = IntVar()
        Chon8 = IntVar()
        Chon9 = IntVar()
        Chon10 = IntVar()

        def Ya():
            global Count3
            if Chon1.get() == 2:
                Count3 = Count3+1

            if Chon3.get() == 3:
                Count3 = Count3+1

            if Chon3.get() == 2:
                Count3 = Count3+1

            if Chon4.get() == 2:
                Count3 = Count3+1

            if Chon5.get() == 1:
                Count3 = Count3+1

            if Chon6.get() == 1:
                Count3 = Count3+1

            if Chon7.get() == 3:
                Count3 = Count3+1

            if Chon8.get() == 2:
                Count3 = Count3+1

            if Chon9.get() == 1:
                Count3 = Count3+1

            if Chon10.get() == 1:
                Count3 = Count3+1

            messagebox.showinfo("Resultado", ("Tienes " + str(Count3) +
                                              "/10 respuestas correctas en la trivia sobre Dosan"))
            window.BotonDosan.config(
                text=("Dosan: " + str(Count3) + "/10"), font="null 12 bold")

            root1.destroy()

        p1 = Label(elFrame, text="1) ¿Cuantos movimientos tiene Dosan?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p11 = Radiobutton(elFrame, variable=Chon1, bg="white", text="21",
                          value=1, font="null 10 bold", justify="center").pack()

        p12 = Radiobutton(elFrame, variable=Chon1, bg="white", text="24",
                          value=2, font="null 10 bold", justify="center").pack()

        p13 = Radiobutton(elFrame, variable=Chon1, bg="white", text="28",
                          value=3, font="null 10 bold", justify="center").pack()

        p2 = Label(elFrame, text="\n2) ¿Qué mociones hay en Dosan?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p21 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Solo normal",
                          value=1, font="null 10 bold", justify="center").pack()

        p22 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Normal y Continua",
                          value=2, font="null 10 bold", justify="center").pack()

        p23 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Normal y Rápida",
                          value=3, font="null 10 bold", justify="center").pack()

        p3 = Label(elFrame, text="\n3) ¿Qué promovió Dosan?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p31 = Radiobutton(elFrame, variable=Chon3, bg="white", text="La guerra",
                          value=1, font="null 10 bold", justify="center").pack()

        p32 = Radiobutton(elFrame, variable=Chon3, bg="white", text="La educación",
                          value=2, font="null 10 bold", justify="center").pack()

        p33 = Radiobutton(elFrame, variable=Chon3, bg="white", text="El Taekwon-Do",
                          value=3, font="null 10 bold", justify="center").pack()

        p4 = Label(elFrame, text="\n4) ¿A que altura se ejecutan las patadas en Dosan?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p41 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona baja",
                          value=1, font="null 10 bold", justify="center").pack()

        p42 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona media",
                          value=2, font="null 10 bold", justify="center").pack()

        p43 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona alta",
                          value=3, font="null 10 bold", justify="center").pack()

        p5 = Label(elFrame, text="\n5) ¿Cuál era el nombre Dosan?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p51 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Ahn Chang Ho",
                          value=1, font="null 10 bold", justify="center").pack()

        p52 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Yi Wang",
                          value=2, font="null 10 bold", justify="center").pack()

        p53 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Yi Soon Sin",
                          value=3, font="null 10 bold", justify="center").pack()

        p6 = Label(elFrame, text="\n6) ¿Qué representa la cantidad de movimientos de Dosan?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p61 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Su vida",
                          value=1, font="null 10 bold", justify="center").pack()

        p62 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Su muerte",
                          value=2, font="null 10 bold", justify="center").pack()

        p63 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Su nacimiento",
                          value=3, font="null 10 bold", justify="center").pack()

        p7 = Label(elFrame, text="\n7) ¿Cuántas Niunja Sogui aparecen en Dosan?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p71 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Ninguna",
                          value=1, font="null 10 bold", justify="center").pack()

        p72 = Radiobutton(elFrame, variable=Chon7, bg="white", text="3",
                          value=2, font="null 10 bold", justify="center").pack()

        p73 = Radiobutton(elFrame, variable=Chon7, bg="white", text="1",
                          value=3, font="null 10 bold", justify="center").pack()

        p8 = Label(elFrame, text="\n8) ¿En que se diferencia el movimiento número 3 y el número 7?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p81 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Son los mismos",
                          value=1, font="null 10 bold", justify="center").pack()

        p82 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Uno es un ataque y otro una defensa",
                          value=2, font="null 10 bold", justify="center").pack()

        p83 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Uno es a zona media y otro a zona alta",
                          value=3, font="null 10 bold", justify="center").pack()

        p9 = Label(elFrame, text="\n9) ¿En que posición se realizan los golpes con canto de mano en Dosan?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p91 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Annun Sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p92 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Niunja Sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p93 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Gunnun Sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p10 = Label(elFrame, text="\n10) ¿Con que pierna vuelvo a la posición inicial?\n",
                    bg="white", fg="blue", font=("null 14 bold")).pack()

        p101 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Derecha",
                           value=1, font="null 10 bold", justify="center").pack()

        p102 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Izquierda",
                           value=2, font="null 10 bold", justify="center").pack()

        p103 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Cualquiera",
                           value=3, font="null 10 bold", justify="center").pack()

        ResultadoP = Button(elFrame, text="RESULTADO",
                            command=Ya, font="null 25 bold").pack(pady=15)

        root1.update()

        c.config(scrollregion=c.bbox("all"))

        root1.mainloop()

# ----------------------WONHYO----------------------------------------


def Wonhyo():
    global Puntaje1
    global Intentos4
    Intentos4 = Intentos4+1
    if Intentos4 >= 2:
        messagebox.showinfo("Error", "Ya has realizado la trivia de Won Hyo")

    else:
        root1 = Toplevel()
        root1.resizable(0, 1)
        root1.geometry("650x500+400+25")
        root1.title("Trivia: Won Hyo")
        scrollbar = Scrollbar(root1)
        c = Canvas(root1, bg="white", yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        elFrame = Frame(c, bg="white", padx=10)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=elFrame, anchor="nw")

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                c.xview_scroll(scroll, "units")
            else:
                c.yview_scroll(scroll, "units")
        c.bind_all("<MouseWheel>", on_mousewheel)

        Chon1 = IntVar()
        Chon2 = IntVar()
        Chon3 = IntVar()
        Chon4 = IntVar()
        Chon5 = IntVar()
        Chon6 = IntVar()
        Chon7 = IntVar()
        Chon8 = IntVar()
        Chon9 = IntVar()
        Chon10 = IntVar()

        def Ya():
            global Count4
            if Chon1.get() == 3:
                Count4 = Count4+1

            if Chon2.get() == 1:
                Count4 = Count4+1

            if Chon3.get() == 3:
                Count4 = Count4+1

            if Chon4.get() == 1:
                Count4 = Count4+1

            if Chon5.get() == 2:
                Count4 = Count4+1

            if Chon6.get() == 1:
                Count4 = Count4+1

            if Chon7.get() == 1:
                Count4 = Count4+1

            if Chon8.get() == 3:
                Count4 = Count4+1

            if Chon9.get() == 3:
                Count4 = Count4+1

            if Chon10.get() == 1:
                Count4 = Count4+1

            messagebox.showinfo("Resultado", ("Tienes " + str(Count4) +
                                              "/10 respuestas correctas en la trivia sobre Won hyo"))
            window.BotonWonhyo.config(
                text=("Won Hyo: " + str(Count4) + "/10"), font="null 12 bold")

            root1.destroy()

        p1 = Label(elFrame, text="1) ¿Cuantos movimientos tiene Won Hyo?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p11 = Radiobutton(elFrame, variable=Chon1, bg="white", text="21",
                          value=1, font="null 10 bold", justify="center").pack()

        p12 = Radiobutton(elFrame, variable=Chon1, bg="white", text="24",
                          value=2, font="null 10 bold", justify="center").pack()

        p13 = Radiobutton(elFrame, variable=Chon1, bg="white", text="28",
                          value=3, font="null 10 bold", justify="center").pack()

        p2 = Label(elFrame, text="\n2) ¿Qué mociones hay en Won Hyo?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p21 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Solo normal",
                          value=1, font="null 10 bold", justify="center").pack()

        p22 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Normal y Continua",
                          value=2, font="null 10 bold", justify="center").pack()

        p23 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Normal y Rápida",
                          value=3, font="null 10 bold", justify="center").pack()

        p3 = Label(elFrame, text="\n3) ¿En que se destacó Won Hyo?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p31 = Radiobutton(elFrame, variable=Chon3, bg="white", text="La guerra",
                          value=1, font="null 10 bold", justify="center").pack()

        p32 = Radiobutton(elFrame, variable=Chon3, bg="white", text="Las artes marciales",
                          value=2, font="null 10 bold", justify="center").pack()

        p33 = Radiobutton(elFrame, variable=Chon3, bg="white", text="El budismo",
                          value=3, font="null 10 bold", justify="center").pack()

        p4 = Label(elFrame, text="\n4) ¿A que altura se ejecutan las patadas frontales en Won Hyo?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p41 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona baja",
                          value=1, font="null 10 bold", justify="center").pack()

        p42 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona media",
                          value=2, font="null 10 bold", justify="center").pack()

        p43 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona alta",
                          value=3, font="null 10 bold", justify="center").pack()

        p5 = Label(elFrame, text="\n5) ¿A qué altura se ejecutan las patadas laterales?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p51 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona alta",
                          value=1, font="null 10 bold", justify="center").pack()

        p52 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona media",
                          value=2, font="null 10 bold", justify="center").pack()

        p53 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona baja",
                          value=3, font="null 10 bold", justify="center").pack()

        p6 = Label(elFrame, text="\n6) ¿Como se llama la posicón de inicio?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p61 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Moa sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p62 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Narani sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p63 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Goburyo sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p7 = Label(elFrame, text="\n7) ¿Cuál de estas posiciones no aparece en Won Hyo?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p71 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Annun sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p72 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Gojung sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p73 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Goburyo sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p8 = Label(elFrame, text="\n8) ¿Cuál de estas posiciones es mas larga?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p81 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Niunja sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p82 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Narani sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p83 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Gojung sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p9 = Label(elFrame, text="\n9) ¿Cómo se reparte el peso en Goburyo sogui?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p91 = Radiobutton(elFrame, variable=Chon9, bg="white", text="La mitad en cada pierna",
                          value=1, font="null 10 bold", justify="center").pack()

        p92 = Radiobutton(elFrame, variable=Chon9, bg="white", text="La mayor parte del peso en la pierna de atrás",
                          value=2, font="null 10 bold", justify="center").pack()

        p93 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Todo el peso en una pierna",
                          value=3, font="null 10 bold", justify="center").pack()

        p10 = Label(elFrame, text="\n10) ¿Con que pierna vuelvo a la posición inicial?\n",
                    bg="white", fg="blue", font=("null 14 bold")).pack()

        p101 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Derecha",
                           value=1, font="null 10 bold", justify="center").pack()

        p102 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Izquierda",
                           value=2, font="null 10 bold", justify="center").pack()

        p103 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Cualquiera",
                           value=3, font="null 10 bold", justify="center").pack()

        ResultadoP = Button(elFrame, text="RESULTADO",
                            command=Ya, font="null 25 bold").pack(pady=15)

        root1.update()

        c.config(scrollregion=c.bbox("all"))

        root1.mainloop()

# ----------------------YULGOK----------------------------------------


def Yulgok():
    global Puntaje1
    global Intentos5
    Intentos5 = Intentos5+1
    if Intentos5 >= 2:
        messagebox.showinfo("Error", "Ya has realizado la trivia de Yulgok")

    else:
        root1 = Toplevel()
        root1.resizable(0, 1)
        root1.geometry("650x500+400+25")
        root1.title("Trivia: Yulgok")
        scrollbar = Scrollbar(root1)
        c = Canvas(root1, bg="white", yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        elFrame = Frame(c, bg="white", padx=10)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=elFrame, anchor="nw")

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                c.xview_scroll(scroll, "units")
            else:
                c.yview_scroll(scroll, "units")
        c.bind_all("<MouseWheel>", on_mousewheel)

        Chon1 = IntVar()
        Chon2 = IntVar()
        Chon3 = IntVar()
        Chon4 = IntVar()
        Chon5 = IntVar()
        Chon6 = IntVar()
        Chon7 = IntVar()
        Chon8 = IntVar()
        Chon9 = IntVar()
        Chon10 = IntVar()

        def Ya():
            global Count5
            if Chon1.get() == 3:
                Count5 = Count5+1

            if Chon2.get() == 3:
                Count5 = Count5+1

            if Chon3.get() == 2:
                Count5 = Count5+1

            if Chon4.get() == 1:
                Count5 = Count5+1

            if Chon5.get() == 2:
                Count5 = Count5+1

            if Chon6.get() == 3:
                Count5 = Count5+1

            if Chon7.get() == 1:
                Count5 = Count5+1

            if Chon8.get() == 3:
                Count5 = Count5+1

            if Chon9.get() == 1:
                Count5 = Count5+1

            if Chon10.get() == 1:
                Count5 = Count5+1

            messagebox.showinfo("Resultado", ("Tienes " + str(Count5) +
                                              "/10 respuestas correctas en la trivia sobre Yulgok"))
            window.BotonYulgok.config(
                text=("Yulgok: " + str(Count5) + "/10"), font="null 12 bold")

            root1.destroy()

        p1 = Label(elFrame, text="1) ¿Cuantos movimientos tiene Yulgok?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p11 = Radiobutton(elFrame, variable=Chon1, bg="white", text="32",
                          value=1, font="null 10 bold", justify="center").pack()

        p12 = Radiobutton(elFrame, variable=Chon1, bg="white", text="28",
                          value=2, font="null 10 bold", justify="center").pack()

        p13 = Radiobutton(elFrame, variable=Chon1, bg="white", text="38",
                          value=3, font="null 10 bold", justify="center").pack()

        p2 = Label(elFrame, text="\n2) ¿En que moción se ejecutan los movimientos 2 y 3?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p21 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Normal",
                          value=1, font="null 10 bold", justify="center").pack()

        p22 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Continua",
                          value=2, font="null 10 bold", justify="center").pack()

        p23 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Rápida",
                          value=3, font="null 10 bold", justify="center").pack()

        p3 = Label(elFrame, text="\n3) ¿En que se destacó Yulgok?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p31 = Radiobutton(elFrame, variable=Chon3, bg="white", text="El budismo",
                          value=1, font="null 10 bold", justify="center").pack()

        p32 = Radiobutton(elFrame, variable=Chon3, bg="white", text="La filosofía",
                          value=2, font="null 10 bold", justify="center").pack()

        p33 = Radiobutton(elFrame, variable=Chon3, bg="white", text="El Taekwon-Do",
                          value=3, font="null 10 bold", justify="center").pack()

        p4 = Label(elFrame, text="\n4) ¿A que altura se ejecutan las patadas frontales en Yulgok?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p41 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona baja",
                          value=1, font="null 10 bold", justify="center").pack()

        p42 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona media",
                          value=2, font="null 10 bold", justify="center").pack()

        p43 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona alta",
                          value=3, font="null 10 bold", justify="center").pack()

        p5 = Label(elFrame, text="\n5) ¿A qué altura se ejecutan las patadas laterales?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p51 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona alta",
                          value=1, font="null 10 bold", justify="center").pack()

        p52 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona media",
                          value=2, font="null 10 bold", justify="center").pack()

        p53 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona baja",
                          value=3, font="null 10 bold", justify="center").pack()

        p6 = Label(elFrame, text="\n6) ¿Como se llamaba Yulgok?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p61 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Ahn",
                          value=1, font="null 10 bold", justify="center").pack()

        p62 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Choi",
                          value=2, font="null 10 bold", justify="center").pack()

        p63 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Yi",
                          value=3, font="null 10 bold", justify="center").pack()

        p7 = Label(elFrame, text="\n7) ¿Qué representa la cantidad de movimientos de Yulgok?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p71 = Radiobutton(elFrame, variable=Chon7, bg="white", text="El lugar de nacimiento de Yulgok",
                          value=1, font="null 10 bold", justify="center").pack()

        p72 = Radiobutton(elFrame, variable=Chon7, bg="white", text="La edad de Yulgok",
                          value=2, font="null 10 bold", justify="center").pack()

        p73 = Radiobutton(elFrame, variable=Chon7, bg="white", text="El lugar donde estudió Yulgok",
                          value=3, font="null 10 bold", justify="center").pack()

        p8 = Label(elFrame, text="\n8) ¿Como se llama la posición del movimiento número 36?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p81 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Waebal sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p82 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Sojik sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p83 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Kiocha sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p9 = Label(elFrame, text="\n9) ¿Qué es el movimiento número 36?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p91 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Un ataque",
                          value=1, font="null 10 bold", justify="center").pack()

        p92 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Una defensa",
                          value=2, font="null 10 bold", justify="center").pack()

        p93 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Ambas",
                          value=3, font="null 10 bold", justify="center").pack()

        p10 = Label(elFrame, text="\n10) ¿Con que pierna vuelvo a la posición inicial?\n",
                    bg="white", fg="blue", font=("null 14 bold")).pack()

        p101 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Derecha",
                           value=1, font="null 10 bold", justify="center").pack()

        p102 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Izquierda",
                           value=2, font="null 10 bold", justify="center").pack()

        p103 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Cualquiera",
                           value=3, font="null 10 bold", justify="center").pack()

        ResultadoP = Button(elFrame, text="RESULTADO",
                            command=Ya, font="null 25 bold").pack(pady=15)

        root1.update()

        c.config(scrollregion=c.bbox("all"))

        root1.mainloop()

# ----------------------JOON GUN----------------------------------------


def JoonGun():
    global Puntaje1
    global Intentos6
    Intentos6 = Intentos6+1
    if Intentos6 >= 2:
        messagebox.showinfo("Error", "Ya has realizado la trivia de Joon Gun")

    else:
        root1 = Toplevel()
        root1.resizable(0, 1)
        root1.geometry("650x500+400+25")
        root1.title("Trivia: Joon Gun")
        scrollbar = Scrollbar(root1)
        c = Canvas(root1, bg="white", yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        elFrame = Frame(c, bg="white", padx=10)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=elFrame, anchor="nw")

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                c.xview_scroll(scroll, "units")
            else:
                c.yview_scroll(scroll, "units")
        c.bind_all("<MouseWheel>", on_mousewheel)

        Chon1 = IntVar()
        Chon2 = IntVar()
        Chon3 = IntVar()
        Chon4 = IntVar()
        Chon5 = IntVar()
        Chon6 = IntVar()
        Chon7 = IntVar()
        Chon8 = IntVar()
        Chon9 = IntVar()
        Chon10 = IntVar()

        def Ya():
            global Count6
            if Chon1.get() == 1:
                Count6 = Count6+1

            if Chon2.get() == 3:
                Count6 = Count6+1

            if Chon3.get() == 1:
                Count6 = Count6+1

            if Chon4.get() == 1:
                Count6 = Count6+1

            if Chon5.get() == 2:
                Count6 = Count6+1

            if Chon6.get() == 1:
                Count6 = Count6+1

            if Chon7.get() == 2:
                Count6 = Count6+1

            if Chon8.get() == 2:
                Count6 = Count6+1

            if Chon9.get() == 2:
                Count6 = Count6+1

            if Chon10.get() == 2:
                Count6 = Count6+1

            messagebox.showinfo("Resultado", ("Tienes " + str(Count6) +
                                              "/10 respuestas correctas en la trivia sobre Joon Gun"))
            window.BotonJoonGun.config(
                text=("Joon Gun: " + str(Count6) + "/10"), font="null 12 bold")

            root1.destroy()

        p1 = Label(elFrame, text="1) ¿Cuantos movimientos tiene Joon Gun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p11 = Radiobutton(elFrame, variable=Chon1, bg="white", text="32",
                          value=1, font="null 10 bold", justify="center").pack()

        p12 = Radiobutton(elFrame, variable=Chon1, bg="white", text="28",
                          value=2, font="null 10 bold", justify="center").pack()

        p13 = Radiobutton(elFrame, variable=Chon1, bg="white", text="38",
                          value=3, font="null 10 bold", justify="center").pack()

        p2 = Label(elFrame, text="\n2) ¿En que moción se ejecutan los movimientos 15 y 16?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p21 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Normal",
                          value=1, font="null 10 bold", justify="center").pack()

        p22 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Continua",
                          value=2, font="null 10 bold", justify="center").pack()

        p23 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Rápida",
                          value=3, font="null 10 bold", justify="center").pack()

        p3 = Label(elFrame, text="\n3) ¿En que año murió Joon Gun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p31 = Radiobutton(elFrame, variable=Chon3, bg="white", text="1910",
                          value=1, font="null 10 bold", justify="center").pack()

        p32 = Radiobutton(elFrame, variable=Chon3, bg="white", text="1901",
                          value=2, font="null 10 bold", justify="center").pack()

        p33 = Radiobutton(elFrame, variable=Chon3, bg="white", text="1932",
                          value=3, font="null 10 bold", justify="center").pack()

        p4 = Label(elFrame, text="\n4) ¿A que altura se ejecutan las patadas frontales en Joon Gun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p41 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona baja",
                          value=1, font="null 10 bold", justify="center").pack()

        p42 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona media",
                          value=2, font="null 10 bold", justify="center").pack()

        p43 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona alta",
                          value=3, font="null 10 bold", justify="center").pack()

        p5 = Label(elFrame, text="\n5) ¿A qué altura se ejecutan las patadas laterales?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p51 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona alta",
                          value=1, font="null 10 bold", justify="center").pack()

        p52 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona media",
                          value=2, font="null 10 bold", justify="center").pack()

        p53 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona baja",
                          value=3, font="null 10 bold", justify="center").pack()

        p6 = Label(elFrame, text="\n6) ¿Como se llamaba Joon Gun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p61 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Ahn",
                          value=1, font="null 10 bold", justify="center").pack()

        p62 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Choi",
                          value=2, font="null 10 bold", justify="center").pack()

        p63 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Yi",
                          value=3, font="null 10 bold", justify="center").pack()

        p7 = Label(elFrame, text="\n7) ¿Qué representa la cantidad de movimientos de Joon Gun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p71 = Radiobutton(elFrame, variable=Chon7, bg="white", text="El lugar de nacimiento de Joon Gun",
                          value=1, font="null 10 bold", justify="center").pack()

        p72 = Radiobutton(elFrame, variable=Chon7, bg="white", text="La edad de Joon Gun",
                          value=2, font="null 10 bold", justify="center").pack()

        p73 = Radiobutton(elFrame, variable=Chon7, bg="white", text="El lugar donde estudió Joon Gun",
                          value=3, font="null 10 bold", justify="center").pack()

        p8 = Label(elFrame, text="\n8) ¿Como se llama la posición del movimiento número 29?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p81 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Gojung sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p82 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Nachuo sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p83 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Kiocha sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p9 = Label(elFrame, text="\n9) ¿Que mociones hay en Joon Gun?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p91 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Normal, lenta y continua",
                          value=1, font="null 10 bold", justify="center").pack()

        p92 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Normal, rápida y lenta",
                          value=2, font="null 10 bold", justify="center").pack()

        p93 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Normal, lenta y conectada",
                          value=3, font="null 10 bold", justify="center").pack()

        p10 = Label(elFrame, text="\n10) ¿Con que pierna vuelvo a la posición inicial?\n",
                    bg="white", fg="blue", font=("null 14 bold")).pack()

        p101 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Derecha",
                           value=1, font="null 10 bold", justify="center").pack()

        p102 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Izquierda",
                           value=2, font="null 10 bold", justify="center").pack()

        p103 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Cualquiera",
                           value=3, font="null 10 bold", justify="center").pack()

        ResultadoP = Button(elFrame, text="RESULTADO",
                            command=Ya, font="null 25 bold").pack(pady=15)

        root1.update()

        c.config(scrollregion=c.bbox("all"))

        root1.mainloop()


# ----------------------TOI GYE----------------------------------------

def ToiGye():
    global Puntaje1
    global Intentos7
    Intentos7 = Intentos7+1
    if Intentos7 >= 2:
        messagebox.showinfo("Error", "Ya has realizado la trivia de Toi Gye")

    else:
        root1 = Toplevel()
        root1.resizable(0, 1)
        root1.geometry("650x500+400+25")
        root1.title("Trivia: Toi Gye")
        scrollbar = Scrollbar(root1)
        c = Canvas(root1, bg="white", yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        elFrame = Frame(c, bg="white", padx=10)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=elFrame, anchor="nw")

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                c.xview_scroll(scroll, "units")
            else:
                c.yview_scroll(scroll, "units")
        c.bind_all("<MouseWheel>", on_mousewheel)

        Chon1 = IntVar()
        Chon2 = IntVar()
        Chon3 = IntVar()
        Chon4 = IntVar()
        Chon5 = IntVar()
        Chon6 = IntVar()
        Chon7 = IntVar()
        Chon8 = IntVar()
        Chon9 = IntVar()
        Chon10 = IntVar()

        def Ya():
            global Count7
            if Chon1.get() == 2:
                Count7 = Count7+1

            if Chon2.get() == 2:
                Count7 = Count7+1

            if Chon3.get() == 1:
                Count7 = Count7+1

            if Chon4.get() == 1:
                Count7 = Count7+1

            if Chon5.get() == 2:
                Count7 = Count7+1

            if Chon6.get() == 1:
                Count7 = Count7+1

            if Chon7.get() == 1:
                Count7 = Count7+1

            if Chon8.get() == 3:
                Count7 = Count7+1

            if Chon9.get() == 3:
                Count7 = Count7+1

            if Chon10.get() == 1:
                Count7 = Count7+1

            messagebox.showinfo("Resultado", ("Tienes " + str(Count7) +
                                              "/10 respuestas correctas en la trivia sobre Toi Gye"))
            window.BotonToiGye.config(
                text=("Toi Gye: " + str(Count7) + "/10"), font="null 12 bold")

            root1.destroy()

        p1 = Label(elFrame, text="1) ¿Cuantos movimientos tiene Toi Gye?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p11 = Radiobutton(elFrame, variable=Chon1, bg="white", text="36",
                          value=1, font="null 10 bold", justify="center").pack()

        p12 = Radiobutton(elFrame, variable=Chon1, bg="white", text="37",
                          value=2, font="null 10 bold", justify="center").pack()

        p13 = Radiobutton(elFrame, variable=Chon1, bg="white", text="38",
                          value=3, font="null 10 bold", justify="center").pack()

        p2 = Label(elFrame, text="\n2) ¿En que moción se ejecutan los movimientos 7 y 8?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p21 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Normal",
                          value=1, font="null 10 bold", justify="center").pack()

        p22 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Continua",
                          value=2, font="null 10 bold", justify="center").pack()

        p23 = Radiobutton(elFrame, variable=Chon2, bg="white", text="Rápida",
                          value=3, font="null 10 bold", justify="center").pack()

        p3 = Label(elFrame, text="\n3) ¿En que se destacó Toi Gye?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p31 = Radiobutton(elFrame, variable=Chon3, bg="white", text="En el neo confusionismo",
                          value=1, font="null 10 bold", justify="center").pack()

        p32 = Radiobutton(elFrame, variable=Chon3, bg="white", text="En el neo budismo",
                          value=2, font="null 10 bold", justify="center").pack()

        p33 = Radiobutton(elFrame, variable=Chon3, bg="white", text="En el neo existensialismo",
                          value=3, font="null 10 bold", justify="center").pack()

        p4 = Label(elFrame, text="\n4) ¿A que altura se ejecutan las patadas frontales en Toi Gye?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p41 = Radiobutton(elFrame, variable=Chon4, bg="white", text="La primera a zona media y las otras dos bajas",
                          value=1, font="null 10 bold", justify="center").pack()

        p42 = Radiobutton(elFrame, variable=Chon4, bg="white", text="La primera a zona baja y las otras dos medias",
                          value=2, font="null 10 bold", justify="center").pack()

        p43 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Todas zona media",
                          value=3, font="null 10 bold", justify="center").pack()

        p5 = Label(elFrame, text="\n5) ¿A dónde golpea la rodilla?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p51 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona alta",
                          value=1, font="null 10 bold", justify="center").pack()

        p52 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona media",
                          value=2, font="null 10 bold", justify="center").pack()

        p53 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Zona baja",
                          value=3, font="null 10 bold", justify="center").pack()

        p6 = Label(elFrame, text="\n6) ¿Como se llamaba Toi Gye?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p61 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Yi Hwang",
                          value=1, font="null 10 bold", justify="center").pack()

        p62 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Choi Hong Hi",
                          value=2, font="null 10 bold", justify="center").pack()

        p63 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Ahn Chang Ho",
                          value=3, font="null 10 bold", justify="center").pack()

        p7 = Label(elFrame, text="\n7) ¿Qué representa la cantidad de movimientos de Toi Gye?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p71 = Radiobutton(elFrame, variable=Chon7, bg="white", text="El lugar de nacimiento de Toi Gye",
                          value=1, font="null 10 bold", justify="center").pack()

        p72 = Radiobutton(elFrame, variable=Chon7, bg="white", text="La edad de Toi Gye",
                          value=2, font="null 10 bold", justify="center").pack()

        p73 = Radiobutton(elFrame, variable=Chon7, bg="white", text="El lugar donde estudió Toi Gye",
                          value=3, font="null 10 bold", justify="center").pack()

        p8 = Label(elFrame, text="\n8) ¿Cuántos movimientos llevan stamping?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p81 = Radiobutton(elFrame, variable=Chon8, bg="white", text="4",
                          value=1, font="null 10 bold", justify="center").pack()

        p82 = Radiobutton(elFrame, variable=Chon8, bg="white", text="5",
                          value=2, font="null 10 bold", justify="center").pack()

        p83 = Radiobutton(elFrame, variable=Chon8, bg="white", text="6",
                          value=3, font="null 10 bold", justify="center").pack()

        p9 = Label(elFrame, text="\n9) ¿Que mociones hay en Toi Gye?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p91 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Normal, lenta, continua y rápida",
                          value=1, font="null 10 bold", justify="center").pack()

        p92 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Normal, rápida y lenta",
                          value=2, font="null 10 bold", justify="center").pack()

        p93 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Normal, lenta y continua",
                          value=3, font="null 10 bold", justify="center").pack()

        p10 = Label(elFrame, text="\n10) ¿Con que pierna vuelvo a la posición inicial?\n",
                    bg="white", fg="blue", font=("null 14 bold")).pack()

        p101 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Derecha",
                           value=1, font="null 10 bold", justify="center").pack()

        p102 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Izquierda",
                           value=2, font="null 10 bold", justify="center").pack()

        p103 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Cualquiera",
                           value=3, font="null 10 bold", justify="center").pack()

        ResultadoP = Button(elFrame, text="RESULTADO",
                            command=Ya, font="null 25 bold").pack(pady=15)

        root1.update()

        c.config(scrollregion=c.bbox("all"))

        root1.mainloop()

# ----------------------HWARANG----------------------------------------


def Hwarang():
    global Puntaje1
    global Intentos8
    Intentos8 = Intentos8+1
    if Intentos8 >= 2:
        messagebox.showinfo("Error", "Ya has realizado la trivia de Hwarang")

    else:
        root1 = Toplevel()
        root1.resizable(0, 1)
        root1.geometry("650x500+400+25")
        root1.title("Trivia: Hwarang")
        scrollbar = Scrollbar(root1)
        c = Canvas(root1, bg="white", yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        elFrame = Frame(c, bg="white", padx=10)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=elFrame, anchor="nw")

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                c.xview_scroll(scroll, "units")
            else:
                c.yview_scroll(scroll, "units")
        c.bind_all("<MouseWheel>", on_mousewheel)

        Chon1 = IntVar()
        Chon2 = IntVar()
        Chon3 = IntVar()
        Chon4 = IntVar()
        Chon5 = IntVar()
        Chon6 = IntVar()
        Chon7 = IntVar()
        Chon8 = IntVar()
        Chon9 = IntVar()
        Chon10 = IntVar()

        def Ya():
            global Count8
            if Chon1.get() == 1:
                Count8 = Count8+1

            if Chon2.get() == 1:
                Count8 = Count8+1

            if Chon3.get() == 2:
                Count8 = Count8+1

            if Chon4.get() == 2:
                Count8 = Count8+1

            if Chon5.get() == 3:
                Count8 = Count8+1

            if Chon6.get() == 1:
                Count8 = Count8+1

            if Chon7.get() == 1:
                Count8 = Count8+1

            if Chon8.get() == 1:
                Count8 = Count8+1

            if Chon9.get() == 2:
                Count8 = Count8+1

            if Chon10.get() == 1:
                Count8 = Count8+1

            messagebox.showinfo("Resultado", ("Tienes " + str(Count8) +
                                              "/10 respuestas correctas en la trivia sobre Hwarang"))
            window.BotonHwarang.config(
                text=("Hwarang: " + str(Count8) + "/10"), font="null 12 bold")

            root1.destroy()

        p1 = Label(elFrame, text="1) ¿Cuantos movimientos tiene Hwarang?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p11 = Radiobutton(elFrame, variable=Chon1, bg="white", text="29",
                          value=1, font="null 10 bold", justify="center").pack()

        p12 = Radiobutton(elFrame, variable=Chon1, bg="white", text="30",
                          value=2, font="null 10 bold", justify="center").pack()

        p13 = Radiobutton(elFrame, variable=Chon1, bg="white", text="31",
                          value=3, font="null 10 bold", justify="center").pack()

        p2 = Label(elFrame, text="\n2) ¿Cuántas patadas tiene esta forma?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p21 = Radiobutton(elFrame, variable=Chon2, bg="white", text="2",
                          value=1, font="null 10 bold", justify="center").pack()

        p22 = Radiobutton(elFrame, variable=Chon2, bg="white", text="3",
                          value=2, font="null 10 bold", justify="center").pack()

        p23 = Radiobutton(elFrame, variable=Chon2, bg="white", text="4",
                          value=3, font="null 10 bold", justify="center").pack()

        p3 = Label(elFrame, text="\n3) ¿Cuántas técnicas se ejecutan en Annun Sogui?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p31 = Radiobutton(elFrame, variable=Chon3, bg="white", text="2",
                          value=1, font="null 10 bold", justify="center").pack()

        p32 = Radiobutton(elFrame, variable=Chon3, bg="white", text="3",
                          value=2, font="null 10 bold", justify="center").pack()

        p33 = Radiobutton(elFrame, variable=Chon3, bg="white", text="4",
                          value=3, font="null 10 bold", justify="center").pack()

        p4 = Label(elFrame, text="\n4) ¿A que altura se ejecutan las patadas circulares en Hwarang?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p41 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona media",
                          value=1, font="null 10 bold", justify="center").pack()

        p42 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Zona alta",
                          value=2, font="null 10 bold", justify="center").pack()

        p43 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Una zona media y otra zona alta",
                          value=3, font="null 10 bold", justify="center").pack()

        p5 = Label(elFrame, text="\n5) ¿Cuál es la herramienta de ataque de las patadas circulares?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p51 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Empeine",
                          value=1, font="null 10 bold", justify="center").pack()

        p52 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Dedos",
                          value=2, font="null 10 bold", justify="center").pack()

        p53 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Metatarso",
                          value=3, font="null 10 bold", justify="center").pack()

        p6 = Label(elFrame, text="\n6) ¿Como se llama la posición nueva que aparece en esta forma?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p61 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Soojik sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p62 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Sasun sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p63 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Waebal sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p7 = Label(elFrame, text="\n7) ¿Qué eran los Hwarang?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p71 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Guerreros",
                          value=1, font="null 10 bold", justify="center").pack()

        p72 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Reyes",
                          value=2, font="null 10 bold", justify="center").pack()

        p73 = Radiobutton(elFrame, variable=Chon7, bg="white", text="Maestros",
                          value=3, font="null 10 bold", justify="center").pack()

        p8 = Label(elFrame, text="\n8) ¿A qué se debe la cantidad de movimientos de la forma?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p81 = Radiobutton(elFrame, variable=Chon8, bg="white", text="El número de un batallón de infantería",
                          value=1, font="null 10 bold", justify="center").pack()

        p82 = Radiobutton(elFrame, variable=Chon8, bg="white", text="El número total de los Hwarang",
                          value=2, font="null 10 bold", justify="center").pack()

        p83 = Radiobutton(elFrame, variable=Chon8, bg="white", text="El número total de posiciones",
                          value=3, font="null 10 bold", justify="center").pack()

        p9 = Label(elFrame, text="\n9) ¿Qué posición no aparece en Hwarang?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p91 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Moa sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p92 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Nachuo sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p93 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Gojung sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p10 = Label(elFrame, text="\n10) ¿Con que pierna vuelvo a la posición inicial?\n",
                    bg="white", fg="blue", font=("null 14 bold")).pack()

        p101 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Derecha",
                           value=1, font="null 10 bold", justify="center").pack()

        p102 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Izquierda",
                           value=2, font="null 10 bold", justify="center").pack()

        p103 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Cualquiera",
                           value=3, font="null 10 bold", justify="center").pack()

        ResultadoP = Button(elFrame, text="RESULTADO",
                            command=Ya, font="null 25 bold").pack(pady=15)

        root1.update()

        c.config(scrollregion=c.bbox("all"))

        root1.mainloop()

# ----------------------CHOONG MOO----------------------------------------


def ChoongMoo():
    global Puntaje1
    global Intentos9
    Intentos9 = Intentos9+1
    if Intentos9 >= 2:
        messagebox.showinfo(
            "Error", "Ya has realizado la trivia de Choong Moo")

    else:
        root1 = Toplevel()
        root1.resizable(0, 1)
        root1.geometry("520x500+400+25")
        root1.title("Trivia: Choong Moo")
        scrollbar = Scrollbar(root1)
        c = Canvas(root1, bg="white", yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        elFrame = Frame(c, bg="white", padx=10)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=elFrame, anchor="nw")

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                c.xview_scroll(scroll, "units")
            else:
                c.yview_scroll(scroll, "units")
        c.bind_all("<MouseWheel>", on_mousewheel)

        Chon1 = IntVar()
        Chon2 = IntVar()
        Chon3 = IntVar()
        Chon4 = IntVar()
        Chon5 = IntVar()
        Chon6 = IntVar()
        Chon7 = IntVar()
        Chon8 = IntVar()
        Chon9 = IntVar()
        Chon10 = IntVar()

        def Ya():
            global Count9
            if Chon1.get() == 2:
                Count9 = Count9+1

            if Chon2.get() == 3:
                Count9 = Count9+1

            if Chon3.get() == 1:
                Count9 = Count9+1

            if Chon4.get() == 2:
                Count9 = Count9+1

            if Chon5.get() == 3:
                Count9 = Count9+1

            if Chon6.get() == 3:
                Count9 = Count9+1

            if Chon7.get() == 3:
                Count9 = Count9+1

            if Chon8.get() == 2:
                Count9 = Count9+1

            if Chon9.get() == 2:
                Count9 = Count9+1

            if Chon10.get() == 2:
                Count9 = Count9+1

            messagebox.showinfo("Resultado", ("Tienes " + str(Count9) +
                                              "/10 respuestas correctas en la trivia sobre Choong Moo"))
            window.BotonChoongMoo.config(
                text=("Choong Moo: " + str(Count9) + "/10"), font="null 12 bold")

            root1.destroy()

        p1 = Label(elFrame, text="1) ¿Cuantos movimientos tiene Choong Moo?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p11 = Radiobutton(elFrame, variable=Chon1, bg="white", text="29",
                          value=1, font="null 10 bold", justify="center").pack()

        p12 = Radiobutton(elFrame, variable=Chon1, bg="white", text="30",
                          value=2, font="null 10 bold", justify="center").pack()

        p13 = Radiobutton(elFrame, variable=Chon1, bg="white", text="31",
                          value=3, font="null 10 bold", justify="center").pack()

        p2 = Label(elFrame, text="\n2) ¿Cuántas patadas tiene esta forma?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p21 = Radiobutton(elFrame, variable=Chon2, bg="white", text="3",
                          value=1, font="null 10 bold", justify="center").pack()

        p22 = Radiobutton(elFrame, variable=Chon2, bg="white", text="5",
                          value=2, font="null 10 bold", justify="center").pack()

        p23 = Radiobutton(elFrame, variable=Chon2, bg="white", text="7",
                          value=3, font="null 10 bold", justify="center").pack()

        p3 = Label(elFrame, text="\n3) ¿A que altura se ejecutan las patadas circulares?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p31 = Radiobutton(elFrame, variable=Chon3, bg="white", text="La primera  zona alta y la segunda  zona media",
                          value=1, font="null 10 bold", justify="center").pack()

        p32 = Radiobutton(elFrame, variable=Chon3, bg="white", text="Las dos a zona alta",
                          value=2, font="null 10 bold", justify="center").pack()

        p33 = Radiobutton(elFrame, variable=Chon3, bg="white", text="La primera a zona media y la segunda zona alta",
                          value=3, font="null 10 bold", justify="center").pack()

        p4 = Label(elFrame, text="\n4) ¿Qué era un Kobukson?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p41 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Un cargo militar",
                          value=1, font="null 10 bold", justify="center").pack()

        p42 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Un tipo de barco",
                          value=2, font="null 10 bold", justify="center").pack()

        p43 = Radiobutton(elFrame, variable=Chon4, bg="white", text="Un grupo de guerreros",
                          value=3, font="null 10 bold", justify="center").pack()

        p5 = Label(elFrame, text="\n5) ¿Como son las posiciones en el salto con giro?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p51 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Saltamos en gojung sogui y caemos en gojung sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p52 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Saltamos y caemos en niunja sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p53 = Radiobutton(elFrame, variable=Chon5, bg="white", text="Saltamos en niunja sogui y caemos en gojung sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p6 = Label(elFrame, text="\n6) ¿Cuál es el verdadero nombre de Choong Moo?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p61 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Choi Hong Hi",
                          value=1, font="null 10 bold", justify="center").pack()

        p62 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Yi Il Hwang",
                          value=2, font="null 10 bold", justify="center").pack()

        p63 = Radiobutton(elFrame, variable=Chon6, bg="white", text="Yi Soon Sin",
                          value=3, font="null 10 bold", justify="center").pack()

        p7 = Label(elFrame, text="\n7) ¿Cuántas goburyo sogui hay en Choong Moo?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p71 = Radiobutton(elFrame, variable=Chon7, bg="white", text="3",
                          value=1, font="null 10 bold", justify="center").pack()

        p72 = Radiobutton(elFrame, variable=Chon7, bg="white", text="2",
                          value=2, font="null 10 bold", justify="center").pack()

        p73 = Radiobutton(elFrame, variable=Chon7, bg="white", text="1",
                          value=3, font="null 10 bold", justify="center").pack()

        p8 = Label(elFrame, text="\n8) ¿Cómo se llama la posición de inicio?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p81 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Moa sogui A",
                          value=1, font="null 10 bold", justify="center").pack()

        p82 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Narani sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p83 = Radiobutton(elFrame, variable=Chon8, bg="white", text="Moa sogui B",
                          value=3, font="null 10 bold", justify="center").pack()

        p9 = Label(elFrame, text="\n9) ¿Qué posición no aparece en Choong Moo?\n",
                   bg="white", fg="blue", font=("null 14 bold")).pack()

        p91 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Gojung sogui",
                          value=1, font="null 10 bold", justify="center").pack()

        p92 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Dwitbal sogui",
                          value=2, font="null 10 bold", justify="center").pack()

        p93 = Radiobutton(elFrame, variable=Chon9, bg="white", text="Annun sogui",
                          value=3, font="null 10 bold", justify="center").pack()

        p10 = Label(elFrame, text="\n10) ¿Con que pierna vuelvo a la posición inicial?\n",
                    bg="white", fg="blue", font=("null 14 bold")).pack()

        p101 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Derecha",
                           value=1, font="null 10 bold", justify="center").pack()

        p102 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Izquierda",
                           value=2, font="null 10 bold", justify="center").pack()

        p103 = Radiobutton(elFrame, variable=Chon10, bg="white", text="Cualquiera",
                           value=3, font="null 10 bold", justify="center").pack()

        ResultadoP = Button(elFrame, text="RESULTADO",
                            command=Ya, font="null 25 bold").pack(pady=15)

        root1.update()

        c.config(scrollregion=c.bbox("all"))

        root1.mainloop()

# ----------------------KWANG-GAE----------------------------------------


def KwangGae():
    root1 = Toplevel()
    root1.config(bg="white")
    root1.resizable(0, 0)
    root1.title("Trivia: Kwang-Gae")
    Chon = IntVar()
    Chon1 = IntVar()
    Chon2 = IntVar()

    def Ya():
        global Count
        if Chon.get() == 2:
            Count = Count+1

        if Chon1.get() == 3:
            Count = Count+1

        if Chon2.get() == 3:
            Count = Count+1

        messagebox.showinfo("Resultado", ("Tienes " + str(Count) +
                                          " Respuestas correctas en la trivia sobre Kwang-Gae"))

        root1.destroy()

    preguntaGradoChon = Label(
        root1, text="¿Qué era Kwang-Gae?", bg="white", fg="blue", font=("null 16 bold"))
    preguntaGradoChon.grid(row=0, column=2, pady=10)

    primerChon = Radiobutton(root1, variable=Chon, bg="white",
                             text="Un presidente", value=1, font="null 12 bold", justify="center")
    primerChon.grid(row=1, column=1, pady=10)

    segundoChon = Radiobutton(root1, variable=Chon, bg="white",
                              text="Un rey", value=2, font="null 12 bold", justify="center")
    segundoChon.grid(row=1, column=2)

    terceroChon = Radiobutton(root1, variable=Chon, bg="white",
                              text="Un educador", value=3, font="null 12 bold", justify="center")
    terceroChon.grid(row=1, column=3)

    preguntaGradoChon = Label(root1, text="¿Cuántos movimientos tiene Kwang-Gae",
                              bg="white", fg="blue", font=("null 16 bold"))
    preguntaGradoChon.grid(row=2, column=2, pady=10)

    primerChon2 = Radiobutton(root1, variable=Chon1, bg="white",
                              text="35", value=1, font="null 12 bold", justify="center")
    primerChon2.grid(row=3, column=1, pady=10)

    segundoChon2 = Radiobutton(root1, variable=Chon1, bg="white",
                               text="45", value=2, font="null 12 bold", justify="center")
    segundoChon2.grid(row=3, column=2)

    terceroChon3 = Radiobutton(root1, variable=Chon1, bg="white",
                               text="39", value=3, font="null 12 bold", justify="center")
    terceroChon3.grid(row=3, column=3)

    preguntaTres = Label(root1, text="¿A qué altura se realizan los movimientos 8 y 9?",
                         bg="white", fg="blue", font=("null 16 bold"))
    preguntaTres.grid(row=4, column=2, pady=10)

    primerChon4 = Radiobutton(root1, variable=Chon2, bg="white",
                              text="Media", value=1, font="null 12 bold", justify="center")
    primerChon4.grid(row=5, column=1, pady=10)

    segundoChon4 = Radiobutton(root1, variable=Chon2, bg="white",
                               text="Baja", value=2, font="null 12 bold", justify="center")
    segundoChon4.grid(row=5, column=2)

    terceroChon4 = Radiobutton(root1, variable=Chon2, bg="white",
                               text="Alta", value=3, font="null 12 bold", justify="center")
    terceroChon4.grid(row=5, column=3)

    FinChon = Button(root1, text="RESULTADO", command=Ya, font=30)
    FinChon.grid(columnspan=4, pady=10)

    root1.mainloop()

# ----------------------GAEBAEK----------------------------------------


def GaeBaek():
    root1 = Toplevel()
    root1.config(bg="white")
    root1.resizable(0, 0)
    root1.title("Trivia: Gae Baek")
    Chon = IntVar()
    Chon1 = IntVar()
    Chon2 = IntVar()

    def Ya():
        global Count
        if Chon.get() == 1:
            Count = Count+1

        if Chon1.get() == 1:
            Count = Count+1

        if Chon2.get() == 1:
            Count = Count+1

        messagebox.showinfo("Resultado", ("Tienes " + str(Count) +
                                          " Respuestas correctas en la trivia sobre Gae Baek"))

        root1.destroy()

    preguntaGradoChon = Label(root1, text="¿Cuantos movimientos tiene Gae Baek?",
                              bg="white", fg="blue", font=("null 16 bold"))
    preguntaGradoChon.grid(row=0, column=2, pady=10)

    primerChon = Radiobutton(root1, variable=Chon, bg="white",
                             text="44", value=1, font="null 12 bold", justify="center")
    primerChon.grid(row=1, column=1, pady=10)

    segundoChon = Radiobutton(root1, variable=Chon, bg="white",
                              text="46", value=2, font="null 12 bold", justify="center")
    segundoChon.grid(row=1, column=2)

    terceroChon = Radiobutton(root1, variable=Chon, bg="white",
                              text="42", value=3, font="null 12 bold", justify="center")
    terceroChon.grid(row=1, column=3)

    preguntaGradoChon = Label(
        root1, text="¿Qué era Gae Baek?", bg="white", fg="blue", font=("null 16 bold"))
    preguntaGradoChon.grid(row=2, column=2, pady=10)

    primerChon2 = Radiobutton(root1, variable=Chon1, bg="white",
                              text="Un militar", value=1, font="null 12 bold", justify="center")
    primerChon2.grid(row=3, column=1, pady=10)

    segundoChon2 = Radiobutton(root1, variable=Chon1, bg="white",
                               text="Un rey", value=2, font="null 12 bold", justify="center")
    segundoChon2.grid(row=3, column=2)

    terceroChon3 = Radiobutton(root1, variable=Chon1, bg="white",
                               text="Un monje", value=3, font="null 12 bold", justify="center")
    terceroChon3.grid(row=3, column=3)

    preguntaTres = Label(root1, text="¿Con que pierna se vuelve a la posición inicial?",
                         bg="white", fg="blue", font=("null 16 bold"))
    preguntaTres.grid(row=4, column=2, pady=10)

    primerChon4 = Radiobutton(root1, variable=Chon2, bg="white",
                              text="Derecha", value=1, font="null 12 bold", justify="center")
    primerChon4.grid(row=5, column=1, pady=10)

    segundoChon4 = Radiobutton(root1, variable=Chon2, bg="white",
                               text="Izquierda", value=2, font="null 12 bold", justify="center")
    segundoChon4.grid(row=5, column=2)

    terceroChon4 = Radiobutton(root1, variable=Chon2, bg="white",
                               text="Ambas", value=3, font="null 12 bold", justify="center")
    terceroChon4.grid(row=5, column=3)

    FinChon = Button(root1, text="RESULTADO", command=Ya, font=30)
    FinChon.grid(columnspan=4, pady=10)

    root1.mainloop()

# ----------------------PO EUN----------------------------------------


def Poeun():
    root1 = Toplevel()
    root1.config(bg="white")
    root1.resizable(0, 0)
    root1.title("Trivia: Po Eun")
    Chon = IntVar()
    Chon1 = IntVar()
    Chon2 = IntVar()

    def Ya():
        global Count
        if Chon.get() == 3:
            Count = Count+1

        if Chon1.get() == 2:
            Count = Count+1

        if Chon2.get() == 3:
            Count = Count+1

        messagebox.showinfo("Resultado", ("Tienes " + str(Count) +
                                          " Respuestas correctas en la trivia sobre Po Eun"))

        root1.destroy()

    preguntaGradoChon = Label(root1, text="¿Cuantos movimientos tiene Po Eun?",
                              bg="white", fg="blue", font=("null 16 bold"))
    preguntaGradoChon.grid(row=0, column=2, pady=10)

    primerChon = Radiobutton(root1, variable=Chon, bg="white",
                             text="32", value=1, font="null 12 bold", justify="center")
    primerChon.grid(row=1, column=1, pady=10)

    segundoChon = Radiobutton(root1, variable=Chon, bg="white",
                              text="36", value=2, font="null 12 bold", justify="center")
    segundoChon.grid(row=1, column=2)

    terceroChon = Radiobutton(root1, variable=Chon, bg="white",
                              text="39", value=3, font="null 12 bold", justify="center")
    terceroChon.grid(row=1, column=3)

    preguntaGradoChon = Label(
        root1, text="¿Qué era Po Eun?", bg="white", fg="blue", font=("null 16 bold"))
    preguntaGradoChon.grid(row=2, column=2, pady=10)

    primerChon2 = Radiobutton(root1, variable=Chon1, bg="white",
                              text="Un militar", value=1, font="null 12 bold", justify="center")
    primerChon2.grid(row=3, column=1, pady=10)

    segundoChon2 = Radiobutton(root1, variable=Chon1, bg="white",
                               text="Un poeta", value=2, font="null 12 bold", justify="center")
    segundoChon2.grid(row=3, column=2)

    terceroChon3 = Radiobutton(root1, variable=Chon1, bg="white",
                               text="Un rey", value=3, font="null 12 bold", justify="center")
    terceroChon3.grid(row=3, column=3)

    preguntaTres = Label(root1, text="¿Cuantos movimientos encadenados hay en la moción continuada?",
                         bg="white", fg="blue", font=("null 16 bold"))
    preguntaTres.grid(row=4, column=2, pady=10)

    primerChon4 = Radiobutton(root1, variable=Chon2, bg="white",
                              text="5", value=1, font="null 12 bold", justify="center")
    primerChon4.grid(row=5, column=1, pady=10)

    segundoChon4 = Radiobutton(root1, variable=Chon2, bg="white",
                               text="6", value=2, font="null 12 bold", justify="center")
    segundoChon4.grid(row=5, column=2)

    terceroChon4 = Radiobutton(root1, variable=Chon2, bg="white",
                               text="7", value=3, font="null 12 bold", justify="center")
    terceroChon4.grid(row=5, column=3)

    FinChon = Button(root1, text="RESULTADO", command=Ya, font=30)
    FinChon.grid(columnspan=4, pady=10)

    root1.mainloop()
