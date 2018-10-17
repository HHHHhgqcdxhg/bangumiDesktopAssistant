from bangumiInfoEditorWindow import BangumiInfoEditorWindow
from PyQt5.QtWidgets import QApplication
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    bangumiEditorWindow = BangumiInfoEditorWindow()
    bangumiEditorWindow.show()
    sys.exit(app.exec_())
