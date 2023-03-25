import shotgun_api3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox


# Replace the values below with your own API key and script name
SERVER_PATH = 'https://moonshine.shotgunstudio.com/'
SCRIPT_NAME = 'easylife122'
API_KEY = 'iqnor4Bifz-gjswpvpliwjpxt'

# Create a connection to the Shotgrid API
sg = shotgun_api3.Shotgun(SERVER_PATH, script_name=SCRIPT_NAME, api_key=API_KEY)

# Fetch a list of all the shots in the project
projects = sg.find('Project', [], ['name'])

# Create a PyQt application and window
app = QApplication([])
window = QWidget()

# Create a layout for the window
layout = QVBoxLayout()

# Add a label for the combo box
label = QLabel('Select a project:')
layout.addWidget(label)

# Create a combo box and add each project name to it
combo_box = QComboBox()
for project in projects:
    combo_box.addItem(project['name'])
layout.addWidget(combo_box)

# Define a slot function to print the selected project name
def print_selected_project_name(project_name):
    print('Selected project:', project_name)

# Connect the currentTextChanged signal of the combo box to the print_selected_project_name slot function
combo_box.currentTextChanged.connect(print_selected_project_name)

# Show the window and start the PyQt event loop
window.setLayout(layout)
window.show()
app.exec_()
