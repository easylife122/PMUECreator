import os
import shutil
import datetime
import shotGridInterface
from pathlib import Path
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Get shotGridInterface.py to a query instance
c_query = shotGridInterface.query

class FolderAniCreator():
    def __init__(self):
        super().__init__()

        self.sf_Common_path =''
        self.sf01Env_path = ''
        self.sf02Ch_path = ''
        self.sf03Seq_path = ''
        self.sf04Temp_path = ''
        self.sfPython_path = ''

    def create_folders(self, top_folder_entry, project_id, ue_version_index, content_type):

        # Read the configuration file
        config.read('N:\Softwares&Tools\Sg2Uproject\Config\config.ini')

        # Get the value of the 'parameter' option in the 'Settings' section
        #icon = config.get('Settings', 'icon')

        # [REPLACE] Create folder to destination
        self.target_dir = config.get('Settings', 'target_dir')

        # Get the value of the 'ExampleUE_version' option in the 'Settings' section
        ExampleUE427 = config.get('Settings', 'ExampleUE_4_27_2')
        ExampleUE503 = config.get('Settings', 'ExampleUE_5_0_3')
        ExampleUE511 = config.get('Settings', 'ExampleUE_5_1_1')

        # [REPLACE] A folder directory for copying UE sample project
        UE_source_folder_array = [ExampleUE427.replace('\\','/'), ExampleUE503.replace('\\','/'), ExampleUE511.replace('\\','/')]
        self.UE_source_folder = UE_source_folder_array[ue_version_index]

        # [REPLACE] Define the UE sample project .uproject name
        example_uproject_name_array = ['ExampleUE_4_27_2.uproject','ExampleUE_5_0_3.uproject','ExampleUE_5_1_1.uproject']
        self.example_uproject_name = example_uproject_name_array[ue_version_index]

        # Inside UE project define mother folder
        self.UEContent_folder_name = 'Content'

        folderPathCommon = config.get('Settings', 'folder_path_common')
        folderPathCharacter = config.get('Settings', 'folder_path_character')
        folderPathVPXR = config.get('Settings', 'folder_path_vpxr')
        folderPathEnv = config.get('Settings', 'folder_path_env')
        folderPathEnvVPXR = config.get('Settings', 'folder_path_env_vpxr')
        folderPathAniPyScript = config.get('Settings', 'folder_path_AniPyScript')

        # [REPLACE] Example Folder Common
        self.folder_path_common = folderPathCommon.replace('\\', '/')


        # [REPLACE] Example Folder Character
        self.folder_path_character = folderPathCharacter.replace('\\', '/')

        # [REPLACE] Example Folder VPXR
        self.folder_path_vpxr = folderPathVPXR.replace('\\', '/')

        # [REPLACE] Example Folder Env
        self.folder_path_env = folderPathEnv.replace('\\', '/')

        # [REPLACE] Example Folder Env
        self.folder_path_env_vpxr = folderPathEnvVPXR.replace('\\', '/')

        # [REPLACE] Example Folder Python Script for Animation
        self.folder_path_AniPyScript = folderPathAniPyScript.replace('\\', '/')

        # Get the current date
        today = datetime.date.today()

        # Format the date as YYYY-MM-DD
        month_str = today.strftime('%Y%m')

        # Get the current date and time
        now_str = datetime.datetime.now()
        # print(now_str)

        # Get input values from text fields and remove space and replace to '_'
        top_folder_entry_remove_colon = top_folder_entry.replace(':', "")
        self.top_folder_entry_remove_space = top_folder_entry_remove_colon.replace(" ", "_")
        self.top_folder_name = self.top_folder_entry_remove_space
        self.date_top_folder_name = month_str + '_' + self.top_folder_name
        self.top_folder_name_OnTop = '_' + self.top_folder_name

        # Pass Shots path for Unreal Script use, store into a shotsPath.txt file
        filename_log = month_str + '_Log.txt'
        # Log Path
        log_folder_path = config.get('Settings', 'log_folder')
        log_file_path = log_folder_path.replace('\\','/') + '/' + filename_log
        print(log_file_path)
        user_name = os.environ['USERNAME']

        if os.path.exists(log_file_path):
            with open(log_file_path, 'a') as f:
                # Get shots array and into a txt file
                f.writelines(str(now_str) + ' -> ' + str(self.top_folder_name) + ' - ' + str(user_name) + '\n')
                # f.write('Hello\n')

        if not os.path.exists(log_file_path):
            filepath_log = os.path.join(log_folder_path, filename_log)
            filepath_log_rename = filepath_log.replace('\\', '/')

            with open(filepath_log_rename, 'w') as f:

                # Get shots array and into a txt file
                f.writelines(str(now_str) + ' -> ' + str(self.top_folder_name) + ' - ' + str(user_name) + '\n')


        if content_type == 'Animation':
            # Define 2nd lvl Folder names
            sub_folder__Common = '_Common'
            sub_folder_01Env = '01_Env'
            sub_folder_02Ch = '02_Ch'
            sub_folder_03Seq = '03_Seq'
            sub_folder_04Temp = '04_Temp'
            sub_folder_Python = 'Python'


            # create the target directory if it doesn't already exist
            if not os.path.exists(self.target_dir):
                os.makedirs(self.target_dir)

            # copy the source folder to the target directory
            copied_folder_path = os.path.join(self.target_dir, self.top_folder_name)
            shutil.copytree(self.UE_source_folder, copied_folder_path)

            # rename the copied folder
            new_folder_name = self.date_top_folder_name
            new_folder_path = self.target_dir + '/' + new_folder_name
            shutil.move(copied_folder_path, new_folder_path)

            new_folder_path_content = new_folder_path + '/Content/'

            # rename .uproject
            old_uproject_path_name = new_folder_path +'/' + self.example_uproject_name
            new_uproject_name = self.top_folder_entry_remove_space + '.uproject'
            new_uproject_path_name = new_folder_path + '/' + new_uproject_name
            os.rename(old_uproject_path_name, new_uproject_path_name)
            # print(old_uproject_path_name, new_uproject_path_name)

            # Create level 2 subfolder path
            self.sf_Common_path = Path(os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, self.top_folder_name_OnTop, sub_folder__Common))
            self.sf01Env_path = Path(os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, self.top_folder_name_OnTop, sub_folder_01Env))
            self.sf02Ch_path = Path(os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, self.top_folder_name_OnTop, sub_folder_02Ch))
            self.sf03Seq_path = Path(os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, self.top_folder_name_OnTop, sub_folder_03Seq))
            self.sf04Temp_path = Path(os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, self.top_folder_name_OnTop, sub_folder_04Temp))


            # create level 2 subfolders _Common
            shutil.copytree(self.folder_path_common, self.sf_Common_path)
            common_example_folder = self.sf_Common_path.joinpath('ExampleFoldersCommon')
            if os.path.exists(common_example_folder):
                os.rename(common_example_folder, self.sf_Common_path)

            # create level 2 subfolders
            self.sf01Env_path.mkdir()
            self.sf02Ch_path.mkdir()
            self.sf03Seq_path.mkdir()
            self.sf04Temp_path.mkdir()

            # Find Content Path
            content_folder_path = Path(os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, sub_folder_Python))

            # copy Python folder
            shutil.copytree(self.folder_path_AniPyScript, content_folder_path)
            python_animation_folder = content_folder_path.joinpath('Python')
            if os.path.exists(python_animation_folder):
                os.rename(python_animation_folder, content_folder_path)


            # Create Sequences and Shots subfolders
            sequences = c_query.shotgridSequence(project_id)
            shots = c_query.shotgridShot(project_id)
            shotsPathArray = []
            shotsNameArray = []
            for sequence in sequences:
                if sequence:
                    SeqPath = self.sf03Seq_path.joinpath(sequence['code'])

                    #Make Sequence folders
                    SeqPath.mkdir()

                    #Make Shot folders
                    for shot in shots:
                        if shot['sg_sequence']['name'] == sequence['code']:
                            ShotPath = SeqPath.joinpath(shot['code'])
                            ShotPath.mkdir()

                            # Make shots into a file path array
                            ShotPathPerline = str(ShotPath) + '+' + str(shot['code']) + '\n'
                            shotsPathArray.append(ShotPathPerline)

                            # Make Sequence name into a file
                            shotsNamePerline = str(shot['code']) + '\n'
                            shotsNameArray.append(shotsNamePerline)

            # Pass Shots path for Unreal Script use, store into a shotsPath.txt file
            filename = 'shotsPath.txt'
            filepath = os.path.join(new_folder_path, 'Content/Python', filename)
            with open(filepath, 'w') as f:

                #Get shots array and into a txt file
                f.writelines(shotsPathArray)

            # Create Sets subfolders
            sets = c_query.shotgridAsset(project_id)
            setsPathArray = []

            for set in sets:
                try:
                    if set:
                        # Create all sg_asset_type: Set folders
                        if str(set['sg_asset_type']) == 'Set':
                            SetPath = self.sf01Env_path.joinpath(set['code'])

                            # Create setsPath.txt  set path + set code
                            SetPathPerline = str(SetPath) + '\Maps' + '+' + str(set['code']) + '\n'
                            setsPathArray.append(SetPathPerline)

                            # Copy example env folder and then rename the folder
                            shutil.copytree(self.folder_path_env, SetPath)
                            example_folder = SetPath.joinpath('ExampleFoldersEnv')
                            if os.path.exists(example_folder):
                                os.rename(example_folder, SetPath)


                except Exception as e1:
                    print(f'An error occurred: {e1}')

            # Pass Sets path for Unreal Script use, store into a setsPath.txt file
            filename = 'setsPath.txt'
            filepath = os.path.join(new_folder_path, 'Content/Python', filename)
            with open(filepath, 'w') as f:

                #Get shots array and into a txt file
                f.writelines(setsPathArray)


            # Create characters subfolders
            characters = c_query.shotgridAsset(project_id)
            chPathArray = []

            for character in characters:
                try:
                    if character:
                        # Create all sg_asset_type: Character folders
                        if str(character['sg_asset_type']) == 'Char':
                            ChPath = self.sf02Ch_path.joinpath(character['code'])
                            ChPathPerline = str(ChPath) + '+' + str(character['code']) + ' \n'
                            chPathArray.append(ChPathPerline)

                             # Copy example env folder and then rename the folder
                            shutil.copytree(self.folder_path_character, ChPath)
                            ch_example_folder = ChPath.joinpath('ExampleFoldersCharacter')
                            if os.path.exists(ch_example_folder):
                                os.rename(ch_example_folder, ChPath)

                except Exception as e2:
                    print(f'An error occurred: {e2}')

            # Pass Sets path for Unreal Script use, store into a setsPath.txt file
            filename = 'chsPath.txt'
            filepath = os.path.join(new_folder_path, 'Content/Python', filename)
            with open(filepath, 'w') as f:

                #Get shots array and into a txt file
                f.writelines(chPathArray)

            # Create ReadMe.txt
            readmefile = c_query.shotgridAsset(project_id)
            readmeArray = []

            for readme in readmefile:
                try:
                    if readme:
                        # Create readme data in
                        readmePerline = str(readme['sg_asset_type']) + ': ' + str(readme['code']) + ' -> ' + str(readme['description']) + ' \n'
                        # print(readmePerline)
                        readmeArray.append(readmePerline)

                except Exception as e2:
                    print(f'An error occurred: {e2}')


            # Pass Readme datas for user
            fileReadmeName = 'ReadMe.txt'
            #print(new_folder_path)
            fileReadMePath = os.path.join(new_folder_path, fileReadmeName)
            with open(fileReadMePath, 'w', encoding='utf-8') as f:

                #Get type code description in txt file
                 f.writelines(readmeArray)


            # Opens the Unreal Engine Project with their prefer engine editor, with the specified project file.
            os.startfile(f'{new_uproject_path_name}')




        if content_type == 'VP / XR':

            # Define 2nd lvl Folder names
            sub_folder__Common = '_Common'
            sub_folder_Python = 'Python'
            sub_folder_Movies = 'Movies'

            # create the target directory if it doesn't already exist
            if not os.path.exists(self.target_dir):
                os.makedirs(self.target_dir)

            # copy the source folder to the target directory
            copied_folder_path = os.path.join(self.target_dir, self.top_folder_name)
            shutil.copytree(self.UE_source_folder, copied_folder_path)

            # rename the copied folder
            new_folder_name = self.date_top_folder_name
            new_folder_path = self.target_dir + '/' + new_folder_name
            shutil.move(copied_folder_path, new_folder_path)

            new_folder_path_content = new_folder_path + '/Content/'

            # rename .uproject
            old_uproject_path_name = new_folder_path + '/' + self.example_uproject_name
            new_uproject_name = self.top_folder_entry_remove_space + '.uproject'
            new_uproject_path_name = new_folder_path + '/' + new_uproject_name
            os.rename(old_uproject_path_name, new_uproject_path_name)
            #print(old_uproject_path_name, new_uproject_path_name)

            # Create _Common subfolder path
            self.sf_Common_path = Path(
                os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, self.top_folder_name_OnTop,
                             sub_folder__Common))
            # Create Level2 folder path
            level2_folder_path = Path(
                os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, self.top_folder_name_OnTop))

            # Create Movie fodler path
            movies_folder_path = Path(os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, sub_folder_Movies))
            movies_folder_path.mkdir()
            movies_folder_path_string = f'{movies_folder_path}'
            movies_folder_path_rename = movies_folder_path_string.replace('\\', '/')
            #print(movies_folder_path_rename)

            # Copy _Common subfolder from ExampleFoldersCommon
            shutil.copytree(self.folder_path_common, self.sf_Common_path)
            common_example_folder = self.sf_Common_path.joinpath('ExampleFoldersCommon')
            if os.path.exists(common_example_folder):
                os.rename(common_example_folder, self.sf_Common_path)

            # Create Content Path
            python_folder_path = Path(
                os.path.join(self.target_dir, self.date_top_folder_name, self.UEContent_folder_name, sub_folder_Python))

            # Copy Python folder
            shutil.copytree(self.folder_path_AniPyScript, python_folder_path)
            python_animation_folder = python_folder_path.joinpath('Python')
            if os.path.exists(python_animation_folder):
                os.rename(python_animation_folder, python_folder_path)

            # Create Empty array
            shotsPathArray = []

            # Pass Shots path for Unreal Script use, store into a shotsPath.txt file
            filename = 'shotsPath.txt'
            filepath = os.path.join(new_folder_path, 'Content/Python', filename)
            with open(filepath, 'w') as f:

                # Get shots array and into a txt file
                f.writelines(shotsPathArray)

            # Create Sets subfolders
            sets = c_query.shotgridAsset(project_id)
            setsPathArray = []

            # Create Env subfolders
            for set in sets:
                try:
                    if set:
                        # Create all sg_asset_type: Set folders
                        if str(set['sg_asset_type']) == 'Set':
                            SetPath = level2_folder_path.joinpath(set['code'])

                            # Create setsPath.txt  set path + set code
                            SetPathPerline = str(SetPath) + '\Maps' + '+' + str(set['code']) + '\n'
                            setsPathArray.append(SetPathPerline)

                            # Copy example env folder and then rename the folder
                            shutil.copytree(self.folder_path_env_vpxr, SetPath)
                            example_folder = SetPath.joinpath('ExampleFoldersEnvVPXR')
                            if os.path.exists(example_folder):
                                os.rename(example_folder, SetPath)


                except Exception as e1:
                    print(f'An error occurred: {e1}')

            # Pass Sets path for Unreal Script use, store into a setsPath.txt file
            filename = 'setsPath.txt'
            filepath = os.path.join(new_folder_path, 'Content/Python', filename)
            with open(filepath, 'w') as f:

                # Get shots array and into a txt file
                f.writelines(setsPathArray)

            # Create characters empty array
            chPathArray = []

            # Pass Sets path for Unreal Script use, store into a setsPath.txt file
            filename = 'chsPath.txt'
            filepath = os.path.join(new_folder_path, 'Content/Python', filename)
            with open(filepath, 'w') as f:

                # Get shots array and into a txt file
                f.writelines(chPathArray)

            # Create ReadMe.txt
            readmefile = c_query.shotgridAsset(project_id)
            readmeArray = []

            for readme in readmefile:
                try:
                    if readme:
                        # Create readme data in
                        readmePerline = str(readme['sg_asset_type']) + ': ' + str(readme['code']) + ' -> ' + str(readme['description']) + ' \n'
                        # print(readmePerline)
                        readmeArray.append(readmePerline)

                except Exception as e2:
                    print(f'An error occurred: {e2}')


            # Pass Readme datas for user
            fileReadmeName = 'ReadMe.txt'
            #print(new_folder_path)
            fileReadMePath = os.path.join(new_folder_path, fileReadmeName)
            with open(fileReadMePath, 'w', encoding='utf-8') as f:

                #Get type code description in txt file
                 f.writelines(readmeArray)

            # Opens the Unreal Engine Project with their prefer engine editor, with the specified project file.
            os.startfile(f'{new_uproject_path_name}')

        

if __name__ == '__main__':
    pass
    # create the application and main window
    folder_creator = FolderAniCreator()


