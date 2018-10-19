from PyQt5.QtWidgets import QFrame,QLabel,QListWidget,QVBoxLayout,QPushButton,QGridLayout,QTextEdit,QComboBox,QFileDialog,QHBoxLayout,QCheckBox
from .platformselector import PlatformSelector

class PlatformsEditor(QFrame):
    def __init__(self,superEl):
        self.superEl = superEl
        super(PlatformsEditor, self).__init__()
        self.mainLayout = QGridLayout()
        self.setFixedHeight(200)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        # self.setStyleSheet("background-color:red")
        self.platformSelector = PlatformSelector(self)

        self.urlInputLabel = QLabel()
        self.urlInputLabel.setText("输入地址 :")

        self.urlEditor = QTextEdit()
        self.urlEditor.setFixedHeight(24)
        self.urlEditor.setFixedWidth(320)


        self.checkBox = QCheckBox()
        self.checkBoxLabel = QLabel()
        self.checkBoxLabel.setText("设为默认:")

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(self.urlInputLabel)
        self.rightLayout.addWidget(self.urlEditor)
        self.rightLayout.addWidget(self.checkBox)


        self.rightLayout.addWidget(self.checkBoxLabel)
        # self.rightFrame.setLayout(self.rightLayout)

        self.mainLayout.addWidget(self.platformSelector,0,0,5,2)
        self.mainLayout.addWidget(self.urlInputLabel,1,3,1,5)
        self.mainLayout.addWidget(self.urlEditor,2,3,1,5)
        self.mainLayout.addWidget(self.checkBoxLabel,3,3,1,5)
        self.mainLayout.addWidget(self.checkBox,3,4,1,1)
        self.setLayout(self.mainLayout)




