# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerwvCMxT.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

import sys

class plans(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Planejamento")
        MainWindow.resize(1058, 512)
        MainWindow.move(850,490)
        self.actionPlanilha = QAction(MainWindow)
        self.actionPlanilha.setObjectName(u"actionPlanilha")
        self.actionExclus_o = QAction(MainWindow)
        self.actionExclus_o.setObjectName(u"actionExclus_o")
        self.actionManual = QAction(MainWindow)
        self.actionManual.setObjectName(u"actionManual")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget = QListWidget(self.frame_2)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 15):
            self.tableWidget.setColumnCount(15)
        if (self.tableWidget.rowCount() < 500):
            self.tableWidget.setRowCount(500)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(500)
        self.tableWidget.setColumnCount(15)

        self.verticalLayout.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1058, 22))
        self.menuCadastro = QMenu(self.menubar)
        self.menuCadastro.setObjectName(u"menuCadastro")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menuCadastro.addAction(self.actionPlanilha)
        self.menuCadastro.addAction(self.actionExclus_o)
        self.menuAjuda.addAction(self.actionManual)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Planejamento", None))
        self.actionPlanilha.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.actionExclus_o.setText(QCoreApplication.translate("MainWindow", u"Exclus\u00e3o", None))
        self.actionManual.setText(QCoreApplication.translate("MainWindow", u"Manual", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Planejamento 1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Planejamento 2", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Planejamento 3", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Planejamento 4", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Planejamento 5", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Planejamento 6", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Planejamento 7", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.menuCadastro.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = plans()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())