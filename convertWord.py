from PyQt5.QtWidgets import QMainWindow, QApplication
from tkinter.filedialog import askopenfilename, asksaveasfilename
from designs.designWord import *
from tkinter import Tk
import PyPDF2
import docx


class WordWindow(QMainWindow, Ui_designWord):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnConverter.clicked.connect(self.convertToWord)
        self.btnArquivo.clicked.connect(self.openFile)

        self.dir = ''

    def openFile(self):
        Tk().withdraw()
        path = askopenfilename()
        
        self.dir = path
        self.listArquivos.addItem(str(path))

    def convertToPdf(self):
        pdfFileObj = open(self.dir, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        doc = docx.Document()

        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            doc.add_paragraph(pageObj.extractText())

        saveDir = asksaveasfilename(defaultextension='.docx')
        doc.save(saveDir)


