from PyQt5.QtWidgets import QLabel,QFrame,QVBoxLayout,QListWidget,QHBoxLayout,QWidget
from .leftcolumn import LeftColumn
from .rightColumn import RightColumn
from PyQt5.QtGui import QIcon
class BangumiInfoEditorWindow(QWidget):
    def __init__(self):
        super(BangumiInfoEditorWindow, self).__init__()
        self.setWindowTitle("追番编辑")
        self.setWindowIcon(QIcon("src/img/icon/icon.ico"))
        self.resize(1600, 800)
        self.mainLayout = QHBoxLayout()
        self.rightColumn = RightColumn(self)
        self.leftColumn = LeftColumn(self)


        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.leftColumn)
        self.mainLayout.addWidget(self.rightColumn)


        self.setLayout(self.mainLayout)


    def closeEvent(self, QCloseEvent):
        # self.appMainWindow().show()
        self.hide()
