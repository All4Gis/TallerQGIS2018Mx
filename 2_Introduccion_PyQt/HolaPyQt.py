# -*- coding: utf-8 -*-

# Ejemplos para el curso de PYQGIS
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Ejemplo basico con PyQt
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------

from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os.path as osp

#Icono
path = r'g_icon.jpg'  

 
class HolaMundo(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.ln_text = QLineEdit(self)
        self.bt = QPushButton('Quiero saludarte..',self)
        layout.addWidget(self.ln_text)
        layout.addWidget(self.bt)
        self.setLayout(layout)
        self.setWindowTitle('Ejemplo')
        self.setWindowIcon(QtGui.QIcon(path))   
        
        #Señal boton
        self.bt.clicked.connect(self.show_msg)
        
    #Funcion mostrar mensaje
    def show_msg(self):
        #Sender
        sender = self.sender()
        #Texto
        txt = self.ln_text.text()
        saludo = 'Hola %s el mensaje lo envio %s'%(txt,sender.text())
        QMessageBox.information(self,'Saludo',saludo)

    #Evento close
    def closeEvent(self, event):
        reply = QMessageBox.critical(self, 'Oooohh!!',
            u'Seguro que quieres hacer eso ? Un gatito puede morir ', QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
#Run
dialog = HolaMundo()
dialog.show()