import RunUE
import shotgun_api3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from CreateAniFolders import FolderAniCreator

# Replace the values below with your own API key and script name
SERVER_PATH = 'https://moonshine.shotgunstudio.com/'
SCRIPT_NAME = 'easylife122'
API_KEY = ''

# Create a connection to the Shotgrid API
sg = shotgun_api3.Shotgun(SERVER_PATH, script_name=SCRIPT_NAME, api_key=API_KEY)

# Fetch a list of all the shots in the project
projects = sg.find('Project', [], ['name'])

# Print the name of each shot
for project in projects:
    print(project['name'])
'''
class UICreator(QMainWindow):

    def __init__(self):
        super().__init__()

         # set the main window title
        self.setWindowTitle("Folder Creator")

        # create a central widget and set its layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # create labels and entry fields for folder names and directory
        top_folder_label = QLabel("Project Name:", self)
        layout.addWidget(top_folder_label)
        self.top_folder_entry = QLineEdit(self)
        layout.addWidget(self.top_folder_entry)

        top_folder_entry = self.top_folder_entry
        # create a button to run the folder creation function
        create_button = QPushButton("Create Folders", self)
        create_button.clicked.connect(lambda: folderAni.create_folders(top_folder_entry))
        layout.addWidget(create_button)

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
'''
