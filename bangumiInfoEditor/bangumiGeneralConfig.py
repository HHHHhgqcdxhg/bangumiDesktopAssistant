from PyQt5.QtWidgets import QFrame,QLabel,QListWidget,QVBoxLayout,QPushButton,QGridLayout,QTextEdit,QComboBox,QFileDialog
from platformsEditor import PlatformsEditor
class BangumiGeneralConfig(QFrame):
    def __init__(self,data):
        super(BangumiGeneralConfig, self).__init__()
        self.mainLayout = QGridLayout()

        self.setFixedWidth(700)
        self.setFixedHeight(800)

        # self.setStyleSheet("background-color:blue;")
        self.initUI()

    def initUI(self):
        self.mainTitleLabel = QLabel()
        self.mainTitleLabel.setText("标题 :")
        self.mainTitleEditor = QTextEdit()
        self.mainTitleEditor.setFixedHeight(24)
        self.mainTitleTip = QLabel()
        self.mainTitleTip.setText("")

        self.mainLayout.addWidget(self.mainTitleLabel,0,0,1,1)
        self.mainLayout.addWidget(self.mainTitleEditor,0,1,1,5)
        self.mainLayout.addWidget(self.mainTitleTip,0,6,1,2)

        self.startDateLabel = QLabel()
        self.startDateLabel.setText("第一次更新的日期 :")
        self.startDateEditor = QTextEdit()
        self.startDateEditor.setFixedHeight(24)
        self.startDateTip = QLabel()
        self.startDateTip.setText("形如2018-06-21\n(用短横线分割)")

        self.mainLayout.addWidget(self.startDateLabel, 1, 0, 1, 1)
        self.mainLayout.addWidget(self.startDateEditor, 1, 1, 1, 5)
        self.mainLayout.addWidget(self.startDateTip, 1, 6, 1, 2)

        self.finalDateLabel = QLabel()
        self.finalDateLabel.setText("最后一次更新的日期 :")
        self.finalDateEditor = QTextEdit()
        self.finalDateEditor.setFixedHeight(24)
        self.finalDateTip = QLabel()
        self.finalDateTip.setText("形如2018-06-21\n(用短横线分割)")

        self.mainLayout.addWidget(self.finalDateLabel, 2, 0, 1, 1)
        self.mainLayout.addWidget(self.finalDateEditor, 2, 1, 1, 5)
        self.mainLayout.addWidget(self.finalDateTip, 2, 6, 1, 2)

        self.dayTimeLabel = QLabel()
        self.dayTimeLabel.setText("更新时间 :")
        self.dayTimeEditor = QTextEdit()
        self.dayTimeEditor.setFixedHeight(24)
        self.dayTimeTip = QLabel()
        self.dayTimeTip.setText("形如08:30\n(用英文冒号分割)")

        self.mainLayout.addWidget(self.dayTimeLabel, 3, 0, 1, 1)
        self.mainLayout.addWidget(self.dayTimeEditor, 3, 1, 1, 5)
        self.mainLayout.addWidget(self.dayTimeTip, 3, 6, 1, 2)

        self.firstUpdateChapterLabel = QLabel()
        self.firstUpdateChapterLabel.setText("第一次更新时的集数 :")
        self.firstUpdateChapterEditor = QTextEdit()
        self.firstUpdateChapterEditor.setFixedHeight(24)
        self.firstUpdateChapterTip = QLabel()
        self.firstUpdateChapterTip.setText("第一次更新时更新第几集")

        self.mainLayout.addWidget(self.firstUpdateChapterLabel, 4, 0, 1, 1)
        self.mainLayout.addWidget(self.firstUpdateChapterEditor, 4, 1, 1, 5)
        self.mainLayout.addWidget(self.firstUpdateChapterTip, 4, 6, 1, 2)

        self.updateTypeLabel = QLabel()
        self.updateTypeLabel.setText("更新类型 :")
        self.updateTypeComboBox = QComboBox()
        self.updateTypeComboBox.addItem("周更")
        self.updateTypeComboBox.addItem("月更")

        self.mainLayout.addWidget(self.updateTypeLabel, 5, 0, 1, 1)
        self.mainLayout.addWidget(self.updateTypeComboBox, 5, 1, 1, 1)

        self.updateDayLabel = QLabel()
        self.updateDayLabel.setText("更新日 :")
        self.updateDayEditor = QTextEdit()
        self.updateDayEditor.setFixedHeight(24)
        self.updateDayTip = QLabel()
        self.updateDayTip.setText("如果为周更,则填周几更新(填文字,如周五)\n如果为月更,则填几号更新(填数字,如14)")

        self.mainLayout.addWidget(self.updateDayLabel, 6, 0, 1, 1)
        self.mainLayout.addWidget(self.updateDayEditor, 6, 1, 1, 1)
        self.mainLayout.addWidget(self.updateDayTip, 6, 2, 1, 2)

        self.followLabel = QLabel()
        self.followLabel.setText("追番 :")
        self.followComboBox = QComboBox()
        self.followComboBox.addItem("是")
        self.followComboBox.addItem("否")

        self.mainLayout.addWidget(self.followLabel, 7, 0, 1, 1)
        self.mainLayout.addWidget(self.followComboBox, 7, 1, 1, 1)

        self.headImageLabel = QLabel()
        self.headImageLabel.setText("番剧头图 :")
        self.headImageSelectButton = QPushButton()
        self.headImageSelectButton.setText("选择文件")
        self.headImagePathDisableLabel = QLabel()
        self.headImagePathDisableLabel.setText("尽量选择64x64像素的jpg或png文件")

        self.mainLayout.addWidget(self.headImageLabel, 8, 0, 1, 1)
        self.mainLayout.addWidget(self.headImageSelectButton, 8, 1, 1, 1)
        self.mainLayout.addWidget(self.headImagePathDisableLabel, 8, 2, 1, 5)

        self.headImageLabel = QLabel()
        self.headImageLabel.setText("看番地址 :")
        self.headImageSelectButton.clicked.connect(self.selectHeadImgFile)

        self.platformsEditor = PlatformsEditor()
        self.mainLayout.addWidget(self.headImageLabel, 9, 0, 1, 1)
        self.mainLayout.addWidget(self.platformsEditor, 9, 1, 1, 6)
        # dir_path = QFileDialog.getExistingDirectory(self, "choose directory", "C:\\")
        self.setLayout(self.mainLayout)




    def selectHeadImgFile(self):
        imgPath = QFileDialog.getOpenFileName(self,"选择图片","", "Image Files (*.jpg;*.png;*.jpeg)")[0]
        self.headImagePathDisableLabel.setText(imgPath)
