import PyQt5
import time
import webbrowser
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog
import configparser
from configparser import ConfigParser


class Ui_Dialog(object):

    def execute(self):
        #Einstellungen für Opera
        #browser_path="C:\Program Files\Opera\launcher.exe"
        #webbrowser.register('opera', None,webbrowser.BackgroundBrowser(browser_path))

        browser_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(browser_path))
        
        if self.check.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste.text()) 
        else:
            print("Box not checked")
            
        if self.check_2.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_2.text())
        else:
            print("Box not checked")

        if self.check_3.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_3.text()) 
        else:
            print("Box not checked")

        if self.check_4.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_4.text()) 
        else:
            print("Box not checked")

        #time.sleep(1)

        if self.check_5.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_5.text()) 
        else:
            print("Box not checked")

        if self.check_6.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_6.text()) 
        else:
            print("Box not checked")

        if self.check_7.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_7.text()) 
        else:
            print("Box not checked")

        if self.check_8.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_8.text()) 
        else:
            print("Box not checked")

        #time.sleep(1)

        if self.check_9.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_9.text()) 
        else:
            print("Box not checked")

        if self.check_10.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_10.text())
        else:
            print("Box not checked")

        if self.check_11.isChecked():       
            webbrowser.get('firefox').open_new_tab(self.adressleiste_11.text()) 
        else:
            print("Box not checked")

        if self.check_12.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_12.text())
        else:
            print("Box not checked")

        #time.sleep(1) 
        
        if self.check_13.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_13.text())
        else:
            print("Box not checked")

        if self.check_14.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_14.text()) 
        else:
            print("Box not checked")

        if self.check_15.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_15.text()) 
        else:
            print("Box not checked")

        if self.check_16.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_16.text()) 
        else:
            print("Box not checked")

        #time.sleep(1)

        if self.check_17.isChecked():
            webbrowser.get('firefox').open_new_tab(self.adressleiste_17.text()) 
        else:
            print("Box not checked")

    def save(self):
        file = "test.ini"
        config = configparser.ConfigParser()
        config.read(file)
        # "gmx.de" input von Adresszeile
        config.set("key", "value_1", self.adressleiste.text())
        config.set("key", "value_2", self.adressleiste_2.text())
        config.set("key", "value_3", self.adressleiste_3.text())
        config.set("key", "value_4", self.adressleiste_4.text())
        config.set("key", "value_5", self.adressleiste_5.text())
        config.set("key", "value_6", self.adressleiste_6.text())
        config.set("key", "value_7", self.adressleiste_7.text())
        config.set("key", "value_8", self.adressleiste_8.text())
        config.set("key", "value_9", self.adressleiste_9.text())
        config.set("key", "value_10", self.adressleiste_10.text())
        config.set("key", "value_11", self.adressleiste_11.text())
        config.set("key", "value_12", self.adressleiste_12.text())
        config.set("key", "value_13", self.adressleiste_13.text())
        config.set("key", "value_14", self.adressleiste_14.text())
        config.set("key", "value_15", self.adressleiste_15.text())
        config.set("key", "value_16", self.adressleiste_16.text())
        config.set("key", "value_17", self.adressleiste_17.text())
        
        with open(file, "w") as configfile:
            config.write(configfile)
       

    #def save(self):
    #    with open("test.txt", "w") as f:
    #        my_text = self.adressleiste.toText()
    #        f.write(my_text)

    #text_1 = config["Browserprogramm"]["Linie_1"]

