import sys
from PyQt5.QtWidgets import *

class Clicker(QWidget):
    def __init__(self) ->None:
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        ...
        #Тут створити layout Та кнопки


app = QApplication(sys.argv)
window = Clicker()
sys.exit(app.exec_())
