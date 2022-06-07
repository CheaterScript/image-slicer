# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 377)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 621, 113))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OutputPathGroup = QtWidgets.QHBoxLayout()
        self.OutputPathGroup.setSpacing(6)
        self.OutputPathGroup.setObjectName("OutputPathGroup")
        self.label_input = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.OutputPathGroup.addWidget(self.label_input)
        self.lineEdit_input = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_input.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.OutputPathGroup.addWidget(self.lineEdit_input)
        self.pushButton_input = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_input.setEnabled(True)
        self.pushButton_input.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_input.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_input.setFont(font)
        self.pushButton_input.setAutoDefault(False)
        self.pushButton_input.setObjectName("pushButton_input")
        self.OutputPathGroup.addWidget(self.pushButton_input)
        self.verticalLayout.addLayout(self.OutputPathGroup)
        self.InputPathGroup = QtWidgets.QHBoxLayout()
        self.InputPathGroup.setSpacing(6)
        self.InputPathGroup.setObjectName("InputPathGroup")
        self.label_output = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.InputPathGroup.addWidget(self.label_output)
        self.lineEdit_output = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_output.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_output.setFont(font)
        self.lineEdit_output.setCursorPosition(9)
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.InputPathGroup.addWidget(self.lineEdit_output)
        self.pushButton_output = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_output.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_output.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_output.setFont(font)
        self.pushButton_output.setObjectName("pushButton_output")
        self.InputPathGroup.addWidget(self.pushButton_output)
        self.verticalLayout.addLayout(self.InputPathGroup)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(80, 280, 500, 40))
        self.pushButton_start.setMinimumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 150, 621, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 141, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_row = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_row.setFont(font)
        self.label_row.setObjectName("label_row")
        self.horizontalLayout.addWidget(self.label_row)
        self.lineEdit_row = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_row.setFont(font)
        self.lineEdit_row.setObjectName("lineEdit_row")
        self.horizontalLayout.addWidget(self.lineEdit_row)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(200, 30, 141, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_col = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_col.setFont(font)
        self.label_col.setObjectName("label_col")
        self.horizontalLayout_3.addWidget(self.label_col)
        self.lineEdit_col = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_col.setFont(font)
        self.lineEdit_col.setObjectName("lineEdit_col")
        self.horizontalLayout_3.addWidget(self.lineEdit_col)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(170, 40, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(80, 280, 501, 31))
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "大图片切割工具"))
        self.groupBox.setTitle(_translate("MainWindow", "文件配置"))
        self.label_input.setText(_translate("MainWindow", "输入文件："))
        self.lineEdit_input.setText(_translate("MainWindow", "asdasdasd"))
        self.pushButton_input.setText(_translate("MainWindow", "浏览"))
        self.label_output.setText(_translate("MainWindow", "输出目录："))
        self.lineEdit_output.setText(_translate("MainWindow", "asdasdasd"))
        self.pushButton_output.setText(_translate("MainWindow", "浏览"))
        self.pushButton_start.setText(_translate("MainWindow", "开始处理"))
        self.groupBox_2.setTitle(_translate("MainWindow", "参数配置"))
        self.label_row.setText(_translate("MainWindow", "行数:"))
        self.label_col.setText(_translate("MainWindow", "列数:"))
        self.label_6.setText(_translate("MainWindow", "×"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())