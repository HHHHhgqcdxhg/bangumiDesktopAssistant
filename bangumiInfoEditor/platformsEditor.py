from PyQt5.QtWidgets import QFrame,QLabel,QListWidget,QVBoxLayout,QPushButton,QGridLayout,QTextEdit,QComboBox,QFileDialog,QHBoxLayout
from platformselector import PlatformSelector

class PlatformsEditor(QFrame):
    def __init__(self,superEl):
        self.superEl = superEl
        super(PlatformsEditor, self).__init__()
        self.mainLayout = QHBoxLayout()
        self.setFixedHeight(200)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        # self.setStyleSheet("background-color:red")
        self.platformSelector = PlatformSelector(self)

        self.urlInputLabel = QLabel()
        self.urlInputLabel.setText("输入地址 :")

        self.urlEditor = QTextEdit()
        self.urlEditor.setFixedHeight(24)
        self.urlEditor.setFixedWidth(315)

        self.mainLayout.addWidget(self.platformSelector)
        self.mainLayout.addWidget(self.urlInputLabel)
        self.mainLayout.addWidget(self.urlEditor)
        self.setLayout(self.mainLayout)
    def closeEvent(self, *args, **kwargs):
        print(1)
