from PyQt5.QtWidgets import QSystemTrayIcon,QMenu,QAction,QStyle
from PyQt5.QtGui import QIcon
from bangumiInfoEditor import showWindow
import sys
from config import PATH
class BangumiSystemTray(QSystemTrayIcon):
    def __init__(self,superEl):
        self.superEl = superEl

        super(BangumiSystemTray, self).__init__(superEl)
        self.setIcon(QIcon(f"{PATH}/src/img/icon/icon.ico"))
        show_action = QAction("追番编辑", self)
        quit_action = QAction("退出", self)
        show_action.triggered.connect(showWindow)
        quit_action.triggered.connect(self.sysExit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.setContextMenu(tray_menu)
        self.show()

    def sysExit(self):
        self.superEl.app.quit()
        sys.exit(0)
