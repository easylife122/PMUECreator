import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox
from PyQt5.QtGui import QIcon, QFont
from createFolders import FolderAniCreator
import shotGridInterface
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Get shotGridInterface.py to a query instance
m_query = shotGridInterface.query

class UICreator(QMainWindow):

    def __init__(self):
        super().__init__()

        # Variable Initialization
        self.project_name = ''
        self.project_id = ''
        self.ue_version_index = 0
        self.content_type = 'Animation'

        # Read the configuration file
        config.read('N:\\Softwares&Tools\\uProjectStarter\\Config\\config.ini')

        # Get the value of the 'parameter' option in the 'Settings' section
        icon = config.get('Settings', 'icon')

        # Set the main window title
        self.setWindowTitle('uProjectStarter 0.1.0')

        # Set the window icon
        self.setWindowIcon(QIcon(icon))

        # Set a fixed size for the window
        self.setFixedSize(400, 200)

        # Apply a dark theme using a style sheet
        self.setStyleSheet("""
                    QWidget {
                        background-color: #2D2D30;
                        color: #F7F7F7;
                    }
                    QPushButton {
                        background-color: #3C3C40;
                        border: 1px solid #5A5A5C;
                        padding: 5px 10px;
                    }
                    QPushButton:hover {
                        background-color: #47474C;
                    }
                    QPushButton:pressed {
                        background-color: #323234;
                    }
                """)

        # Create a central widget and set its layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Add a label for the combo box
        top_folder_label = QLabel('Select a project:')

        layout.addWidget(top_folder_label)

        # Call shotGridInterface.py to get projects
        self.projects = m_query.shotgridProject()

        # Create a combo box and add each project name to it
        self.combo_box = QComboBox()
        for project in self.projects:
            self.combo_box.addItem(project['name'])

        layout.addWidget(self.combo_box)

        # Connect the currentTextChanged signal of the combo box to the print_selected_project_name slot function
        self.combo_box.currentTextChanged.connect(self.get_selected_project_name)






        #########################################################################
        # Add a label for the engine version combo box
        engine_version_label = QLabel('Select Unreal Engine version:')
        layout.addWidget(engine_version_label)

        # Create an engine version combo box and add items to it
        self.engine_version_combo_box = QComboBox()
        self.engine_version_combo_box.addItems(['UE 4.27', 'UE 5.0', 'UE 5.1'])
        layout.addWidget(self.engine_version_combo_box)


        #########################################################################
        # Add a label for the choose menu combo box
        choose_menu_label = QLabel('Select content type:')
        layout.addWidget(choose_menu_label)

        # Create a choose menu combo box and add items to it
        self.choose_menu_combo_box = QComboBox()
        self.choose_menu_combo_box.addItems(['Animation', 'VP / XR'])
        layout.addWidget(self.choose_menu_combo_box)

        # Retrieve engine version Index Number from UI
        self.engine_version_combo_box.currentIndexChanged.connect(self.engine_version_changed)
        # Retrieve menu Text from UI
        self.choose_menu_combo_box.currentTextChanged.connect(self.menu_changed)

        #########################################################################
        # Create a button to run the folder creation function
        create_button = QPushButton('Create Folders', self)
        create_button.clicked.connect(self.clicked_create_folder)
        layout.addWidget(create_button)

        # print(self.ue_version_index, self.content_type)

    # Select Engine Version
    def engine_version_changed(self, index):
        # This function will be called whenever the user selects a different engine version
        # The text parameter contains the text of the currently selected item
        self.ue_version_index = index
        # print(f'Engine version: {index}')

    # Select content type
    def menu_changed(self, text):
        # This function will be called whenever the user selects a different menu
        # The text parameter contains the text of the currently selected item
        self.content_type = text
        # print(f'Content Type: {text}')


    # Define a slot function to print the selected project name
    def get_selected_project_name(self):
        self.project_name = self.combo_box.currentText()

    # A function to call create folder
    def clicked_create_folder(self):
        # store the current combo_box text to project_name
        self.project_name = self.combo_box.currentText()

        # find match project name to get id
        for project in self.projects:
            if project['name'] == self.project_name:
                self.project_id = project['id']
                # print(self.project_id)


        # Run create animation folder module
        folderAni.create_folders(self.project_name, self.project_id, self.ue_version_index, self.content_type)






# Call CreateAniFolders
folderAni = FolderAniCreator()

# create the application and main window
app = QApplication(sys.argv)
ui_create = UICreator()
ui_create.show()

# start the event loop
sys.exit(app.exec_())



