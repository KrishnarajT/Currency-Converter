# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm:\Programs\Python\Currency Converter\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 700)
        Dialog.setStyleSheet("background-color: rgb(204, 183, 198);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 100, 1000, 600))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: white;")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab)
        self.comboBox_5.setGeometry(QtCore.QRect(260, 390, 71, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(770, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_6.setObjectName("label_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab)
        self.comboBox_7.setGeometry(QtCore.QRect(670, 280, 71, 31))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(610, 150, 71, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(540, 480, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(16)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("color:rgb(72, 60, 70);")
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(770, 330, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(360, 340, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(770, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(210, 150, 71, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(260, 340, 71, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(360, 390, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_3.setObjectName("label_3")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab)
        self.comboBox_6.setGeometry(QtCore.QRect(670, 380, 71, 31))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(390, 480, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(360, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(72, 60, 70);")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(330, 150, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(260, 290, 71, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab)
        self.comboBox_8.setGeometry(QtCore.QRect(670, 330, 71, 31))
        self.comboBox_8.setObjectName("comboBox_8")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(340, 40, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_10.setObjectName("label_10")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(730, 150, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(16)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(300, 30, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(350, 30, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_3, "")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 100))
        self.frame.setStyleSheet("background-color: rgb(72, 60, 70);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(270, 10, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(36)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(204, 183, 198);")
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "9999.99"))
        self.label_4.setText(_translate("Dialog", "9999.99"))
        self.label_2.setText(_translate("Dialog", "9999.99"))
        self.label_5.setText(_translate("Dialog", "9999.99"))
        self.label_3.setText(_translate("Dialog", "9999.99"))
        self.label_7.setText(_translate("Dialog", "On Date"))
        self.label.setText(_translate("Dialog", "9999.99"))
        self.label_10.setText(_translate("Dialog", "Find out Exchange Rates on Any Date"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Convert"))
        self.label_8.setText(_translate("Dialog", "The Value of INR to QAR in the past week"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Past Week"))
        self.label_9.setText(_translate("Dialog", "The Value of INR to QAR in the past"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Historical Data"))
        self.label_11.setText(_translate("Dialog", "Currency Converter"))
