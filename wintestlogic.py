from PyQt5 import QtGui,QtWidgets,QtCore
# from untitled import Ui_MainWindow
from wintest import Ui_MainWindow
import sys


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Main()
    win.show()

    sys.exit(app.exec_())