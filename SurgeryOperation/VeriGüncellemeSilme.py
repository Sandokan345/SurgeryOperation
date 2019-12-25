from PyQt5 import QtCore, QtGui, QtWidgets
from veri_deposu import *
from VeriEkle import *


class Ui_FormVGS(object):

    def onayButon(self):
        ad = self.lineEdit.text()
        unvan = self.lineEdit_2.text()
        sehir = self.lineEdit_2.text()
        puan = self.lineEdit_2.text()
        fiyat = self.lineEdit_2.text()
        if cmb == "Doktor Silme":
            veri_silme(ad)
        elif cmb == "Unvan değişikliği":
            veri_guncelle1(ad, unvan)
        elif cmb == "Çalışılan şehir değişikliği":
            veri_guncelle2(ad, sehir)
        elif cmb == "Kullanıcı Puanı değişikliği":
            veri_guncelle3(ad, puan)
        elif cmb == "Fiyat değişikliği":
            veri_guncelle4(ad, fiyat)
    def veriEkle(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_FormEkle()
        self.ui.setupUi(self.window)
        self.window.show()

    def combo(self):
        global cmb
        cmb = self.comboBox.currentText()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 30, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(220, 100, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated[str].connect(self.combo)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 170, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(254, 232, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onayButon)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 232, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.veriEkle)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Veri Güncelle"))
        self.label.setText(_translate("Form", "Değişim yapmak istediğiniz doktor adı:"))
        self.comboBox.setItemText(1, _translate("Form", "Doktor Silme"))
        self.comboBox.setItemText(2, _translate("Form", "Unvan değişikliği"))
        self.comboBox.setItemText(3, _translate("Form", "Çalışılan şehir değişikliği"))
        self.comboBox.setItemText(4, _translate("Form", "Kullanıcı Puanı değişikliği"))
        self.comboBox.setItemText(5, _translate("Form", "Fiyat değişikliği"))
        self.label_2.setText(_translate("Form", "Yapılacak İşlem:"))
        self.label_3.setText(_translate("Form", "Yeni durum:"))
        self.pushButton.setText(_translate("Form", "Onay"))
        self.pushButton_2.setText(_translate("Form", "Veri Ekleme"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormVGS()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

