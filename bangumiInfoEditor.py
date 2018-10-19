import bangumiInfoEditor
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bangumiInfoEditor.showWindow()
    sys.exit(app.exec_())
