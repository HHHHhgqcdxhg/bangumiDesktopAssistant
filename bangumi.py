import sys
from PyQt5.QtWidgets import QApplication
from mainWindow import MainWindow
from bangumiInfoEditor import BangumiInfoEditorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    bangumiInfoEditorWindow = BangumiInfoEditorWindow()
    mainWindow.show()

    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec_())


