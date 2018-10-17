from PyQt5.QtWidgets import QFrame,QLabel,QListWidget,QVBoxLayout,QPushButton,QGridLayout,QTextEdit,QComboBox,QFileDialog,QHBoxLayout
from platformselector import PlatformSelector

class PlatformsEditor(QFrame):
    def __init__(self):
        super(PlatformsEditor, self).__init__()
        self.mainLayout = QHBoxLayout()
        self.setFixedHeight(200)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        # self.setStyleSheet("background-color:red")
        self.platformSelector = PlatformSelector()

        self.mainLayout.addWidget(self.platformSelector)
        self.setLayout(self.mainLayout)
