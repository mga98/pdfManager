from PyQt5.QtWidgets import QMainWindow, QApplication
from tkinter.filedialog import askopenfilename, asksaveasfilename
from designs.designDelPage import *
from tkinter import Tk
import PyPDF2


class delPageWindow(QMainWindow, Ui_desingPageDel):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        ### Lista de diretórios ###
        self.dir = ''

    ### Botões da interface ###

    ### Abrir o arquivo PDF ###
    def openFile(self):
        Tk().withdraw()
        path = askopenfilename()
        self.dir = str(path)

    ### Limpar o diretório da lista de PDF's ###
    def clearList(self):
        self.dir.clear()
    
    ### Editar o arquivo PDF selecionado ###
    def editPdf(self):
        pdfFileObj = open(self.dir)
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            # Continua a partir daqui...

