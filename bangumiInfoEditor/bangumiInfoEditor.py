from .bangumiInfoEditorWindow import BangumiInfoEditorWindow
from PyQt5.QtWidgets import QApplication
import sys

def showWindow(mainwindow = ""):
    bangumiEditorWindow = BangumiInfoEditorWindow(mainwindow)
    bangumiEditorWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    showWindow()
    sys.exit(app.exec_())
