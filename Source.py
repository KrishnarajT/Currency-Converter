import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets, QtCore
from currency_window import MainWindow
import currency as cd
import requests, json, os, urllib
import PIL
from datetime import date, time, datetime



if __name__ == '__main__':
    

    
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()  
    ui.show()
    sys.exit(app.exec_())