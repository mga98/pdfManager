# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designWord.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_designWord(object):
    def setupUi(self, designWord):
        designWord.setObjectName("designWord")
        designWord.resize(541, 228)
        designWord.setStyleSheet("background-image: url(:/bgword/images/texturaBg.jpg);")
        self.label = QtWidgets.QLabel(designWord)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 71))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
"background-color: rgba(8, 12, 255, 0.5);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnArquivo = QtWidgets.QPushButton(designWord)
        self.btnArquivo.setGeometry(QtCore.QRect(400, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnArquivo.setFont(font)
        self.btnArquivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnArquivo.setWhatsThis("")
        self.btnArquivo.setAccessibleDescription("")
        self.btnArquivo.setStyleSheet("background-color: rgba(8, 12, 255, 0.5);\n"
"color: rgb(255, 255, 255);")
        self.btnArquivo.setObjectName("btnArquivo")
        self.btnClear = QtWidgets.QPushButton(designWord)
        self.btnClear.setGeometry(QtCore.QRect(400, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnClear.setFont(font)
        self.btnClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClear.setStyleSheet("background-color: rgba(8, 12, 255, 0.5);\n"
"color: rgb(255, 255, 255);")
        self.btnClear.setObjectName("btnClear")
        self.btnConverter = QtWidgets.QPushButton(designWord)
        self.btnConverter.setGeometry(QtCore.QRect(400, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnConverter.setFont(font)
        self.btnConverter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConverter.setStyleSheet("background-color: rgba(8, 12, 255, 0.5);\n"
"color: rgb(255, 255, 255);")
        self.btnConverter.setObjectName("btnConverter")
        self.listArquivos = QtWidgets.QListWidget(designWord)
        self.listArquivos.setGeometry(QtCore.QRect(10, 80, 381, 71))
        self.listArquivos.setStyleSheet("background: transparent;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.listArquivos.setObjectName("listArquivos")
        self.label_2 = QtWidgets.QLabel(designWord)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 381, 31))
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

        self.retranslateUi(designWord)
        QtCore.QMetaObject.connectSlotsByName(designWord)

    def retranslateUi(self, designWord):
        _translate = QtCore.QCoreApplication.translate
        designWord.setWindowTitle(_translate("designWord", "WordToPDF"))
        self.label.setText(_translate("designWord", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">WordToPDF</span></p></body></html>"))
        self.btnArquivo.setText(_translate("designWord", "Adicionar doc."))
        self.btnClear.setText(_translate("designWord", "Limpar"))
        self.btnConverter.setText(_translate("designWord", "Converter"))

from . import BgWord