import ControlMultimeter
class PhysVel(object):

    @classmethod
    def temperature(cls, resistance):
        r0 = 1000
        c=resistance/r0-1
        d1=255.819
        d2=9.1455
        d3=2.92363
        d4=1.7909

        temper=(c*d1+c*d2+c*d3+c*d3+c*d4)*0.94
        return temper

    @classmethod
    def termResist(cls, temperatureEnd, list_my):
        x=len(list_my)
        tR=((90.0+10*x-temperatureEnd)/(250.0+10*x))
        return tR

    @classmethod
    def sr(cls, list_my):
        suma=sum(list_my)
        k=len(list_my)
        return suma/k

    @classmethod
    def teploprovodnost(cls, temperatureEnd, f, list_my):
        x=len(list_my)
        a=(230.0+10*x)*0.008
        b=90.0+10*x-temperatureEnd
        tP=(a/b)/f
        return tP

    @classmethod
    def ploschadL(cls, s):
        if s=="L":
            f=0.002704
        else: f=0.00264

        return f
