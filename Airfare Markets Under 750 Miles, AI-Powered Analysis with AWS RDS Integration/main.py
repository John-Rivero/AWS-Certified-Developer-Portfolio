
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
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
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
        self.Title = QtWidgets.QLabel(parent=self.widget)
        self.Title.setMaximumSize(QtCore.QSize(16777215, 50))
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
        self.gridLayout_2.addWidget(self.Title, 0, 0, 1, 3)
        self.label = QtWidgets.QTextEdit(parent=self.widget)
        self.label.setStyleSheet("QTextEdit\n"
"{\n"
"\n"
"border: 1px solid rgb(200,200,200);\n"
"border-radius: 3px;\n"
"background-color: rgb(255, 255, 255)\n"
"\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 5, 2)
        self.LoadData_Button = QtWidgets.QPushButton(parent=self.widget)
        self.LoadData_Button.clicked.connect(lambda: button_functions.Buttons.LoadData_Button_Clicked(self))
        self.LoadData_Button.setMinimumSize(QtCore.QSize(199, 30))
        self.LoadData_Button.setMaximumSize(QtCore.QSize(199, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.LoadData_Button.setFont(font)
        self.LoadData_Button.setStyleSheet("QPushButton {\n"
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
        self.LoadData_Button.setObjectName("LoadData_Button")
        self.gridLayout_2.addWidget(self.LoadData_Button, 6, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 35))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Search_Button = QtWidgets.QPushButton(parent=self.widget_2)
        self.Search_Button.clicked.connect(lambda: button_functions.Buttons.Search_Button_Clicked(self))
        self.Search_Button.setMinimumSize(QtCore.QSize(0, 30))
        self.Search_Button.setMaximumSize(QtCore.QSize(99999, 30))
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
        self.gridLayout_3.addWidget(self.Search_Button, 0, 0, 1, 1)
        self.Clear_Button = QtWidgets.QPushButton(parent=self.widget_2)
        self.Clear_Button.clicked.connect(lambda:button_functions.Buttons.Clear_Button_Clicked(self) )
        self.Clear_Button.setMinimumSize(QtCore.QSize(0, 30))
        self.Clear_Button.setMaximumSize(QtCore.QSize(9999, 30))
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
        self.gridLayout_3.addWidget(self.Clear_Button, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 6, 2, 1, 1)
        self.UserInput_TextEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.UserInput_TextEdit.setMinimumSize(QtCore.QSize(400, 100))
        self.UserInput_TextEdit.setMaximumSize(QtCore.QSize(400, 100))
        self.UserInput_TextEdit.setStyleSheet("QTextEdit\n"
"{\n"
"\n"
"\n"
"border-radius:  3px;\n"
"border: 1px solid rgb(200,200,200);\n"
"}")
        self.UserInput_TextEdit.setObjectName("UserInput_TextEdit")
        self.gridLayout_2.addWidget(self.UserInput_TextEdit, 5, 2, 1, 1)
        self.AI_Result_TextEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.AI_Result_TextEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.AI_Result_TextEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.AI_Result_TextEdit.setStyleSheet("QTextEdit\n"
"{\n"
"\n"
"border: 1px solid rgb(200,200,200);\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.AI_Result_TextEdit.setReadOnly(True)
        self.AI_Result_TextEdit.setObjectName("AI_Result_TextEdit")
        self.gridLayout_2.addWidget(self.AI_Result_TextEdit, 1, 2, 4, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "Airfare Market AI"))
        self.LoadData_Button.setText(_translate("MainWindow", "Load Data"))
        self.Search_Button.setText(_translate("MainWindow", "Search"))
        self.Clear_Button.setText(_translate("MainWindow", "Clear"))
        self.UserInput_TextEdit.setPlaceholderText(_translate("MainWindow", "Message AI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
