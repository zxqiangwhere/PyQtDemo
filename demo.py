from PyQt5 import QtGui,QtWidgets,QtCore
# from untitled import Ui_MainWindow
from untitled2 import Ui_MainWindow
import wintestlogic
import sys


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.addwin)


    def addwin(self):
        self.addwin = wintestlogic.Main()
        self.ui.mdiArea.addSubWindow(self.addwin)
        self.addwin.show()
        print('show Sub Window')


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Main()
    win.show()

    sys.exit(app.exec_())