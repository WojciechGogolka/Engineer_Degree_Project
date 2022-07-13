# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from .resources_rc import *

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(655, 592)
        SettingsWindow.setStyleSheet(u"QWidget{\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5p"
                        "x;\n"
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
"/* ///////////////////////////////////////////////////////////////////////////////"
                        "//////////////////\n"
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
"}\n"
"\n"
""
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
"/*//////////////////////////////////"
                        "///////////////////////////////////////////////////////////////\n"
"DateEdit*/\n"
"QDateEdit{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"#contentTopBg{\n"
"	background-color:rgb(0,0,0);\n"
"}\n"
"\n"
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
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-l"
                        "eft-radius: 4px;\n"
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
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"  "
                        "   height: 20px;\n"
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
        self.horizontalLayout_12 = QHBoxLayout(SettingsWindow)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.bgApp = QFrame(SettingsWindow)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMinimumSize(QSize(550, 0))
        self.bgApp.setMaximumSize(QSize(16777215, 16777215))
        self.bgApp.setStyleSheet(u"")
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
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
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
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
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
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.contentBottom)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.main_stackedWidget = QStackedWidget(self.contentBottom)
        self.main_stackedWidget.setObjectName(u"main_stackedWidget")
        self.main_stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.main_stackedWidget.setStyleSheet(u"background: transparent;")
        self.database_tables = QWidget()
        self.database_tables.setObjectName(u"database_tables")
        self.database_tables.setMinimumSize(QSize(400, 500))
        self.database_tables.setMaximumSize(QSize(16777215, 16777215))
        self.database_tables.setStyleSheet(u"/*Edit Buttons */\n"
"QPushButton { background-color: rgba(255, 255, 255,0); border: none;  border-radius: 5px; }\n"
"QPushButton:hover { background-color: rgb(0, 0, 0); border-style: solid; border-radius: 4px; }\n"
"QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        self.verticalLayout_20 = QVBoxLayout(self.database_tables)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.database_groupBox_inputs = QGroupBox(self.database_tables)
        self.database_groupBox_inputs.setObjectName(u"database_groupBox_inputs")
        self.database_groupBox_inputs.setMinimumSize(QSize(320, 125))
        self.database_groupBox_inputs.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_8 = QHBoxLayout(self.database_groupBox_inputs)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.database_stackedWidget = QStackedWidget(self.database_groupBox_inputs)
        self.database_stackedWidget.setObjectName(u"database_stackedWidget")
        self.database_cities = QWidget()
        self.database_cities.setObjectName(u"database_cities")
        self.horizontalLayout_16 = QHBoxLayout(self.database_cities)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.database_tables_label0 = QLabel(self.database_cities)
        self.database_tables_label0.setObjectName(u"database_tables_label0")

        self.horizontalLayout_15.addWidget(self.database_tables_label0)

        self.database_tables_le0 = QLineEdit(self.database_cities)
        self.database_tables_le0.setObjectName(u"database_tables_le0")

        self.horizontalLayout_15.addWidget(self.database_tables_le0)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)

        self.database_stackedWidget.addWidget(self.database_cities)
        self.database_di = QWidget()
        self.database_di.setObjectName(u"database_di")
        self.horizontalLayout_13 = QHBoxLayout(self.database_di)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setVerticalSpacing(10)
        self.database_tables_label1 = QLabel(self.database_di)
        self.database_tables_label1.setObjectName(u"database_tables_label1")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.database_tables_label1)

        self.database_tables_label2 = QLabel(self.database_di)
        self.database_tables_label2.setObjectName(u"database_tables_label2")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.database_tables_label2)

        self.database_tables_le1 = QLineEdit(self.database_di)
        self.database_tables_le1.setObjectName(u"database_tables_le1")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.database_tables_le1)

        self.database_tables_le2 = QLineEdit(self.database_di)
        self.database_tables_le2.setObjectName(u"database_tables_le2")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.database_tables_le2)


        self.horizontalLayout_13.addLayout(self.formLayout_5)

        self.database_stackedWidget.addWidget(self.database_di)
        self.database_radio = QWidget()
        self.database_radio.setObjectName(u"database_radio")
        self.horizontalLayout_14 = QHBoxLayout(self.database_radio)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setVerticalSpacing(10)
        self.database_tables_label3 = QLabel(self.database_radio)
        self.database_tables_label3.setObjectName(u"database_tables_label3")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.database_tables_label3)

        self.database_tables_label4 = QLabel(self.database_radio)
        self.database_tables_label4.setObjectName(u"database_tables_label4")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.database_tables_label4)

        self.database_tables_le3 = QLineEdit(self.database_radio)
        self.database_tables_le3.setObjectName(u"database_tables_le3")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.database_tables_le3)

        self.database_tables_radio1 = QRadioButton(self.database_radio)
        self.database_tables_radio1.setObjectName(u"database_tables_radio1")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.database_tables_radio1)


        self.horizontalLayout_14.addLayout(self.formLayout_6)

        self.database_stackedWidget.addWidget(self.database_radio)

        self.horizontalLayout_8.addWidget(self.database_stackedWidget)


        self.horizontalLayout_7.addWidget(self.database_groupBox_inputs)

        self.database_buttons = QVBoxLayout()
        self.database_buttons.setObjectName(u"database_buttons")
        self.database_buttons.setSizeConstraint(QLayout.SetMinimumSize)
        self.database_buttons.setContentsMargins(-1, 10, -1, -1)
        self.btn1_settings_add = QPushButton(self.database_tables)
        self.btn1_settings_add.setObjectName(u"btn1_settings_add")
        self.btn1_settings_add.setMinimumSize(QSize(35, 35))
        self.btn1_settings_add.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn1_settings_add.setIcon(icon1)

        self.database_buttons.addWidget(self.btn1_settings_add)

        self.btn2_settings_delete = QPushButton(self.database_tables)
        self.btn2_settings_delete.setObjectName(u"btn2_settings_delete")
        self.btn2_settings_delete.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn2_settings_delete.setIcon(icon2)

        self.database_buttons.addWidget(self.btn2_settings_delete)

        self.btn3_settings_edit = QPushButton(self.database_tables)
        self.btn3_settings_edit.setObjectName(u"btn3_settings_edit")
        self.btn3_settings_edit.setMaximumSize(QSize(35, 35))
        self.btn3_settings_edit.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-text-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn3_settings_edit.setIcon(icon3)

        self.database_buttons.addWidget(self.btn3_settings_edit)


        self.horizontalLayout_7.addLayout(self.database_buttons)


        self.verticalLayout_20.addLayout(self.horizontalLayout_7)

        self.settings_table = QTableWidget(self.database_tables)
        self.settings_table.setObjectName(u"settings_table")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.settings_table.sizePolicy().hasHeightForWidth())
        self.settings_table.setSizePolicy(sizePolicy2)
        self.settings_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_20.addWidget(self.settings_table)

        self.main_stackedWidget.addWidget(self.database_tables)

        self.horizontalLayout_4.addWidget(self.main_stackedWidget)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.verticalLayout_3.addWidget(self.contentBox)


        self.horizontalLayout_12.addWidget(self.bgApp)


        self.retranslateUi(SettingsWindow)

        self.main_stackedWidget.setCurrentIndex(0)
        self.database_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Form", None))
        self.titleRightInfo.setText(QCoreApplication.translate("SettingsWindow", u"PANEL USTAWIE\u0143", None))
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("SettingsWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.database_groupBox_inputs.setTitle(QCoreApplication.translate("SettingsWindow", u"GroupBox", None))
        self.database_tables_label0.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.database_tables_label1.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.database_tables_label2.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.database_tables_label3.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.database_tables_label4.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.database_tables_radio1.setText("")
        self.btn1_settings_add.setText("")
        self.btn2_settings_delete.setText("")
        self.btn3_settings_edit.setText("")
    # retranslateUi

