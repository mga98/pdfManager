from PyQt5.QtWidgets import QMainWindow, QApplication
from designs.designJuntar import *


class JuntarWindow(QMainWindow, Ui_designJuntar):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
