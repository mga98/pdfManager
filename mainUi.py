from PyQt5.QtWidgets import QMainWindow, QApplication
from convertWord import WordWindow
from designs.designMenu import Ui_designMenu
from converterUi import *
from juntarUi import *
import sys


class MenuWindow(QMainWindow, Ui_designMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        ### Botões da interface ###
        self.btnJuntarPdf.clicked.connect(self.juntarPdf)
        self.btnImgToPdf.clicked.connect(self.converterPdf)
        self.btnWordToPdf.clicked.connect(self.pdfToWord)

    ### Abre a janela para juntar arquivos PDF's ###
    def juntarPdf(self):
        self.juntar = JuntarWindow()
        self.juntar.show()

    ### Abre a janela para transformar imagens em PDF ###
    def converterPdf(self):
        self.converter = ConverterWindow()
        self.converter.show()

    ### Abre a janela para transformar PDF's em arquivos .docx ###
    def pdfToWord(self):
        self.word = WordWindow()
        self.word.show()


### Inicializador do sistema ###
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = MenuWindow()
    app.show()
    qt.exec_()
