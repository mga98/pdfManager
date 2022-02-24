from PyQt5.QtWidgets import QMainWindow, QApplication
from designs.designConverter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk
from PIL import Image


class ConverterWindow(QMainWindow, Ui_designConverter):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Lita que armazena diretórios
        self.dirList = []

        # Botões da interface
        self.btnArquivo.clicked.connect(self.openImgs)
        self.btnConverter.clicked.connect(self.convertToPdf)
        self.btnDeletar.clicked.connect(self.deleteSelectedItem)
        self.btnClear.clicked.connect(self.clearList)

    # Abrindo as imagens:
    def openImgs(self):
        Tk().withdraw()
        path = askopenfilename()

        self.listArquivos.addItem(str(path))

        for index in range(self.listArquivos.count()):
            a = self.listArquivos.item(index)

        self.dirList.append(a.text())

        print(self.dirList)

    # Limpando as listas:
    def clearList(self):
        self.dirList.clear()
        self.listArquivos.clear()
        self.label_2.setText('')

    # Deleta o item selecionado na interface das listas:
    def deleteSelectedItem(self):
        try:
            for selectedItem in self.listArquivos.selectedItems():
                numItem = int(self.listArquivos.currentRow())

                self.listArquivos.takeItem(self.listArquivos.row(selectedItem))

                self.dirList.pop(numItem)

        except Exception as e:
            self.label_2.setText('Não foi possível deletar este diretório.')

    # Convertendo as imagens selecionadas em PDF:
    def convertToPdf(self):
        imgList = []

        try:
            for dirs in self.dirList:
                img = Image.open(fr'{dirs}')
                im = img.convert('RGB')
                imgList.append(im)

            save_file_name = asksaveasfilename(defaultextension='.pdf')
            imgList[0].save(save_file_name, save_all=True,
                            append_images=imgList[1:])

            img.close()

            self.label_2.setText('Arquivo PDF criado com sucesso!')

        except Exception as e:
            self.label_2.setText('Erro! Verifique os diretórios das imagens.')
