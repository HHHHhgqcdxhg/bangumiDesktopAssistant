from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

class AddScheduleButton(QPushButton):
    def __init__(self,superEl):
        super(AddScheduleButton, self).__init__()
        self.setFixedWidth(200)
        self.setText("添加任务")
        self.superEl = superEl

    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            self.superEl.scheduleList.addItem("666")

