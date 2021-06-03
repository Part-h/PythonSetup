from PyQt5 import QtCore,QtGui,QtWidgets,uic
import os,sys
import qrcode
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from datetime import date
import datetime


class mainproject(QtWidgets.QMainWindow):                      #inheriting class QMainWindow
    def __init__(self):
        super(mainproject,self).__init__()                     #to load ui file class need to call using super()
        uic.loadUi('project.ui',self)
        self.vaccineDate.setMinimumDate(date.today())
        
        self.saveq.clicked.connect(self.save_button)    
    def save_button(self):
         print("hhhh")
         #file_name=str(datetime.datetime.now())
         
         try:
            #  currentDate = self.currentDate.selectedDate().toString("yyyy-MM-dd")
            #  vaccinationDate = (self.vaccineDate.selectedDate().toString("yyyy-MM-dd"))
             
            #  print(currentDate,vaccinationDate)
            #  mdate1 = datetime.datetime.strptime(vaccinationDate, "%Y-%m-%d").date()                    #parse a string according to format of time 
            #  rdate1 = datetime.datetime.strptime(currentDate, "%Y-%m-%d").date()
            #  delta =  (mdate1 - rdate1).days
            #  self.label.setText(str(delta))
             print('delta')
         except Exception as e:
             print(e)
import sys
app=QtWidgets.QApplication(sys.argv)                                 #app here is object for QtWidgets class 
app.setStyleSheet('QPushButton{Height:30px;font-size:10px}')
window=mainproject()
window.show()
sys.exit(app.exec_())                                                #on exiting will release all resources & app execution other parameter
