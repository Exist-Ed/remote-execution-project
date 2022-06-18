from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QDialog


class ShowWindow(QDialog):
    def __init__(self, output: str):
        super().__init__()
        self.setWindowTitle('Output')
        self.setFixedSize(700, 600)
        self.move(415, 10)

        self.output = output

        self.main_layout = QVBoxLayout()
        self.add_widgets()

        self.setLayout(self.main_layout)

    def add_widgets(self):
        self.output_edit = QTextEdit()
        self.output_edit.setStyleSheet('font-size: 18px; height: 25px;')
        self.output_edit.setText(self.output)
        self.main_layout.addWidget(self.output_edit)
