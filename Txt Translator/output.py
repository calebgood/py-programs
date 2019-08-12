# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translatetxt.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import os,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from googletrans import Translator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.input = QtWidgets.QTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(20, 30, 411, 111))
        self.input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.input.setObjectName("input")

        self.output = QtWidgets.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 250, 411, 111))
        self.output.setReadOnly(True)
        self.output.setObjectName("output")

        self.selectfile = QtWidgets.QLabel(self.centralwidget)
        self.selectfile.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.selectfile.setObjectName("selectfile")
        self.outputtxt = QtWidgets.QLabel(self.centralwidget)

        self.outputtxt.setGeometry(QtCore.QRect(20, 230, 61, 16))
        self.outputtxt.setObjectName("outputtxt")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(180, 180, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.inlang = QtWidgets.QComboBox(self.centralwidget)
        self.inlang.setGeometry(QtCore.QRect(40, 180, 111, 21))
        self.inlang.setObjectName("inlang")
        self.inlang.addItem("")

        self.inlang.addItem('Amharic')
        self.inlang.addItem('Arabic')
        self.inlang.addItem('Basque')
        self.inlang.addItem('Bengali')
        self.inlang.addItem('English (UK)')
        self.inlang.addItem('Portuguese (Brazil)')
        self.inlang.addItem('Bulgarian')
        self.inlang.addItem('Catalan')
        self.inlang.addItem('Cherokee')
        self.inlang.addItem('Croatian')
        self.inlang.addItem('Czech')
        self.inlang.addItem('Danish')
        self.inlang.addItem('Dutch')
        self.inlang.addItem('English (US)')
        self.inlang.addItem('Estonian')
        self.inlang.addItem('Filipino')
        self.inlang.addItem('Finnish')
        self.inlang.addItem('French')
        self.inlang.addItem('German')
        self.inlang.addItem('Greek')
        self.inlang.addItem('Gujarati')
        self.inlang.addItem('Hebrew')
        self.inlang.addItem('Hindi')
        self.inlang.addItem('Hungarian')
        self.inlang.addItem('Icelandic')
        self.inlang.addItem('Indonesian')
        self.inlang.addItem('Italian')
        self.inlang.addItem('Japanese')
        self.inlang.addItem('Kannada')
        self.inlang.addItem('Korean')
        self.inlang.addItem('Latvian')
        self.inlang.addItem('Lithuanian')
        self.inlang.addItem('Malay')
        self.inlang.addItem('Malayalam')
        self.inlang.addItem('Marathi')
        self.inlang.addItem('Norwegian')
        self.inlang.addItem('Polish')
        self.inlang.addItem('Portuguese (Portugal)')
        self.inlang.addItem('Romanian')
        self.inlang.addItem('Russian')
        self.inlang.addItem('Serbian')
        self.inlang.addItem('Chinese (PRC)')
        self.inlang.activated[str].connect(self.inp)

        self.outlang = QtWidgets.QComboBox(self.centralwidget)
        self.outlang.setGeometry(QtCore.QRect(300, 180, 111, 21))
        self.outlang.setObjectName("outlang")
        self.outlang.addItem("")

        self.outlang.addItem('Amharic')
        self.outlang.addItem('Arabic')
        self.outlang.addItem('Basque')
        self.outlang.addItem('Bengali')
        self.outlang.addItem('English (UK)')
        self.outlang.addItem('Portuguese (Brazil)')
        self.outlang.addItem('Bulgarian')
        self.outlang.addItem('Catalan')
        self.outlang.addItem('Cherokee')
        self.outlang.addItem('Croatian')
        self.outlang.addItem('Czech')
        self.outlang.addItem('Danish')
        self.outlang.addItem('Dutch')
        self.outlang.addItem('English (US)')
        self.outlang.addItem('Estonian')
        self.outlang.addItem('Filipino')
        self.outlang.addItem('Finnish')
        self.outlang.addItem('French')
        self.outlang.addItem('German')
        self.outlang.addItem('Greek')
        self.outlang.addItem('Gujarati')
        self.outlang.addItem('Hebrew')
        self.outlang.addItem('Hindi')
        self.outlang.addItem('Hungarian')
        self.outlang.addItem('Icelandic')
        self.outlang.addItem('Indonesian')
        self.outlang.addItem('Italian')
        self.outlang.addItem('Japanese')
        self.outlang.addItem('Kannada')
        self.outlang.addItem('Korean')
        self.outlang.addItem('Latvian')
        self.outlang.addItem('Lithuanian')
        self.outlang.addItem('Malay')
        self.outlang.addItem('Malayalam')
        self.outlang.addItem('Marathi')
        self.outlang.addItem('Norwegian')
        self.outlang.addItem('Polish')
        self.outlang.addItem('Portuguese (Portugal)')
        self.outlang.addItem('Romanian')
        self.outlang.addItem('Russian')
        self.outlang.addItem('Serbian')
        self.outlang.addItem('Chinese (PRC)')
        self.outlang.addItem('Slovak')
        self.outlang.addItem('Slovenian')
        self.outlang.addItem('Spanish')
        self.outlang.addItem('Swahili')
        self.outlang.addItem('Swedish')
        self.outlang.addItem('Tamil')
        self.outlang.addItem('Telugu')
        self.outlang.addItem('Thai')
        self.outlang.addItem('Chinese (Taiwan)')
        self.outlang.addItem('Turkish')
        self.outlang.addItem('Urdu')
        self.outlang.addItem('Ukrainian')
        self.outlang.addItem('Vietnamese')
        self.outlang.addItem('Welsh')
        self.outlang.activated[str].connect(self.out)
        
        self.Translate = QtWidgets.QPushButton(self.centralwidget)
        self.Translate.setGeometry(QtCore.QRect(450, 180, 81, 23))
        self.Translate.setObjectName("Translate")
        self.Translate.clicked.connect(self.translate)

        self.saveas = QtWidgets.QPushButton(self.centralwidget)
        self.saveas.setGeometry(QtCore.QRect(450, 40, 75, 23))
        self.saveas.setObjectName("saveas")

        self.Overwrite = QtWidgets.QPushButton(self.centralwidget)
        self.Overwrite.setGeometry(QtCore.QRect(450, 250, 75, 23))
        self.Overwrite.setObjectName("Overwrite")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setDisabled(True)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 160, 91, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 160, 91, 16))
        self.label_2.setObjectName("label_2")

        self.clearAll = QtWidgets.QPushButton(self.centralwidget)
        self.clearAll.setGeometry(QtCore.QRect(450, 70, 75, 23))
        self.clearAll.setObjectName("clearAll")

        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(210, 10, 47, 13))
        self.loading.setObjectName("loading")
        self.loading.hide()
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        #MenuBar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File.triggered.connect(self.accept)
        
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.close_application)
    
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionExit)

        self.menuAbout.addAction(self.actionAbout)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.clearAll.clicked.connect(self.input.clear)
        self.clearAll.clicked.connect(self.output.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.selectfile.setText(_translate("MainWindow", "Selected File:"))
        self.outputtxt.setText(_translate("MainWindow", "Output Text:"))
        self.inlang.setItemText(0, _translate("MainWindow", "---Select---"))
        self.outlang.setItemText(0, _translate("MainWindow", "---Select---"))
        self.Translate.setText(_translate("MainWindow", "Translate"))
        self.saveas.setText(_translate("MainWindow", "Save As..."))
        self.Overwrite.setText(_translate("MainWindow", "Save..."))
        self.label.setText(_translate("MainWindow", "Input Language:"))
        self.label_2.setText(_translate("MainWindow", "Output Language:"))
        self.clearAll.setText(_translate("MainWindow", "Clear All"))
        self.loading.setText(_translate("MainWindow", "Loading..."))
        self.pushButton.setText(_translate("MainWindow", "Copy text"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About.."))

    def accept(self):
        global translator
        global OutputLang
        global InputLang
        global Filename
        global fname
        global check
        global data
        translator = Translator()
        dlg = QtWidgets.QFileDialog()
        fname = dlg.getOpenFileName(None, 'Open file', "", "Text Files(*.txt);;All Files (*)")
        if fname != ('', ''):
            print(fname)
            fname = fname[0]
            fname, Filename = os.path.split(os.path.abspath(fname))
            print(fname)
            print(Filename)
            self.lineEdit.setText(Filename)
            InputLang = ""
            print(os.path.splitext(Filename)[1])
            try:
                subs = open(fname + '\\' + Filename)
                try:
                    self.loading.show()
                    self.input.setText(subs.read())
                    data=self.input.toPlainText()
                    #check variable has number of characters count
                    check=len(data)
                    data=data.split("\n")
                    InputLang = translator.detect(data[0]).lang
                    self.inlang.setCurrentText(InputLang)
                    self.loading.hide()
                    subs.close()
                except Exception as e:
                    print(e)
                    QtWidgets.QMessageBox.question(None, 'Error', "No Internet eh?!!", QtWidgets.QMessageBox.Ok)
                    self.loading.hide()
                    self.cupper()
                    #self.lineEdit.setText('')
                if InputLang != '':
                    self.inlang.setCurrentText(InputLang)
                    #InputLang = self.lang(InputLang)
            except Exception as e:
                print(e)
                QtWidgets.QMessageBox.question(None, 'Error', "Unable to parse given file", QtWidgets.QMessageBox.Ok)
                Filename, fname = '', ''
                self.lineEdit.setText('')

    def cupper(self):
        global InputLang
        try:
            time.sleep(5)
            InputLang = translator.detect(data[0]).lang 
            self.inlang.setCurrentText(InputLang)
        except Exception as e:
            print("Cupper:",e)
            self.cupper()

    def lang(self,text):
        codes = {'English': 'en', 'Amharic': 'am', 'Arabic': 'ar', 'Basque': 'eu', 'Bengali': 'bn',
                 'English (UK)': 'en', 'Portuguese (Brazil)': 'pt-BR', 'Bulgarian': 'bg', 'Catalan': 'ca',
                 'Cherokee': 'chr', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl',
                 'English (US)': 'en', 'Estonian': 'et', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr',
                 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Hebrew': 'iw', 'Hindi': 'hi', 'Hungarian': 'hu',
                 'Icelandic': 'is', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kannada': 'kn',
                 'Korean': 'ko', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Malay': 'ms', 'Malayalam': 'ml', 'Marathi': 'mr',
                 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese (Portugal)': 'pt-PT', 'Romanian': 'ro', 'Russian': 'ru',
                 'Serbian': 'sr', 'Chinese (PRC)': 'zh-CN', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es',
                 'Swahili': 'sw', 'Swedish': 'sv', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th',
                 'Chinese (Taiwan)': 'zh-TW', 'Turkish': 'tr', 'Urdu': 'ur', 'Ukrainian': 'uk', 'Vietnamese': 'vi',
                 'Welsh': 'cy'}
        #print(codes[text])
        return (codes[text])

    def out(self, text):
        global OutputLang
        OutputLang = self.lang(text)
        #self.output.setText(OutputLang)
    def inp(self,text):
        global InputLang
        InputLang = self.lang(text)
        #self.input.setText(InputLang)

    def translate(self):
        try:
            global OutputLang
            global InputLang
            global data
            global translator
            global check
            a = 50
            self.safety()
            print(InputLang)
            full=str()
            full_trans=str()
            # Translating...
            print("Started Translating:")
            print("\n###",InputLang,"\n",OutputLang,"###")
            if check>1000:
                for k in range(0, a):
                    for i in range((k * len(data)) // a, ((k + 1) * len(data)) // a):
                        full = full + data[i]
                    if len(full)>200:
                        for i in range((k * len(full)) // a, ((k + 1) * len(full)) // a):
                            half+=full[i]
                        full_trans += translator.translate(full, dest=OutputLang, src=InputLang).text
                        half=""
                    else:
                        full_trans += translator.translate(full, dest=OutputLang, src=InputLang).text
                    full=""
                    QApplication.processEvents()
                    self.progressBar.setValue(((k + 1) * 100) // a)
                    print(k + 1, "/", a, "parts Done")
            else:
                for i in range(len(data)):
                    full_trans += translator.translate(data[i], dest=OutputLang, src=InputLang).text
            
            
            self.output.setText(full_trans)
            
           # full.pop(0)
            
        except Exception as op:
            print(op)
            QtWidgets.QMessageBox.question(None, 'Error', "Can't Translate Now!!", QtWidgets.QMessageBox.Ok)

    def safety(self):
        global OutputLang
        if OutputLang:
            pass
        else:
            OutputLang = "English"

    def save(self):
        global OutputLang
        global Filename
        global fname
        global full

        if self.progressBar.value()==100:
            try:
                print("saving...")
                subs.save(fname + '\\' + os.path.splitext(Filename)[0] + "-" + OutputLang + ".srt", encoding='utf-8')
                self.progressBar.setValue(0)
                self.lineEdit.setText('')
                print("Done...")
            except:
                QtWidgets.QMessageBox.question(None, 'Error', "Something went wrong!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.question(None, 'Error', "Not Yet Translated!!", QtWidgets.QMessageBox.Ok)

    def close_application(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
