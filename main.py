import sys

from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow

import config


def main():
    app = QApplication(sys.argv)

    app.setApplicationName(config.APP_NAME)
    app.setApplicationVersion(config.VERSION)
    app.setOrganizationName(config.ORGANIZATION)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()