# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        #Company
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        
        #Username
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 31))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        #Password
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 71, 21))
        self.label_3.setObjectName("label_3")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 130, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        #lcds
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(130, 190, 64, 23))
        #Lcd  Coloring
        palette = self.lcdNumber.palette()
        # foreground color
        palette.setColor(palette.WindowText, QtGui.QColor(255, 0, 0))
        # background color
        palette.setColor(palette.Background, QtGui.QColor(0,0,0))
        # "Light" border
        palette.setColor(palette.Light, QtGui.QColor(0, 0, 0))
        # set the palette
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcds()
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 111, 21))
        self.label_4.setObjectName("label_4")

        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 170, 371, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.updater)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 250, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 10, 181, 31))
        self.label_5.setObjectName("label_5")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(194, 250, 101, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Saver"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Company:</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Username:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "Number of passwords:"))
        self.pushButton.setText(_translate("Dialog", "Add entry"))
        self.pushButton_2.setText(_translate("Dialog", "View entries"))
        self.pushButton_3.setText(_translate("Dialog", "Close"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Password saver:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Dialog", "Open in Notepad"))

    def counter(self):
        #counts number of entries
        i=0
        with open('Password.txt','+r') as file:
            for line in file:
                for part in line.split():
                    if "Username:" in part:
                        i+=1
        print("entries:",i)
        return(i)
    def lcds(self):
        i=self.counter()
        #print(i)
        self.lcdNumber.display(i)
    def updater(self):
        global comp
        global name
        global passw

        comp=self.lineEdit.text()
        name=self.lineEdit_2.text()
        passw=self.lineEdit_3.text()
        print("enries:",comp,name,passw,".")
        if comp =='' or name=='' or passw=='':
            print("error")
            QtWidgets.QMessageBox.question(None, 'Error', "Please fill all the fields", QtWidgets.QMessageBox.Ok)
        else:
            #Testing
            k=[]
            var=True
            with open('Password.txt','+r') as file:
               for line in file:
                    for part in line.split():
                        if ':' in part:
                            k.append(part.split(':'))
            for i in range(0,len(k),3):
                if k[i][1]=='':
                    if comp==k[i][0] and name==k[i+1][1] and passw==k[i+2][1]:
                        print("already copied")
                        var=False
            #updating
            if var:
                with open('Password.txt','a') as file:
                    file.write(comp+':\n\nUsername:'+name+'\nPassword:'+passw+'\n\n')
                print("added successfully")
                self.lcds()
            else:
               QtWidgets.QMessageBox.question(None, 'Error', "Entry Already Exists!", QtWidgets.QMessageBox.Ok) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
