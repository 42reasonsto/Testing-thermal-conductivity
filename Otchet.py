import openpyxl
from datetime import datetime
from win32com.client import Dispatch


class Otchet(object):
    @classmethod
    def zavodskoyNomer(cls, listNumber, s):
      if listNumber<10:
          zavodNomer = s + "00" + str(listNumber)
      else:
          if listNumber<100:
              zavodNomer = s + "0" + str(listNumber)
          else:
              zavodNomer = s + str(listNumber)
      return zavodNomer

    @classmethod
    def sozdatXl(cls, path1, path2):
        xl = Dispatch("Excel.Application")
        xl.Visible = False

        wb = xl.Workbooks.Add()
        wb.SaveAs(path2)
        wb.Close()

        wb1 = xl.Workbooks.Open(Filename=path1)
        wb2 = xl.Workbooks.Open(Filename=path2)

        ws1 = wb1.Worksheets(1)
        ws1.Copy(Before=wb2.Worksheets(1))

        wb1.Close(SaveChanges=False)
        wb2.Close(SaveChanges=True)
        xl.Quit()

    @classmethod
    def sdelatOtchetPl(cls, list_resist, s, listNumber):
        number = listNumber[0]

        zN = str(Otchet.zavodskoyNomer(number, s))

        dt=datetime.now().strftime('%d.%m.%Y')

        path1 = 'G:\\Godnost_radiatora — копия.xlsx'
        path2 = 'G:\\Godnost_radiatora — '+zN+' '+dt+'.xlsx'

        Otchet.sozdatXl(path1, path2)

        i=22

        k=0

        wb_obj = openpyxl.load_workbook(path2)

        sheet_obj = wb_obj.active

        c1=sheet_obj['C1']

        c1.value="ПРОТОКОЛ № ПЛАСТИНА / " + zN + " ОТ " + dt

        b3 = sheet_obj['B3']

        a14 = sheet_obj['A14']

        a14.value = s

        c51 = sheet_obj['C51']

        if s == "L":
            b3.value = "предъявительских испытаний пластины зав. № " + zN
            c51.value = "пластины зав. № "
        else:
            b3.value = "предъявительских испытаний пластины зав. № " + zN
            c51.value = "пластины зав. № "

        while i<28:
          sheet_obj['B'+str(i)].value=list_resist[k]
          i=i+1
          k=k+1

        f51 = sheet_obj['F51']

        f51.value = zN

        wb_obj.save(path2)

        Otchet.udalit(listNumber)


    @classmethod
    def sdelatOtchetTr(cls, list_resist, s, listNumber):
          number = listNumber[0]

          zN = str(Otchet.zavodskoyNomer(number, s))

          dt = datetime.now().strftime('%d.%m.%Y')

          path1 = 'G:\\Godnost_teplovoy_trubki — копия.xlsx'
          path2 = 'G:\\Godnost_teplovoy_trubki — ' + zN + ' ' + dt + '.xlsx'

          Otchet.sozdatXl(path1, path2)

          i = 17

          k = 0

          wb_obj = openpyxl.load_workbook(path2)

          sheet_obj = wb_obj.active

          c1 = sheet_obj['C1']

          c1.value = "ПРОТОКОЛ № ТРУБКА / " + zN + " ОТ " + dt

          b3 = sheet_obj['B3']

          c46= sheet_obj['C46']

          if s=="А":
            b3.value = "предъявительских испытаний тепловой трубки зав. № " + zN
            c46.value = " тепловой трубки"

          else:
            b3.value = "предъявительских испытаний тепловой трубки зав. № " + zN
            c46.value =" тепловой трубки"

          while i < 23:
              sheet_obj['B' + str(i)].value = list_resist[k]
              i = i + 1
              k = k + 1

          e46 = sheet_obj['E46']

          e46.value = zN

          wb_obj.save(path2)

          Otchet.udalit(listNumber)

    @classmethod
    def dobavit(cls, s, list_resist):
        list_resist.append(s)
        return list_resist

    @classmethod
    def udalit(cls, list_resist):
        k=len(list_resist)
        list_resist.pop(k-1)
        return list_resist

    @classmethod
    def ochistit(cls, list_resist):
        list_resist.clear()
        return list_resist





