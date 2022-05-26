import sys
from PyQt6.QtWidgets import QFileDialog, QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        files = QFileDialog.getOpenFileNames()
        print(files)

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
