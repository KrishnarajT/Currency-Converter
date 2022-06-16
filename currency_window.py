# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys, os
import currency as cd
from datetime import date, timedelta
from PyQt5 import QtGui
import numpy as np
import pandas as pd
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currency_database = cd.query_all_data()
        self.latest_currency_database = cd.gen_latest_currency_database(self.currency_database)
        
        # Setting some basic parameters
        self.setObjectName("Currency Converter")
        self.resize(1000, 700)
        self.setStyleSheet("background-color: rgb(204, 183, 198);")
        
        
        self.setupUi()
    
    def convert(self):
        print('you pressed to convert')
        
        # Setting the date and making the relevant currency_database
        
        self.selected_date = self.date_edit.date().toPyDate()
        self.dated_currency_database = self.currency_database[self.currency_database['date'] == self.selected_date.isoformat()]
        
        print(self.currency_database)
        
        # Getting the currently selected currencies. 
        
        self.cur1 = self.curncy_1_combo_box.currentText()
        self.cur2 = self.curncy_2_combo_box.currentText()
        self.cur3 = self.curncy_3_combo_box.currentText()
        self.cur4 = self.curncy_4_combo_box.currentText()
        self.cur5 = self.curncy_5_combo_box.currentText()
        self.cur6 = self.curncy_6_combo_box.currentText()
        self.cur7 = self.curncy_7_combo_box.currentText()
        self.cur8 = self.curncy_8_combo_box.currentText()
        
        
        # Getting the conversion value        
        self.cur_1_value = float(self.curncy_1_line_edit.text())
        
        # Converting the currencies, and setting their values to the respective labels. 
        
        self.cur_2_value = self.cur_1_value * cd.convert_currency(self.cur1, self.cur2, self.dated_currency_database)
        self.curncy_2_line_edit.setText(str(round(self.cur_2_value, 4)))
        
        self.cur_3_value = self.cur_1_value * cd.convert_currency(self.cur1, self.cur3, self.dated_currency_database)
        self.curncy_3_value_lbl.setText(str(round(self.cur_3_value, 4)))
        
        self.cur_4_value = self.cur_1_value * cd.convert_currency(self.cur1, self.cur4, self.dated_currency_database)
        self.curncy_4_value_lbl.setText(str(round(self.cur_4_value, 4)))
        
        self.cur_5_value = self.cur_1_value * cd.convert_currency(self.cur1, self.cur5, self.dated_currency_database)
        self.curncy_5_value_lbl.setText(str(round(self.cur_5_value, 4)))
        
        self.cur_6_value = self.cur_1_value * cd.convert_currency(self.cur1, self.cur6, self.dated_currency_database)
        self.curncy_6_value_lbl.setText(str(round(self.cur_6_value, 4)))
        
        self.cur_7_value = self.cur_1_value * cd.convert_currency(self.cur1, self.cur7, self.dated_currency_database)
        self.curncy_7_value_lbl.setText(str(round(self.cur_7_value, 4)))
        
        self.cur_8_value = self.cur_1_value * cd.convert_currency(self.cur1, self.cur8, self.dated_currency_database)
        self.curncy_8_value_lbl.setText(str(round(self.cur_8_value, 4)))
        
        # Debugging
        
        print(self.selected_date)
        print(self.cur1, self.cur2, 'are the selected currencies')
        print(self.dated_currency_database)
        print(self.cur_2_value)
    
        # Add the Graph for Past week Data. 
    
        cd.make_weekly_chart(self.cur1, self.cur2, self.currency_database)    
        self.im = QPixmap(os.path.join(os.getcwd(), 'images', f'{self.cur1} to {self.cur2} in the past Week.png'))
        self.im = self.im.scaledToHeight(self.week_graph_frame.height())
        self.label = QLabel(self.week_graph_frame)
        self.label.setPixmap(self.im)
        self.label.resize(self.im.width(), self.im.height())
        self.week_text_lbl.setText(f'Value of {self.cur1} to {self.cur2} in the Past Week')
    
        cd.gen_decade_graph(self.cur1, self.cur2)
        self.im = QPixmap(os.path.join(os.getcwd(), 'images', f'{self.cur1} to {self.cur2} 1999 - 2020.png'))
        self.im = self.im.scaledToHeight(self.historical_graph_frame.height())
        self.label = QLabel(self.historical_graph_frame)
        self.label.setPixmap(self.im)
        self.label.resize(self.im.width(), self.im.height())
        self.week_text_lbl.setText(f'Value of {self.cur1} to {self.cur2} in the Past 2 Decades')
    
    def setupUi(self):
        
        # Setting the Base Font
        
        font = QtGui.QFont()
        font.setFamily("Arvo")
        font.setPointSize(16)
        
        # Defining the Main QTab Widget to hold the tabs. 
        
        self.Navigation_tab = QtWidgets.QTabWidget(self)
        self.Navigation_tab.setGeometry(QtCore.QRect(0, 100, 1000, 600))
        self.Navigation_tab.setFont(font)
        self.Navigation_tab.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Navigation_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Navigation_tab.setAutoFillBackground(False)
        self.Navigation_tab.setStyleSheet("background-color: white;")
        self.Navigation_tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.Navigation_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Navigation_tab.setObjectName("Navigation_tab")
        
        
        #############################################################################################
        #### Tab 1 - Convert Tab ######        
        #############################################################################################
        
        self.convert_tab = QtWidgets.QWidget()
        self.convert_tab.setObjectName("convert_tab")
        self.Navigation_tab.addTab(self.convert_tab, "")
        
        # Defining the Elements inside that tab.
        
        self.curncy_7_combo_box = QtWidgets.QComboBox(self.convert_tab)
        self.curncy_7_combo_box.setGeometry(QtCore.QRect(240, 370, 90, 31))
        self.curncy_7_combo_box.setObjectName("curncy_7_combo_box")
        self.curncy_7_combo_box.addItems(list(self.latest_currency_database.index))
        
        font.setPointSize(18)
        self.curncy_4_value_lbl = QtWidgets.QLabel(self.convert_tab)
        self.curncy_4_value_lbl.setGeometry(QtCore.QRect(680, 270, 200, 31))
        self.curncy_4_value_lbl.setFont(font)
        self.curncy_4_value_lbl.setStyleSheet("color:rgb(72, 60, 70);")
        self.curncy_4_value_lbl.setObjectName("curncy_4_value_lbl")
        
        
        self.curncy_4_combo_box = QtWidgets.QComboBox(self.convert_tab)
        self.curncy_4_combo_box.setGeometry(QtCore.QRect(580, 270, 90, 31))
        self.curncy_4_combo_box.setObjectName("curncy_4_combo_box")
        self.curncy_4_combo_box.addItems(list(self.latest_currency_database.index))
        
        
        self.curncy_2_combo_box = QtWidgets.QComboBox(self.convert_tab)
        self.curncy_2_combo_box.setGeometry(QtCore.QRect(550, 140, 90, 31))
        self.curncy_2_combo_box.setObjectName("curncy_2_combo_box")
        self.curncy_2_combo_box.addItems(list(self.latest_currency_database.index))
        self.curncy_2_combo_box.setCurrentIndex(66)
        self.cur2 = self.curncy_2_combo_box.currentText()

        
        self.date_edit = QtWidgets.QDateEdit(self.convert_tab)
        self.date_edit.setGeometry(QtCore.QRect(480, 470, 191, 31))

        font.setPointSize(16)
        self.date_edit.setFont(font)
        self.date_edit.setStyleSheet("color:rgb(72, 60, 70);")
        self.date_edit.setObjectName("date_edit")

        font.setPointSize(18)
        self.curncy_6_value_lbl = QtWidgets.QLabel(self.convert_tab)
        self.curncy_6_value_lbl.setGeometry(QtCore.QRect(680, 320, 200, 31))
        self.curncy_6_value_lbl.setFont(font)
        self.curncy_6_value_lbl.setStyleSheet("color:rgb(72, 60, 70);")
        self.curncy_6_value_lbl.setObjectName("curncy_6_value_lbl")
        
        self.curncy_5_value_lbl = QtWidgets.QLabel(self.convert_tab)
        self.curncy_5_value_lbl.setGeometry(QtCore.QRect(340, 320, 200, 31))
        self.curncy_5_value_lbl.setFont(font)
        self.curncy_5_value_lbl.setStyleSheet("color:rgb(72, 60, 70);")
        self.curncy_5_value_lbl.setObjectName("curncy_5_value_lbl")
        
        self.curncy_8_value_lbl = QtWidgets.QLabel(self.convert_tab)
        self.curncy_8_value_lbl.setGeometry(QtCore.QRect(680, 370, 200, 31))
        self.curncy_8_value_lbl.setFont(font)
        self.curncy_8_value_lbl.setStyleSheet("color:rgb(72, 60, 70);")
        self.curncy_8_value_lbl.setObjectName("curncy_8_value_lbl")
        
        self.curncy_1_combo_box = QtWidgets.QComboBox(self.convert_tab)
        self.curncy_1_combo_box.setGeometry(QtCore.QRect(150, 140, 90, 31))
        self.curncy_1_combo_box.setObjectName("curncy_1_combo_box")
        self.curncy_1_combo_box.addItems(list(self.latest_currency_database.index))
        
        
        self.curncy_5_combo_box = QtWidgets.QComboBox(self.convert_tab)
        self.curncy_5_combo_box.setGeometry(QtCore.QRect(240, 320, 90, 31))
        self.curncy_5_combo_box.setObjectName("curncy_5_combo_box")
        self.curncy_5_combo_box.addItems(list(self.latest_currency_database.index))
        
        self.curncy_7_value_lbl = QtWidgets.QLabel(self.convert_tab)
        self.curncy_7_value_lbl.setGeometry(QtCore.QRect(340, 370, 200, 31))
        self.curncy_7_value_lbl.setFont(font)
        self.curncy_7_value_lbl.setStyleSheet("color:rgb(72, 60, 70);")
        self.curncy_7_value_lbl.setObjectName("curncy_7_value_lbl")
        
        self.curncy_8_combo_box = QtWidgets.QComboBox(self.convert_tab)
        self.curncy_8_combo_box.setGeometry(QtCore.QRect(580, 370, 90, 31))
        self.curncy_8_combo_box.setObjectName("curncy_8_combo_box")
        self.curncy_8_combo_box.addItems(list(self.latest_currency_database.index))
        
        self.date_label = QtWidgets.QLabel(self.convert_tab)
        self.date_label.setGeometry(QtCore.QRect(330, 470, 111, 31))

        font.setPointSize(18)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("color:rgb(72, 60, 70);")
        self.date_label.setObjectName("date_label")
        
        font.setPointSize(18)
        self.curncy_3_value_lbl = QtWidgets.QLabel(self.convert_tab)
        self.curncy_3_value_lbl.setGeometry(QtCore.QRect(340, 270, 200, 31))
        self.curncy_3_value_lbl.setFont(font)
        self.curncy_3_value_lbl.setStyleSheet("color:rgb(72, 60, 70);")
        self.curncy_3_value_lbl.setObjectName("curncy_3_value_lbl")
        
        font.setPointSize(16)
        self.curncy_1_line_edit = QtWidgets.QLineEdit(self.convert_tab)
        self.curncy_1_line_edit.setGeometry(QtCore.QRect(270, 140, 191, 31))
        self.curncy_1_line_edit.setFont(font)
        self.curncy_1_line_edit.setObjectName("curncy_1_line_edit")
        
        
        self.curncy_3_combo_box = QtWidgets.QComboBox(self.convert_tab)
        self.curncy_3_combo_box.setGeometry(QtCore.QRect(240, 270, 90, 31))
        self.curncy_3_combo_box.setObjectName("curncy_3_combo_box")
        self.curncy_3_combo_box.addItems(list(self.latest_currency_database.index))
        
        self.curncy_6_combo_box = QtWidgets.QComboBox(self.convert_tab)
        self.curncy_6_combo_box.setGeometry(QtCore.QRect(580, 320, 90, 31))
        self.curncy_6_combo_box.setObjectName("curncy_6_combo_box")
        self.curncy_6_combo_box.addItems(list(self.latest_currency_database.index))
        
        font.setPointSize(18)
        self.label_10 = QtWidgets.QLabel(self.convert_tab)
        self.label_10.setGeometry(QtCore.QRect(280, 30, 501, 31))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(72, 60, 70);")
        self.label_10.setObjectName("label_10")
        
        font.setPointSize(16)
        self.curncy_2_line_edit = QtWidgets.QLineEdit(self.convert_tab)
        self.curncy_2_line_edit.setGeometry(QtCore.QRect(670, 140, 191, 31))
        self.curncy_2_line_edit.setFont(font)
        self.curncy_2_line_edit.setObjectName("curncy_2_line_edit")
        
        self.convert_btn = QtWidgets.QPushButton(self.convert_tab)
        self.convert_btn.setGeometry(QtCore.QRect(350, 520, 311, 31))
        self.convert_btn.setFont(font)
        self.convert_btn.setAutoFillBackground(False)
        self.convert_btn.setStyleSheet("background-color:rgb(218, 203, 212);color:black;")
        self.convert_btn.setObjectName("convert_btn")
        self.convert_btn.clicked.connect(lambda: self.convert())
        
        #############################################################################################
        #### Tab 2 - Past Week Tab ######        
        #############################################################################################
        
        self.past_week_tab = QtWidgets.QWidget()
        self.past_week_tab.setObjectName("past_week_tab")
        self.Navigation_tab.addTab(self.past_week_tab, "")
       
        # Adding the elements inside the tab. 
       
        self.week_text_lbl = QtWidgets.QLabel(self.past_week_tab)
        self.week_text_lbl.setGeometry(QtCore.QRect(280, 20, 501, 31))

        font.setPointSize(18)
        self.week_text_lbl.setFont(font)
        self.week_text_lbl.setStyleSheet("color:rgb(72, 60, 70);")
        self.week_text_lbl.setObjectName("week_text_lbl")
       
        self.week_graph_frame = QtWidgets.QFrame(self.past_week_tab)
        self.week_graph_frame.setGeometry(QtCore.QRect(120, 80, 750, 450))
        self.week_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.week_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.week_graph_frame.setObjectName("week_graph_frame")
       
       
        #############################################################################################
        #### Tab 3 - Historical Tab ######        
        #############################################################################################
        
       
        self.historical_tab = QtWidgets.QWidget()
        self.historical_tab.setObjectName("historical_tab")
        self.Navigation_tab.addTab(self.historical_tab, "")
        
        self.historical_text_lbl = QtWidgets.QLabel(self.historical_tab)
        self.historical_text_lbl.setGeometry(QtCore.QRect(280, 30, 441, 31))

        font.setPointSize(18)
        self.historical_text_lbl.setFont(font)
        self.historical_text_lbl.setStyleSheet("color:rgb(72, 60, 70);")
        self.historical_text_lbl.setObjectName("historical_text_lbl")
        
        self.historical_graph_frame = QtWidgets.QFrame(self.historical_tab)
        self.historical_graph_frame.setGeometry(QtCore.QRect(120, 80, 750, 450))
        self.historical_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historical_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historical_graph_frame.setObjectName("historical_graph_frame")
        
        
        self.Title_frame = QtWidgets.QFrame(self)
        self.Title_frame.setGeometry(QtCore.QRect(0, 0, 1000, 100))
        self.Title_frame.setStyleSheet("background-color: rgb(72, 60, 70);")
        self.Title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title_frame.setObjectName("Title_frame")
        
        self.label_11 = QtWidgets.QLabel(self.Title_frame)
        self.label_11.setGeometry(QtCore.QRect(270, 10, 501, 81))

        font.setPointSize(36)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(204, 183, 198);")
        self.label_11.setObjectName("label_11")

        #############################################################################################
        #### Tab 4 - Help and Credits Tab ######        
        #############################################################################################
        


        self.help_tab = QtWidgets.QWidget()
        self.help_tab.setObjectName("help_tab")
        self.Navigation_tab.addTab(self.help_tab, "")

        font.setPointSize(18)
        self.help_lbl = QtWidgets.QLabel(self.help_tab)
        self.help_lbl.setText("Some text will be here. ")
        self.help_lbl.setFont(font)
        self.help_lbl.setStyleSheet("color:rgb(72, 60, 70);")
        self.help_lbl.setObjectName("help_lbl")
        
        
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.curncy_4_value_lbl.setText(_translate("Dialog", "9999.99"))
        self.curncy_6_value_lbl.setText(_translate("Dialog", "9999.99"))
        self.curncy_5_value_lbl.setText(_translate("Dialog", "9999.99"))
        self.curncy_8_value_lbl.setText(_translate("Dialog", "9999.99"))
        self.curncy_7_value_lbl.setText(_translate("Dialog", "9999.99"))
        self.date_label.setText(_translate("Dialog", "On Date"))
        self.curncy_3_value_lbl.setText(_translate("Dialog", "9999.99"))
        self.label_10.setText(_translate("Dialog", "Find out Exchange Rates on Any Date"))
        self.convert_btn.setText(_translate("Dialog", "Convert for this Date"))
        self.Navigation_tab.setTabText(self.Navigation_tab.indexOf(self.convert_tab), _translate("Dialog", "Convert"))
        self.week_text_lbl.setText(_translate("Dialog", "The Value of INR to QAR in the past week"))
        self.Navigation_tab.setTabText(self.Navigation_tab.indexOf(self.past_week_tab), _translate("Dialog", "Past Week Data"))
        self.historical_text_lbl.setText(_translate("Dialog", "The Value of INR to QAR in the past"))
        self.Navigation_tab.setTabText(self.Navigation_tab.indexOf(self.historical_tab), _translate("Dialog", "Historical Data"))
        self.Navigation_tab.setTabText(self.Navigation_tab.indexOf(self.help_tab), _translate("Dialog", "Help and Credits"))
        self.Navigation_tab.setCurrentIndex(self.Navigation_tab.indexOf(self.convert_tab))
        self.label_11.setText(_translate("Dialog", "Currency Converter"))
        
        # Setting the default values of the combo boxes
        
        self.curncy_1_combo_box.setCurrentIndex(int(np.where(self.latest_currency_database.index == 'USD')[0]))
        self.curncy_2_combo_box.setCurrentIndex(int(np.where(self.latest_currency_database.index == 'INR')[0]))
        self.curncy_3_combo_box.setCurrentIndex(int(np.where(self.latest_currency_database.index == 'QAR')[0]))
        self.curncy_4_combo_box.setCurrentIndex(int(np.where(self.latest_currency_database.index == 'EUR')[0]))
        self.curncy_5_combo_box.setCurrentIndex(int(np.where(self.latest_currency_database.index == 'BTC')[0]))
        self.curncy_6_combo_box.setCurrentIndex(int(np.where(self.latest_currency_database.index == 'JPY')[0]))
        self.curncy_7_combo_box.setCurrentIndex(int(np.where(self.latest_currency_database.index == 'SAR')[0]))
        self.curncy_8_combo_box.setCurrentIndex(int(np.where(self.latest_currency_database.index == 'AED')[0]))
        
        
        self.date_edit.setDate(date.today() + timedelta(days =-1))
        
        
        self.validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'[0-9].+'))
        self.curncy_1_line_edit.setValidator(self.validator)
        self.curncy_1_line_edit.setText('1.000')
        self.cur_1_value = 1.000
        self.curncy_2_line_edit.setValidator(self.validator)
