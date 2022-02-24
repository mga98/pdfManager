from PyQt5.QtWidgets import QMainWindow, QApplication
from designs.designConverter import *


class ConverterWindow(QMainWindow, Ui_designConverter):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
