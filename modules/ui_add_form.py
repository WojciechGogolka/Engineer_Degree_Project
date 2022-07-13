# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        if not AddWindow.objectName():
            AddWindow.setObjectName(u"AddWindow")
        AddWindow.resize(560, 1083)
        AddWindow.setMinimumSize(QSize(560, 960))
        AddWindow.setMaximumSize(QSize(560, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        AddWindow.setPalette(palette)
        self.styleSheet = QWidget(AddWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMinimumSize(QSize(560, 960))
        self.styleSheet.setMaximumSize(QSize(560, 12312312))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 15pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButto"
                        "n:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QS"
                        "crollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	bo"
                        "rder-radius: 13px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	backgrou"
                        "nd-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"/*/////////////////////////////////////////////////////////////////////////////////////////////////\n"
"DateEdit*/\n"
"QDateEdit{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QPushButton{\n"
"	font-weight: bold;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"\n"
"#contentTopBg{\n"
"	background-color:rgb(0,0,0);\n"
"}\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMaximumSize(QSize(540, 16777215))
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMaximumSize(QSize(540, 16777215))
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(540, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy1)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.closeAppBtn.setFont(font1)
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(25, 0, 25, 10)
        self.stackedWidget = QStackedWidget(self.contentBottom)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.data_input = QWidget()
        self.data_input.setObjectName(u"data_input")
        self.verticalLayout = QVBoxLayout(self.data_input)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.data_input)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(185, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.data_input)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(185, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.data_input)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(185, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.le_nameAdd = QLineEdit(self.data_input)
        self.le_nameAdd.setObjectName(u"le_nameAdd")
        self.le_nameAdd.setMinimumSize(QSize(250, 40))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_nameAdd)

        self.le_lastnameAdd = QLineEdit(self.data_input)
        self.le_lastnameAdd.setObjectName(u"le_lastnameAdd")
        self.le_lastnameAdd.setMinimumSize(QSize(250, 40))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_lastnameAdd)

        self.cb_contractAdd = QComboBox(self.data_input)
        self.cb_contractAdd.setObjectName(u"cb_contractAdd")
        self.cb_contractAdd.setMinimumSize(QSize(250, 40))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_contractAdd)


        self.verticalLayout_4.addLayout(self.formLayout)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.gB1_contract = QGroupBox(self.data_input)
        self.gB1_contract.setObjectName(u"gB1_contract")
        self.gB1_contract.setMaximumSize(QSize(540, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.gB1_contract)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setHorizontalSpacing(15)
        self.label_4 = QLabel(self.gB1_contract)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(185, 0))

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.date_contractStart = QDateEdit(self.gB1_contract)
        self.date_contractStart.setObjectName(u"date_contractStart")
        self.date_contractStart.setMinimumSize(QSize(200, 35))
        self.date_contractStart.setFont(font)
        self.date_contractStart.setAccelerated(False)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.date_contractStart)

        self.date_contractEnd = QDateEdit(self.gB1_contract)
        self.date_contractEnd.setObjectName(u"date_contractEnd")
        self.date_contractEnd.setMinimumSize(QSize(200, 35))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.date_contractEnd)

        self.label_5 = QLabel(self.gB1_contract)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(185, 0))

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.le_workTime = QLineEdit(self.gB1_contract)
        self.le_workTime.setObjectName(u"le_workTime")
        self.le_workTime.setMinimumSize(QSize(200, 40))

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.le_workTime)

        self.rb_contractEnd = QRadioButton(self.gB1_contract)
        self.rb_contractEnd.setObjectName(u"rb_contractEnd")
        self.rb_contractEnd.setLayoutDirection(Qt.RightToLeft)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.rb_contractEnd)


        self.verticalLayout_3.addLayout(self.formLayout_3)


        self.verticalLayout.addWidget(self.gB1_contract)

        self.gB2_personalData = QGroupBox(self.data_input)
        self.gB2_personalData.setObjectName(u"gB2_personalData")
        self.gB2_personalData.setMaximumSize(QSize(540, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.gB2_personalData)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_4.setHorizontalSpacing(15)
        self.label_14 = QLabel(self.gB2_personalData)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(185, 0))

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.le_peselAdd = QLineEdit(self.gB2_personalData)
        self.le_peselAdd.setObjectName(u"le_peselAdd")
        self.le_peselAdd.setMinimumSize(QSize(200, 40))

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.le_peselAdd)

        self.label_12 = QLabel(self.gB2_personalData)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(185, 0))

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.gB2_personalData)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(185, 0))

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.label_11 = QLabel(self.gB2_personalData)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(185, 0))

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.label_10 = QLabel(self.gB2_personalData)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(185, 0))

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.label_9 = QLabel(self.gB2_personalData)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(185, 0))

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_9)

        self.label_18 = QLabel(self.gB2_personalData)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(185, 0))

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_18)

        self.label_7 = QLabel(self.gB2_personalData)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(185, 0))

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.gB2_personalData)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(185, 0))

        self.formLayout_4.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.date_birthdayAdd = QDateEdit(self.gB2_personalData)
        self.date_birthdayAdd.setObjectName(u"date_birthdayAdd")
        self.date_birthdayAdd.setMinimumSize(QSize(200, 35))

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.date_birthdayAdd)

        self.le_addressAdd = QLineEdit(self.gB2_personalData)
        self.le_addressAdd.setObjectName(u"le_addressAdd")
        self.le_addressAdd.setMinimumSize(QSize(200, 40))

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.le_addressAdd)

        self.le_zipAdd = QLineEdit(self.gB2_personalData)
        self.le_zipAdd.setObjectName(u"le_zipAdd")
        self.le_zipAdd.setMinimumSize(QSize(200, 40))

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.le_zipAdd)

        self.cb_cityAdd = QComboBox(self.gB2_personalData)
        self.cb_cityAdd.setObjectName(u"cb_cityAdd")
        self.cb_cityAdd.setMinimumSize(QSize(200, 40))

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.cb_cityAdd)

        self.le_phoneAdd = QLineEdit(self.gB2_personalData)
        self.le_phoneAdd.setObjectName(u"le_phoneAdd")
        self.le_phoneAdd.setMinimumSize(QSize(200, 40))

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.le_phoneAdd)

        self.cb_educationAdd = QComboBox(self.gB2_personalData)
        self.cb_educationAdd.setObjectName(u"cb_educationAdd")
        self.cb_educationAdd.setMinimumSize(QSize(200, 40))

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.cb_educationAdd)

        self.rb_foreigner = QRadioButton(self.gB2_personalData)
        self.rb_foreigner.setObjectName(u"rb_foreigner")
        self.rb_foreigner.setMinimumSize(QSize(200, 30))
        self.rb_foreigner.setAutoExclusive(False)

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.rb_foreigner)

        self.rb_invalid = QRadioButton(self.gB2_personalData)
        self.rb_invalid.setObjectName(u"rb_invalid")
        self.rb_invalid.setMinimumSize(QSize(200, 30))
        self.rb_invalid.setAutoExclusive(False)

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.rb_invalid)


        self.verticalLayout_5.addLayout(self.formLayout_4)


        self.verticalLayout.addWidget(self.gB2_personalData)

        self.gB3_disability = QGroupBox(self.data_input)
        self.gB3_disability.setObjectName(u"gB3_disability")
        self.gB3_disability.setMaximumSize(QSize(540, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.gB3_disability)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_5.setHorizontalSpacing(15)
        self.label_15 = QLabel(self.gB3_disability)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(185, 0))

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.cb_disabilityAdd = QComboBox(self.gB3_disability)
        self.cb_disabilityAdd.setObjectName(u"cb_disabilityAdd")
        self.cb_disabilityAdd.setMinimumSize(QSize(200, 40))

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.cb_disabilityAdd)

        self.label_16 = QLabel(self.gB3_disability)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(185, 0))

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.date_disabilityStart = QDateEdit(self.gB3_disability)
        self.date_disabilityStart.setObjectName(u"date_disabilityStart")
        self.date_disabilityStart.setMinimumSize(QSize(200, 35))

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.date_disabilityStart)

        self.date_disabilityEnd = QDateEdit(self.gB3_disability)
        self.date_disabilityEnd.setObjectName(u"date_disabilityEnd")
        self.date_disabilityEnd.setMinimumSize(QSize(200, 35))

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.date_disabilityEnd)

        self.rb_invalidEnd = QRadioButton(self.gB3_disability)
        self.rb_invalidEnd.setObjectName(u"rb_invalidEnd")
        self.rb_invalidEnd.setMinimumSize(QSize(190, 0))
        self.rb_invalidEnd.setLayoutDirection(Qt.RightToLeft)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.rb_invalidEnd)


        self.verticalLayout_7.addLayout(self.formLayout_5)


        self.verticalLayout.addWidget(self.gB3_disability)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.bt_addWorker = QPushButton(self.data_input)
        self.bt_addWorker.setObjectName(u"bt_addWorker")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bt_addWorker.sizePolicy().hasHeightForWidth())
        self.bt_addWorker.setSizePolicy(sizePolicy2)
        self.bt_addWorker.setMinimumSize(QSize(160, 40))
        self.bt_addWorker.setMaximumSize(QSize(160, 50))
        self.bt_addWorker.setBaseSize(QSize(300, 50))
        self.bt_addWorker.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_addWorker.setLayoutDirection(Qt.LeftToRight)
        self.bt_addWorker.setAutoDefault(False)

        self.horizontalLayout_5.addWidget(self.bt_addWorker)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.data_input)
        self.data_edit = QWidget()
        self.data_edit.setObjectName(u"data_edit")
        self.verticalLayout_8 = QVBoxLayout(self.data_edit)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gB4_editView = QGroupBox(self.data_edit)
        self.gB4_editView.setObjectName(u"gB4_editView")
        self.gB4_editView.setFont(font)
        self.gB4_editView.setFlat(False)
        self.verticalLayout_9 = QVBoxLayout(self.gB4_editView)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_2.setHorizontalSpacing(15)
        self.formLayout_2.setVerticalSpacing(25)
        self.lb_name = QLabel(self.gB4_editView)
        self.lb_name.setObjectName(u"lb_name")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lb_name)

        self.lb_lastname = QLabel(self.gB4_editView)
        self.lb_lastname.setObjectName(u"lb_lastname")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lb_lastname)

        self.lb_date = QLabel(self.gB4_editView)
        self.lb_date.setObjectName(u"lb_date")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lb_date)

        self.lb_foreigner = QLabel(self.gB4_editView)
        self.lb_foreigner.setObjectName(u"lb_foreigner")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lb_foreigner)

        self.lb_pesel = QLabel(self.gB4_editView)
        self.lb_pesel.setObjectName(u"lb_pesel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lb_pesel)

        self.lb_address = QLabel(self.gB4_editView)
        self.lb_address.setObjectName(u"lb_address")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lb_address)

        self.lb_zip = QLabel(self.gB4_editView)
        self.lb_zip.setObjectName(u"lb_zip")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lb_zip)

        self.lb_city = QLabel(self.gB4_editView)
        self.lb_city.setObjectName(u"lb_city")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.lb_city)

        self.lb_phone = QLabel(self.gB4_editView)
        self.lb_phone.setObjectName(u"lb_phone")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.lb_phone)

        self.lb_education = QLabel(self.gB4_editView)
        self.lb_education.setObjectName(u"lb_education")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.lb_education)

        self.le_name = QLineEdit(self.gB4_editView)
        self.le_name.setObjectName(u"le_name")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_name)

        self.le_lastname = QLineEdit(self.gB4_editView)
        self.le_lastname.setObjectName(u"le_lastname")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_lastname)

        self.date_birthday = QDateEdit(self.gB4_editView)
        self.date_birthday.setObjectName(u"date_birthday")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.date_birthday)

        self.cb_foreigner = QComboBox(self.gB4_editView)
        self.cb_foreigner.setObjectName(u"cb_foreigner")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.cb_foreigner)

        self.le_pesel = QLineEdit(self.gB4_editView)
        self.le_pesel.setObjectName(u"le_pesel")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.le_pesel)

        self.le_address = QLineEdit(self.gB4_editView)
        self.le_address.setObjectName(u"le_address")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.le_address)

        self.le_zip = QLineEdit(self.gB4_editView)
        self.le_zip.setObjectName(u"le_zip")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.le_zip)

        self.cb_city = QComboBox(self.gB4_editView)
        self.cb_city.setObjectName(u"cb_city")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.cb_city)

        self.cb_education = QComboBox(self.gB4_editView)
        self.cb_education.setObjectName(u"cb_education")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.cb_education)

        self.le_phone = QLineEdit(self.gB4_editView)
        self.le_phone.setObjectName(u"le_phone")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.le_phone)


        self.verticalLayout_9.addLayout(self.formLayout_2)


        self.verticalLayout_8.addWidget(self.gB4_editView)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.bt_EditWorker = QPushButton(self.data_edit)
        self.bt_EditWorker.setObjectName(u"bt_EditWorker")
        self.bt_EditWorker.setMinimumSize(QSize(150, 40))

        self.horizontalLayout_6.addWidget(self.bt_EditWorker)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.data_edit)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_4.addWidget(self.bgApp)

        AddWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(AddWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.bt_addWorker.setDefault(False)


        QMetaObject.connectSlotsByName(AddWindow)
    # setupUi

    def retranslateUi(self, AddWindow):
        AddWindow.setWindowTitle(QCoreApplication.translate("AddWindow", u"MainWindow", None))
        self.titleRightInfo.setText(QCoreApplication.translate("AddWindow", u"Wojciech Gog\u00f3\u0142ka Urlops APP", None))
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("AddWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label.setText(QCoreApplication.translate("AddWindow", u"Imi\u0119:", None))
        self.label_2.setText(QCoreApplication.translate("AddWindow", u"Nazwisko:", None))
        self.label_3.setText(QCoreApplication.translate("AddWindow", u"Rodzaj umowy:", None))
        self.gB1_contract.setTitle(QCoreApplication.translate("AddWindow", u"Informacje o umowie", None))
        self.label_4.setText(QCoreApplication.translate("AddWindow", u"Data rozpocz\u0119cia", None))
        self.label_5.setText(QCoreApplication.translate("AddWindow", u"Wymiar pracy:", None))
        self.rb_contractEnd.setText(QCoreApplication.translate("AddWindow", u"Data zako\u0144czenia", None))
        self.gB2_personalData.setTitle(QCoreApplication.translate("AddWindow", u"Dane personalne", None))
        self.label_14.setText(QCoreApplication.translate("AddWindow", u"PESEL:", None))
        self.label_12.setText(QCoreApplication.translate("AddWindow", u"Data urodzenia:", None))
        self.label_13.setText(QCoreApplication.translate("AddWindow", u"Adres zamieszkania:", None))
        self.label_11.setText(QCoreApplication.translate("AddWindow", u"Kod ZIP:", None))
        self.label_10.setText(QCoreApplication.translate("AddWindow", u"Miasto zamieszkania:", None))
        self.label_9.setText(QCoreApplication.translate("AddWindow", u"Numer telefonu:", None))
        self.label_18.setText(QCoreApplication.translate("AddWindow", u"Wykszta\u0142cenie:", None))
        self.label_7.setText(QCoreApplication.translate("AddWindow", u"Obcokrajowiec:", None))
        self.label_8.setText(QCoreApplication.translate("AddWindow", u"Status inwalidy:", None))
        self.rb_foreigner.setText("")
        self.rb_invalid.setText("")
        self.gB3_disability.setTitle(QCoreApplication.translate("AddWindow", u"Status inwalidy", None))
        self.label_15.setText(QCoreApplication.translate("AddWindow", u"Niepe\u0142nosprawno\u015b\u0107:", None))
        self.label_16.setText(QCoreApplication.translate("AddWindow", u"Data o\u015bwiadczenia:", None))
        self.rb_invalidEnd.setText(QCoreApplication.translate("AddWindow", u"Data zako\u0144czenia:", None))
        self.bt_addWorker.setText(QCoreApplication.translate("AddWindow", u"DODAJ", None))
        self.gB4_editView.setTitle(QCoreApplication.translate("AddWindow", u"Dane personalne", None))
        self.lb_name.setText(QCoreApplication.translate("AddWindow", u"Imi\u0119:", None))
        self.lb_lastname.setText(QCoreApplication.translate("AddWindow", u"Nazwisko:", None))
        self.lb_date.setText(QCoreApplication.translate("AddWindow", u"Data urodzenia:", None))
        self.lb_foreigner.setText(QCoreApplication.translate("AddWindow", u"Obcokrajowiec:", None))
        self.lb_pesel.setText(QCoreApplication.translate("AddWindow", u"PESEL:", None))
        self.lb_address.setText(QCoreApplication.translate("AddWindow", u"Adres zamieszkania:", None))
        self.lb_zip.setText(QCoreApplication.translate("AddWindow", u"Kod ZIP:", None))
        self.lb_city.setText(QCoreApplication.translate("AddWindow", u"Miasto zamieszkania:", None))
        self.lb_phone.setText(QCoreApplication.translate("AddWindow", u"Numer telefonu:", None))
        self.lb_education.setText(QCoreApplication.translate("AddWindow", u"Wykszta\u0142cenie:", None))
        self.bt_EditWorker.setText(QCoreApplication.translate("AddWindow", u"EDYTUJ", None))
    # retranslateUi

