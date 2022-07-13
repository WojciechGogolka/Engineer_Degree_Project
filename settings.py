import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
#from modules.ui_add_form import Ui_AddWindow
from modules.ui_settings import Ui_SettingsWindow
from widgets import CustomGrip
from database import db_connection
from database import db_worker_functions
from PySide6 import QtWidgets
import ast
from database.myconverter import MyConverter
from database import db_settings_functions
from PySide6.QtCore import QRegularExpression
from modules.updateMainTable import updateWorkerColumn
from PySide6.QtGui import *


data = None
settings_lineEdit_input_list = []
table = None
previousValue = None

class SettingsWindow(QWidget):
    def __init__(self, parent):
        super(SettingsWindow,self).__init__(parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        # STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
        #Buttons section
        self.ui.settings_table.cellClicked.connect(self.load_to_lineedit)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.titleRightInfo.mouseMoveEvent = moveWindow

        # CUSTOM GRIPS
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

    #Function setting window size and widgets parameters
    def window_parameters(self,windowType):
        global table
        table = windowType
        #Setting multi view parameters-----------------------------------------------------------
        self.ui.settings_table.setFocusPolicy(Qt.NoFocus)
        self.ui.settings_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.settings_table.verticalHeader().setVisible(False)
        self.ui.settings_table.horizontalHeader().sectionPressed.disconnect()
        self.ui.settings_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.settings_table.setStyleSheet("""
        QHeaderView::section { color:white; background-color:#232326; }
        QTableWidget { selection-color: rgb(255,255,255); selection-background-color:rgb(47, 49, 51); }""")

        # Initializing header configuration
        header = self.ui.settings_table.horizontalHeader()
        #header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setHighlightSections(False)

        #INITIALIZE INSERT VALUES RESTRICTION
        self.restrictInputValues(windowType)

        #Settings Cities database view parameters-----------------------------------------------
        if windowType == 'cities':
            #Setting window parameters
            self.ui.bgApp.setFixedSize(500, 565)
            self.ui.main_stackedWidget.setCurrentIndex(1)
            self.ui.database_stackedWidget.setCurrentIndex(0)
            self.ui.database_groupBox_inputs.setTitle("Opcje edycji miast")
            self.ui.database_tables_label0.setText("Nazwa miasta:")

            # Fixing the size of Window - must be manipulated by setting table size
            self.ui.database_groupBox_inputs.setFixedHeight(120)

            #Setting table parameters
            self.ui.settings_table.setFixedSize(465, 350)
            self.ui.settings_table.setColumnCount(2)
            self.ui.settings_table.setHorizontalHeaderLabels(['ID', 'Nazwa miasta'])
            self.ui.settings_table.setColumnWidth(1, 395)
            self.ui.settings_table.setColumnWidth(0, 60)

        #Settings Education database window parameters-------------------------------------------a
        elif windowType == 'education':
            # Setting window parameters
            self.ui.bgApp.setFixedWidth(570)
            self.ui.main_stackedWidget.setCurrentIndex(1)
            self.ui.database_stackedWidget.setCurrentIndex(1)
            self.ui.database_groupBox_inputs.setTitle("Opcje edycji wykształcenia")
            self.ui.database_tables_label1.setText("Nazwa wykształcenia:")
            self.ui.database_tables_label2.setText("Lata do historii zatrudnienia:")

            # Fixing the size of Window - must be manipulated by setting table size
            self.ui.database_groupBox_inputs.setFixedHeight(140)

            #Setting table parameters
            #Table parameters
            self.ui.settings_table.setColumnCount(3)
            self.ui.settings_table.setHorizontalHeaderLabels(['ID', 'Nazwa wykształcenia', 'Lata do HZ'])
            self.ui.settings_table.setColumnWidth(0, 60)
            self.ui.settings_table.setColumnWidth(1, 275)
            self.ui.settings_table.setColumnWidth(2, 190)

        # Settings Agreements database window parameters------------------------------------------
        elif windowType == 'agreements':
            # Setting window parameters
            self.ui.bgApp.setFixedWidth(610)
            self.ui.main_stackedWidget.setCurrentIndex(1)
            self.ui.database_stackedWidget.setCurrentIndex(2)
            self.ui.database_groupBox_inputs.setTitle("Opcje edycji rodzai umów")
            self.ui.database_tables_label3.setText("Nazwa umowy:")
            self.ui.database_tables_label4.setText("Naliczanie urlopu:")
            self.ui.database_tables_radio1.setText("")

            # Fixing the size of Window - must be manipulated by setting table size
            self.ui.database_groupBox_inputs.setFixedHeight(130)

            # Setting table parameters
            # Table parameters
            self.ui.settings_table.setColumnCount(3)
            self.ui.settings_table.setHorizontalHeaderLabels(['ID', 'Nazwa umowy', 'Naliczanie urlopu'])
            self.ui.settings_table.setColumnWidth(0, 60)
            self.ui.settings_table.setColumnWidth(1, 365)
            self.ui.settings_table.setColumnWidth(2, 140)

        # Settings Invalids database window parameters---------------------------------------------
        elif windowType == 'invalids':
            self.ui.bgApp.setFixedWidth(598)
            # Setting window parameters
            self.ui.main_stackedWidget.setCurrentIndex(1)
            self.ui.database_stackedWidget.setCurrentIndex(1)
            self.ui.database_groupBox_inputs.setTitle("Opcje edycji poziomów niepełnosprawności")
            self.ui.database_tables_label1.setText("Poziom niepełnosprawności:")
            self.ui.database_tables_label2.setText("Dodatkowy urlop:")

            # Fixing the size of Window - must be manipulated by setting table size
            self.ui.database_groupBox_inputs.setFixedHeight(130)
            self.ui.btn1_settings_add.setDisabled(True)

            # Setting table parameters
            # Table parameters
            self.ui.settings_table.setColumnCount(3)
            self.ui.settings_table.setHorizontalHeaderLabels(['ID', 'Poziom niepełnosprawności', 'Dodatkowy urlop'])
            self.ui.settings_table.setColumnWidth(0, 60)
            self.ui.settings_table.setColumnWidth(1, 310)
            self.ui.settings_table.setColumnWidth(2, 180)

        elif windowType =='urlops':
            # Setting window parameters
            self.ui.bgApp.setFixedWidth(598)
            self.ui.main_stackedWidget.setCurrentIndex(1)
            self.ui.database_stackedWidget.setCurrentIndex(1)
            self.ui.database_groupBox_inputs.setTitle("Opcje edycji urlopów")
            self.ui.database_tables_label1.setText("Nazwa urlopu:")
            self.ui.database_tables_label2.setText("Roczny limit:")

            # Fixing the size of Window - must be manipulated by setting table size
            self.ui.database_groupBox_inputs.setFixedHeight(130)

            # Setting table parameters
            # Table parameters
            self.ui.settings_table.setColumnCount(3)
            self.ui.settings_table.setHorizontalHeaderLabels(['ID', 'Nazwa urlopu', 'Roczny limit'])
            self.ui.settings_table.setColumnWidth(0, 60)
            self.ui.settings_table.setColumnWidth(1, 375)
            self.ui.settings_table.setColumnWidth(2, 118)

            #DISABLE ADD BUTTON
            self.ui.btn1_settings_add.setDisabled(True)

        #CONNECT BUTTONS
        self.ui.btn1_settings_add.clicked.connect(lambda: self.insertSettingsRecord(windowType))
        self.ui.btn2_settings_delete.clicked.connect(lambda: self.deleteSettingsRecord(windowType))
        self.ui.btn3_settings_edit.clicked.connect(lambda: self.UpdateSettingsRecord(windowType))

        self.ui.btn2_settings_delete.setDisabled(True)
        self.ui.btn3_settings_edit.setDisabled(True)

    def download_settings(self,table):
        #Download data from database
        global data
        data = db_settings_functions.selectSettingsTable(table)
        if data is None:
            # Download data error
            print("No data here")
        else:
            for row in data:
                self.add_Table(table,MyConverter(row))

    def add_Table(self,table,columns):
        rowPosition = self.ui.settings_table.rowCount()
        self.ui.settings_table.insertRow(rowPosition)
        for i, column in enumerate(columns):
            print(column)
            if table == 'agreements' and i == 2:
                if column == '1' or column == True:
                    column = 'Tak'
                else:
                    column = 'Nie'
            item = QtWidgets.QTableWidgetItem(str(column))
            if column == 'None':
                self.ui.settings_table.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(''))
            else:
                self.ui.settings_table.setItem(rowPosition, i, item)
            item.setTextAlignment(Qt.AlignHCenter)

    def load_to_lineedit(self):
        global previousValue
        global table
        #ENABLE BUTTONS
        self.ui.btn2_settings_delete.setDisabled(False)
        self.ui.btn3_settings_edit.setDisabled(False)
        #LOAD DATA
        global settings_lineEdit_input_list
        settings_lineEdit_input_list = []
        index= self.ui.settings_table.selectionModel().currentIndex()
        columns = self.ui.settings_table.columnCount()
        #Load data into list
        for i in range(columns):
            value = index.sibling(index.row(),i).data()
            #print(value)
            #print(type(value))
            settings_lineEdit_input_list.append(value)
        #Load from list to lineedits
        view = self.ui.database_stackedWidget.currentIndex()
        #print(view)
        if view == 0:
            self.ui.database_tables_le0.setText(settings_lineEdit_input_list[1])
        elif view == 1:
            self.ui.database_tables_le1.setText(settings_lineEdit_input_list[1])
            self.ui.database_tables_le2.setText(settings_lineEdit_input_list[2])
        elif view == 2:
            self.ui.database_tables_le3.setText(settings_lineEdit_input_list[1])
            print(settings_lineEdit_input_list[2])
            if settings_lineEdit_input_list[2] == 'Tak':
                self.ui.database_tables_radio1.setChecked(True)
            else:
                self.ui.database_tables_radio1.setChecked(False)
        previousValue = settings_lineEdit_input_list[1]

        if table == 'urlops':
            self.disableUrlopsDelete()

        if table == 'invalids':
            self.ui.btn1_settings_add.setDisabled(True)
            self.ui.btn2_settings_delete.setDisabled(True)
            self.ui.btn3_settings_edit.setDisabled(True)

    def disableUrlopsDelete(self):
        self.ui.btn1_settings_add.setDisabled(True)
        self.ui.btn2_settings_delete.setDisabled(True)
        self.ui.btn3_settings_edit.setDisabled(True)
        """index = (self.ui.settings_table.selectionModel().currentIndex())
        value = index.sibling(index.row(), 0).data()  # will return cell data
        record_id = int(value)
        if record_id in range(1,8,1):
            self.ui.btn2_settings_delete.setDisabled(True)
        else:
            self.ui.btn2_settings_delete.setDisabled(False)"""


    #Buttons operations:
    def insertSettingsRecord(self, table):
        if self.showDialog('Potwierdź operację','Czy na pewno chcesz dodać nową pozycję?','askConfirmation'):
            if table == 'cities':
                city_name = self.ui.database_tables_le0.text()
                if city_name == '' or city_name.isspace():
                    city_name = None
                print(city_name)
                values = (city_name,)
            elif table == 'education':
                edu_name = self.ui.database_tables_le1.text()
                if edu_name == '' or edu_name.isspace():
                    edu_name = None
                edu_years = self.ui.database_tables_le2.text()
                if edu_years == '' or edu_years.isspace():
                    edu_years = 0
                print(edu_name, edu_years)
                values = (edu_name,edu_years)
            elif table == 'agreements':
                agreement_name = self.ui.database_tables_le3.text()
                if agreement_name == '' or agreement_name.isspace():
                    agreement_name = None
                agreement_bool = self.ui.database_tables_radio1.isChecked()
                print(agreement_name, agreement_bool)
                values = (agreement_name, agreement_bool)
            elif table == 'invalids':
                invalid_name = self.ui.database_tables_le1.text()
                if invalid_name.isspace() or invalid_name =='':
                    invalid_name = None
                invalid_additional = self.ui.database_tables_le2.text()
                if invalid_additional.isspace() or invalid_additional == '':
                    invalid_additional = 0
                print(invalid_name, invalid_additional)
                values = (invalid_name, invalid_additional)
            elif table == 'urlops':
                urlop_name = self.ui.database_tables_le1.text()
                if urlop_name.isspace() or urlop_name == '':
                    urlop_name = None
                urlop_annual = self.ui.database_tables_le2.text()
                if urlop_annual == '':
                    urlop_annual = None
                print(urlop_name, urlop_annual)
                values = (urlop_name, urlop_annual)
            #EXECUTE COMMAND
            if db_settings_functions.insertSettingsRecord(table, values):
                newID = db_settings_functions.getNewRecordID(table)
                tmpList = [newID]
                for item in values:
                    tmpList.append(item)
                insertList = tuple(tmpList)
                print(insertList)
                self.add_Table(table,insertList)
                self.showDialog('Dodawanie zakończone', 'Rekord został dodany do bazy danych.','information')
            else:
                self.showDialog('Operacja przerwana', 'Wprowadzanie nowych danych zostało przerwane, sprawdź poprawność danych.',
                                'information')
    def deleteSettingsRecord(self, table):
        index = (self.ui.settings_table.selectionModel().currentIndex())
        index.row()  # gives current selected row.
        record_id = index.sibling(index.row(), 0).data()  # will return cell data
        print("Delete record from",table, record_id)
        if self.showDialog('Potwierdź operację','Czy na pewno chcesz usunąć wybrane dane?','askConfirmation'):
            if db_settings_functions.deleteSettingsRecord(table, record_id):
                self.ui.settings_table.removeRow(index.row())
                self.showDialog('Usuwanie zakończone', 'Rekord został usunięty z bazy danych.',
                                'information')
            else:
                self.showDialog('Błąd podczas usuwania', 'Wybrane dane są powiązane w bazie i nie można ich usunąć.',
                                'information')

    def UpdateSettingsRecord(self, table):
        if self.showDialog('Potwierdź operacje', 'Czy na pewno chcesz zmodyfikować rekord w bazie danych?', 'askConfirmation'):
            index = (self.ui.settings_table.selectionModel().currentIndex())
            index.row()  # gives current selected row.
            record_id = index.sibling(index.row(), 0).data()  # will return cell data
            print("Edit record in", table, record_id)

            values = self.getSettingsData(table,'updateDatabase')
            tmpValues = list(values)
            tmpValues.append(record_id)
            values = tuple(tmpValues)
            if db_settings_functions.updateSettingsRecord(table, values):
                self.updateSettingsRow()
                self.showDialog('Aktualizacja zakończona', 'Rekord został zmodyfikowany.',
                                'information')
            else:
                self.showDialog('Operacja przerwana', 'Aktualizacja danych nie była możliwa, sprawdź ponownie poprawność danych.',
                                'information')

    def updateSettingsRow(self):
        values = self.getSettingsData(table,'updateTable')
        index = self.ui.settings_table.selectionModel().currentIndex()
        print(self.ui.settings_table.columnCount())
        for i, column in enumerate(values):
            item = QtWidgets.QTableWidgetItem(str(column))
            self.ui.settings_table.setItem(index.row(), i+1, item)
            item.setTextAlignment(Qt.AlignHCenter)
        self.collectUpdateData(table)

    def collectUpdateData(self,table):
        pValue = previousValue
        if table == 'cities':
            nValue = self.ui.database_tables_le0.text()
            updateWorkerColumn(self.parent(),8,pValue,nValue)
        elif table == 'education':
            nValue = self.ui.database_tables_le1.text()
            updateWorkerColumn(self.parent(),10, pValue, nValue)
        #print(pValue,nValue)


    def getSettingsData(self,table,operationType):
        if table == 'cities':
            city_name = self.ui.database_tables_le0.text()
            # print(city_name)
            values = (city_name, )
            # print(values)
        elif table == 'education':
            edu_name = self.ui.database_tables_le1.text()
            edu_years = self.ui.database_tables_le2.text()
            if edu_years.isspace() or edu_years == '':
                edu_years = 0
            # print(edu_name, edu_years)
            values = (edu_name, edu_years, )
        elif table == 'agreements':
            agreement_name = self.ui.database_tables_le3.text()
            agreement_bool = self.ui.database_tables_radio1.isChecked()
            if operationType == 'updateTable':
                if agreement_bool:
                    agreement_bool = 'Tak'
                else:
                    agreement_bool = 'Nie'
            # print(agreement_name, agreement_bool)
            values = (agreement_name, agreement_bool, )
        elif table == 'invalids':
            invalid_name = self.ui.database_tables_le1.text()
            invalid_additional = self.ui.database_tables_le2.text()
            if invalid_additional.isspace() or invalid_additional == '':
                invalid_additional = 0
            # print(invalid_name, invalid_additional)
            values = (invalid_name, invalid_additional, )
        elif table == 'urlops':
            urlop_name = self.ui.database_tables_le1.text()
            urlop_annual = self.ui.database_tables_le2.text()
            if operationType == 'updateTable' and (urlop_annual == '' or urlop_annual == '0'):
                urlop_annual = ''
            elif urlop_annual == '' or urlop_annual == '0':
                urlop_annual = None
            # print(urlop_name, urlop_annual)
            values = (urlop_name, urlop_annual, )
        return values


    def restrictInputValues(self,windowType):
        letters_only = QRegularExpression("[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻżqQvV -]{0,40}")
        if windowType == 'cities':
            citieNames = self.ui.database_tables_le0
            citieNames.setValidator(QRegularExpressionValidator( QRegularExpression(letters_only), self ))
        if windowType == 'agreements':
            agreementNames = self.ui.database_tables_le3
            agreementNames.setValidator(QRegularExpressionValidator(QRegularExpression(letters_only), self))
        else:
            self.onlyInt = QIntValidator()
            self.ui.database_tables_le1.setValidator(QRegularExpressionValidator(QRegularExpression(letters_only), self))
            self.ui.database_tables_le2.setValidator(self.onlyInt)
            self.ui.database_tables_le2.setMaxLength(3)

    def showDialog(self,messageText,detailedText, messageOption):
        msg = QMessageBox()
        msg.setStyleSheet("""QLabel{min-width: 550px; min-height: 70px;color: white; }
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









