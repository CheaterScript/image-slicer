# Form implementation generated from reading ui file 'inputDialog.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 208)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_width = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_width.setGeometry(QtCore.QRect(20, 60, 113, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_width.setFont(font)
        self.lineEdit_width.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_width.setObjectName("lineEdit_width")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_height = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_height.setGeometry(QtCore.QRect(150, 60, 113, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_height.setFont(font)
        self.lineEdit_height.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.lineEdit_channels = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_channels.setGeometry(QtCore.QRect(280, 60, 113, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_channels.setFont(font)
        self.lineEdit_channels.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_channels.setObjectName("lineEdit_channels")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(280, 30, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 311, 16))
        self.label_4.setStyleSheet("*{\n"
"color:rgb(255, 0, 0)\n"
"}")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "输入RAW图片信息"))
        self.label.setText(_translate("Dialog", "宽度："))
        self.label_2.setText(_translate("Dialog", "高度："))
        self.lineEdit_channels.setText(_translate("Dialog", "3"))
        self.label_3.setText(_translate("Dialog", "通道数："))
        self.label_4.setText(_translate("Dialog", "*Photoshop Raw格式不包含宽高信息，需要手动输入。"))