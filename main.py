import cv2
import os
import numpy as np
import os
import stat
import time
from pathlib import Path

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QGuiApplication
from tools.tiff_processer import TIFF
from ui.Ui_MainWindow import Ui_MainWindow

from tools.raw_processer import Raw
from tools.png_processer import PNG
from tools.jpg_processer import JPG

# 支持的格式, 不在其中的会跳过处理
FILE_TYPES = ('.jpg', '.jpge', '.png', '.raw', '.tif', '.tiff')


class ToolWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ToolWindow, self).__init__(parent)

    def openFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开文件", os.getcwd(
        ), "All Images(*.jpg;*jpge;*.png;*.raw;*.tiff;*.tif);;PNG(*.png);;Photoshop RAW(*.raw);;JEPE(*.jpg;*jpge);;TIFF(*.tif;*.tiff)")

        self.lineEdit_input.setText(fileName)

    def ouputDir(self):
        dirPath = QtWidgets.QFileDialog.getExistingDirectory(
            self, "选择输出路径", os.getcwd())
        self.lineEdit_output.setText(dirPath)

    def center(self):
        screen = QGuiApplication.screenAt(QtCore.QPoint(
            self.frameGeometry().x(), self.frameGeometry().y()))
        qr = self.frameGeometry()
        cp = screen.availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self, MainWindow):
        self.setupUi(MainWindow)
        self.pushButton_start = self.pushButton_3
        self.center()

        # 打开文件
        self.pushButton_input.clicked.connect(self.openFile)
        # self.pushButton_input.clicked.connect(self.test)
        # 输出目录
        self.pushButton_output.clicked.connect(self.ouputDir)
        # 开始处理
        self.pushButton_start.clicked.connect(self.start)

    def setIsEnabled(self, isEnabled):
        self.lineEdit_input.setEnabled(isEnabled)
        self.lineEdit_output.setEnabled(isEnabled)
        self.pushButton_input.setEnabled(isEnabled)
        self.pushButton_output.setEnabled(isEnabled)
        self.lineEdit_row.setEnabled(isEnabled)
        self.lineEdit_col.setEnabled(isEnabled)
        self.pushButton_start.setEnabled(isEnabled)
        # 等分

    def start(self):
        if(self.checkInput() == False):
            return

        # 禁用所有控件
        self.setIsEnabled(False)
        # 隐藏开始按钮
        self.pushButton_start.setVisible(False)
        # 显示进度条
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)

        self.handle()

    def complete(self):
        self.pushButton_start.setVisible(True)
        self.progressBar.setVisible(False)
        self.setIsEnabled(True)

    def test(self):
        QtWidgets.QMessageBox.warning(
            self, "提示", "输入文件不存在或类型错误！")

    def checkInput(self):
        inputPath = Path(self.lineEdit_input.text())
        outputPath = Path(self.lineEdit_output.text())

        if not inputPath.is_file() or inputPath.suffix not in FILE_TYPES:
            QtWidgets.QMessageBox.warning(
                self, "提示", "输入文件不存在或类型错误！")
            return False
        if not outputPath.is_dir():
            QtWidgets.QMessageBox.warning(
                self, "提示", "输出目录不存在！")
            return False
        # print(os.access(outputPath, os.X_OK | os.R_OK | os.X_OK | os.F_OK))
        # print(os.access(outputPath, os.R_OK))
        if not os.access(self.lineEdit_output.text(), os.W_OK):
            print(os.access(outputPath, os.X_OK))
            QtWidgets.QMessageBox.warning(
                self, "提示", "输出目录没有写入权限，请重新选择！")
            return False

        # os.chmod(outputPath, stat.S_IWRITE)
        try:
            f = open(self.lineEdit_output.text() + '/test.txt', 'w')
            f.close()
            os.remove(self.lineEdit_output.text() + '/test.txt')
        except PermissionError:
            QtWidgets.QMessageBox.warning(
                self, "提示", "输出目录没有写入权限，请重新选择！")
            return False

        try:
            row = int(self.lineEdit_row.text())
        except ValueError as e:
            QtWidgets.QMessageBox.warning(
                self, "提示", "行数不是一个整数！")
            return False

        try:
            col = int(self.lineEdit_col.text())
        except ValueError as e:
            QtWidgets.QMessageBox.warning(
                self, "提示", "列数不是一个整数！")
            return False

        return True

    def showProgress(self, value):
        self.progressBar.setValue(value)

    def handle(self):
        inputPath = self.lineEdit_input.text()
        outputPath = self.lineEdit_output.text()
        row = int(self.lineEdit_row.text())
        col = int(self.lineEdit_col.text())

        _, extension_name = os.path.splitext(inputPath)
        extension_name = extension_name.lower()
        if extension_name not in FILE_TYPES:
            raise Exception("文件打开失败")
        if extension_name == '.raw':
            processer = Raw(inputPath, outputPath, row, col)
        if extension_name == '.png':
            processer = PNG(inputPath, outputPath, row, col)
        if extension_name == '.jpg' or extension_name == '.jpge':
            processer = JPG(inputPath, outputPath, row, col)
        if extension_name == '.tif' or extension_name == '.tiff':
            processer = TIFF(inputPath, outputPath, row, col)

        if not processer:
            self.complete()
            return

        processer.update.connect(self.showProgress)

        time.sleep(0.5)

        processer.slice()

        time.sleep(0.5)

        QtWidgets.QMessageBox.information(
            self, "处理完成提示", "恭喜，处理完成！")

        self.complete()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ToolWindow()
    ui.initUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
