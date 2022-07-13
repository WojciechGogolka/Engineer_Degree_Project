# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from modules.ui_add_form import Ui_AddWindow
from modules.ui_settings import Ui_SettingsWindow
from modules.ui_functions import *
from database.db_connection import *
from database.db_worker_functions import *
from database.myconverter import MyConverter
from mysql import connector
from widgets import *
from settings import *
from worker_addForm import AddWindow
from worker_stackedForm import WorkerForms
from database.db_urlops_functions import checkActualAgreement
from PySide6.QtGui import *
from datetime import date
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
workers = None
workers_list = None

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        global widgets
        widgets = self.ui
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        #Setting APP Name and top description
        # APP NAME
        title = "WGUrlops"
        description = "Aplikacja urlopowa WG"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # BUTTONS CLICK
        # LEFT MENUS
        widgets.btn1_menu_add.clicked.connect(self.buttonClick_worker)
        widgets.btn2_menu_delete.clicked.connect(self.buttonClick_worker)
        widgets.btn3_menu_edit.clicked.connect(self.buttonClick_worker)
        widgets.btn4_menu_agreements.clicked.connect(self.buttonClick_worker)
        widgets.btn5_menu_child.clicked.connect(self.buttonClick_worker)
        widgets.btn6_menu_invalid.clicked.connect(self.buttonClick_worker)
        widgets.btn7_menu_workhist.clicked.connect(self.buttonClick_worker)
        widgets.btn8_menu_urlopcard.clicked.connect(self.buttonClick_worker)
        # SETTINGS MENUS
        widgets.btn2_settings_cities.clicked.connect(self.buttonClick_settings)
        widgets.btn3_settings_education.clicked.connect(self.buttonClick_settings)
        widgets.btn4_settings_agreements.clicked.connect(self.buttonClick_settings)
        widgets.btn5_settings_invalids.clicked.connect(self.buttonClick_settings)
        widgets.btn6_settings_urlops.clicked.connect(self.buttonClick_settings)
        #WORKERS TABLE
        self.ui.workersTable.cellClicked.connect(self.getWorkerData)


        if db_connection.db_connect():
            self.downloadWorkers()
        else:
            self.showDialog('Nie znaleziono bazy danych','Połączenie nie zostało nawiązane','information')
            self.disableMenu()



        #BLOCK BUTTONS
        self.enableButtons(False)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)

    def getWorkerData(self):
        global workers_list
        workers_list = []
        index = self.ui.workersTable.selectionModel().currentIndex()
        columns = self.ui.workersTable.columnCount()
        # Load data into list
        for i in range(columns):
            value = index.sibling(index.row(), i).data()
            workers_list.append(value)
        self.enableButtons(True)

    # BUTTONS CLICK
    # Functions for button in the worker interface
    def buttonClick_worker(self):
        btn = self.sender()
        btnName = btn.objectName()
        # Blocking option to interact with main window untill child window is open
        #self.settingsWidget.setWindowModality(Qt.ApplicationModal)

        # OPEN NEW WORKER FORM
        if btnName == "btn1_menu_add":
            self.add_worker = AddWindow(self)
            # Blocking option to interact with main window untill child window is open
            self.add_worker.setWindowFlags(self.windowFlags() | Qt.Window)
            self.add_worker.setParent(self)
            self.add_worker.setWindowModality(Qt.ApplicationModal)
            self.add_worker.addView()
            self.add_worker.show()

        # DELETE WORKER FROM DB
        if btnName == "btn2_menu_delete":
            index = (self.ui.workersTable.selectionModel().currentIndex())
            index.row()  # gives current selected row.
            record_id = index.sibling(index.row(), 0).data()  # will return cell data
            print("Delete worker with id:", record_id)
            if self.showDialog('Potwierdź operacje','Czy na pewno chcesz usunąć pracownika z bazy danych?','askConfirmation'):
                if db_worker_functions.deleteWorker(record_id):
                    self.deleteWorkerFromTable()
                    self.showDialog('Usuwanie zakończone', 'Pracownik został usunięty z bazy danych.',
                                    'information')
                    self.enableButtons(False)
                else:
                    self.showDialog('Błąd w trakcie usuwania',
                                    'Pracownik jest powiązany z innymi danymi. Najpierw usuń pozostałe dane.',
                                    'information')


        # SHOW EDIT FORM
        if btnName == "btn3_menu_edit":
            self.add_worker = AddWindow(self)
            # Blocking option to interact with main window untill child window is open
            self.add_worker.setWindowFlags(self.windowFlags() | Qt.Window)
            self.add_worker.setParent(self)
            self.add_worker.setWindowModality(Qt.ApplicationModal)
            self.add_worker.editView(workers_list)
            self.add_worker.show()

        else:
            self.worker_form = WorkerForms(self)
            # Blocking option to interact with main window untill child window is open
            self.worker_form.setWindowFlags(self.windowFlags() | Qt.Window)
            self.worker_form.setParent(self)
            self.worker_form.setWindowModality(Qt.ApplicationModal)

            # SHOW AGREEMENTS FORM
            if btnName == "btn4_menu_agreements":
                self.worker_form.setViewParameteres('agreements', workers_list)
                self.worker_form.show()

            # SHOW CHILDREN FORM
            if btnName == "btn5_menu_child":
                self.worker_form.setViewParameteres('child', workers_list)
                self.worker_form.show()

            # SHOW INVALID FORM
            if btnName == "btn6_menu_invalid":
                self.worker_form.setViewParameteres('invalid', workers_list)
                self.worker_form.show()

            # SHOW WORKHISTORY FORM
            if btnName == "btn7_menu_workhist":
                self.worker_form.setViewParameteres('workhist', workers_list)
                self.worker_form.show()

            # SHOW WORKHISTORY FORM
            if btnName == "btn8_menu_urlopcard":
                if checkActualAgreement(workers_list[0]):
                    self.worker_form.setViewParameteres('urlop', workers_list)
                    self.worker_form.show()
                else:
                    self.showDialog('Brak aktualnej umowy',
                                    'Zanim przejdziesz do karty urlopowej dodaj pracownikowi aktualną umowę.',
                                    'information')

        UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

    # BUTTONS CLICK
    # Functions for button in the settings interface
    def buttonClick_settings(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        self.settingsWidget = SettingsWindow(self)
        # Blocking option to interact with main window untill child window is open
        self.settingsWidget.setWindowFlags(self.windowFlags() | Qt.Window)
        self.settingsWidget.setParent(self)
        self.settingsWidget.setWindowModality(Qt.ApplicationModal)

        # SHOW CITIES DATABASE PAGE--------------------------------------------------------
        if btnName == "btn2_settings_cities":
            # Setting window parameters
            self.settingsWidget.window_parameters('cities')
            self.settingsWidget.download_settings('cities')
            self.settingsWidget.show()
            # Reseting button style
            UIFunctions.resetStyle_settings(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW EDUCATION DATABASE PAGE
        if btnName == "btn3_settings_education":
            # Setting window parameters
            self.settingsWidget.window_parameters('education')
            self.settingsWidget.download_settings('education')
            self.settingsWidget.show()
            UIFunctions.resetStyle_settings(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW AGREEMENTS CONFIGURATION PAGE
        if btnName == "btn4_settings_agreements":
            # Setting window parameters
            self.settingsWidget.window_parameters('agreements')
            self.settingsWidget.download_settings('agreements')
            self.settingsWidget.show()
            # Reseting button style
            UIFunctions.resetStyle_settings(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW INVALIDS DATABASE PAGE
        if btnName == "btn5_settings_invalids":
            # Setting window parameters
            self.settingsWidget.window_parameters('invalids')
            self.settingsWidget.download_settings('invalids')
            self.settingsWidget.show()
            # Reseting button style
            UIFunctions.resetStyle_settings(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW CITIES DATABASE PAGE
        if btnName == "btn6_settings_urlops":
            # Setting window parameters
            self.settingsWidget.window_parameters('urlops')
            self.settingsWidget.download_settings('urlops')
            self.settingsWidget.show()
            # Reseting button style
            UIFunctions.resetStyle_settings(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def downloadWorkers(self):
        # Setting multi view parameters-----------------------------------------------------------
        self.ui.workersTable.setFocusPolicy(Qt.NoFocus)
        self.ui.workersTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.workersTable.verticalHeader().setVisible(False)
        self.ui.workersTable.horizontalHeader().sectionPressed.disconnect()
        self.ui.workersTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.workersTable.setStyleSheet("""
                        QHeaderView::section { color:white; background-color:#232326;} 
                        QTableWidget { selection-color: rgb(255,255,255); selection-background-color:rgb(47, 49, 51); }""")

        # Initializing header configuration
        header = self.ui.workersTable.horizontalHeader()
        header.setStretchLastSection(True)
        header.setHighlightSections(False)
        self.ui.workersTable.setColumnCount(11)
        self.ui.workersTable.setHorizontalHeaderLabels(['ID', 'Imię', 'Nazwisko', 'Data urodzenia','Obcokrajowiec', 'PESEL', 'Adres zamieszkania', 'Kod ZIP', 'Miasto', 'Numer telefonu', 'Wykształcenie'])
        count = self.ui.workersTable.columnCount()
        for i in range(count):
            self.ui.workersTable.setColumnWidth(i, 180)
        global workers
        workers = load_workers_list()
        if workers is None:
            # Download data error
            print("No data here")
        else:
            for row in workers:
                self.add_Table(MyConverter(row))

    def add_Table(self,columns):
        rowPosition = widgets.workersTable.rowCount()
        widgets.workersTable.insertRow(rowPosition)

        for i, column in enumerate(columns):
            item = QtWidgets.QTableWidgetItem(str(column))
            self.ui.workersTable.setItem(rowPosition, i, item)
            item.setTextAlignment(Qt.AlignHCenter)

    def updateColumnInTable(self,column,pValue,nValue):
        rowPosition = self.ui.workersTable.rowCount()
        #print(pValue,nValue,rowPosition)
        for row in range(rowPosition):
            value = self.ui.workersTable.item(row,column).text()
            #print("up",row,value, pValue)
            if value == pValue:
                #print("update",row)
                item = QtWidgets.QTableWidgetItem(str(nValue))
                self.ui.workersTable.setItem(row, column, item)
                item.setTextAlignment(Qt.AlignHCenter)

    def addWorkerRecordInTable(self,values):
        self.add_Table(values)

    def deleteWorkerFromTable(self):
        index = (self.ui.workersTable.selectionModel().currentIndex())
        self.ui.workersTable.removeRow(index.row())

    def updateWorkerInTable(self,values):
        print(values)
        index = self.ui.workersTable.selectionModel().currentIndex()
        print(index)
        for i, column in enumerate(values):
            item = QtWidgets.QTableWidgetItem(str(column))
            self.ui.workersTable.setItem(index.row(), i + 1, item)
            item.setTextAlignment(Qt.AlignHCenter)

    def showDialog(self,messageText,detailedText, messageOption):
        msg = QMessageBox()
        msg.setStyleSheet("""QLabel{min-width: 450px; min-height: 70px;color: white; }
                                    QMessageBox {background-color: #333333; font-size:18px; border: 5px solid black; min-width: 550px;}
                                    QPushButton {background-color:  rgb(27, 29, 35); color:white; font-family: Arial; font-size:20px; width:150px;}""")
        msg.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        msg.setText(messageText)
        msg.setInformativeText(detailedText)

        if messageOption == 'askConfirmation':
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
            buttonY = msg.button(QMessageBox.Ok)
            buttonY.setText('Tak')
            buttonN = msg.button(QMessageBox.No)
            buttonN.setText('Nie')
            ret = msg.exec_()
            if ret == QMessageBox.Ok:
                print('OPERACJA POTWIERDZONA')
                return True

        if messageOption == 'information':
            msg.setStandardButtons(QMessageBox.Ok)
            ret = msg.exec_()
            print('DIALOG INFORMACYJNY')
            return False

    def enableButtons(self,bool):
        # BLOCK BUTTONS
        widgets.btn2_menu_delete.setEnabled(bool)
        widgets.btn3_menu_edit.setEnabled(bool)
        widgets.btn4_menu_agreements.setEnabled(bool)
        widgets.btn5_menu_child.setEnabled(bool)
        widgets.btn6_menu_invalid.setEnabled(bool)
        widgets.btn7_menu_workhist.setEnabled(bool)
        widgets.btn8_menu_urlopcard.setEnabled(bool)

    def disableMenu(self):
        self.ui.btn1_menu_add.setDisabled(True)
        self.ui.btn2_settings_cities.setDisabled(True)
        self.ui.btn3_settings_education.setDisabled(True)
        self.ui.btn4_settings_agreements.setDisabled(True)
        self.ui.btn5_settings_invalids.setDisabled(True)
        self.ui.btn6_settings_urlops.setDisabled(True)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))

    window = MainWindow()

    sys.exit(app.exec_())


