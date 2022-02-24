# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_designMenu(object):
    def setupUi(self, designMenu):
        designMenu.setObjectName("designMenu")
        designMenu.resize(541, 277)
        designMenu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        designMenu.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(designMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 71))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("background-color: rgba(0, 85, 127, 0.5);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 71, 201, 291))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnJuntarPdf = QtWidgets.QPushButton(self.frame)
        self.btnJuntarPdf.setGeometry(QtCore.QRect(10, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnJuntarPdf.setFont(font)
        self.btnJuntarPdf.setStyleSheet("background-color: rgba(255, 0, 0, 0.7);\n"
"color: rgb(255, 255, 255);")
        self.btnJuntarPdf.setObjectName("btnJuntarPdf")
        self.btnImgToPdf = QtWidgets.QPushButton(self.frame)
        self.btnImgToPdf.setGeometry(QtCore.QRect(10, 80, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnImgToPdf.setFont(font)
        self.btnImgToPdf.setStyleSheet("background-color: rgba(147, 6, 133, 0.7);\n"
"color: rgb(255, 255, 255);")
        self.btnImgToPdf.setObjectName("btnImgToPdf")
        self.btnWordToPdf = QtWidgets.QPushButton(self.frame)
        self.btnWordToPdf.setGeometry(QtCore.QRect(10, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnWordToPdf.setFont(font)
        self.btnWordToPdf.setStyleSheet("background-color: rgba(8, 12, 255, 0.7);\n"
"color: rgb(255, 255, 255);")
        self.btnWordToPdf.setObjectName("btnWordToPdf")
        designMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(designMenu)
        QtCore.QMetaObject.connectSlotsByName(designMenu)

    def retranslateUi(self, designMenu):
        _translate = QtCore.QCoreApplication.translate
        designMenu.setWindowTitle(_translate("designMenu", "PDF Manager"))
        self.label.setText(_translate("designMenu", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">PDF Manager</span></p></body></html>"))
        self.btnJuntarPdf.setText(_translate("designMenu", "JuntarPDF"))
        self.btnImgToPdf.setText(_translate("designMenu", "ImgToPDF"))
        self.btnWordToPdf.setText(_translate("designMenu", "WordToPDF"))
