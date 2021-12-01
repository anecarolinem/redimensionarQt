import sys
from Newredimensiona.desinge import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap  #manipula imagem

class RedimImagem(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self) #herança de desinge
        self.btnEscolherarquivo.clicked.connect(self.open_img)
        self.btnredimensionar.clicked.connect(self.redimensionar)
        self.btnsalvar.clicked.connect(self.salvar)

    def open_img(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            r'C:\Users\aneca\Pictures',
            #options=QFileDialog.DontUseNativeDialog
        )

        self.inputAbrirarquivo.setText(imagem) #abrir imagem no input
        self.origin_img = QPixmap(imagem) #criar imagem original
        self.labelimg.setPixmap(self.origin_img)
        self.inputlargura.setText(str(self.origin_img.width()))
        self.inputaltura.setText(str(self.origin_img.height()))

    def redimensionar(self):
        largura = int(self.inputlargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelimg.setPixmap(self.nova_imagem)
        self.inputlargura.setText(str(self.nova_imagem.width()))
        self.inputaltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem',
             r'C:\Users\aneca\Pictures',
            #options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    redimensiona = RedimImagem()
    redimensiona.show() #mostrar class
    qt.exec_()
