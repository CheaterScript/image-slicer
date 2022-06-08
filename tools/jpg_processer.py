import cv2
from tools.processer import Processer
from pathlib import Path
import math
from PyQt6 import QtWidgets
import numpy as np


class JPG(Processer):
    def load(self) -> None:
        self.img = cv2.imdecode(np.fromfile(
            self.input, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        self.inputPath = Path(self.input)

    def slice(self) -> None:
        self.load()
        total = self.rows * self.cols
        shape = self.img.shape
        singleWidth = math.ceil(shape[1] / self.cols)
        singleHeight = math.ceil(shape[0] / self.rows)

        if singleWidth * self.cols != shape[0] or singleHeight * self.rows != shape[1]:
            self.img = cv2.resize(
                self.img, (singleWidth * self.cols, singleHeight * self.rows))

        for i in range(self.rows):
            for j in range(self.cols):
                percent = int((i*self.rows+j + 1) / total * 100)
                self.update.emit(percent)

                x = j * singleWidth
                y = i * singleHeight

                new_img = self.img[y:y+singleHeight, x: x+singleWidth]

                self.save(new_img, i*self.rows+j)
                print("正在处理%d/%d张……" % (i*self.rows+j, total))

    def save(self, img, index) -> None:
        cv2.imencode(self.inputPath.suffix, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])[
            1].tofile("%s/%s_%03d%s" %
                      (self.output, self.inputPath.stem, index, self.inputPath.suffix))
