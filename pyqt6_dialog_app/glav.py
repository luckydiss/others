from PyQt6 import QtCore, QtWidgets
from win1 import MainWindow
from win2 import MainWindow2
from FibonnaciDialog import FibonnaciDialog
from PrimeDialog import PrimeDialog

# Создается основное окно программы
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 308)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 90, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 160, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Задание 3"))
        self.pushButton.setText(_translate("Dialog", "Числа Фибонначи"))
        self.pushButton_2.setText(_translate("Dialog", "Простые числа"))


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # При нажатие кнопок открываем соответствующие окна
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton_2.clicked.connect(self.openWindow2)
        
        # Создаем соответствующие экземпляры классов
        self.mainWindow = MainWindow()
        self.mainWindow2 = MainWindow2() 
        
        # Создаем экземпляр класса для диалога ввода чисел Фибонначи и по нажатию кнопки обновляем окно с числами
        self.fibonnaciDialog= FibonnaciDialog()
        self.mainWindow.pushButton_2.clicked.connect(self.openFibonnaciDialog)
        self.mainWindow.pushButton_2.clicked.connect(self.mainWindow.TextEdit.clear)
        self.fibonnaciDialog.pushButton.clicked.connect(self.updateWindow1)
        self.fibonnaciDialog.pushButton.clicked.connect(self.fibonnaciDialog.close)
        
        # Создаем экземпляр класса для диалога ввода простых чисел и по нажатию кнопки обновляем окно с числами
        self.primeDialog= PrimeDialog()
        self.mainWindow2.pushButton_2.clicked.connect(self.openPrimeDialog)
        self.mainWindow2.pushButton_2.clicked.connect(self.mainWindow2.TextEdit.clear)
        self.primeDialog.pushButton.clicked.connect(self.updateWindow2)
        self.primeDialog.pushButton.clicked.connect(self.primeDialog.close)

    # Открыть первое окно (числа Фибонначи)
    def openWindow(self):
#-        self.mainWindow = MainWindow()
        self.mainWindow.show()

    # Открыть второе окно (Простые числа)
    def openWindow2(self):
#-        self.mainWindow2 = MainWindow2()
        #self.updateWindow2()                                                    # +++
        self.mainWindow2.show()

    # Открыть первый диалог (числа Фибонначи)
    def openFibonnaciDialog(self):
        self.fibonnaciDialog.show()
    
    # Открыть второй диалог (Простые числа)
    def openPrimeDialog(self):
        self.primeDialog.show()
    
    # Обновление окна с числами Фибонначи
    def updateWindow1(self):
        message1 = QtWidgets.QMessageBox()
        if self.fibonnaciDialog.lineEdit.text() == "":
            message1.information(self,"Уведомление" ,"Заполните поля корректно")
        else:
            self.n = int(self.fibonnaciDialog.lineEdit.text())
            fib1 = fib2 = 1
            self.fibonnaci_list = [fib1,fib2]
            for i in range(2, self.n):
                fib1, fib2 = fib2, fib1 + fib2
                self.fibonnaci_list.append(fib2)
                
            for i in self.fibonnaci_list:
                i = str(i)
                self.mainWindow.TextEdit.append(i)
    
    # Обновление окна с простыми числами
    def updateWindow2(self):
        message2 = QtWidgets.QMessageBox()
        if self.primeDialog.lineEdit.text() == "":
            message2.information(self,"Уведомление" ,"Заполните поля корректно")
        else:
            self.n = int(self.primeDialog.lineEdit.text())
            self.prime_list = []
            prime = 2
            counter = 0
            while (counter < self.n):
                if all (prime % i != 0 for i in range(2,prime)):
                    self.prime_list.append(prime)
                counter += 1
                prime += 1
            
            for i in self.prime_list:
                i = str(i)
                self.mainWindow2.TextEdit.append(i)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec())
