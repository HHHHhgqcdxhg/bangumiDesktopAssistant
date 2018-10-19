import sys
from PyQt5.QtWidgets import QApplication
from mainWindow import MainWindow
from bangumiInfoEditor import BangumiInfoEditorWindow

def bangumi():
    app = QApplication(sys.argv)
    mainWindow = MainWindow(app)
    bangumiInfoEditorWindow = BangumiInfoEditorWindow()
    mainWindow.show()

    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec_())

if __name__ == '__main__':
    bangumi()


