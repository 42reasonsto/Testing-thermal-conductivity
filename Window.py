import tkinter as tk
from tkinter import *
import Otchet as o
import ControlMultimeter
import PhysVel


class Window():
    termResistSr = 0.2

    teploprovodnostSr = 150

    @classmethod
    def addValue(cls, mystring, listNumber):
        listNumber.append(int(mystring.get()))
        return listNumber

    @classmethod
    def framePl(cls, s, plschd, resists, listNumber):

        cm = ControlMultimeter.ControlMultimeter()

        pv = PhysVel.PhysVel()

        otc = o.Otchet()

        k = cm.counter(resists)

        measResist = cm.measure()

        flMeasResist = cm.inToFloat(measResist)

        temper = pv.temperature(flMeasResist)

        termRes = pv.termResist(temper, resists)

        teploprovodnost = pv.teploprovodnost(temper, plschd, resists)

        labelPloschadName = tk.Label(text="Площадь изделия", font=("Times New Roman", 12), fg="white", bg="black")
        labelPloschadName.place(x=50, y=150)

        labelTemperatureName = tk.Label(text="Температура изделия", font=("Times New Roman", 12), fg="white",
                                        bg="black")
        labelTemperatureName.place(x=50, y=200)

        labelTermResistName = tk.Label(text="Термическое сопротивление", font=("Times New Roman", 12), fg="white",
                                       bg="black")
        labelTermResistName.place(x=50, y=250)

        labelTermResistSrName = tk.Label(text="Среднее термическое сопротивление", font=("Times New Roman", 12),
                                         fg="white", bg="black")
        labelTermResistSrName.place(x=50, y=300)

        labelTeploprovodnostName = tk.Label(text="Теплопроводность", font=("Times New Roman", 12), fg="white",
                                            bg="black")
        labelTeploprovodnostName.place(x=50, y=350)

        labelTeploprovodnostSrName = tk.Label(text="Средняя теплопроводность", font=("Times New Roman", 12),
                                              fg="white", bg="black")
        labelTeploprovodnostSrName.place(x=50, y=400)

        labelPloschad = tk.Label(text=str(plschd), font=("Times New Roman", 12), fg="white", bg="black")
        labelPloschad.place(x=350, y=150)

        labelTemperature = tk.Label(text=str(temper), font=("Times New Roman", 12), fg="white", bg="black")
        labelTemperature.place(x=350, y=200)

        labelTermResist = tk.Label(text=str(termRes), font=("Times New Roman", 12), fg="white", bg="black")
        labelTermResist.place(x=350, y=250)

        if termRes > 0.3:
            labelTermResistError = tk.Label(text="Брак", font=("Times New Roman", 12), fg="red", bg="black")
            labelTermResistError.place(x=650, y=250)

        labelTermResistSr = tk.Label(text=str(Window.termResistSr), font=("Times New Roman", 12), fg="white",
                                     bg="black")
        labelTermResistSr.place(x=350, y=300)

        labelTeploprovodnost = tk.Label(text=str(teploprovodnost), font=("Times New Roman", 12), fg="white", bg="black")
        labelTeploprovodnost.place(x=350, y=350)

        if teploprovodnost < 130:
            labelTeploprovodnostError = tk.Label(text="Брак", font=("Times New Roman", 12), fg="red", bg="black")
            labelTeploprovodnostError.place(x=650, y=350)

        labelTeploprovodnostSr = tk.Label(text=str(Window.teploprovodnostSr), font=("Times New Roman", 12), fg="white",
                                          bg="black")
        labelTeploprovodnostSr.place(x=350, y=400)

        labelKolichestvo = tk.Label(text="Количество измерений " + str(k), font=("Times New Roman", 12), fg="white",
                                    bg="black")
        labelKolichestvo.place(x=450, y=475)

        btnDobavit = Button(text="Добавить", command=lambda: otc.dobavit(flMeasResist, resists), width="47", fg="black",
                            bg="white")
        btnDobavit.place(x=50, y=550)

        btnUdalit = Button(text="Удалить последнее", command=lambda: otc.udalit(resists), width="47", fg="black",
                           bg="white")
        btnUdalit.place(x=450, y=550)

        btnOchistit = Button(text="Очистить все значения", command=lambda: otc.ochistit(resists), width="47",
                             fg="black",
                             bg="white")
        btnOchistit.place(x=850, y=550)

        mystring = tk.StringVar()

        eNumber = Entry(textvariable=mystring, width="47", fg="black", bg="white")
        eNumber.place(x=50, y=600)

        buttonNumber = tk.Button(text='Номер изделия', width="47", fg="black", bg="white", command=lambda: Window().addValue(mystring, listNumber))
        buttonNumber.place(x=550, y=600)

        if k == 6:
            btnSdelatOtchet = Button(text="Сделать отчет", command=lambda: otc.sdelatOtchetPl(resists, s, listNumber),
                                     width="47", fg="black", bg="white")
            btnSdelatOtchet.place(x=250, y=650)
        else:
            labelErrorKolichestvo = tk.Label(text="Неправильное количество измерений", font=("Times New Roman", 12),
                                             fg="red", bg="black")
            labelErrorKolichestvo.place(x=250, y=650)

    @classmethod
    def frameTr(cls, s, resists, listNumber):

        cm = ControlMultimeter.ControlMultimeter()

        pv = PhysVel.PhysVel()

        otc = o.Otchet()

        k = cm.counter(resists)

        measResist = cm.measure()

        flMeasResist = cm.inToFloat(measResist)

        temper = pv.temperature(flMeasResist)

        termRes = pv.termResist(temper, resists)

        labelTemperatureName = tk.Label(text="Температура изделия", font=("Times New Roman", 12), fg="white",
                                        bg="black")
        labelTemperatureName.place(x=50, y=200)

        labelTermResistName = tk.Label(text="Термическое сопротивление", font=("Times New Roman", 12), fg="white",
                                       bg="black")
        labelTermResistName.place(x=50, y=250)

        labelTermResistSrName = tk.Label(text="Среднее термическое сопротивление", font=("Times New Roman", 12),
                                         fg="white", bg="black")
        labelTermResistSrName.place(x=50, y=300)

        labelTemperature = tk.Label(text=str(temper), font=("Times New Roman", 12), fg="white", bg="black")
        labelTemperature.place(x=350, y=200)

        labelTermResist = tk.Label(text=str(termRes), font=("Times New Roman", 12), fg="white", bg="black")
        labelTermResist.place(x=350, y=250)

        if termRes > 0.3:
            labelTermResistError = tk.Label(text="Брак", font=("Times New Roman", 12), fg="red", bg="black")
            labelTermResistError.place(x=650, y=250)

        labelTermResistSr = tk.Label(text=str(Window.termResistSr), font=("Times New Roman", 12), fg="white",
                                     bg="black")
        labelTermResistSr.place(x=350, y=300)

        labelKolichestvo = tk.Label(text="Количество измерений " + str(k), font=("Times New Roman", 12), fg="white",
                                    bg="black")
        labelKolichestvo.place(x=450, y=475)

        btnDobavit = Button(text="Добавить", command=lambda: otc.dobavit(flMeasResist, resists), width="47", fg="black",
                            bg="white")
        btnDobavit.place(x=50, y=550)

        btnUdalit = Button(text="Удалить последнее", command=lambda: otc.udalit(resists), width="47", fg="black",
                           bg="white")
        btnUdalit.place(x=450, y=550)

        btnOchistit = Button(text="Очистить все значения", command=lambda: otc.ochistit(resists), width="47",
                             fg="black",
                             bg="white")
        btnOchistit.place(x=850, y=550)

        mystring = tk.StringVar()

        eNumber = Entry(textvariable=mystring, width="47", fg="black", bg="white")
        eNumber.place(x=50, y=600)

        buttonNumber = tk.Button(text='Номер изделия', width="47", fg="black",
                                 bg="white", command=lambda: Window().addValue(mystring, listNumber))
        buttonNumber.place(x=550, y=600)

        if k == 6:
            btnSdelatOtchet = Button(text="Сделать отчет", command=lambda: otc.sdelatOtchetTr(resists, s, listNumber),
                                     width="47", fg="black", bg="white")
            btnSdelatOtchet.place(x=250, y=650)
        else:
            labelErrorKolichestvo = tk.Label(text="Неправильное количество измерений", font=("Times New Roman", 12),
                                             fg="red", bg="black")
            labelErrorKolichestvo.place(x=250, y=650)

    @classmethod
    def plastina(cls):
        resists = list()
        listNumber = list()

        btnL = Button(text="L", command=lambda: Window().plL(resists, listNumber), width="47", fg="black", bg="white")
        btnL.place(x=50, y=100)

        btnS = Button(text="S", command=lambda: Window().plS(resists, listNumber), width="47", fg="black", bg="white")
        btnS.place(x=450, y=100)

    @classmethod
    def plL(cls, resists, listNumber):

        s = "L"

        plschd = 0.0032

        Window().framePl(s, plschd, resists, listNumber)

    @classmethod
    def plS(cls, resists, listNumber):
        s = "S"

        plschd = 0.002704

        Window().framePl(s, plschd, resists, listNumber)

    @classmethod
    def trubka(cls):
        resists = list()
        listNumber = list()

        btnA = Button(text="А", command=lambda: Window().trA(resists, listNumber), width="47", fg="black", bg="white")
        btnA.place(x=50, y=100)

        btnB = Button(text="Б", command=lambda: Window().trB(resists, listNumber), width="47", fg="black",
                      bg="white")
        btnB.place(x=400, y=100)

        btnV = Button(text="В", command=lambda: Window().trV(resists, listNumber), width="47", fg="black", bg="white")
        btnV.place(x=750, y=100)

    @classmethod
    def trA(cls, resists, listNumber):
        s = "А"

        Window().frameTr(s, resists, listNumber)

    @classmethod
    def trB(cls, resists, listNumber):
        s = "Б"

        Window().frameTr(s, resists, listNumber)

    @classmethod
    def trV(cls, resists, listNumber):
        s = "В"

        Window().frameTr(s, resists, listNumber)

    @classmethod
    def oformlenie(cls):

        root = tk.Tk()

        root.title('Создание отчета проверки трубок и пластин')

        root.geometry('1200x950')

        root["bg"] = "black"

        btnPlastina = Button(text="Пластина", command=lambda: Window().plastina(), width="47", fg="black", bg="white")
        btnPlastina.place(x=50, y=50)

        btnTrubka = Button(text="Трубка", command=lambda: Window().trubka(), width="47", fg="black", bg="white")
        btnTrubka.place(x=450, y=50)
        root.mainloop()
