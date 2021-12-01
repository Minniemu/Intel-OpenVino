from PyQt5 import QtWidgets, QtGui, QtCore

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        # self.ui.pushButton.setText('Print message!')
        # self.clicked_counter = 0
        self.ui.pushButton_1.clicked.connect(self.buttonClicked_line)
        self.ui.pushButton_2.clicked.connect(self.buttonClicked_text)
        self.ui.pushButton_3.clicked.connect(self.buttonClicked_plain)
    
    def buttonClicked_line(self):
        msg = self.ui.LineEdit.text()
        self.ui.Output_1.setText(msg)
    
    def buttonClicked_text(self):
        msg = self.ui.textEdit.toPlainText()
        self.ui.Output_2.setText(msg)
    
    def buttonClicked_plain(self):
        msg = self.ui.plainTextEdit.toPlainText()
        self.ui.Output_3.setText(msg)

    
