import sys
#import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == '_main_':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("you are gay")
    w.show()
    sys.exit(app.exec_())
