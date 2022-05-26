from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView

import os
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Reset Password")
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("file:///C:/Users/artur/Desktop/ERP/password/forgot-password.html"))
        self.setCentralWidget(self.browser)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()