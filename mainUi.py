from PyQt5.QtWidgets import QMainWindow, QApplication
from designs.designMenu import Ui_designMenu
from converterUi import *
from juntarUi import *
import sys

class MenuWindow(QMainWindow, Ui_designMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnJuntarPdf.clicked.connect(self.juntarPdf)
        self.btnImgToPdf.clicked.connect(self.converterPdf)

    ### Abre a janela para juntar arquivos PDF's ###
    def juntarPdf(self):
        self.juntar = JuntarWindow()
        self.juntar.show()

    def converterPdf(self):
        self.converter = ConverterWindow()
        self.converter.show()

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = MenuWindow()
    app.show()
    qt.exec_()
