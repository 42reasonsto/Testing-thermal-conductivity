import pyvisa as pv

class ControlMultimeter(object):

    @classmethod
    def measure(cls):
        rm = pv.ResourceManager()
        dev = list(rm.list_resources())
        scope = rm.open_resource(dev[0])
        scope.write(':FUNCtion:RESistance')
        resMeasured = scope.query(':MEASure:RESistance?')

        return resMeasured

    @classmethod
    def inToFloat(cls, s):
        new_list = s[0:7]
        number=float(new_list)*1000
        return number

    @classmethod
    def counter(cls, list_my):
        k=len(list_my)
        return k