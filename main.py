
import sys
from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *
#import testestestes_rc

from Windows.plans import plans
from Windows.funcionario import Funcionarios as func
from Windows.users import Ui_MainWindow as users


class Ui_MainWindow(QMainWindow):

    

    def openPlans(self):

        self.MainWindow = QMainWindow()
        self.ui = plans()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
    
    def openFunc(self):

        self.MainWindow = QMainWindow()
        self.ui = func()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
    
    def openUsers(self):

        self.MainWindow = QMainWindow()
        self.ui = users()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)

        icon = QIcon()
        icon.addFile(u"Cheetah.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.setWindowIcon(QIcon("logo.png"))
        self.actionImportar = QAction(MainWindow)
        self.actionImportar.setObjectName(u"actionImportar")
        self.actionExportar = QAction(MainWindow)
        self.actionExportar.setObjectName(u"actionExportar")
        self.actionMateriais = QAction(MainWindow)
        self.actionMateriais.setObjectName(u"actionMateriais")
        self.actionEquipamentos = QAction(MainWindow)
        self.actionEquipamentos.setObjectName(u"actionEquipamentos")
        self.actionFuncion_rios = QAction(MainWindow)
        self.actionFuncion_rios.setObjectName(u"actionFuncion_rios")
        self.actionMateriais_2 = QAction(MainWindow)
        self.actionMateriais_2.setObjectName(u"actionMateriais_2")
        self.actionPlanilha = QAction(MainWindow)
        self.actionPlanilha.setObjectName(u"actionPlanilha")
        self.actionUsu_rios = QAction(MainWindow)
        self.actionUsu_rios.setObjectName(u"actionUsu_rios")
        self.actionUsu_rios.triggered.connect(self.openUsers)
        self.actionConfigura_es_Gen_ricas = QAction(MainWindow)
        self.actionConfigura_es_Gen_ricas.setObjectName(
            u"actionConfigura_es_Gen_ricas")
        self.actionLogo = QAction(MainWindow)
        self.actionLogo.setObjectName(u"actionLogo")
        self.actions = QAction(MainWindow)
        self.actions.setObjectName(u"actions")
        self.actionA = QAction(MainWindow)
        self.actionA.setObjectName(u"actionA")
        self.actionRelat_rios_2 = QAction(MainWindow)
        self.actionRelat_rios_2.setObjectName(u"actionRelat_rios_2")
        self.actionBI = QAction(MainWindow)
        self.actionBI.setObjectName(u"actionBI")
        self.actionData_Science = QAction(MainWindow)
        self.actionData_Science.setObjectName(u"actionData_Science")
        self.actionContas = QAction(MainWindow)
        self.actionContas.setObjectName(u"actionContas")
        self.actionNFE = QAction(MainWindow)
        self.actionNFE.setObjectName(u"actionNFE")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.graphlayout = QHBoxLayout(self.frame_2)
        self.graphlayout.setContentsMargins(0,0,0,0)
        self.graphlayout.setSpacing(0)

        series2  = QPieSeries()

        #append some data to the series 
        series2.append("João", 75)
        series2.append("Carlos", 20)
        series2.append("Joana", 10)
        series2.append("Carla", 12)
        series2.append("Outros", 30)
 
        #slice
        my_slice2 = series2.slices()[0]
        my_slice2.setExploded(True)
        my_slice2.setLabelVisible(True)
        my_slice2.setPen(QPen(Qt.green))
        my_slice2.setBrush(Qt.green) 
 
        #create QChart object
        chart2 = QChart()
        chart2.setContentsMargins(0,0,0,0)
        chart2.addSeries(series2)
        chart2.setAnimationOptions(QChart.SeriesAnimations)
        chart2.setTitle("Top Clients")
        chart2.setTheme(QChart.ChartThemeDark)
        #chart2.setBackgroundBrush(QColor("Transparent"))

        categories = [" Período Janeiro"]

        set04 = QBarSet("Janeiro")
        set05 = QBarSet("Fevereiro")
        set06 = QBarSet("Março")
        set07 = QBarSet("Abril")
        set08 = QBarSet("Maio")

        teste = (7250)

        set04 << 4500
        set05 << 3950
        set06 << 5020
        set07 << 5125
        set08 << (teste)

        series4 = QBarSeries()
        series4.append(set04)
        series4.append(set05)
        series4.append(set06)
        series4.append(set07)
        series4.append(set08) 
 
        chart4 = QChart()
        chart4.addSeries(series4)
        chart4.setAnimationOptions(QChart.SeriesAnimations)
        chart4.setTitle("Vendas")
        chart4.setTheme(QChart.ChartThemeDark)

        categories4 = ["Atualmente"]
 
        axis4 = QBarCategoryAxis()
        axis4.append(categories)
        chart4.createDefaultAxes()
        chart4.setAxisX(axis4, series4)
 
        # create QChartView object and add chart in thier 
        
        

        chartview2 = QChartView(chart2)
        chartview4 = QChartView(chart4)

        self.graphlayout.addWidget(chartview2)
        self.graphlayout.addWidget(chartview4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(150, 16777215))
        self.frame_5.setMinimumSize(QSize(150,150))
        self.frame_5.setStyleSheet(u"image: url(logo.png);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        '''self.button = QPushButton(self.frame_5)
        secontWindow = plansWindow()
        self.button.clicked.connect(secontWindow.show())'''
        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(550, 110, 120, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_3)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 987, 22))
        self.menuArquivos = QMenu(self.menubar)
        self.menuArquivos.setObjectName(u"menuArquivos")
        self.menuCadastro = QMenu(self.menuArquivos)
        self.menuCadastro.setObjectName(u"menuCadastro")
        self.menuPlanejamento = QMenu(self.menubar)
        self.menuPlanejamento.setObjectName(u"menuPlanejamento")
        self.menuAnalise_de_Dados = QMenu(self.menuPlanejamento)
        self.menuAnalise_de_Dados.setObjectName(u"menuAnalise_de_Dados")
        self.menuConfigura_es = QMenu(self.menubar)
        self.menuConfigura_es.setObjectName(u"menuConfigura_es")
        self.menuEmpresa = QMenu(self.menuConfigura_es)
        self.menuEmpresa.setObjectName(u"menuEmpresa")
        self.menuFinanceiro = QMenu(self.menubar)
        self.menuFinanceiro.setObjectName(u"menuFinanceiro")
        self.menuCadastro_2 = QMenu(self.menuFinanceiro)
        self.menuCadastro_2.setObjectName(u"menuCadastro_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArquivos.menuAction())
        self.menubar.addAction(self.menuPlanejamento.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())
        self.menubar.addAction(self.menuConfigura_es.menuAction())
        self.menuArquivos.addAction(self.menuCadastro.menuAction())
        self.menuArquivos.addAction(self.actionImportar)
        self.menuArquivos.addAction(self.actionExportar)
        self.menuCadastro.addAction(self.actionMateriais)
        self.menuCadastro.addAction(self.actionEquipamentos)
        self.menuCadastro.addAction(self.actionFuncion_rios)
        self.actionFuncion_rios.triggered.connect(self.openFunc)
        self.menuCadastro.addAction(self.actionMateriais_2)

        self.menuPlanejamento.addAction(self.actionPlanilha)
        self.actionPlanilha.triggered.connect(self.openPlans)

        self.menuPlanejamento.addAction(self.menuAnalise_de_Dados.menuAction())
        self.menuPlanejamento.addAction(self.actionRelat_rios_2)
        self.menuAnalise_de_Dados.addAction(self.actionBI)
        self.menuConfigura_es.addAction(self.actionUsu_rios)
        self.menuConfigura_es.addAction(self.menuEmpresa.menuAction())
        self.menuConfigura_es.addAction(self.actionConfigura_es_Gen_ricas)
        self.menuEmpresa.addAction(self.actionLogo)
        self.menuEmpresa.addAction(self.actions)
        self.menuFinanceiro.addAction(self.menuCadastro_2.menuAction())
        self.menuCadastro_2.addAction(self.actionContas)
        self.menuCadastro_2.addAction(self.actionNFE)

        
        
        self.retranslateUi(MainWindow)

        

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Cheetah ERP", None))
        self.actionImportar.setText(
            QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.actionExportar.setText(QCoreApplication.translate(
            "MainWindow", u"Importar/Exportar", None))
        self.actionMateriais.setText(QCoreApplication.translate(
            "MainWindow", u"Equipamentos", None))
        self.actionEquipamentos.setText(
            QCoreApplication.translate("MainWindow", u"Fornecedores", None))
        self.actionFuncion_rios.setText(QCoreApplication.translate(
            "MainWindow", u"Funcion\u00e1rios", None))
        self.actionMateriais_2.setText(
            QCoreApplication.translate("MainWindow", u"Materiais", None))
        self.actionPlanilha.setText(
            QCoreApplication.translate("MainWindow", u"Planilha", None))
        self.actionUsu_rios.setText(QCoreApplication.translate(
            "MainWindow", u"Usu\u00e1rios", None))
        self.actionConfigura_es_Gen_ricas.setText(QCoreApplication.translate(
            "MainWindow", u"Configura\u00e7\u00f5es Gen\u00e9ricas", None))
        self.actionLogo.setText(QCoreApplication.translate(
            "MainWindow", u"Defini\u00e7\u00f5es", None))
        self.actions.setText(QCoreApplication.translate(
            "MainWindow", u"Tela Inicial", None))
        self.actionA.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.actionRelat_rios_2.setText(QCoreApplication.translate(
            "MainWindow", u"Relat\u00f3rios", None))
        self.actionBI.setText(
            QCoreApplication.translate("MainWindow", u"BI", None))
        self.actionData_Science.setText(
            QCoreApplication.translate("MainWindow", u"Data Science", None))
        self.actionContas.setText(
            QCoreApplication.translate("MainWindow", u"Contas", None))
        self.actionNFE.setText(QCoreApplication.translate(
            "MainWindow", u"Gerenciamento de NFE", None))
        self.menuArquivos.setTitle(
            QCoreApplication.translate("MainWindow", u"Arquivos", None))
        self.menuCadastro.setTitle(
            QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.menuPlanejamento.setTitle(
            QCoreApplication.translate("MainWindow", u"Planejamento", None))
        self.menuAnalise_de_Dados.setTitle(
            QCoreApplication.translate("MainWindow", u"Analise de Dados", None))
        self.menuConfigura_es.setTitle(QCoreApplication.translate(
            "MainWindow", u"Configura\u00e7\u00f5es", None))
        self.menuEmpresa.setTitle(
            QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.menuFinanceiro.setTitle(
            QCoreApplication.translate("MainWindow", u"Financeiro", None))
        self.menuCadastro_2.setTitle(
            QCoreApplication.translate("MainWindow", u"Cadastro", None))
        
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())
