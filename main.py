import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QToolTip, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')


        
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('this is a <b>Qwidget</b> widget')

        btn = QPushButton('Button',self)
        btn.setToolTip('this is a <b>Qwidget</b> widget')
        btn.move(50,50)
        btn.resize(btn.sizeHint())


        self.setWindowTitle('로스트아크 영지제작')
        self.setWindowIcon(QIcon('rimworld.jpg'))
        self.setGeometry(1000, 300, 300, 200)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())