import sys

from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QGridLayout, \
    QFileDialog, QAbstractItemView, QLabel, QTextEdit, QVBoxLayout, QListWidgetItem

import connection_window
import network_logic
import output_show_window

FILEPATHS = []


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Remote execution project')
        self.setFixedSize(550, 600)

        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(10)

        # adding widgets in main layout:
        self.adding_orchestration_script_widgets()
        self.adding_configuration_widgets()

        self.setLayout(self.main_layout)

        con_window = connection_window.ConnectionWindow()
        con_window.exec()

    def adding_orchestration_script_widgets(self):
        layout = QVBoxLayout()

        label = QLabel()
        label.setText('Control script:')
        label.setStyleSheet('font-size: 20px; height: 25px')
        layout.addWidget(label)

        self.orchestration_script_edit = QTextEdit()
        self.orchestration_script_edit.setStyleSheet('font-size: 18px; height: 25px; color: blue')
        self.orchestration_script_edit.setFixedWidth(350)
        self.orchestration_script_edit.setText('#!bin/bash\n')
        layout.addWidget(self.orchestration_script_edit)

        run_button = QPushButton('Run')
        run_button.setStyleSheet('font-size: 16px; height: 25px; background-color: green')
        run_button.clicked.connect(self.run_button_clicked_action)
        layout.addWidget(run_button)

        self.main_layout.addLayout(layout, 0, 0)

    def adding_configuration_widgets(self):
        layout = QVBoxLayout()

        add_files_button = QPushButton('Add files')
        add_files_button.setStyleSheet('font-size: 16px; height: 25px')
        add_files_button.clicked.connect(self.add_files_button_clicked_action)
        layout.addWidget(add_files_button)

        delete_files_button = QPushButton('Delete file')
        delete_files_button.setStyleSheet('font-size: 16px; height: 25px')
        delete_files_button.clicked.connect(self.delete_files_button_clicked_action)
        layout.addWidget(delete_files_button)

        label = QLabel()
        label.setText('    Uploaded files:')
        label.setStyleSheet('font-size: 20px; height: 25px')
        layout.addWidget(label)

        self.files_table = QListWidget()
        self.files_table.setStyleSheet('font-size: 15px;')
        self.files_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        layout.addWidget(self.files_table)

        change_server_button = QPushButton('Change the server')
        change_server_button.setStyleSheet('font-size: 16px; height: 25px')
        change_server_button.clicked.connect(self.change_server_button_clicked_action)
        layout.addWidget(change_server_button)

        clear_button = QPushButton('Clear')
        clear_button.setStyleSheet('font-size: 16px; height: 25px; background-color: red')
        clear_button.clicked.connect(self.clear_button_clicked_action)
        layout.addWidget(clear_button)

        self.main_layout.addLayout(layout, 0, 1)

    def add_files_button_clicked_action(self):
        filepaths = QFileDialog.getOpenFileNames()[0]
        FILEPATHS.extend(filepaths)

        for path in filepaths:
            item = QListWidgetItem(path.split('/')[-1])
            self.files_table.addItem(item)

    def change_server_button_clicked_action(self):
        con_window = connection_window.ConnectionWindow()
        con_window.exec()

    def clear_button_clicked_action(self):
        self.files_table.clear()
        FILEPATHS.clear()

        self.orchestration_script_edit.clear()
        self.orchestration_script_edit.setText('#!bin/bash\n')

    def delete_files_button_clicked_action(self):
        selected_items = self.files_table.selectedItems()
        for item in selected_items:
            self.files_table.takeItem(self.files_table.row(item))

        for item in selected_items:
            for i in FILEPATHS:
                if i.endswith(item.text()):
                    FILEPATHS.remove(i)
                    break

    def run_button_clicked_action(self):
        IP = connection_window.IP
        Port = connection_window.PORT

        response = network_logic.main(IP, Port, FILEPATHS, self.orchestration_script_edit.toPlainText())
        output_show_window.ShowWindow(response).exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
