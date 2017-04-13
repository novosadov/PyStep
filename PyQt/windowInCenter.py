#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):               
        self.resize(250, 150)
        self.center()#Код, который будет центрировать окно,
                     #размещён в специальном методе center()
        self.setWindowTitle('Center')    
        self.show()
        
    def center(self):
        qr = self.frameGeometry()# Мы получаем прямоугольник,
                                 # точно определяющий форму главного окна.
                                 
        cp = QDesktopWidget().availableGeometry().center()
        ''' Мы выясняем разрешение экрана нашего монитора.
        Из этого разрешения, мы получаем центральную точку.'''
                             
        qr.moveCenter(cp)
        ''' Наш прямоугольник уже имеет высоту и ширину.
        Теперь мы устанавливаем центр прямоугольника в центр экрана.
        Размер прямоугольника не изменяется.'''

        
        self.move(qr.topLeft())
        '''Мы перемещаем верхнюю левую точку окна приложения
           в верхнюю левую точку прямоугольника qr,
           таким образом центрируя окно на нашем экране.'''
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
