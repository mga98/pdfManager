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
        self.btnArquivo.clicked.connect(self.openFile)
        self.btnClear.clicked.connect(self.clearList)
        self.btnDelPage.clicked.connect(self.delPage)

    ### Abrir o arquivo PDF ###
    def openFile(self):
        Tk().withdraw()
        path = askopenfilename()

        self.dir = path
        self.listArquivos.takeItem(0)
        self.listArquivos.addItem(path)

    ### Limpar o diretório da lista de PDF's ###
    def clearList(self):
        self.dir = ''
        self.listArquivos.clear()
        self.inputPageNum.setText('')
        self.label_2.setText('')

    ### Editar o arquivo PDF selecionado ###
    def delPage(self):
        try:
            pdfFileObj = open(fr'{self.dir}', 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pdfWriter = PyPDF2.PdfFileWriter()

            pageToDelete = int(self.inputPageNum.text())

            for pageNum in range(pdfReader.numPages):
                if pageNum != pageToDelete - 1:
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                
            save = asksaveasfilename(defaultextension='.pdf')
            pdfOutput = open(save, 'wb')
            pdfWriter.write(pdfOutput)
            pdfOutput.close()

            self.label_2.setText('Página deletada com súcesso!')

        except Exception as e:
            self.label_2.setText('Erro! Verifique os diretórios dos PDFs.')
            