import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets, QtCore
from currency_window import MainWindow
import currency as cd
import requests, json, os, urllib
import PIL
from datetime import date, time, datetime


#! todo 
# fix the strptime thing, for that while taking from csv, make sure to convert the date and then return the dataframe
# make all the other places where you used strptime to the default one
# download historical dtaa
# Make historical datframe, and make the csv file
# make another folder for the csv files. 
# Load historical dataframe graph, after making it
# implement the same day checking and not using api feature. 
# implement using the previous day's api if error in retreiving today's API date feature
# Add Credits and Help
# Comment and Clean Code
# Take screenshots of working and put in the folder. 
# Make EXE and linux Executable File.
# Write readme for uploading to GitHub with images. 


if __name__ == '__main__':
    

    
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()  
    ui.show()
    sys.exit(app.exec_())