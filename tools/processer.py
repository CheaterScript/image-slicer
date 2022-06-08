import abc
from PyQt6.QtCore import pyqtSignal,QThread

class Processer(QThread):
    update = pyqtSignal(int)

    def __init__(self, input, output, rows, cols) -> None:
        super(Processer, self).__init__()
        self.input = input
        self.output = output
        self.rows = rows
        self.cols = cols

    @abc.abstractmethod
    def load(self) -> None:
        pass

    @abc.abstractmethod
    def slice() -> None:
        pass

    @abc.abstractmethod
    def save() -> None:
        pass
