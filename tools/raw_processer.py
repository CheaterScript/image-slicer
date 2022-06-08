import cv2
from tools.processer import Processer
from pathlib import Path
import math
from PyQt6 import QtWidgets
import numpy as np


class Raw(Processer):
    def __init__(self, input, output, rows, cols, shape) -> None:
        super().__init__(input, output, rows, cols)
        self.shape = shape

    def load(self) -> None:
        self.img = np.fromfile(self.input, dtype=np.uint8)
        self.inputPath = Path(self.input)

    def slice(self) -> None:
        self.load()
        try:
            self.img = self.img.reshape(self.shape)
        except ValueError as e:
            return "宽高或通道数与Raw文件大小不匹配！"
        total = self.rows * self.cols
        shape = self.img.shape
        singleWidth = math.ceil(shape[0] / self.cols)
        singleHeight = math.ceil(shape[1] / self.rows)

        if singleWidth * self.cols != shape[0] or singleHeight * self.rows != shape[1]:
            self.img = cv2.resize(
                self.img, (singleHeight * self.rows, singleWidth * self.cols))

        for i in range(self.rows):
            for j in range(self.cols):
                percent = int((i*self.rows+j + 1) / total * 100)
                self.update.emit(percent)

                x = j * singleWidth
                y = i * singleHeight

                new_img = cv2.cvtColor(
                    self.img[y:y+singleHeight, x: x+singleWidth], cv2.COLOR_BGR2RGB)

                self.save(new_img, i*self.rows+j)
                print("正在处理%d/%d张……" % (i*self.rows+j, total))

        return False
    def save(self, img, index) -> None:
        cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])[
            1].tofile("%s/%s_%03d%s" %
                      (self.output, self.inputPath.stem, index, '.jpg'))
