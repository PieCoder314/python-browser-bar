import sys, webbrowser
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("website.ui")[0]


class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.actionExit.triggered.connect(self.menuExit_selected) # This line makes the exit button do something.
        self.SiteGo.clicked.connect(self.SiteGo_clicked) # This line makes the go button do something.
        
    def menuExit_selected(self): # This paragraph makes the exit button close the window.
        self.close()
        
    def SiteGo_clicked(self): # This paragraph makes the Go button save the website input and then goes to the website.
        url = str(self.SiteEnter.text())
        webbrowser.open(str(url))     
        
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
