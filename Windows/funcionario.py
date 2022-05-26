
import sys
from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Funcionarios(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 260)
        MainWindow.setMinimumSize(QSize(800, 260))
        MainWindow.setMaximumSize(QSize(800, 260))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 782, 250))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 49, 16))
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 61, 16))
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 80, 49, 16))
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 100, 71, 21))
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 130, 51, 16))
        self.buttonBox = QDialogButtonBox(self.frame_5)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(20, 170, 156, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_2.addWidget(self.lineEdit_5)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro de Funcionários", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o Nome do Funcion\u00e1rio", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a matr\u00edcula do funcion\u00e1rio", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o CPF do funcion\u00e1rio", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite onde o Funcion\u00e1rio mora", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o cargo que ir\u00e1 ocupar", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Funcionarios()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())