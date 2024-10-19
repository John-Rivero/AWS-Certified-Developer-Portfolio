
from PyQt6 import QtCore, QtGui, QtWidgets

import button_functions as button_functions


class MyMainWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        file = 'textfile/count'
        with open(file, 'w') as file2:
            file2.write("0")
            
        event.accept() 


class Ui_MainWindow(object):
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setStyleSheet("QWidget #widget\n"
"{\n"
"border: 1px solid rgb(200,200,200);\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.UserInput_TextEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.UserInput_TextEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.UserInput_TextEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.UserInput_TextEdit.setStyleSheet("QTextEdit\n"
"{\n"
"\n"
"\n"
"border-radius:  3px;\n"
"border: 1px solid rgb(200,200,200);\n"
"}")
        self.UserInput_TextEdit.setObjectName("UserInput_TextEdit")
        self.gridLayout_2.addWidget(self.UserInput_TextEdit, 2, 0, 1, 2)
        self.Title = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setStyleSheet("QLabel\n"
"{\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"background-color:rgb(79, 161, 255);\n"
"border-radius:10px;\n"
"color:#fff\n"
"}")
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title.setObjectName("Title")
        self.gridLayout_2.addWidget(self.Title, 0, 0, 1, 2)
        self.Clear_Button = QtWidgets.QPushButton(parent=self.widget)
        self.Clear_Button.clicked.connect(lambda:button_functions.Buttons.Clear_Button_Clicked(self) )
        self.Clear_Button.setMinimumSize(QtCore.QSize(0, 30))
        self.Clear_Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.Clear_Button.setFont(font)
        self.Clear_Button.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(33, 126, 70);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(58, 202, 111);\n"
"    border: 1px solid #fff;\n"
"}\n"
"")
        self.Clear_Button.setObjectName("Clear_Button")
        self.gridLayout_2.addWidget(self.Clear_Button, 3, 1, 1, 1)
        self.Search_Button = QtWidgets.QPushButton(parent=self.widget)
        self.Search_Button.clicked.connect(lambda: button_functions.Buttons.Search_Button_Clicked(self))
        self.Search_Button.setMinimumSize(QtCore.QSize(0, 30))
        self.Search_Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.Search_Button.setFont(font)
        self.Search_Button.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(33, 126, 70);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(58, 202, 111);\n"
"    border: 1px solid #fff;\n"
"}\n"
"")
        self.Search_Button.setObjectName("Search_Button")
        self.gridLayout_2.addWidget(self.Search_Button, 3, 0, 1, 1)
        self.AI_Result_TextEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.AI_Result_TextEdit.setStyleSheet("QTextEdit\n"
"{\n"
"\n"
"border: 1px solid rgb(200,200,200);\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.AI_Result_TextEdit.setReadOnly(True)
        self.AI_Result_TextEdit.setObjectName("AI_Result_TextEdit")
        self.gridLayout_2.addWidget(self.AI_Result_TextEdit, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UserInput_TextEdit.setPlaceholderText(_translate("MainWindow", "Message AI"))
        self.Title.setText(_translate("MainWindow", "Airfare Market AI"))
        self.Clear_Button.setText(_translate("MainWindow", "Clear"))
        self.Search_Button.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