#TESTEN, OB SET TEXT AUCH NACH NEUSTARTT DES PROGRAMMS SPEICHERT
#    WENN JA: rausfinden, wie -settext geändert werden kann, ggf. input()
#    WENN NEIN: parsing, savefile, txt file speichern
#2. Lösung Liste in schon erstellter config.ini erstellen und nach adressleisten füllen


    def setupUi(self, Dialog):
        self.file = "test.ini"
        self.config = ConfigParser()
        self.config.read(self.file)

        self.speichern = QtWidgets.QPushButton(Dialog)
        self.speichern.setGeometry(QtCore.QRect(230, 570, 75, 23))
        self.speichern.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.speichern.setObjectName("speichern")
        ###################################################################
        self.speichern.clicked.connect(self.save)
        ###################################################################
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(330, 570, 75, 23))
        self.ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok.setObjectName("ok")
        ###################################################################
        self.ok.clicked.connect(self.execute)
        ###################################################################
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(50, 20, 501, 531))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.adressleiste = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste.setObjectName("adressleiste")
        self.adressleiste.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste.setText(self.config["key"]["value_1"])
        self.adressleiste_2 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_2.setObjectName("adressleiste_2")
        self.adressleiste_2.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_2.setText(self.config["key"]["value_2"])
        self.adressleiste_3 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_3.setObjectName("adressleiste_3")
        self.adressleiste_3.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_3.setText(self.config["key"]["value_3"])
        self.adressleiste_4 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_4.setObjectName("adressleiste_4")
        self.adressleiste_4.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_4.setText(self.config["key"]["value_4"])
        self.adressleiste_5 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_5.setObjectName("adressleiste_5")
        self.adressleiste_5.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_5.setText(self.config["key"]["value_5"])
        self.adressleiste_6 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_6.setObjectName("adressleiste_6")
        self.adressleiste_6.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_6.setText(self.config["key"]["value_6"])
        self.adressleiste_7 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_7.setObjectName("adressleiste_7")
        self.adressleiste_7.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_7.setText(self.config["key"]["value_7"])
        self.adressleiste_8 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_8.setObjectName("adressleiste_8")
        self.adressleiste_8.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_8.setText(self.config["key"]["value_8"])
        self.adressleiste_9 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_9.setObjectName("adressleiste_9")
        self.adressleiste_9.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_9.setText(self.config["key"]["value_9"])
        self.adressleiste_10 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_10.setObjectName("adressleiste_10")
        self.adressleiste_10.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_10.setText(self.config["key"]["value_10"])
        self.adressleiste_11 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_11.setObjectName("adressleiste_11")
        self.adressleiste_11.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_11.setText(self.config["key"]["value_11"])
        self.adressleiste_12 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_12.setObjectName("adressleiste_12")
        self.adressleiste_12.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_12.setText(self.config["key"]["value_12"])
        self.adressleiste_13 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_13.setObjectName("adressleiste_13")
        self.adressleiste_13.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_13.setText(self.config["key"]["value_13"])
        self.adressleiste_14 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_14.setObjectName("adressleiste_14")
        self.adressleiste_14.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_14.setText(self.config["key"]["value_14"])
        self.adressleiste_15 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_15.setObjectName("adressleiste_15")
        self.adressleiste_15.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_15.setText(self.config["key"]["value_15"])
        self.adressleiste_16 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_16.setObjectName("adressleiste_16")
        self.adressleiste_16.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_16.setText(self.config["key"]["value_16"])
        self.adressleiste_17 = QtWidgets.QLineEdit(self.splitter)
        self.adressleiste_17.setObjectName("adressleiste_17")
        self.adressleiste_17.setPlaceholderText("Hier einen Link reinziehen/einfügen/reinschreieben")
        self.adressleiste_17.setText(self.config["key"]["value_17"])
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(560, 10, 20, 561))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.check = QtWidgets.QCheckBox(self.widget)
        self.check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check.setText("")
        self.check.setChecked(False)
        self.check.setObjectName("check")
        self.verticalLayout.addWidget(self.check)
        self.check_2 = QtWidgets.QCheckBox(self.widget)
        self.check_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_2.setText("")
        self.check_2.setObjectName("check_2")
        self.verticalLayout.addWidget(self.check_2)
        self.check_3 = QtWidgets.QCheckBox(self.widget)
        self.check_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_3.setText("")
        self.check_3.setObjectName("check_3")
        self.verticalLayout.addWidget(self.check_3)
        self.check_4 = QtWidgets.QCheckBox(self.widget)
        self.check_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_4.setText("")
        self.check_4.setObjectName("check_4")
        self.verticalLayout.addWidget(self.check_4)
        self.check_5 = QtWidgets.QCheckBox(self.widget)
        self.check_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_5.setText("")
        self.check_5.setObjectName("check_5")
        self.verticalLayout.addWidget(self.check_5)
        self.check_6 = QtWidgets.QCheckBox(self.widget)
        self.check_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_6.setText("")
        self.check_6.setObjectName("check_6")
        self.verticalLayout.addWidget(self.check_6)
        self.check_7 = QtWidgets.QCheckBox(self.widget)
        self.check_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_7.setText("")
        self.check_7.setObjectName("check_7")
        self.verticalLayout.addWidget(self.check_7)
        self.check_8 = QtWidgets.QCheckBox(self.widget)
        self.check_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_8.setText("")
        self.check_8.setObjectName("check_8")
        self.verticalLayout.addWidget(self.check_8)
        self.check_9 = QtWidgets.QCheckBox(self.widget)
        self.check_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_9.setText("")
        self.check_9.setObjectName("check_9")
        self.verticalLayout.addWidget(self.check_9)
        self.check_10 = QtWidgets.QCheckBox(self.widget)
        self.check_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_10.setText("")
        self.check_10.setObjectName("check_10")
        self.verticalLayout.addWidget(self.check_10)
        self.check_11 = QtWidgets.QCheckBox(self.widget)
        self.check_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_11.setText("")
        self.check_11.setObjectName("check_11")
        self.verticalLayout.addWidget(self.check_11)
        self.check_12 = QtWidgets.QCheckBox(self.widget)
        self.check_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_12.setText("")
        self.check_12.setObjectName("check_12")
        self.verticalLayout.addWidget(self.check_12)
        self.check_13 = QtWidgets.QCheckBox(self.widget)
        self.check_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_13.setText("")
        self.check_13.setObjectName("check_13")
        self.verticalLayout.addWidget(self.check_13)
        self.check_14 = QtWidgets.QCheckBox(self.widget)
        self.check_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_14.setText("")
        self.check_14.setObjectName("check_14")
        self.verticalLayout.addWidget(self.check_14)
        self.check_15 = QtWidgets.QCheckBox(self.widget)
        self.check_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_15.setText("")
        self.check_15.setObjectName("check_15")
        self.verticalLayout.addWidget(self.check_15)
        self.check_16 = QtWidgets.QCheckBox(self.widget)
        self.check_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_16.setText("")
        self.check_16.setObjectName("check_16")
        self.verticalLayout.addWidget(self.check_16)
        self.check_17 = QtWidgets.QCheckBox(self.widget)
        self.check_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_17.setText("")
        self.check_17.setObjectName("check_17")
        self.verticalLayout.addWidget(self.check_17)

        self.retranslateUi(Dialog)
        self.check.toggled['bool'].connect(self.check.setChecked)
        self.check_2.toggled['bool'].connect(self.check_2.setChecked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.speichern.setText(_translate("Dialog", "Speichern"))
        self.ok.setText(_translate("Dialog", "Ausführen"))
        Dialog.setWindowTitle(_translate("Dialog", "Programm"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowIcon(QIcon("browser.png"))
    Dialog.show()
    sys.exit(app.exec_())

#LINKS
#https://www.tutorialspoint.com/pyqt/pyqt_qfiledialog_widget.htm                                                      - PyQt - QFileDialog Widget
#https://www.tutorialspoint.com/configuration-file-parser-in-python-configparser                                      - Configparser
#https://www.tutorialspoint.com/pyqt/pyqt_qlineedit_widget.htm                                                        - PyQt - QLineEdit Widget
#https://zetcode.com/pyqt/qlineedit/                                                                                  - PyQt QLineEdit
#https://www.qtcentre.org/threads/14579-How-to-save-file-with-QFileDialog                                             - How to save file with QFileDialog
#https://david-estevez.gitbooks.io/tutorial-pyside-pyqt4/content/06_dialog.html                                       - save and load file
#https://www.learnpyqt.com/tutorials/basic-widgets/                                                                   - widgets
#https://gist.github.com/eyllanesc/be8a476bb7038c7579c58609d7d0f031                                                   - save and load file
#https://stackoverflow.com/questions/49837565/how-to-save-text-in-qlineedits-in-pyqt-even-if-the-widget-gets-closed   - save and restore
#https://www.programcreek.com/python/example/103045/PyQt5.QtWidgets.QFileDialog.getSaveFileName                       - PyQt5.QtWidgets.QFileDialog.getSaveFileName()
#https://www.programcreek.com/python/example/103046/PyQt5.QtWidgets.QFileDialog.getOpenFileName                       - PyQt5.QtWidgets.QFileDialog.getOpenFileName()
#https://www.programcreek.com/python/index/9804/PyQt5.QtWidgets.QFileDialog                                           - get OpenFileName,SaveFileName,ExistingDirectory
#https://www.youtube.com/watch?v=Gdw0-QGq-z0                                                                          - config file
#https://www.youtube.com/watch?v=fH0GQuF0FdE                                                                          - File Open and Save
#https://stackoverflow.com/questions/52076299/pyqt5-doesnt-save-settings-to-ini-files                                 - save settings to ini files
#https://python-forum.io/Thread-Save-User-Input-From-LineEdit-Box-To-Variable                                         - Save User Input From LineEdit
#https://stackoverflow.com/questions/48988871/pyqt5-save-qlineedit-to-text-file-with-qfiledialog/48989730             - Save QlineEdit to text file
#https://www.youtube.com/watch?v=4B3kYF5BhB4&t=477s                                                                   - QFileDialog widget example

#Eingaben speichern
#Programm speichern Links
    #https://doc.qt.io/qt-5/designer-preview.html
    #https://doc.qt.io/qt-5/qtwidgets-tutorials-addressbook-part6-example.html
    #https://www.youtube.com/watch?v=oO5vX353N1A
    #https://www.qtcentre.org/threads/64488-Saving-content-of-a-QLineEdit INI FORMAT
    #https://doc.qt.io/qt-5/qsettings.html #QSettings
    #https://doc.qt.io/qt-5/qsettings.html#setValue #QSettings
    #https://doc.qt.io/qt-5/qsavefile.html #QSaveFile Class
    #https://forum.qt.io/topic/40425/save-input-text-to-file-through-button-click/4
    #https://stackoverflow.com/questions/49837565/how-to-save-text-in-qlineedits-in-pyqt-even-if-the-widget-gets-closed
    #https://stackoverflow.com/questions/23279125/python-pyqt4-functions-to-save-and-restore-ui-widget-values
#pytoexe