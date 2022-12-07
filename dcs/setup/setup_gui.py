import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget,  QFormLayout, QGridLayout, QTabWidget, QLineEdit, QDateEdit, QPushButton, QLabel
from PyQt6.QtCore import Qt, pyqtSlot

class MainWindow(QWidget):
    btn_save = None
    tab = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Configure Distributed Cloud Storage')

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        self.tab = QTabWidget(self)

        # setup airtable
        at_setup = self.atable_setup()

        # setup dropbox
        db_setup = self.dbox_setup()

        # add setup widets to the tab widget
        self.tab.addTab(at_setup, 'Airtable*')
        self.tab.addTab(db_setup, 'Dropbox*')
        
        main_layout.addWidget(self.tab, 0, 0, 2, 1)

        self.btn_save = QPushButton('Save ' + self.get_tab_name())
        self.btn_save.setEnabled(False)
        self.tab.currentChanged.connect(self.change)
        self.btn_save.clicked.connect(self.on_save_click)

        main_layout.addWidget(self.btn_save, 2, 0,
                              alignment=Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(QPushButton('Cancel'), 2, 0,
                              alignment=Qt.AlignmentFlag.AlignRight)

        self.show()
    
    def get_tab_name(self):
        index = self.tab.currentIndex()
        if index==0:
            return "Airtable key"
        elif index == 1:
            return "Dropbox key"
        elif index == 2:
            return "Google Drive key"

    def change(self, val):
        self.btn_save.setText("Save " + self.get_tab_name())
        print(val)

    @pyqtSlot()
    def on_save_click(self):
        print("Save currently not support")
        #Uncomment to support saving env vars
        # index = self.tab.currentIndex()
        # if index==0 and not os.environ.get('AIRTABLE_API_KEY', False) and self.airtable_api_key:
        #     print("here")
        #     res = subprocess.run("")
        #     os.environ["AIRTABLE_API_KEY"] = self.airtable_api_key.text()
        # elif index == 1:
        #     os.environ["AIRTABLE_API_KEY"]
        # elif index == 2:
        #     os.environ["DROPBOX_API_KEY"]
        # print(os.environ.get('AIRTABLE_API_KEY', False))

    def atable_setup(self):
        airtable_setup = QWidget(self)
        layout = QFormLayout()
        airtable_setup.setLayout(layout)
        self.airtable_info = QLabel("Configure Airtable for centralized hashed shared keys.")
        
        # TODO: move api key get to init file
        airtable_key = os.environ.get('AIRTABLE_API_KEY', 'No Airtable API key found.')
        self.airtable_api_key = QLineEdit(airtable_key)
        self.airtable_api_key.setEnabled(False)
        self.airtable_api_key.setMinimumWidth(300)
        at_help_link = QLabel('''Don't have a key? <a href='https://support.airtable.com/docs/how-do-i-get-my-api-key'>Get Help.</a>''')
        at_help_link.setStyleSheet("font-size: 13px;"
                                "color: #aba8b3;"
                                "margin-top:20px;")
        at_success = QLabel()
        at_success.setText('<font color="#29d91c">●</font><font color="#82817f"> You are all set configuring Airtable!</font>')
        at_success.setStyleSheet("margin-top:20px;")
        at_help_link.setOpenExternalLinks(True)
        layout.addRow(self.airtable_info)
        layout.addRow('API Key:', self.airtable_api_key)
        if airtable_key != 'No Airtable API key found.':
            layout.addRow(at_success)
        else:
            layout.addRow(at_help_link)
        
        return airtable_setup

    def dbox_setup(self):
        dropbox_setup = QWidget(self)
        layout = QFormLayout()
        dropbox_setup.setLayout(layout)
        
        # TODO: move api key get to init file
        dropbox_key = os.environ.get('DROPBOX_API_KEY', 'No Dropbox API key found.')
        self.dropbox_info = QLabel("Configure Airtable for centralized hashed shared keys.")
        self.dropbox_api_key = QLineEdit(dropbox_key)
        self.dropbox_api_key.setEnabled(False)
        self.dropbox_api_key.setMinimumWidth(300)
        db_help_link = QLabel('''Don't have a key? <a href='https://www.dropbox.com/developers/apps/create'>Get Help.</a>''')
        db_help_link.setStyleSheet("font-size: 13px;"
                                "color: #aba8b3;"
                                "margin-top:20px;")
        db_help_link.setOpenExternalLinks(True)
        db_success = QLabel()
        db_success.setText('<font color="#29d91c">●</font><font color="#82817f"> You are all set configuring Dropbox!</font>')
        db_success.setStyleSheet("margin-top:20px;")
        layout.addRow(self.dropbox_info)
        layout.addRow('API Key:', self.dropbox_api_key)
        if dropbox_key != 'No Dropbox API key found.':
            layout.addRow(db_success)
        else:
            layout.addRow(db_help_link)

        return dropbox_setup




app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())