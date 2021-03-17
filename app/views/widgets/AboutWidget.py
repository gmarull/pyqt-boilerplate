from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import qVersion

from app.Constants import APP_VERSION

from app.ui.AboutWidget_ui import Ui_AboutWidget


class AboutWidget(QWidget):
    """About Widget."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutWidget()
        self.ui.setupUi(self)

        self.ui.version.setText(APP_VERSION)
        self.ui.qtVersion.setText(qVersion())

        self.ui.builtWithQtBtn.clicked.connect(qApp.aboutQt)
