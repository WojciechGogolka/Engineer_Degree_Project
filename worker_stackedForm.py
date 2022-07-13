import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
#from modules.ui_add_form import Ui_AddWindow
from modules.ui_settings import Ui_SettingsWindow
from modules.ui_worker_stackedForm import Ui_WorkerForms
from widgets import CustomGrip
from database import db_connection
from database import db_worker_functions
from PySide6 import QtWidgets
import ast
from database.myconverter import MyConverter
from datetime import datetime
from database import db_urlops_functions

data = None
workerData = None
agreement_comboBox = None
disability_comboBox = None
urlop_comboBox = None
workerTableData = None
daysLimit = None
daysBilans = None
dateLimitCheck = False

urlopHours = None
urlopDays = None
paidLeave = None

class WorkerForms(QMainWindow):
    def __init__(self, parent):
        super(WorkerForms,self).__init__(parent)
        self.ui = Ui_WorkerForms()
        self.ui.setupUi(self)

        #STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Setting APP Name and top description

        # CONNECT DATE EDITS EVENTS
        self.ui.date_AgreementstartDate.dateChanged.connect(lambda : self.agreementsDateCheck('Start'))
        self.ui.date_AgreementEndDate.dateChanged.connect(lambda : self.agreementsDateCheck('End'))
        self.ui.date_ChildDateOfBirth.dateChanged.connect(lambda : self.childBirthdayCheck())
        self.ui.date_D_Start.dateChanged.connect(lambda : self.disabilityDateCheck('Start'))
        self.ui.date_D_End.dateChanged.connect(lambda : self.disabilityDateCheck('End'))

        #WORK HISTORY END
        self.ui.date_WH_Start.dateChanged.connect(lambda : self.workHistoryDateCheck())
        self.ui.date_WH_End.dateChanged.connect(lambda : self.workHistoryDateCheck())
        self.ui.date_U_DateStart.dateChanged.connect(lambda : self.urlopDateCheck())
        self.ui.date_U_DateEnd.dateChanged.connect(lambda: self.urlopDateCheck())

        # CONNECT LINE EDITS EVENTS
        self.ui.le_workTime.textChanged.connect(lambda : self.WorkTimeLimit())

        # CONNECT BUTTONS
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
        self.ui.button_U_calculate.clicked.connect(lambda : self.calculateDays())
        self.ui.worker_table.cellClicked.connect(lambda : self.loadDataFromTable())

        # CONNECT RADIO BUTTON
        self.ui.rb_A_Expiration.toggled.connect(lambda : self.agreementDateEnd())
        self.ui.rb_D_Expiration.toggled.connect(lambda : self.disabilityDateEnd())
        self.ui.rb_ChildParentID.toggled.connect(lambda : self.childParentChange())

        # CONNECT COMBOBOX
        self.ui.cb_urlop.currentIndexChanged.connect(lambda : self.urlopsTypeChanged())


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

    def setViewParameteres(self,viewMode, datalist):
        global workerData
        workerData = datalist
        # APPLY TITLE
        description = datalist[1] + ' ' + datalist[2]
        if viewMode == 'agreements':
            description += ' - Umowy'
        if viewMode == 'child':
            description += ' - Dzieci'
        if viewMode == 'invalid':
            description += ' - Karta niepełnosprawności'
        if viewMode == 'workhist':
            description += ' - Historia zatrudnienia'
        if viewMode == 'urlop':
            description += ' - Karta urlopowa'
        self.ui.titleRightInfo.setText(description)
        self.configurateWindow(viewMode)
        self.configurateTable(viewMode)
        self.downloadWorkerData(viewMode)

        self.restrictInputData(viewMode)


    def configurateWindow(self, viewMode):
        self.ui.btn1_workerForm_add.clicked.connect(lambda: self.addWorkerFormRecord(viewMode))
        self.ui.btn2_workerForm_delete.clicked.connect(lambda: self.deleteWorkerFormRecord(viewMode))
        if viewMode != 'child':
            self.ui.btn3_workerForm_edit.clicked.connect(lambda: self.updateDatabaseRecord(viewMode))

        if viewMode == 'agreements':
            self.ui.worker_stackedWidget.setCurrentIndex(0)
            self.ui.worker_groupBox_inputs.setTitle("Informacje o umowie")
            self.ui.bgApp.setFixedSize(900,600)
            self.ui.contentTopBg.setFixedSize(900,50)
            self.ui.worker_groupBox_inputs.setFixedSize(820,150)
            self.ui.cb_agreement.setFixedSize(265,35)
            self.agreementDateEnd()
            self.setNewAgreementStartDate()

            self.ui.le_workTime.setText('1')
            self.ui.le_workTime.setReadOnly(True)

        if viewMode == 'child':
            self.ui.worker_stackedWidget.setCurrentIndex(1)
            self.ui.worker_groupBox_inputs.setTitle("Informacje o dziecku")
            self.ui.bgApp.setFixedSize(700,650)
            self.ui.contentTopBg.setFixedSize(700,50)
            self.ui.worker_groupBox_inputs.setFixedSize(620,170)
            self.ui.cb_agreement.setFixedSize(265,35)
            self.ui.le_ChildParentID.setDisabled(True)
            self.ui.btn3_workerForm_edit.clicked.connect(lambda: self.updateChildRecord())

        if viewMode == 'invalid':
            self.ui.worker_stackedWidget.setCurrentIndex(2)
            self.ui.worker_groupBox_inputs.setTitle("Informacje o niepełnosprawności")
            self.ui.bgApp.setFixedSize(800,600)
            self.ui.contentTopBg.setFixedSize(800,50)
            self.ui.worker_groupBox_inputs.setFixedSize(720,150)
            #self.ui.cb_agreement.setFixedSize(265,35)
            self.disabilityDateEnd()

        if viewMode == 'workhist':
            self.ui.worker_stackedWidget.setCurrentIndex(3)
            self.ui.worker_groupBox_inputs.setTitle("Informacje o poprzednim zatrudnieniu")
            #self.ui.bgApp.setFixedSize(950,650)
            self.ui.worker_groupBox_inputs.setFixedSize(870,250)
            self.ui.cb_agreement.setFixedSize(265,35)
            self.workHistoryDateCheck()

        if viewMode == 'urlop':
            self.ui.worker_stackedWidget.setCurrentIndex(4)
            self.ui.worker_groupBox_inputs.setTitle("Parametry urlopu")
            self.ui.bgApp.setFixedWidth(941)
            self.ui.worker_groupBox_inputs.setFixedSize(875,150)
            self.ui.cb_urlop.setFixedSize(275,35)

            #INPUTS SIZE
            self.ui.cb_urlop.setFixedSize(265,45)
            self.ui.le_U_availableLimit.setFixedSize(125,45)
            self.ui.date_U_DateStart.setFixedSize(160,45)
            self.ui.date_U_DateEnd.setFixedSize(160, 45)
            self.ui.button_U_calculate.setFixedSize(100,55)
            self.ui.le_U_availableLimit.setReadOnly(True)

    def configurateTable(self, viewMode):
        # Setting multi view parameters-----------------------------------------------------------
        self.ui.worker_table.setFocusPolicy(Qt.NoFocus)
        self.ui.worker_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.worker_table.verticalHeader().setVisible(False)
        self.ui.worker_table.horizontalHeader().sectionPressed.disconnect()
        self.ui.worker_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.worker_table.setStyleSheet("""
            QHeaderView::section { color:white; background-color:#232326;} 
            QTableWidget { color:white; background: transparent; }
            QTableWidget { selection-color: rgb(255,255,255); selection-background-color:rgb(47, 49, 51); }""")

        # Initializing header configuration
        header = self.ui.worker_table.horizontalHeader()
        # header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setHighlightSections(False)

        # Setting table parameters
        # Table parameters
        if viewMode == 'agreements':
            #self.ui.worker_table.setFixedSize(875, 500)
            self.ui.worker_table.setColumnCount(5)
            self.ui.worker_table.setHorizontalHeaderLabels(['ID', 'Rodzaj umowy', 'Data rozpoczęcia','Data zakończenia','Wymiar pracy'])
            self.ui.worker_table.setColumnWidth(0, 80)
            self.ui.worker_table.setColumnWidth(1, 300)
            self.ui.worker_table.setColumnWidth(2, 190)
            self.ui.worker_table.setColumnWidth(3, 190)
            self.ui.worker_table.setColumnWidth(4, 108)
        elif viewMode == 'child':
            #self.ui.worker_table.setFixedSize(675, 500)
            self.ui.worker_table.setColumnCount(4)
            self.ui.worker_table.setHorizontalHeaderLabels(['ID', 'Imię dziecka', 'Nazwisko dziecka','Data urodzenia'])
            self.ui.worker_table.setColumnWidth(0, 80)
            self.ui.worker_table.setColumnWidth(1, 210)
            self.ui.worker_table.setColumnWidth(2, 210)
            self.ui.worker_table.setColumnWidth(3, 169)
        elif viewMode == 'invalid':
            #self.ui.worker_table.setFixedSize(675, 500)
            self.ui.worker_table.setColumnCount(4)
            self.ui.worker_table.setHorizontalHeaderLabels(['ID', 'Poziom niepełnosprawności', 'Data wydania oświadczenia','Data wygaśnięcia'])
            self.ui.worker_table.setColumnWidth(0, 80)
            self.ui.worker_table.setColumnWidth(1, 255)
            self.ui.worker_table.setColumnWidth(2, 250)
            self.ui.worker_table.setColumnWidth(3, 184)
        elif viewMode == 'workhist':
            #self.ui.worker_table.setFixedSize(925, 300)
            self.ui.worker_table.setColumnCount(10)
            header.setSectionResizeMode(QHeaderView.Interactive)
            self.ui.worker_table.setHorizontalHeaderLabels(['ID', 'Nazwa firmy', 'Data rozpoczęcia','Data zakończenia','Urlop płatny','Opieka nad dzieckiem','Urlop na żądanie','Urlop bezpłatny','Nieobecność nieusprawiedliwiona','Ekwiwalent'])
            self.ui.worker_table.setColumnWidth(0, 80)
            self.ui.worker_table.setColumnWidth(1, 300)
            self.ui.worker_table.setColumnWidth(2, 160)
            self.ui.worker_table.setColumnWidth(3, 160)
            self.ui.worker_table.setColumnWidth(4, 160)
            self.ui.worker_table.setColumnWidth(5, 180)
            self.ui.worker_table.setColumnWidth(6, 180)
            self.ui.worker_table.setColumnWidth(7, 180)
            self.ui.worker_table.setColumnWidth(8, 270)

        elif viewMode == 'urlop':
            #self.ui.worker_table.setFixedSize(915, 500)
            self.ui.worker_table.setColumnCount(6)
            self.ui.worker_table.setHorizontalHeaderLabels(['ID', 'Rodzaj urlopu', 'Data rozpoczęcia','Data zakończenia','Dni','Godziny'])
            self.ui.worker_table.setColumnWidth(0, 80)
            self.ui.worker_table.setColumnWidth(1, 285)
            self.ui.worker_table.setColumnWidth(2, 180)
            self.ui.worker_table.setColumnWidth(3, 180)
            self.ui.worker_table.setColumnWidth(4, 95)
            self.ui.worker_table.setColumnWidth(5, 89)
            self.ui.btn1_workerForm_add.setDisabled(True)

        #DISABLE EDIT BUTTONS
        self.ui.btn2_workerForm_delete.setDisabled(True)
        self.ui.btn3_workerForm_edit.setDisabled(True)

    def downloadWorkerData(self,viewMode):
        global data
        global workerData
        global agreement_comboBox
        global disability_comboBox
        global urlop_comboBox
        #DOWNLOAD WORKER AGREEMENTS-----------------------------------------
        if viewMode == 'agreements':
            data = db_worker_functions.downloadWorkerFormsData('agreements', workerData[0])
            agreement_comboBox = db_worker_functions.downloadComboBox('agreements')
            if agreement_comboBox is None:
                # Download data error
                print("No data here")
            else:
                self.loadToCombo('agreements',agreement_comboBox)

        #DOWNLOAD WORKER CHILD DATA
        elif viewMode == 'child':
            data = db_worker_functions.downloadWorkerFormsData('child', workerData[0])
        #DOWNLOAD WORKER DISABILITIES HISTORY-----------------------------
        elif viewMode == 'invalid':
            data = db_worker_functions.downloadWorkerFormsData('invalid', workerData[0])
            disability_comboBox = db_worker_functions.downloadComboBox('invalid')
            if disability_comboBox is None:
                # Download data error
                print("No data here")
            else:
                self.loadToCombo('invalid',disability_comboBox)
        #DOWNLOAD WORKER WORKHISTORY-------------------------------------
        elif viewMode == 'workhist':
            data = db_worker_functions.downloadWorkerFormsData('workhist', workerData[0])
        #DOWNLAOD WORKER URLOP HISTORY----------------------------------
        elif viewMode == 'urlop':
            data = db_worker_functions.downloadWorkerFormsData('urlop', workerData[0])
            urlop_comboBox = db_worker_functions.downloadComboBox('urlop')
            if urlop_comboBox is None:
                # Download data error
                print("No data here")
            else:
                self.loadToCombo('urlop',urlop_comboBox)

        #CHECKING IF DATA IS NONE
        if data is None:
            # Download data error
            print("No data here")
        else:
            for row in data:
                self.add_Table(MyConverter(row))

    def add_Table(self,columns):
        rowPosition = self.ui.worker_table.rowCount()
        self.ui.worker_table.insertRow(rowPosition)
        for i, column in enumerate(columns):
            #print(column)
            item = QtWidgets.QTableWidgetItem(str(column))
            if column == 'None':
                self.ui.worker_table.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(''))
            else:
                self.ui.worker_table.setItem(rowPosition, i, item)
            item.setTextAlignment(Qt.AlignHCenter)

    def updateFormRecord(self,values):
        index = self.ui.worker_table.selectionModel().currentIndex()
        for i, column in enumerate(values):
            item = QtWidgets.QTableWidgetItem(str(column))
            self.ui.worker_table.setItem(index.row(), i + 1, item)
            item.setTextAlignment(Qt.AlignHCenter)

    def childParentChange(self):
        if self.ui.rb_ChildParentID.isChecked():
            self.ui.le_ChildParentID.setDisabled(False)
        else:
            self.ui.le_ChildParentID.setDisabled(True)

    def loadToCombo(self, viewForm, comboData):
        self.ui.cb_agreement.clear()
        self.ui.cb_disability.clear()
        self.ui.cb_urlop.clear()
        if viewForm == 'agreements':
            agreements_list = []
            comboBox = self.ui.cb_agreement
            for row,column in enumerate(comboData):
                agreements_list.append(column[0])
            comboBox.addItems(agreements_list)
        elif viewForm == 'invalid':
            disability_comboBox = []
            comboBox = self.ui.cb_disability
            for row,column in enumerate(comboData):
                disability_comboBox.append(column[0])
            comboBox.addItems(disability_comboBox)
        elif viewForm == 'urlop':
            urlop_comboBox = []
            comboBox = self.ui.cb_urlop
            for row, column in enumerate(comboData):
                urlop_comboBox.append(column[0])
            comboBox.addItems(urlop_comboBox)

    def loadDataFromTable(self):
        global workerTableData
        workerTableData = []
        index = self.ui.worker_table.selectionModel().currentIndex()
        columns = self.ui.worker_table.columnCount()
        # LOAD DATA INTO LIST
        for i in range(columns):
            value = index.sibling(index.row(),i).data()
            workerTableData.append(value)
        # LOAD DATA INTO EDITS
        formView = self.ui.worker_stackedWidget.currentIndex()
        date_Start = None
        date_End = None
        # format
        format = '%Y-%m-%d'
        # WORKER'S AGREEMENT
        if formView == 0:
            self.ui.cb_agreement.setCurrentText(workerTableData[1])
            # CONVERTING DATE FROM STRING TO QDATEEDIT
            date_Start = workerTableData[2]
            date_Start_obj = datetime.strptime(date_Start, format)
            self.ui.date_AgreementstartDate.setDate(date_Start_obj)

            if not workerTableData[3] == '':
                date_End = workerTableData[3]
                date_End_obg = datetime.strptime(date_End, format)
                self.ui.date_AgreementEndDate.setDate(date_End_obg)
                self.ui.rb_A_Expiration.setChecked(True)
            else:
                self.ui.rb_A_Expiration.setChecked(False)
            self.ui.le_workTime.setText(workerTableData[4])

        # WORKER'S CHILD
        elif formView == 1:
            self.ui.le_ChildName.setText(workerTableData[1])
            self.ui.le_ChildLastname.setText(workerTableData[2])
            birth_Date = workerTableData[3]
            birth_Date_obj = datetime.strptime(birth_Date,format)
            self.ui.date_ChildDateOfBirth.setDate(birth_Date_obj)

        # WORKER'S DISABILITY
        elif formView == 2:
            self.ui.cb_disability.setCurrentText(workerTableData[1])
            # CONVERTING DATE FROM STRING TO QDATEEDIT
            date_Start = workerTableData[2]
            date_Start_obj = datetime.strptime(date_Start, format)
            self.ui.date_D_Start.setDate(date_Start_obj)
            if not workerTableData[3] == '':
                date_End = workerTableData[3]
                date_End_obj = datetime.strptime(date_End, format)
                self.ui.date_D_End.setDate(date_End_obj)
                self.ui.rb_D_Expiration.setChecked(True)
            else:
                self.ui.rb_D_Expiration.setChecked(False)

        # WORKER'S WORK HISTORY
        elif formView == 3:
            self.ui.le_WH_CompanyName.setText(workerTableData[1])
            # CONVERTING DATE FROM STRING TO QDATEEDIT
            date_Start = workerTableData[2]
            date_Start_obj = datetime.strptime(date_Start, format)
            self.ui.date_WH_Start.setDate(date_Start_obj)
            date_End = workerTableData[3]
            date_End_obg = datetime.strptime(date_End, format)
            self.ui.date_WH_End.setDate(date_End_obg)
            #used_urlops = [le_WH_PaidLeave, le_WH_Childcare, le_WH_Requested, le_WH_Unpaid, le_WH_Absence, le_WH_Equivalent]
            #LOAD USED DAYS
            self.ui.le_WH_PaidLeave.setText(workerTableData[4])
            self.ui.le_WH_Childcare.setText(workerTableData[5])
            self.ui.le_WH_Requested.setText(workerTableData[6])
            self.ui.le_WH_Unpaid.setText(workerTableData[7])
            self.ui.le_WH_Absence.setText(workerTableData[8])
            self.ui.le_WH_Equivalent.setText(workerTableData[9])

        # WORKER'S URLOPS
        elif formView == 4:
            self.ui.cb_urlop.setCurrentText(workerTableData[1])
            # CONVERTING DATE FROM STRING TO QDATEEDIT
            date_Start = workerTableData[2]
            date_Start_obj = datetime.strptime(date_Start, format)
            self.ui.date_U_DateStart.setDate(date_Start_obj)
            if not workerTableData[3] == '':
                date_End = workerTableData[3]
                date_End_obg = datetime.strptime(date_End, format)
                self.ui.date_U_DateEnd.setDate(date_End_obg)

        #ENABLE EDIT BUTTONS
        self.ui.btn2_workerForm_delete.setDisabled(False)
        if not formView == 4:
            self.ui.btn3_workerForm_edit.setDisabled(False)

    def addWorkerFormRecord(self, table):
        if self.showDialog('Potwierdź operację', 'Czy na pewno chcesz dodać nową pozycję do bazy danych?', 'askConfirmation'):
                insertList = self.getData(table, 'updateDatabase')
                # print(insertList)
                if db_worker_functions.insertWorkerFormRecord(table, insertList):
                    newRecordID = db_worker_functions.getNewFormRecordID(table)
                    updateList = self.getData(table,'updateTable')
                    tmpList = [newRecordID]
                    for item in updateList:
                        tmpList.append(item)
                    updateList = tuple(tmpList)
                    self.add_Table(updateList)
                    self.showDialog('Dodawanie zakończone', 'Nowy rekord został dodany do bazy danych', 'information')

                else:
                    self.showDialog('Operacja przerwana', 'Podane dane są niepoprawne, sprawdź wszystkie pola przed powtórzeniem operacji.', 'information')

    def deleteWorkerFormRecord(self, table):
        # GET INDEX VALUE
        record_id = self.getTableIndex()
        #DELETE DATA FROM DATABASE
        if self.showDialog('Potwierdź operację', 'Czy na pewno chcesz usunąć wybraną pozycję? Operacja ta będzie nieodwracalna.', 'askConfirmation'):
            if db_worker_functions.deleteWorkerFormRecord(table, record_id):
                index = (self.ui.worker_table.selectionModel().currentIndex())
                self.ui.worker_table.removeRow(index.row())
                self.showDialog('Usuwanie zakończone', 'Dane zostały usunięte.', 'information')
            else:
                self.showDialog('Operacja przerwana',"Nie można było usunąć wybranych danych.",'information')

    def updateDatabaseRecord(self, table):
        #GET DATA FROM INLINES
        editList = self.getData(table, 'updateDatabase')
        #GET INDEX VALUE
        record_id = self.getTableIndex()
        #EDIT DATA IN DATABASE
        #print(record_id,editList)
        if self.showDialog('Potwierdź operację','Czy na pewno chcesz zmodyfikować wybrane dane?','askConfirmation'):
            if db_worker_functions.updateWorkerFormRecord(table, record_id, editList):
                updateList = self.getData(table, 'updateTable')
                print('update list:',updateList)
                self.updateFormRecord(updateList)
                self.showDialog('Operacja zakończona', 'Dane w bazie danych zostały zmodyfikowane', 'information')
            else:
                self.showDialog('Operacja przewana',
                                'Wprowadzone dane są niepoprawne, sprawdź wszystkie pola przed powtórzeniem operacji',
                                'information')

    def updateChildRecord(self):
        newParentID = self.ui.le_ChildParentID.text()
        #print('New ID ',newParentID)
        #print(self.ui.rb_ChildParentID.isChecked())
        if self.showDialog('Potwierdź operację', 'Czy na pewno chcesz zmodyfikować dane dziecka?', 'askConfirmation'):
            if self.ui.rb_ChildParentID.isChecked():
                idFromDatabase = db_worker_functions.getParentID(newParentID)
                print(idFromDatabase)
                if idFromDatabase:
                    # ADD DATA TO LIST
                    childID = self.getTableIndex()
                    #print(newParentID)
                    # GET CHILD DATA
                    editList = self.getData('child', 'updateDatabase')
                    dataList = [newParentID]
                    tempList = list(editList)
                    tempList.pop(0)
                    for item in tempList:
                        dataList.append(item)
                    dataList.append(childID)
                    values = tuple(dataList)
                    #print(dataList)
                    if db_worker_functions.updateChildParent(values):
                        index = (self.ui.worker_table.selectionModel().currentIndex())
                        self.ui.worker_table.removeRow(index.row())
                        self.showDialog('Operacja ukończona', 'Dziecko zostało przypisane nowemu rodzicowi.', 'information')
                else:
                    self.showDialog('Operacja przerwana', 'Nie ma pracownika o wskazanym ID.', 'information')
            else:
                self.updateDatabaseRecord('child')

    def getTableIndex(self):
        index = (self.ui.worker_table.selectionModel().currentIndex())
        index.row()  # gives current selected row.
        record_id = index.sibling(index.row(), 0).data()  # will return cell data
        return record_id

    def getData(self, table, operationType):
        if table == 'agreements':
            # GET AGREEMENT ID
            agreementName = self.ui.cb_agreement.currentText()
            agreementID = db_worker_functions.getComboID('agreements', agreementName)
            # GET AGREEMENT DATA
            workStart = self.ui.date_AgreementstartDate.date().toString(Qt.ISODate)
            if self.ui.rb_A_Expiration.isChecked():
                workEnd = self.ui.date_AgreementEndDate.date().toString(Qt.ISODate)
            else:
                if operationType == 'updateDatabase':
                    workEnd = None
                else:
                    workEnd = ''
            workTime = self.ui.le_workTime.text()
            # ADD DATA TO LIST
            if operationType == 'updateDatabase':
                dataList = (workerData[0], agreementID, workStart, workEnd, workTime)
            else:
                dataList = (agreementName,workStart,workEnd,workTime)


        elif table == 'child':
            # GET CHILD DATA
            childName = self.ui.le_ChildName.text()
            childLastName = self.ui.le_ChildLastname.text()
            childBirthDay = self.ui.date_ChildDateOfBirth.date().toString(Qt.ISODate)
            # ADD DATA TO LIST
            if operationType == 'updateDatabase':
                dataList = (workerData[0], childName, childLastName, childBirthDay)
            else:
                dataList = (childName, childLastName, childBirthDay)

        elif table == 'invalid':
            # GET INVALID STATUS ID
            disabilityName = self.ui.cb_disability.currentText()
            disabilityID = db_worker_functions.getComboID('invalid', disabilityName)
            # GET INVALID DATA
            disabilityStart = self.ui.date_D_Start.date().toString(Qt.ISODate)
            if self.ui.rb_D_Expiration.isChecked():
                disabilityEnd = self.ui.date_D_End.date().toString(Qt.ISODate)
            else:
                if operationType == 'updateDatabase':
                    disabilityEnd = None
                else:
                    disabilityEnd = ''
            # ADD DATA TO LIST
            if operationType == 'updateDatabase':
                dataList = (workerData[0], disabilityID, disabilityStart, disabilityEnd)
            else:
                dataList = (disabilityName, disabilityStart, disabilityEnd)

        elif table == 'workhist':
            companyName = self.ui.le_WH_CompanyName.text()
            whStartDate = self.ui.date_WH_Start.date().toString(Qt.ISODate)
            whEndDate = self.ui.date_WH_End.date().toString(Qt.ISODate)
            whPaidLeave = self.ui.le_WH_PaidLeave.text()
            whChildCare = self.ui.le_WH_Childcare.text()
            whRequested = self.ui.le_WH_Requested.text()
            whUnpaid = self.ui.le_WH_Unpaid.text()
            whAbsence = self.ui.le_WH_Absence.text()
            whEquivalent = self.ui.le_WH_Equivalent.text()
            # ADD DATA TO LIST
            if operationType == 'updateDatabase':
                dataList = (workerData[0],companyName,whStartDate,whEndDate,whPaidLeave,whChildCare,whRequested,whUnpaid,whAbsence,whEquivalent)
            else:
                dataList = (companyName, whStartDate, whEndDate, whPaidLeave, whChildCare, whRequested, whUnpaid, whAbsence, whEquivalent)

        elif table == 'urlop':
            # GET URLOP NAME ID
            urlopName = self.ui.cb_urlop.currentText()
            urlopID = db_worker_functions.getComboID('urlop',urlopName)
            # GET URLOP DATA
            urlopStart = self.ui.date_U_DateStart.date().toString(Qt.ISODate)
            urlopEnd = self.ui.date_U_DateEnd.date().toString(Qt.ISODate)
            # ADD DATA TO LIST
            if operationType == 'updateDatabase':
                dataList = (workerData[0], urlopID, urlopStart, urlopEnd, urlopDays,urlopHours)
            else:
                dataList = ( urlopName, urlopStart, urlopEnd, urlopDays,urlopHours)
            self.ui.btn1_workerForm_add.setDisabled(True)
            self.ui.btn3_workerForm_edit.setDisabled(True)

        if operationType == 'updateDatabase':
            forList = list(dataList)
            print('Rzutowanie na liste', dataList)
            tmpList = []
            for item in forList:
                try:
                    if item.isspace() or item == '':
                        item = None
                except:
                    pass
                print(item)
                tmpList.append(item)
            print(tmpList)
            dataList = tuple(tmpList)
        return dataList

    def restrictInputData(self, tableView):
        letters_only = QRegularExpression(
            "[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻżqQvVxX -]{0,50}")
        if tableView == 'agreements':
            workTime = QRegularExpression("[.0123456789]{0,4}")
            self.ui.le_workTime.setValidator(QRegularExpressionValidator(QRegularExpression(workTime), self))
        elif tableView == 'child':
            self.ui.le_ChildName.setValidator(QRegularExpressionValidator(QRegularExpression(letters_only), self))
            self.ui.le_ChildLastname.setValidator(QRegularExpressionValidator(QRegularExpression(letters_only), self))
            parentID = QRegularExpression("[0123456789]{0,4}")
            self.ui.le_ChildParentID.setValidator(QRegularExpressionValidator(QRegularExpression(parentID), self))
        elif tableView == 'workhist':
            self.ui.le_WH_CompanyName.setValidator(QRegularExpressionValidator(QRegularExpression(letters_only), self))

    def setNewAgreementStartDate(self):
        dateEnd = db_worker_functions.getLastAgreement(workerData[0])
        if dateEnd == None:
            pass
        else:
            self.ui.date_AgreementstartDate.setDate(dateEnd)

    def agreementsDateCheck(self, type):
        contractStart = self.ui.date_AgreementstartDate.date()
        contractEnd = self.ui.date_AgreementEndDate.date()
        endCheck = self.ui.rb_A_Expiration.isChecked()
        if type == 'Start' and contractEnd < contractStart:
            self.ui.date_AgreementEndDate.setDate(contractStart)
        if type == 'End' and endCheck and contractEnd < contractStart:
            self.ui.date_AgreementEndDate.setDate(contractStart)

    def disabilityDateCheck(self,type):
        disabilityCheck = self.ui.rb_D_Expiration.isChecked()
        disabilityStart = self.ui.date_D_Start.date()
        disabilityEnd = self.ui.date_D_End.date()
        if type == 'Start' and disabilityEnd < disabilityStart:
            self.ui.date_D_End.setDate(disabilityStart)
        if type == 'End' and disabilityCheck and disabilityEnd < disabilityStart:
            self.ui.date_D_End.setDate(disabilityStart)

    def childBirthdayCheck(self):
        birthday = self.ui.date_ChildDateOfBirth.date()
        today = QDate.currentDate()
        if birthday > today:
            self.ui.date_ChildDateOfBirth.setDate(today)

    def workHistoryDateCheck(self):
        workStart = self.ui.date_WH_Start.date()
        workEnd = self.ui.date_WH_End.date()
        yearCurrent = QDate.currentDate().year()
        if workEnd < workStart:
            self.ui.date_WH_End.setDate(workStart)
        if workEnd.year() != yearCurrent:
            self.workHistInput(True)
        else:
            self.workHistInput(False)

    def workHistInput(self,bool):
        self.ui.le_WH_PaidLeave.setDisabled(bool)
        self.ui.le_WH_Childcare.setDisabled(bool)
        self.ui.le_WH_Requested.setDisabled(bool)
        self.ui.le_WH_Equivalent.setDisabled(bool)

    def agreementDateEnd(self):
        checkStatus = self.ui.rb_A_Expiration.isChecked()
        if checkStatus:
            self.ui.date_AgreementEndDate.setReadOnly(False)
        else:
            self.ui.date_AgreementEndDate.setReadOnly(True)

    def disabilityDateEnd(self):
        checkStatus = self.ui.rb_D_Expiration.isChecked()
        if checkStatus:
            self.ui.date_D_End.setReadOnly(False)
        else:
            self.ui.date_D_End.setReadOnly(True)

    def WorkTimeLimit(self):
        value = self.ui.le_workTime.text()
        try:
            floatValue = float(value)
            #print(floatValue)
            if floatValue and floatValue > 1:
                self.ui.le_workTime.setText("1")
        except:
            pass

    def urlopsTypeChanged(self):
        global daysLimit
        global daysBilans
        global dateLimitCheck
        global paidLeave
        currentIndex = self.ui.cb_urlop.currentIndex()
        print('Actual comboBox index',currentIndex)
        dateStart = self.ui.date_U_DateStart
        daysUsed = None
        if currentIndex == 0: #PAID LEAVE!
            print('calculating #PAID LEAVE')
            daysLimit = db_urlops_functions.getWorkerUrlopDays(workerData[0])
            #DAYS USED REQUESTED---------------------------------------------------------------
            daysUsedReq = db_urlops_functions.checkUsedUrlop(3,
                workerData[0]) + db_urlops_functions.checkWorkHistory(
                'requested', workerData[0])
            if daysUsedReq == False:
                daysUsedReq =0
            #DAYS USED PAID URLOP--------------------------------------------------------------
            daysUsedPaid = db_urlops_functions.checkUsedPaidUrlop(workerData[0])
            if daysUsedPaid == False:
                daysUsedPaid = 0
            #ADDITIONAL DISABILITY URLOP-------------------------------------------------------
            disabilityIndexList = db_urlops_functions.getDisabilityWorkerList(workerData[0])
            print(disabilityIndexList)
            if disabilityIndexList != []:
                print('lista indexow niepelnosprawnosci', disabilityIndexList)
                disabilityDays = self.countDisabilityDays(disabilityIndexList)
            else:
                print('Brak wpisów')
                disabilityDays = 0
            print('limit',daysLimit,daysUsedPaid,daysUsedReq,disabilityDays)
            daysBilans = daysLimit - daysUsedPaid - daysUsedReq + disabilityDays
            self.ui.le_U_availableLimit.setText(str(daysBilans))
            paidLeave = daysBilans
        #----------------------------------------------------------------------------------------------------
        if currentIndex == 1: # CHILDCARE
            print('calculating CHILDCARE')
            daysUsed = db_urlops_functions.checkUsedUrlop(currentIndex+1, workerData[0]) + db_urlops_functions.checkWorkHistory('childcare',workerData[0])
            daysLimit = db_urlops_functions.checkWorkerChilds(workerData[0])
            daysBilans = daysLimit - daysUsed

            if daysLimit == False:
                self.ui.le_U_availableLimit.setText(str('0'))
            else:
                self.ui.le_U_availableLimit.setText(str(daysBilans))
        # ----------------------------------------------------------------------------------------------------
        if currentIndex == 2: # REQUESTED
            print('calculating REQUESTED')
            daysUsed = db_urlops_functions.checkUsedUrlop(currentIndex+1, workerData[0]) + db_urlops_functions.checkWorkHistory('requested',workerData[0])
            daysLimit = db_urlops_functions.checkRequestedUrlopDateAmmount()
            daysBilans = daysLimit - daysUsed
            print(daysUsed,daysLimit,daysBilans)
            self.ui.le_U_availableLimit.setText(str(daysBilans))
        # ----------------------------------------------------------------------------------------------------
        if currentIndex == 3: # CIRCUMSTANCES
            print('calculating CIRCUMSTANCES')
            dateLimitCheck = True
            self.ui.le_U_availableLimit.setText(str(''))
        # ----------------------------------------------------------------------------------------------------
        if currentIndex == 4: # UNPAID
            print('calculating UNPAID')
            self.ui.le_U_availableLimit.setText(str(''))
        if currentIndex == 5: # EQUIVALENT
            print('calculating EQUIVALENT')
            dateLimitCheck = True
            self.ui.le_U_availableLimit.setText(str(paidLeave))

    def countDisabilityDays(self,disabilityIndexList):
        tempList = []
        disability_days = 0
        for i, column in enumerate(disabilityIndexList):
            tempList.append(column[0])
            print('DISABILITY INDEX:', column[0])
        for index,item in enumerate(tempList):
            if item == tempList[0]:
                print(workerData[0],0,item)
                daysLimit = int(db_urlops_functions.getDisabilityDays(workerData[0],0,item))
            else:
                print(workerData[0],tempList[index-1],item)
                daysLimit = int(db_urlops_functions.getDisabilityDays(workerData[0],tempList[index-1],item))
            disability_days += daysLimit
        print(disability_days)
        return disability_days

    def urlopDateCheck(self):
        currentIndex = self.ui.cb_urlop.currentIndex()
        uStart = self.ui.date_U_DateStart.date()
        uEnd = self.ui.date_U_DateEnd.date()
        #print(dateLimitCheck)
        if currentIndex == 3:
            wy = uStart.year()
            wm = uStart.month()
            wd = uStart.day() + 1
            maxDate = QDate(wy, wm, wd)
            self.ui.date_U_DateEnd.setMaximumDate(maxDate)
            if uEnd < uStart:
                self.ui.date_U_DateEnd.setDate(uStart)
        elif currentIndex == 5:
            self.ui.date_U_DateEnd.setDate(uStart)
        else:
            maxDate = QDate(2999, 12, 31)
            self.ui.date_U_DateEnd.setMaximumDate(maxDate)
            if uEnd < uStart:
                self.ui.date_U_DateEnd.setDate(uStart)

    def calculateDays(self):
        workStart = self.ui.date_U_DateStart.date()
        workEnd = self.ui.date_U_DateEnd.date()
        daysCount = workStart.daysTo(workEnd) + 1
        #print(daysCount)
        #print(daysLimit)
        # DEFINE GLOBAL VARIABLES USED TO INSERT/EDIT DATA IN DATABASE
        global urlopHours
        global urlopDays
        currentIndex = self.ui.cb_urlop.currentIndex()

        if currentIndex == 5:
            if self.showDialog('Potwierdź operację',
                               'Zamierzasz dodać: ' + self.ui.cb_urlop.currentText() + ',\nNa długość: ' +
                               str(paidLeave) + ' dni, ' + str((paidLeave) * 8) + ' godzin.',
                               'askConfirmation'):
                self.ui.btn1_workerForm_add.setDisabled(False)
                self.ui.btn3_workerForm_edit.setDisabled(False)
                urlopHours = paidLeave * 8
                urlopDays = paidLeave

        if  daysBilans - daysCount >= 0:
            if self.showDialog('Potwierdź operację',
                               'Zamierzasz dodać: ' + self.ui.cb_urlop.currentText() + ',\nNa długość: ' +
                                       str(daysCount) + ' dni, ' +str((daysCount)*8)+' godzin.',
                               'askConfirmation'):

                self.ui.btn1_workerForm_add.setDisabled(False)
                self.ui.btn3_workerForm_edit.setDisabled(False)
                urlopHours = daysCount * 8
                urlopDays = daysCount
        else:
            if self.showDialog('Ostrzeżenie',
                               'Przekroczono dostępny limit dni do wykorzystania, czy na pewno chcesz kontynuować?',
                               'askConfirmation'):
                if self.showDialog('Potwierdź operację',
                               'Zamierzasz dodać: ' + self.ui.cb_urlop.currentText() + ',\nNa długość: ' +
                                       str(daysCount) + ' dni, ' +str((daysCount)*8)+' godzin.',
                               'askConfirmation'):
                    self.ui.btn1_workerForm_add.setDisabled(False)
                    self.ui.btn3_workerForm_edit.setDisabled(False)
                    urlopIndex = currentIndex
                    urlopHours = daysCount * 8
                    urlopDays = daysCount


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


