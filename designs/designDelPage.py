# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designDelPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_desingPageDel(object):
    def setupUi(self, desingPageDel):
        desingPageDel.setObjectName("desingPageDel")
        desingPageDel.resize(541, 269)
        desingPageDel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-image: url(:/bgedit/images/textureBg11.png);")
        self.label = QtWidgets.QLabel(desingPageDel)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
"background-color: rgba(71, 238, 0, 0.5);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnArquivo = QtWidgets.QPushButton(desingPageDel)
        self.btnArquivo.setGeometry(QtCore.QRect(400, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnArquivo.setFont(font)
        self.btnArquivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnArquivo.setWhatsThis("")
        self.btnArquivo.setAccessibleDescription("")
        self.btnArquivo.setStyleSheet("background-color: rgba(71, 238, 0, 0.5);\n"
"color: rgb(255, 255, 255);")
        self.btnArquivo.setObjectName("btnArquivo")
        self.btnClear = QtWidgets.QPushButton(desingPageDel)
        self.btnClear.setGeometry(QtCore.QRect(400, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnClear.setFont(font)
        self.btnClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClear.setStyleSheet("background-color: rgba(71, 238, 0, 0.5);\n"
"color: rgb(255, 255, 255);")
        self.btnClear.setObjectName("btnClear")
        self.btnDelPage = QtWidgets.QPushButton(desingPageDel)
        self.btnDelPage.setGeometry(QtCore.QRect(400, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnDelPage.setFont(font)
        self.btnDelPage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDelPage.setStyleSheet("background-color: rgba(71, 238, 0, 0.5);\n"
"color: rgb(255, 255, 255);")
        self.btnDelPage.setObjectName("btnDelPage")
        self.listArquivos = QtWidgets.QListWidget(desingPageDel)
        self.listArquivos.setGeometry(QtCore.QRect(10, 80, 381, 111))
        self.listArquivos.setStyleSheet("background: transparent;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.listArquivos.setObjectName("listArquivos")
        self.label_2 = QtWidgets.QLabel(desingPageDel)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 381, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: transparent;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.inputPageNum = QtWidgets.QLineEdit(desingPageDel)
        self.inputPageNum.setGeometry(QtCore.QRect(400, 120, 131, 31))
        self.inputPageNum.setStyleSheet("color: rgb(255, 255, 255);")
        self.inputPageNum.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPageNum.setObjectName("inputPageNum")

        self.retranslateUi(desingPageDel)
        QtCore.QMetaObject.connectSlotsByName(desingPageDel)

    def retranslateUi(self, desingPageDel):
        _translate = QtCore.QCoreApplication.translate
        desingPageDel.setWindowTitle(_translate("desingPageDel", "PageDelPDF"))
        self.label.setText(_translate("desingPageDel", "<html><head/><body><p><span style=\" color:#ffffff;\">PageDelPDF</span></p></body></html>"))
        self.btnArquivo.setText(_translate("desingPageDel", "Adicionar doc."))
        self.btnClear.setText(_translate("desingPageDel", "Limpar"))
        self.btnDelPage.setText(_translate("desingPageDel", "Deletar página"))
        self.inputPageNum.setPlaceholderText(_translate("desingPageDel", "Numero da página"))
from . import BgEdit
