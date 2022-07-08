from PyQt6 import QtCore,QtWidgets

# Создается окно для вывода простых
class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(320, 240)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        
        self.TextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit.setGeometry(QtCore.QRect(120, 60, 101, 131))
        self.TextEdit.setObjectName("TextEdit")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 60, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 22))
        self.menubar.setObjectName("menubar")
        
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow", "Простые числа"))
        self.pushButton_2.setText(_translate("MainWindow", "ClickMe"))


class MainWindow2(QtWidgets.QMainWindow, Ui_MainWindow2):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow2()
    w.show()
    sys.exit(app.exec())
