from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QDialog


class ShowWindow(QDialog):
    def __init__(self, output: str):
        super().__init__()
        self.setWindowTitle('Connecting to the server')
        self.setFixedSize(250, 150)

        self.output = output

        self.main_layout = QVBoxLayout()
        self.add_widgets()

        self.setLayout(self.main_layout)

    def add_widgets(self):
        self.output_edit = QTextEdit()
        self.output_edit.setStyleSheet('font-size: 18px; height: 25px; color: blue')
        self.output_edit.setText(self.output)
        self.main_layout.addWidget(self.output_edit)
