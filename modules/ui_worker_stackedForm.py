# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker_stackedForm.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_WorkerForms(object):
    def setupUi(self, WorkerForms):
        if not WorkerForms.objectName():
            WorkerForms.setObjectName(u"WorkerForms")
        WorkerForms.resize(1000, 668)
        WorkerForms.setMinimumSize(QSize(950, 0))
        WorkerForms.setMaximumSize(QSize(1000, 16777215))
        WorkerForms.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(WorkerForms)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bgApp = QFrame(WorkerForms)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMinimumSize(QSize(950, 650))
        self.bgApp.setMaximumSize(QSize(16777215, 16777215))
        self.bgApp.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 13pt \"Segoe UI\";\n"
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
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-"
                        "radius: 5px;\n"
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
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////"
                        "////////////////////////////\n"
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
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(255, 255, 255);\n"
"	border: 4px solid rgb(52, 59, 72);	\n"
""
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
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(255, 255, 255);\n"
"}\n"
"/*///////////////////////"
                        "//////////////////////////////////////////////////////////////////////////\n"
"DateEdit*/\n"
"QDateEdit{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentTopBg{\n"
"	background-color:rgb(0,0,0);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb"
                        "(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	borde"
                        "r: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bgApp)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMaximumSize(QSize(16777215, 16777215))
        self.contentBox.setBaseSize(QSize(0, 0))
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
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
        self.titleRightInfo.setMaximumSize(QSize(900, 45))
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
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
        self.closeAppBtn.setMaximumSize(QSize(35, 35))
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
        self.contentBottom.setMaximumSize(QSize(16777215, 16777215))
        self.contentBottom.setStyleSheet(u"/*Edit Buttons */\n"
"QPushButton { background-color: rgba(255, 255, 255,0); border: none;  border-radius: 5px; }\n"
"QPushButton:hover { background-color: rgb(0, 0, 0); border-style: solid; border-radius: 4px; }\n"
"QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.contentBottom)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.worker_groupBox_inputs = QGroupBox(self.contentBottom)
        self.worker_groupBox_inputs.setObjectName(u"worker_groupBox_inputs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.worker_groupBox_inputs.sizePolicy().hasHeightForWidth())
        self.worker_groupBox_inputs.setSizePolicy(sizePolicy2)
        self.worker_groupBox_inputs.setMinimumSize(QSize(850, 250))
        self.worker_groupBox_inputs.setMaximumSize(QSize(16777215, 250))
        self.horizontalLayout_8 = QHBoxLayout(self.worker_groupBox_inputs)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.worker_stackedWidget = QStackedWidget(self.worker_groupBox_inputs)
        self.worker_stackedWidget.setObjectName(u"worker_stackedWidget")
        self.worker_agreements = QWidget()
        self.worker_agreements.setObjectName(u"worker_agreements")
        self.horizontalLayout_16 = QHBoxLayout(self.worker_agreements)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_workTime = QLabel(self.worker_agreements)
        self.lb_workTime.setObjectName(u"lb_workTime")
        self.lb_workTime.setMinimumSize(QSize(100, 0))
        self.lb_workTime.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.lb_workTime, 0, 3, 1, 1)

        self.lb_agreement = QLabel(self.worker_agreements)
        self.lb_agreement.setObjectName(u"lb_agreement")

        self.gridLayout.addWidget(self.lb_agreement, 0, 0, 1, 1)

        self.lb_dateStart = QLabel(self.worker_agreements)
        self.lb_dateStart.setObjectName(u"lb_dateStart")
        self.lb_dateStart.setMinimumSize(QSize(150, 0))
        self.lb_dateStart.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.lb_dateStart, 0, 1, 1, 1)

        self.cb_agreement = QComboBox(self.worker_agreements)
        self.cb_agreement.setObjectName(u"cb_agreement")
        self.cb_agreement.setMinimumSize(QSize(300, 0))
        self.cb_agreement.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.cb_agreement, 1, 0, 1, 1)

        self.le_workTime = QLineEdit(self.worker_agreements)
        self.le_workTime.setObjectName(u"le_workTime")
        self.le_workTime.setMinimumSize(QSize(100, 0))
        self.le_workTime.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.le_workTime, 1, 3, 1, 1)

        self.date_AgreementstartDate = QDateEdit(self.worker_agreements)
        self.date_AgreementstartDate.setObjectName(u"date_AgreementstartDate")

        self.gridLayout.addWidget(self.date_AgreementstartDate, 1, 1, 1, 1)

        self.date_AgreementEndDate = QDateEdit(self.worker_agreements)
        self.date_AgreementEndDate.setObjectName(u"date_AgreementEndDate")
        self.date_AgreementEndDate.setStyleSheet(u"")

        self.gridLayout.addWidget(self.date_AgreementEndDate, 1, 2, 1, 1)

        self.rb_A_Expiration = QRadioButton(self.worker_agreements)
        self.rb_A_Expiration.setObjectName(u"rb_A_Expiration")
        self.rb_A_Expiration.setMinimumSize(QSize(150, 0))
        self.rb_A_Expiration.setMaximumSize(QSize(200, 16777215))
        self.rb_A_Expiration.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.rb_A_Expiration, 0, 2, 1, 1)


        self.horizontalLayout_16.addLayout(self.gridLayout)

        self.worker_stackedWidget.addWidget(self.worker_agreements)
        self.worker_children = QWidget()
        self.worker_children.setObjectName(u"worker_children")
        self.horizontalLayout_13 = QHBoxLayout(self.worker_children)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(10)
        self.date_ChildDateOfBirth = QDateEdit(self.worker_children)
        self.date_ChildDateOfBirth.setObjectName(u"date_ChildDateOfBirth")

        self.gridLayout_2.addWidget(self.date_ChildDateOfBirth, 1, 2, 1, 1)

        self.le_ChildName = QLineEdit(self.worker_children)
        self.le_ChildName.setObjectName(u"le_ChildName")

        self.gridLayout_2.addWidget(self.le_ChildName, 1, 0, 1, 1)

        self.lb_dateOfBirth = QLabel(self.worker_children)
        self.lb_dateOfBirth.setObjectName(u"lb_dateOfBirth")
        self.lb_dateOfBirth.setMinimumSize(QSize(200, 0))

        self.gridLayout_2.addWidget(self.lb_dateOfBirth, 0, 2, 1, 1)

        self.lb_childName = QLabel(self.worker_children)
        self.lb_childName.setObjectName(u"lb_childName")

        self.gridLayout_2.addWidget(self.lb_childName, 0, 0, 1, 1)

        self.lb_childLastname = QLabel(self.worker_children)
        self.lb_childLastname.setObjectName(u"lb_childLastname")

        self.gridLayout_2.addWidget(self.lb_childLastname, 0, 1, 1, 1)

        self.le_ChildParentID = QLineEdit(self.worker_children)
        self.le_ChildParentID.setObjectName(u"le_ChildParentID")
        self.le_ChildParentID.setEchoMode(QLineEdit.Normal)

        self.gridLayout_2.addWidget(self.le_ChildParentID, 2, 1, 1, 1)

        self.rb_ChildParentID = QRadioButton(self.worker_children)
        self.rb_ChildParentID.setObjectName(u"rb_ChildParentID")
        self.rb_ChildParentID.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_2.addWidget(self.rb_ChildParentID, 2, 0, 1, 1)

        self.le_ChildLastname = QLineEdit(self.worker_children)
        self.le_ChildLastname.setObjectName(u"le_ChildLastname")

        self.gridLayout_2.addWidget(self.le_ChildLastname, 1, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_2)

        self.worker_stackedWidget.addWidget(self.worker_children)
        self.worker_disability = QWidget()
        self.worker_disability.setObjectName(u"worker_disability")
        self.horizontalLayout_14 = QHBoxLayout(self.worker_disability)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.database_tables_label4 = QLabel(self.worker_disability)
        self.database_tables_label4.setObjectName(u"database_tables_label4")
        self.database_tables_label4.setMinimumSize(QSize(175, 0))
        self.database_tables_label4.setMaximumSize(QSize(215, 150))

        self.gridLayout_3.addWidget(self.database_tables_label4, 0, 1, 1, 1)

        self.cb_disability = QComboBox(self.worker_disability)
        self.cb_disability.setObjectName(u"cb_disability")
        self.cb_disability.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_3.addWidget(self.cb_disability, 1, 0, 1, 1)

        self.database_tables_label3 = QLabel(self.worker_disability)
        self.database_tables_label3.setObjectName(u"database_tables_label3")
        self.database_tables_label3.setMinimumSize(QSize(0, 0))
        self.database_tables_label3.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_3.addWidget(self.database_tables_label3, 0, 0, 1, 1)

        self.date_D_Start = QDateEdit(self.worker_disability)
        self.date_D_Start.setObjectName(u"date_D_Start")

        self.gridLayout_3.addWidget(self.date_D_Start, 1, 1, 1, 1)

        self.date_D_End = QDateEdit(self.worker_disability)
        self.date_D_End.setObjectName(u"date_D_End")

        self.gridLayout_3.addWidget(self.date_D_End, 1, 2, 1, 1)

        self.rb_D_Expiration = QRadioButton(self.worker_disability)
        self.rb_D_Expiration.setObjectName(u"rb_D_Expiration")
        self.rb_D_Expiration.setMinimumSize(QSize(0, 0))
        self.rb_D_Expiration.setMaximumSize(QSize(180, 16777215))
        self.rb_D_Expiration.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_3.addWidget(self.rb_D_Expiration, 0, 2, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_3)

        self.worker_stackedWidget.addWidget(self.worker_disability)
        self.worker_workHistory = QWidget()
        self.worker_workHistory.setObjectName(u"worker_workHistory")
        self.worker_workHistory.setMinimumSize(QSize(0, 0))
        self.gridLayoutWidget_2 = QWidget(self.worker_workHistory)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 841, 71))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.le_WH_CompanyName = QLineEdit(self.gridLayoutWidget_2)
        self.le_WH_CompanyName.setObjectName(u"le_WH_CompanyName")
        self.le_WH_CompanyName.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.le_WH_CompanyName, 1, 0, 1, 1)

        self.lb_WH_CompanyName = QLabel(self.gridLayoutWidget_2)
        self.lb_WH_CompanyName.setObjectName(u"lb_WH_CompanyName")
        self.lb_WH_CompanyName.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.lb_WH_CompanyName, 0, 0, 1, 1)

        self.lb_WH_dateStart = QLabel(self.gridLayoutWidget_2)
        self.lb_WH_dateStart.setObjectName(u"lb_WH_dateStart")
        self.lb_WH_dateStart.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.lb_WH_dateStart, 0, 1, 1, 1)

        self.lb_WH_dateEnd = QLabel(self.gridLayoutWidget_2)
        self.lb_WH_dateEnd.setObjectName(u"lb_WH_dateEnd")
        self.lb_WH_dateEnd.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.lb_WH_dateEnd, 0, 2, 1, 1)

        self.date_WH_Start = QDateEdit(self.gridLayoutWidget_2)
        self.date_WH_Start.setObjectName(u"date_WH_Start")
        self.date_WH_Start.setMinimumSize(QSize(220, 0))
        self.date_WH_Start.setMaximumSize(QSize(220, 16777215))

        self.gridLayout_5.addWidget(self.date_WH_Start, 1, 1, 1, 1)

        self.date_WH_End = QDateEdit(self.gridLayoutWidget_2)
        self.date_WH_End.setObjectName(u"date_WH_End")
        self.date_WH_End.setMinimumSize(QSize(220, 0))
        self.date_WH_End.setMaximumSize(QSize(220, 16777215))

        self.gridLayout_5.addWidget(self.date_WH_End, 1, 2, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.worker_workHistory)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 110, 881, 91))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lb_requested = QLabel(self.gridLayoutWidget_3)
        self.lb_requested.setObjectName(u"lb_requested")

        self.gridLayout_6.addWidget(self.lb_requested, 1, 2, 1, 1)

        self.lb_childcare = QLabel(self.gridLayoutWidget_3)
        self.lb_childcare.setObjectName(u"lb_childcare")

        self.gridLayout_6.addWidget(self.lb_childcare, 1, 1, 1, 1)

        self.lb_absence = QLabel(self.gridLayoutWidget_3)
        self.lb_absence.setObjectName(u"lb_absence")
        self.lb_absence.setMinimumSize(QSize(160, 0))
        self.lb_absence.setMaximumSize(QSize(160, 16777215))

        self.gridLayout_6.addWidget(self.lb_absence, 1, 4, 1, 1)

        self.lb_urlopUsed = QLabel(self.gridLayoutWidget_3)
        self.lb_urlopUsed.setObjectName(u"lb_urlopUsed")

        self.gridLayout_6.addWidget(self.lb_urlopUsed, 0, 0, 1, 1)

        self.lb_paidLeave = QLabel(self.gridLayoutWidget_3)
        self.lb_paidLeave.setObjectName(u"lb_paidLeave")

        self.gridLayout_6.addWidget(self.lb_paidLeave, 1, 0, 1, 1)

        self.lb_equivalent = QLabel(self.gridLayoutWidget_3)
        self.lb_equivalent.setObjectName(u"lb_equivalent")

        self.gridLayout_6.addWidget(self.lb_equivalent, 1, 5, 1, 1)

        self.lb_unpaid = QLabel(self.gridLayoutWidget_3)
        self.lb_unpaid.setObjectName(u"lb_unpaid")

        self.gridLayout_6.addWidget(self.lb_unpaid, 1, 3, 1, 1)

        self.le_WH_PaidLeave = QLineEdit(self.gridLayoutWidget_3)
        self.le_WH_PaidLeave.setObjectName(u"le_WH_PaidLeave")
        self.le_WH_PaidLeave.setMinimumSize(QSize(145, 0))
        self.le_WH_PaidLeave.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_6.addWidget(self.le_WH_PaidLeave, 2, 0, 1, 1)

        self.le_WH_Childcare = QLineEdit(self.gridLayoutWidget_3)
        self.le_WH_Childcare.setObjectName(u"le_WH_Childcare")
        self.le_WH_Childcare.setMinimumSize(QSize(125, 0))
        self.le_WH_Childcare.setMaximumSize(QSize(165, 16777215))

        self.gridLayout_6.addWidget(self.le_WH_Childcare, 2, 1, 1, 1)

        self.le_WH_Requested = QLineEdit(self.gridLayoutWidget_3)
        self.le_WH_Requested.setObjectName(u"le_WH_Requested")
        self.le_WH_Requested.setMinimumSize(QSize(125, 0))
        self.le_WH_Requested.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_6.addWidget(self.le_WH_Requested, 2, 2, 1, 1)

        self.le_WH_Unpaid = QLineEdit(self.gridLayoutWidget_3)
        self.le_WH_Unpaid.setObjectName(u"le_WH_Unpaid")
        self.le_WH_Unpaid.setMinimumSize(QSize(125, 0))
        self.le_WH_Unpaid.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_6.addWidget(self.le_WH_Unpaid, 2, 3, 1, 1)

        self.le_WH_Absence = QLineEdit(self.gridLayoutWidget_3)
        self.le_WH_Absence.setObjectName(u"le_WH_Absence")
        self.le_WH_Absence.setMaximumSize(QSize(160, 16777215))

        self.gridLayout_6.addWidget(self.le_WH_Absence, 2, 4, 1, 1)

        self.le_WH_Equivalent = QLineEdit(self.gridLayoutWidget_3)
        self.le_WH_Equivalent.setObjectName(u"le_WH_Equivalent")
        self.le_WH_Equivalent.setMinimumSize(QSize(125, 0))
        self.le_WH_Equivalent.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_6.addWidget(self.le_WH_Equivalent, 2, 5, 1, 1)

        self.line = QFrame(self.worker_workHistory)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 841, 41))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.worker_stackedWidget.addWidget(self.worker_workHistory)
        self.worker_urlops = QWidget()
        self.worker_urlops.setObjectName(u"worker_urlops")
        self.gridLayoutWidget = QWidget(self.worker_urlops)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 841, 96))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.date_U_DateStart = QDateEdit(self.gridLayoutWidget)
        self.date_U_DateStart.setObjectName(u"date_U_DateStart")
        self.date_U_DateStart.setMinimumSize(QSize(160, 0))
        self.date_U_DateStart.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_4.addWidget(self.date_U_DateStart, 1, 2, 1, 1)

        self.lb_U_dateStart = QLabel(self.gridLayoutWidget)
        self.lb_U_dateStart.setObjectName(u"lb_U_dateStart")
        self.lb_U_dateStart.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.lb_U_dateStart, 0, 2, 1, 1)

        self.lb_U_dateEnd = QLabel(self.gridLayoutWidget)
        self.lb_U_dateEnd.setObjectName(u"lb_U_dateEnd")
        self.lb_U_dateEnd.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.lb_U_dateEnd, 0, 3, 1, 1)

        self.lb_urlopType = QLabel(self.gridLayoutWidget)
        self.lb_urlopType.setObjectName(u"lb_urlopType")
        self.lb_urlopType.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.lb_urlopType, 0, 0, 1, 1)

        self.le_U_availableLimit = QLineEdit(self.gridLayoutWidget)
        self.le_U_availableLimit.setObjectName(u"le_U_availableLimit")
        self.le_U_availableLimit.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_4.addWidget(self.le_U_availableLimit, 1, 1, 1, 1)

        self.date_U_DateEnd = QDateEdit(self.gridLayoutWidget)
        self.date_U_DateEnd.setObjectName(u"date_U_DateEnd")
        self.date_U_DateEnd.setMinimumSize(QSize(160, 0))
        self.date_U_DateEnd.setMaximumSize(QSize(160, 16777215))

        self.gridLayout_4.addWidget(self.date_U_DateEnd, 1, 3, 1, 1)

        self.button_U_calculate = QPushButton(self.gridLayoutWidget)
        self.button_U_calculate.setObjectName(u"button_U_calculate")
        self.button_U_calculate.setMinimumSize(QSize(65, 65))
        self.button_U_calculate.setMaximumSize(QSize(100, 100))

        self.gridLayout_4.addWidget(self.button_U_calculate, 1, 4, 1, 1)

        self.lb_availableLimit = QLabel(self.gridLayoutWidget)
        self.lb_availableLimit.setObjectName(u"lb_availableLimit")
        self.lb_availableLimit.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.lb_availableLimit, 0, 1, 1, 1)

        self.cb_urlop = QComboBox(self.gridLayoutWidget)
        self.cb_urlop.setObjectName(u"cb_urlop")
        self.cb_urlop.setMinimumSize(QSize(275, 0))
        self.cb_urlop.setMaximumSize(QSize(275, 16777215))

        self.gridLayout_4.addWidget(self.cb_urlop, 1, 0, 1, 1)

        self.worker_stackedWidget.addWidget(self.worker_urlops)

        self.horizontalLayout_8.addWidget(self.worker_stackedWidget)


        self.horizontalLayout_7.addWidget(self.worker_groupBox_inputs)

        self.database_buttons = QVBoxLayout()
        self.database_buttons.setObjectName(u"database_buttons")
        self.database_buttons.setSizeConstraint(QLayout.SetMinimumSize)
        self.database_buttons.setContentsMargins(-1, 10, -1, -1)
        self.btn1_workerForm_add = QPushButton(self.contentBottom)
        self.btn1_workerForm_add.setObjectName(u"btn1_workerForm_add")
        self.btn1_workerForm_add.setMinimumSize(QSize(35, 35))
        self.btn1_workerForm_add.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn1_workerForm_add.setIcon(icon1)

        self.database_buttons.addWidget(self.btn1_workerForm_add)

        self.btn2_workerForm_delete = QPushButton(self.contentBottom)
        self.btn2_workerForm_delete.setObjectName(u"btn2_workerForm_delete")
        self.btn2_workerForm_delete.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn2_workerForm_delete.setIcon(icon2)

        self.database_buttons.addWidget(self.btn2_workerForm_delete)

        self.btn3_workerForm_edit = QPushButton(self.contentBottom)
        self.btn3_workerForm_edit.setObjectName(u"btn3_workerForm_edit")
        self.btn3_workerForm_edit.setMaximumSize(QSize(35, 35))
        self.btn3_workerForm_edit.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-text-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn3_workerForm_edit.setIcon(icon3)

        self.database_buttons.addWidget(self.btn3_workerForm_edit)


        self.horizontalLayout_7.addLayout(self.database_buttons)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.worker_table = QTableWidget(self.contentBottom)
        self.worker_table.setObjectName(u"worker_table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.worker_table.sizePolicy().hasHeightForWidth())
        self.worker_table.setSizePolicy(sizePolicy3)
        self.worker_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.worker_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.worker_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout.addWidget(self.worker_table)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.verticalLayout_3.addWidget(self.contentBox)


        self.verticalLayout_4.addWidget(self.bgApp)


        self.retranslateUi(WorkerForms)

        self.worker_stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(WorkerForms)
    # setupUi

    def retranslateUi(self, WorkerForms):
        WorkerForms.setWindowTitle(QCoreApplication.translate("WorkerForms", u"Form", None))
        self.titleRightInfo.setText(QCoreApplication.translate("WorkerForms", u"Settings Panel", None))
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("WorkerForms", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.worker_groupBox_inputs.setTitle(QCoreApplication.translate("WorkerForms", u"GroupBox", None))
        self.lb_workTime.setText(QCoreApplication.translate("WorkerForms", u"Wymiar pracy:", None))
        self.lb_agreement.setText(QCoreApplication.translate("WorkerForms", u"Rodzaj umowy:", None))
        self.lb_dateStart.setText(QCoreApplication.translate("WorkerForms", u"Data podpisania:", None))
        self.le_workTime.setPlaceholderText("")
        self.rb_A_Expiration.setText(QCoreApplication.translate("WorkerForms", u"Data wyga\u015bni\u0119cia:", None))
        self.le_ChildName.setPlaceholderText("")
        self.lb_dateOfBirth.setText(QCoreApplication.translate("WorkerForms", u"Data urodzenia:", None))
        self.lb_childName.setText(QCoreApplication.translate("WorkerForms", u"Imi\u0119 dziecka:", None))
        self.lb_childLastname.setText(QCoreApplication.translate("WorkerForms", u"Nazwisko dziecka:", None))
        self.le_ChildParentID.setInputMask("")
        self.le_ChildParentID.setText("")
        self.le_ChildParentID.setPlaceholderText(QCoreApplication.translate("WorkerForms", u"Podaj nowe ID", None))
        self.rb_ChildParentID.setText(QCoreApplication.translate("WorkerForms", u"Zmie\u0144 rodzica", None))
        self.le_ChildLastname.setPlaceholderText("")
        self.database_tables_label4.setText(QCoreApplication.translate("WorkerForms", u"Data wydania o\u015bwiadczenia:", None))
        self.database_tables_label3.setText(QCoreApplication.translate("WorkerForms", u"Poziom niepe\u0142nosprawno\u015bci:", None))
        self.rb_D_Expiration.setText(QCoreApplication.translate("WorkerForms", u"Data wyga\u015bni\u0119cia:", None))
        self.lb_WH_CompanyName.setText(QCoreApplication.translate("WorkerForms", u"Nazwa firmy:", None))
        self.lb_WH_dateStart.setText(QCoreApplication.translate("WorkerForms", u"Data rozpocz\u0119cia:", None))
        self.lb_WH_dateEnd.setText(QCoreApplication.translate("WorkerForms", u"Data zako\u0144czenia:", None))
        self.lb_requested.setText(QCoreApplication.translate("WorkerForms", u"Na \u017c\u0105danie", None))
        self.lb_childcare.setText(QCoreApplication.translate("WorkerForms", u"Opieka nad dzieckiem", None))
        self.lb_absence.setText(QCoreApplication.translate("WorkerForms", u"Nieobecno\u015b\u0107", None))
        self.lb_urlopUsed.setText(QCoreApplication.translate("WorkerForms", u"Urlop wykorzystany", None))
        self.lb_paidLeave.setText(QCoreApplication.translate("WorkerForms", u"P\u0142atny:", None))
        self.lb_equivalent.setText(QCoreApplication.translate("WorkerForms", u"Ekwiwalent", None))
        self.lb_unpaid.setText(QCoreApplication.translate("WorkerForms", u"Bezp\u0142atny", None))
        self.lb_U_dateStart.setText(QCoreApplication.translate("WorkerForms", u"Data rozpocz\u0119cia:", None))
        self.lb_U_dateEnd.setText(QCoreApplication.translate("WorkerForms", u"Data zako\u0144czenia:", None))
        self.lb_urlopType.setText(QCoreApplication.translate("WorkerForms", u"Rodzaj urlopu:", None))
        self.button_U_calculate.setText(QCoreApplication.translate("WorkerForms", u"PRZELICZ", None))
        self.lb_availableLimit.setText(QCoreApplication.translate("WorkerForms", u"Dost\u0119pny limit:", None))
        self.btn1_workerForm_add.setText("")
        self.btn2_workerForm_delete.setText("")
        self.btn3_workerForm_edit.setText("")
    # retranslateUi

