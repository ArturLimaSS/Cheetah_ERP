import webbrowser
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from time import sleep
#from PySide6.QtWebEngineWidgets import *
#from PySide6.QtWebEngineWidgets import QWebEngineView

from main import Ui_MainWindow as mainW


import sys

class Ui_MainWindow(QMainWindow):
    def openMain(self):
        self.MainWindow = QMainWindow()
        self.ui = mainW()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
    
    def forgotPsw(self):
        webbrowser.open ("file:///C:/Users/artur/Desktop/ERP/password/forgot-password.html")

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QSize(400, 0))
        MainWindow.setMaximumSize(QSize(500, 600))
        self.icon = QIcon()
        self.icon.addFile(u"Cheetah.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(self.icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 600))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(60, 0, 60, 50)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"label")
        self.frame.setStyleSheet(u"image: url(CHEETAHERP.png)")

        self.verticalLayout.addWidget(self.frame)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
                                    "border: 2px solid gray;\n"
                                    " border-radius: 10px}\n"
                                    "\n"
                                    "QLineEdit:focus {\n"
                                    "	border:2px solid rgb(170, 174, 255);\n"
                                    "}")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(50, 30))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
                                      "border: 2px solid gray;\n"
                                      " border-radius: 10px}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "	border:2px solid rgb(170, 174, 255);\n"
                                      "}")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
                                        "		border: 2px solid gray;\n"
                                        " border-radius: 10px;\n"
                                        "	background-color: rgb(230, 230, 230);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	background-color: rgb(170, 188, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "		\n"
                                        "	background-color: rgb(79, 88, 255);\n"
                                        "}")
        self.pushButton_2.clicked.connect(self.loginCheck)
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 30))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
                                        "		border: 2px solid gray;\n"
                                        " border-radius: 10px;\n"
                                        "	background-color: rgb(230, 230, 230);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	background-color: rgb(170, 188, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "		\n"
                                        "	background-color: rgb(79, 88, 255);\n"
                                        "}")

        self.pushButton_3.clicked.connect(self.forgotPsw)

        self.verticalLayout.addWidget(self.pushButton_3)

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


    def loginCheck(self):
        loginError = QMessageBox()
        loginError.setIcon(QMessageBox.Critical)
        #loginError.setText("Login Inválido")
        loginError.setInformativeText("""Login Inválido!
Para visualizar os acessos, contate o 
Administrador do sistema!

""")
        loginError.setWindowTitle("Erro Login")
        loginError.setWindowIcon(self.icon)

        senhaError = QMessageBox()
        senhaError.setIcon(QMessageBox.Critical)
        #senhaError.setText("Senha Inválida")
        senhaError.setInformativeText('''Senha Inválida! 
Para redefinir sua senha, clique no botão "Esqueci Minha Senha"''')
        senhaError.setWindowTitle("Senha Inválida!")
        senhaError.setWindowIcon(self.icon)

        self.login = "artur"
        self.logininput = self.lineEdit.text()

        self.senha = "Senha"
        self.senhaInput = self.lineEdit_2.text()
        if not self.logininput == self.login:
            self.statusbar.showMessage("Login Inválido! Para visualizar os acessos, contate o Administrador do sistema!")
            #loginError.exec()
            
        elif not self.senhaInput == self.senha:
            self.statusbar.showMessage('Senha Inválida! Para redefinir sua senha, clique no botão "Esqueci Minha Senha"')
            #senhaError.exec()
            

        else:
            self.statusbar.showMessage("Operando")
            self.openMain()

    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Senha", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.pushButton_3.setText(QCoreApplication.translate(
            "MainWindow", u"Esqueci Minha Senha", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
