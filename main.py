import RunUE
import shotgun_api3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox
from CreateAniFolders import FolderAniCreator

# Replace the values below with your own API key and script name
SERVER_PATH = 'https://moonshine.shotgunstudio.com/'
SCRIPT_NAME = 'easylife122'
API_KEY = ''

# Create a connection to the Shotgrid API
sg = shotgun_api3.Shotgun(SERVER_PATH, script_name=SCRIPT_NAME, api_key=API_KEY)

# Fetch a list of all the shots in the project
projects = sg.find('Project', [], ['name'])

class UICreator(QMainWindow):

    def __init__(self):
        super().__init__()

        # Variable Initialization
        self.project_name = ""

         # Set the main window title
        self.setWindowTitle("Folder Creator")

        # Create a central widget and set its layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Add a label for the combo box
        top_folder_label = QLabel('Select a project:')
        layout.addWidget(top_folder_label)

        # Create a combo box and add each project name to it
        self.combo_box = QComboBox()
        for project in projects:
            self.combo_box.addItem(project['name'])
        layout.addWidget(self.combo_box)

        # Connect the currentTextChanged signal of the combo box to the print_selected_project_name slot function
        self.combo_box.currentTextChanged.connect(self.get_selected_project_name)

        # Create a button to run the folder creation function
        create_button = QPushButton("Create Folders", self)
        create_button.clicked.connect(self.clicked_create_folder)
        layout.addWidget(create_button)

    # Define a slot function to print the selected project name
    def get_selected_project_name(self):
        self.project_name = self.combo_box.currentText()

    # A function to call create folder
    def clicked_create_folder(self):
        self.project_name = self.combo_box.currentText()
        folderAni.create_folders(self.project_name)

# Call CreateAniFolders
folderAni = FolderAniCreator()

# create the application and main window
app = QApplication(sys.argv)
ui_create = UICreator()
ui_create.show()

# start the event loop
sys.exit(app.exec_())

path = 'D:/Projects/UEProjectTemp/202303_GGGG/ExampleUE_5_1_1.uproject'
# RunUE.open_ue_project(path)

