from PyQt6.QtWidgets import QLineEdit, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QDialog, QMessageBox

IP = str()
PORT = int()

PREV_CONNECTION_FILEPATH = 'prev_connection.txt'


class ConnectionWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Connecting to the server')
        self.setFixedSize(250, 150)

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(10)

        self.add_widgets()

        self.setLayout(self.main_layout)

    def add_widgets(self):

        ip_layout = QHBoxLayout()

        ip_label = QLabel()
        ip_label.setText('IP:')
        ip_label.setStyleSheet('font-size: 20px; height: 25px')
        ip_layout.addWidget(ip_label)

        self.ip_line = QLineEdit()
        self.ip_line.setStyleSheet('font-size: 18px; height: 25px;')
        self.ip_line.setFixedWidth(160)
        ip_layout.addWidget(self.ip_line)

        self.main_layout.addLayout(ip_layout)

        port_layout = QHBoxLayout()

        port_label = QLabel()
        port_label.setText('Port:')
        port_label.setStyleSheet('font-size: 20px; height: 25px')
        port_layout.addWidget(port_label)

        self.port_line = QLineEdit()
        self.port_line.setStyleSheet('font-size: 18px; height: 25px;')
        self.port_line.setFixedWidth(160)
        port_layout.addWidget(self.port_line)

        self.main_layout.addLayout(port_layout)

        run_button = QPushButton('Connect')
        run_button.setStyleSheet('font-size: 16px; height: 25px; background-color: green')
        run_button.clicked.connect(self.connect_action)
        self.main_layout.addWidget(run_button)

        try:
            with open(PREV_CONNECTION_FILEPATH, 'r') as prev_connection:
                IP, PORT = prev_connection.readlines()
                self.ip_line.setText(IP)
                self.port_line.setText(PORT)
        except Exception as e:
            print(f'previous connection file error!\n{e.args}')

    def connect_action(self):
        global IP, PORT

        IP = self.ip_line.text()
        try:
            PORT = int(self.port_line.text())
        except ValueError:
            QMessageBox(QMessageBox.Icon.Warning, 'Error!', 'Port must be a natural number!').exec()
            return

        with open(PREV_CONNECTION_FILEPATH, 'w') as prev_connection:
            prev_connection.write(IP + '\n' + str(PORT))

        self.close()
