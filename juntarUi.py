from PyQt5.QtWidgets import QMainWindow, QApplication
from tkinter.filedialog import askopenfilename, asksaveasfilename
from designs.designJuntar import *
from tkinter import Tk
import PyPDF2


class JuntarWindow(QMainWindow, Ui_designJuntar):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Lista que armazena diretórios
        self.directoryList = []

        # Botões da interface
        self.btnArquivo.clicked.connect(self.listMaker)
        self.btnJuntar.clicked.connect(self.addToWriter)
        self.btnDel.clicked.connect(self.deleteSelectedItem)
        self.btnClear.clicked.connect(self.clearList)

    # Adicionando os diretórios dos PDF's a lista:
    def listMaker(self):
        Tk().withdraw()
        path = askopenfilename()

        self.listDir.addItem(str(path))

        for index in range(self.listDir.count()):
            a = self.listDir.item(index)

        self.directoryList.append(a.text())

        print(self.directoryList)

    # Limpa as listas de diretórios:
    def clearList(self):
        self.directoryList.clear()
        self.listDir.clear()

    # Deletando um diretório selecionado da lsita:
    def deleteSelectedItem(self):
        try:
            for selectedItem in self.listDir.selectedItems():
                numItem = int(self.listDir.currentRow())

                self.listDir.takeItem(self.listDir.row(selectedItem))
                self.directoryList.pop(numItem)

        except Exception as e:
            self.label_2.setText('Impossível deletar este arquivo.')

    # Juntando os PDF's e criando um novo arquivo PDF:
    def addToWriter(self):
        try:
            pdfWriter = PyPDF2.PdfFileWriter()

            for dir in self.directoryList:
                pdfFileObj = open(dir, 'rb')
                pdfReader = PyPDF2.PdfFileReader(
                    pdfFileObj)

                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)

            save = asksaveasfilename(defaultextension='.pdf')
            pdfOutput = open(save, 'wb')
            pdfWriter.write(pdfOutput)
            pdfOutput.close()

            self.label_2.setText('Arquivo PDF criado com sucesso!')

        except Exception as e:
            self.label_2.setText('Erro! Verifique os diretórios dos PDFs.')
