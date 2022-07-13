import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
#from modules.ui_add_form import Ui_AddWindow
from modules.ui_add_form import Ui_AddWindow
from widgets import CustomGrip
from database import db_worker_functions
from PySide6 import QtWidgets
import ast
from database.myconverter import MyConverter
from datetime import datetime
from modules.updateMainTable import updateWorker
from modules.updateMainTable import addNewWorkerRow

worker_id = None

class AddWindow(QMainWindow):
    def __init__(self, parent):
        super(AddWindow, self).__init__(parent)
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self)

        #STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Setting APP Name and top description

        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
        self.ui.bt_EditWorker.clicked.connect(lambda : self.updateWorkerData(worker_id))
        self.ui.bt_addWorker.clicked.connect(lambda : self.addNewWorkerDatabase())

        # RADIO BUTTONS SELECTION EVENTS
        self.ui.rb_invalid.toggled.connect(lambda : self.invalidButtonStatus())
        self.ui.rb_foreigner.toggled.connect(lambda : self.foreignerButtonStatus())
        self.ui.rb_invalidEnd.toggled.connect(lambda : self.invalidDateEnd())
        self.ui.rb_contractEnd.toggled.connect(lambda : self.contractDateEnd())

        # CONNECT DATE EDITS EVENTS
        self.ui.date_birthdayAdd.dateChanged.connect(lambda : self.birthdayCheck())
        self.ui.date_contractStart.dateChanged.connect(lambda : self.agreementCheck('Start'))
        self.ui.date_contractEnd.dateChanged.connect(lambda: self.agreementCheck('End'))
        self.ui.date_disabilityStart.dateChanged.connect(lambda: self.disabilityCheck('Start'))
        self.ui.date_disabilityEnd.dateChanged.connect(lambda: self.disabilityCheck('End',))

        # CONNECT LINE EDITS EVENTS
        self.ui.le_workTime.textChanged.connect(lambda : self.WorkTimeLimit())

        #Setting FORM Name and top description
        description = "Dodaj nowego pracownika"
        # APPLY TEXTS
        self.ui.titleRightInfo.setText(description)

        # LOAD COMBOBOXES
        self.downloadComboAgreements()
        self.downloadComboCities()
        self.downloadComboEducation()
        self.downloadComboInvalid()
        self.setForeignerCombo()

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


    # DECLARING WIDGET VIEWS PARAMETERS--------------------------------------------------------
    # EDIT VIEW
    def editView(self,datalist):
        #SETTING WINDOW PARAMETERS
        self.ui.styleSheet.setFixedHeight(770)
        #SETTING WINDOW PERSONALIZED DESCRIPTION
        global worker_id
        worker_id = datalist[0]
        self.ui.stackedWidget.setCurrentIndex(1)
        description = datalist[1] + ' ' + datalist[2] + ' - dane personalne'
        #print(description)
        #APPLY TEXTS
        self.ui.titleRightInfo.setText(description)
        # LOAD WORKER DATA
        self.loadDataFromTable(datalist)

        #INITIALIZE INSERT VALUES RESTRICTION
        self.restrictInputValues('edit')

    # ADD VIEW
    def addView(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        # DISABLE INVALID OPTIONS ON START
        self.ui.bgApp.setFixedSize(540, 880)
        self.ui.gB3_disability.setVisible(False)
        self.ui.date_disabilityEnd.setReadOnly(True)
        self.ui.date_contractEnd.setReadOnly(True)
        #SET INPUTS WIDTH
        self.ui.cb_cityAdd.setFixedWidth(226)
        self.ui.cb_contractAdd.setFixedWidth(265)
        self.ui.le_nameAdd.setFixedWidth(265)
        self.ui.le_lastnameAdd.setFixedWidth(265)
        self.ui.le_peselAdd.setFixedWidth(225)
        self.ui.le_addressAdd.setFixedWidth(225)
        self.ui.le_zipAdd.setFixedWidth(225)
        self.ui.le_phoneAdd.setFixedWidth(225)
        self.ui.date_birthdayAdd.setFixedWidth(225)
        self.ui.cb_educationAdd.setFixedWidth(225)
        self.ui.le_workTime.setFixedWidth(225)
        self.ui.date_contractStart.setFixedWidth(225)
        self.ui.date_contractEnd.setFixedWidth(225)
        self.ui.cb_disabilityAdd.setFixedWidth(205)
        self.ui.date_disabilityStart.setFixedWidth(205)
        self.ui.date_disabilityEnd.setFixedWidth(205)

        self.ui.le_workTime.setText('1')
        self.ui.le_workTime.setReadOnly(True)

        #INITIALIZE INSERT VALUES RESTRICTION
        self.restrictInputValues('add')


    # DOWNLOAD DATA TO COMBO BOXES-------------------------------------------------------------
    def downloadComboAgreements(self):
        agreements = db_worker_functions.downloadComboBox('agreements')
        agreements_list = self.loadDataToCombo(agreements)
        self.ui.cb_contractAdd.addItems(agreements_list)

    def downloadComboCities(self):
        cities = db_worker_functions.downloadComboBox('city')
        cities_list = self.loadDataToCombo(cities)
        self.ui.cb_city.addItems(cities_list)
        self.ui.cb_cityAdd.addItems(cities_list)

    def downloadComboEducation(self):
        education = db_worker_functions.downloadComboBox('education')
        education_list = self.loadDataToCombo(education)
        self.ui.cb_education.addItems(education_list)
        self.ui.cb_educationAdd.addItems(education_list)

    def downloadComboInvalid(self):
        disability = db_worker_functions.downloadComboBox('invalid')
        invalid_list = self.loadDataToCombo(disability)
        self.ui.cb_disabilityAdd.addItems(invalid_list)

    def loadDataToCombo(self,receivedList):
        tmpList = []
        for row, column in enumerate(receivedList):
            tmpList.append(column[0])
        return tmpList
    # ----------------------------------------------------------------------------------------

    # RADIO BUTTONS FUNCTIONS
    def invalidButtonStatus(self):
        r_button = self.ui.rb_invalid
        if r_button.isChecked():
            print("Disability card Enabled")
            self.ui.gB3_disability.setVisible(True)
            self.ui.bgApp.setFixedSize(540,1065)
        else:
            print("Disability card Disabled")
            self.ui.gB3_disability.setVisible(False)
            self.ui.bgApp.setFixedSize(540, 880)

    def foreignerButtonStatus(self):
        if self.ui.rb_foreigner.isChecked():
            return 1
        else:
            return 0

    def invalidDateEnd(self):
        rb_invalid = self.ui.rb_invalidEnd
        if rb_invalid.isChecked():
            self.ui.date_disabilityEnd.setReadOnly(False)
        else:
            self.ui.date_disabilityEnd.setReadOnly(True)

    def contractDateEnd(self):
        rb_contract = self.ui.rb_contractEnd
        if rb_contract.isChecked():
            self.ui.date_contractEnd.setReadOnly(False)
        else:
            self.ui.date_contractEnd.setReadOnly(True)

    # ----------------------------------------------------------------------------------------

    # GET IDs FROM COMBOBOXES
    def getComboID(self, comboBox, comboType):
        comboName = comboBox.currentText()
        comboID = db_worker_functions.getComboID(comboType, comboName)
        return comboID

    # ----------------------------------------------------------------------------------------

    def setForeignerCombo(self):
        foreignerList = ["Tak","Nie"]
        self.ui.cb_foreigner.addItems(foreignerList)

    # -------------------------------------------------------------------------------------------------------------------
    # COLLECT INFORMATIONS ABOUT NEW WORKER
    def addNewWorkerDatabase(self):
        personalDataList = self.getNewWorkerData('insertDatabase')
        if personalDataList == False:
            pass
        else:
             # ADD WORKER TO DATABASE-------------------------------------------
            if self.showDialog('Potwierdź wykonanie operacji','Czy napewno chcesz dodać nowego pracownika do bazy danych?','askConfirmation'):
                if db_worker_functions.addNewWorker(personalDataList):
                    # GET NEW WORKER ID
                    newWorkerID = db_worker_functions.getNewWorkerID()
                    self.addNewWorkerAgreement(newWorkerID)
                    if self.ui.rb_invalid.isChecked():
                        self.addNewWorkerDisability(newWorkerID)
                    self.addNewWorkerTable(newWorkerID)
                    self.showDialog('Dodawanie zakończone', 'Nowy pracownik został dodany do bazy danych.','information')
                    self.close()
                else:
                    self.showDialog('Operacja przerwana','Wprowadzone dane są niepoprawne.','information')
    # -------------------------------------------------------------------------------------------------------------------

    def addNewWorkerAgreement(self,newWorkerID):
        #COLLECT WORKER AGREEMENT DATA
        agreement = self.ui.cb_contractAdd
        workerAgreement = self.getComboID(agreement, 'agreements')
        workerAgreementStart = self.ui.date_contractStart.date().toString(Qt.ISODate)
        if self.ui.rb_contractEnd.isChecked():
            workerAgreementEnd = self.ui.date_contractEnd.date().toString(Qt.ISODate)
        else:
            workerAgreementEnd = None
        workerWorkTime = self.ui.le_workTime.text()

        agreementDataList = (newWorkerID, workerAgreement, workerAgreementStart, workerAgreementEnd, workerWorkTime)
        #ADD NEW WORKER AGREEMENT TO DATABASE
        db_worker_functions.insertWorkerFormRecord('agreements',agreementDataList)

    def addNewWorkerDisability(self,newWorkerID):
        #LOAD DATA FROM DISABILITY GROUPBOX IF CHECKED
        ivalid = self.ui.cb_disabilityAdd
        workerDisability = self.getComboID(ivalid,'invalid')
        workerDisabilityStart = self.ui.date_disabilityStart.date().toString(Qt.ISODate)
        workerDisabilityEnd = self.ui.date_disabilityEnd.date().toString(Qt.ISODate)
        if self.ui.rb_invalidEnd.isChecked():
            workerDisabilityEnd = self.ui.date_disabilityEnd.date().toString(Qt.ISODate)
        else:
            workerDisabilityEnd = None
        disabilityDataList = (newWorkerID, workerDisability, workerDisabilityStart, workerDisabilityEnd)
        #print(disabilityDataList)
        db_worker_functions.insertWorkerFormRecord('invalid',disabilityDataList)
    #-------------------------------------------------------------------------------------------------------------------
    # INSERT NEW WORKER INTO TABLE
    def addNewWorkerTable(self,newWorkerID):
        personalDataList = self.getNewWorkerData('insertTable')
        tmpList = [newWorkerID]
        for item in personalDataList:
            tmpList.append(item)
        personalDataList = tuple(tmpList)
        addNewWorkerRow(self.parent(), personalDataList)
        #self.close()
    # -------------------------------------------------------------------------------------------------------------------
    # INSERT WORKER DATA
    def getNewWorkerData(self, operationType):
        workerName = self.ui.le_nameAdd.text()
        if workerName.isspace() or workerName == '':
            self.showDialog('Błąd podczas wprowadzania danych', 'Pole imienia nie może być puste ani zawierać tylko białych znaków.','information')
            return False
        workerLastname = self.ui.le_lastnameAdd.text()
        if workerLastname.isspace() or workerLastname == '':
            self.showDialog('Błąd podczas wprowadzania danych', 'Pole nazwiska nie może być puste ani zawierać tylko białych znaków.','information')
            return False
        workerBirthday = self.ui.date_birthdayAdd.date().toString(Qt.ISODate)
        workerPESEL = self.ui.le_peselAdd.text()
        if workerPESEL == '':
            self.showDialog('Błąd podczas wprowadzania danych', 'Pole PSESEL nie może być puste.','information')
            return False
        workerAddress = self.ui.le_addressAdd.text()
        if workerAddress.isspace() or workerAddress == '':
            self.showDialog('Błąd podczas wprowadzania danych', 'Pole adresu zamieszkania nie może być puste ani zawierać tylko białych znaków.','information')
            return False
        workerZip = self.ui.le_zipAdd.text()
        if workerZip == '':
            self.showDialog('Błąd podczas wprowadzania danych', 'Pole ZIP nie może być puste.','information')
            return False
        workerPhone = self.ui.le_phoneAdd.text()

        # WORKER AGREEMENT DATA
        workerAgreementStart = self.ui.date_contractStart.date().toString(Qt.ISODate)
        if self.ui.rb_contractEnd.isChecked():
            workerAgreementEnd = self.ui.date_contractEnd.date().toString(Qt.ISODate)
        else:
            workerAgreementEnd = None
        workerWorkTime = self.ui.le_workTime.text()

        # COLLECT DATA FROM COMBOBOXES
        agreement = self.ui.cb_contractAdd
        workerAgreement = self.getComboID(agreement, 'agreements')
        city = self.ui.cb_cityAdd
        workerCity = self.getComboID(city, 'city')
        education = self.ui.cb_educationAdd
        workerEducation = self.getComboID(education, 'education')

        # CHECKING IF WORKER IS FOREIGNER
        workerForeigner = self.foreignerButtonStatus()
        if operationType == 'insertTable':
            if workerForeigner == 1:
                workerForeigner = 'Tak'
            else:
                workerForeigner = 'Nie'

        if operationType == 'insertTable':
            workerCity = self.ui.cb_cityAdd.currentText()
            workerAgreement = self.ui.cb_contractAdd.currentText()
            workerEducation = self.ui.cb_educationAdd.currentText()
        print(workerForeigner)
        personalDataList = (
        workerName, workerLastname, workerBirthday, workerForeigner, workerPESEL, workerAddress, workerZip, workerCity,
        workerPhone, workerEducation)

        return personalDataList
        # print(personalDataList)

    # LOAD WORKER DATA INTO EDIT VIEW
    def loadDataFromTable(self, datalist):
        convertList = list(datalist)
        listSize = len(datalist)
        for item in range(listSize):
            if convertList[item] == 'None':
                convertList[item] = ''
        datalist = tuple(convertList)
        self.ui.le_name.setText(datalist[1])
        self.ui.le_lastname.setText(datalist[2])
        date_time = datalist[3]
        #print(datalist)
        # format
        format = '%Y-%m-%d'
        date_obj = datetime.strptime(date_time,format)
        self.ui.date_birthday.setDate(date_obj)
        self.ui.cb_foreigner.setCurrentText(datalist[4])
        self.ui.le_pesel.setText(datalist[5])
        self.ui.le_address.setText(datalist[6])
        self.ui.le_zip.setText(datalist[7])
        self.ui.cb_city.setCurrentText(datalist[8])
        self.ui.le_phone.setText(datalist[9])
        self.ui.cb_education.setCurrentText(datalist[10])

    # UPDATE WORKER DATA IN TABLE
    def updateWorkerData(self, worker_id):
        workerDataList = self.getWorkerPersonalData('updateDatabase')
        if workerDataList == False:
            pass
        else:
            #print(worker_id, workerDataList)
            if self.showDialog('Potwierdź wprowadzone zmiany', 'Czy napewno chcesz zmodyfikować dane pracownika?', 'askConfirmation'):
                if db_worker_functions.updateWorkerPersonalData(worker_id,workerDataList):
                    updateList = self.getWorkerPersonalData('updateTable')
                    updateWorker(self.parent(),updateList)
                    self.showDialog('Edycja zakończona', "Dane pracownika zostały zmodyfikowane.", 'information')
                    self.close()
                else:
                    self.showDialog('Operacja przerwana', 'Wprowadzone dane są niepoprawne.', 'information')

    # EDIT WORKER DATA
    def getWorkerPersonalData(self, operationType):
        workerName = self.ui.le_name.text()
        if workerName.isspace() or workerName == '':
            self.showDialog('Błąd podczas edycji danych', 'Pole imienia nie może być puste ani zawierać tylko białych znaków.','information')
            return False
        workerLastName = self.ui.le_lastname.text()
        if workerLastName.isspace() or workerLastName == '':
            self.showDialog('Błąd podczas edycji danych', 'Pole nazwiska nie może być puste ani zawierać tylko białych znaków.','information')
            return False
        workerBirthday = self.ui.date_birthday.date().toString(Qt.ISODate)
        if operationType == 'updateDatabase':
            if self.ui.cb_foreigner.currentText() == 'Tak':
                workerForeigner = 1
            else:
                workerForeigner = 0
        else:
            workerForeigner = self.ui.cb_foreigner.currentText()
        workerPESEL = self.ui.le_pesel.text()
        if workerPESEL == '':
            self.showDialog('Błąd podczas edycji danych', 'Pole PESEL nie może być puste.','information')
            return False
        workerAddress = self.ui.le_address.text()
        if workerAddress.isspace() or workerAddress == '':
            self.showDialog('Błąd podczas edycji danych', 'Pole adresu zamieszkania nie może być puste ani zawierać tylko białych znaków.','information')
            return False
        workerZip = self.ui.le_zip.text()
        if workerZip == '':
            self.showDialog('Błąd podczas edycji danych', 'Pole ZIP nie może być puste.','information')
            return False
        workerCity = self.ui.cb_city.currentText()
        cityID = db_worker_functions.getComboID('city', workerCity)
        workerPhoneNumber = self.ui.le_phone.text()
        workerEducation = self.ui.cb_education.currentText()
        educationID = db_worker_functions.getComboID('education', workerEducation)
        if operationType == 'updateDatabase':
            DataList = (
                workerName,workerLastName,workerBirthday,
                workerForeigner,workerPESEL,workerAddress,
                workerZip,cityID,workerPhoneNumber,educationID)
        else:
            DataList = (
                workerName, workerLastName, workerBirthday,
                workerForeigner, workerPESEL, workerAddress,
                workerZip, workerCity, workerPhoneNumber, workerEducation)
        return DataList

    def restrictInputValues(self, operationType):
        letters_only = QRegularExpression(
            "[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻżqQvVxX -]{0,50}")
        operation = QRegularExpressionValidator(QRegularExpression(letters_only), self)
        phone_number = QRegularExpression("[+0123456789]{0,12}")
        zip_code = QRegularExpression("[0123456789]{0,5}")
        pesel = QRegularExpression("[0123456789]{0,11}")
        workTime = QRegularExpression("[.0123456789]{0,4}")
        if operationType == 'edit':
            self.ui.le_name.setValidator(operation)
            self.ui.le_lastname.setValidator(operation)
            self.ui.le_address.setMaxLength(50)
            self.ui.le_phone.setValidator(QRegularExpressionValidator( QRegularExpression(phone_number), self ))
            self.ui.le_zip.setValidator(QRegularExpressionValidator(QRegularExpression(zip_code), self))
            self.ui.le_pesel.setValidator(QRegularExpressionValidator(QRegularExpression(pesel), self))
        else:
            self.ui.le_workTime.setValidator(QRegularExpressionValidator( QRegularExpression(workTime), self ))
            self.ui.le_nameAdd.setValidator(operation)
            self.ui.le_lastnameAdd.setValidator(operation)
            self.ui.le_addressAdd.setMaxLength(50)
            self.ui.le_phoneAdd.setValidator(QRegularExpressionValidator(QRegularExpression(phone_number), self))
            self.ui.le_zipAdd.setValidator(QRegularExpressionValidator(QRegularExpression(zip_code), self))
            self.ui.le_peselAdd.setValidator(QRegularExpressionValidator(QRegularExpression(pesel), self))

    def birthdayCheck(self):
        birthday = self.ui.date_birthdayAdd.date()
        contractStart = self.ui.date_contractStart.date()
        if birthday > contractStart:
            self.ui.date_birthdayAdd.setDate(contractStart)

    def agreementCheck(self,time):
        agreementCheck = self.ui.rb_contractEnd.isChecked()
        contractStart = self.ui.date_contractStart.date()
        contractEnd = self.ui.date_contractEnd.date()
        if time == 'Start' and contractEnd < contractStart:
            self.ui.date_contractEnd.setDate(contractStart)
        if time == 'End' and agreementCheck and contractEnd < contractStart:
            self.ui.date_contractEnd.setDate(contractStart)

    def disabilityCheck(self,time):
        disabilityCheck = self.ui.rb_invalidEnd.isChecked()
        disabilityStart = self.ui.date_disabilityStart.date()
        disabilityEnd = self.ui.date_disabilityEnd.date()
        if time == 'Start' and disabilityEnd < disabilityStart:
            self.ui.date_disabilityEnd.setDate(disabilityStart)
        if time == 'End' and disabilityCheck and disabilityEnd < disabilityStart:
            self.ui.date_disabilityEnd.setDate(disabilityStart)

    def WorkTimeLimit(self):
            value = self.ui.le_workTime.text()
            try:
                floatValue = float(value)
                print(floatValue)
                if floatValue and floatValue > 1:
                    self.ui.le_workTime.setText("1")
            except:
                return 0

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




