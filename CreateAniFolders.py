import os
import shutil
import datetime
import ShotGridInterface
from pathlib import Path

# Get ShotGridInterface.py to a query instance
c_query = ShotGridInterface.query

class FolderAniCreator():
    def __init__(self):
        super().__init__()

        self.sf_Common_path =''
        self.sf01Env_path = ''
        self.sf02Ch_path = ''
        self.sf03Seq_path = ''
        self.sef04Temp_path = ''

    def create_folders(self, top_folder_entry, project_id):

        # Create folder to destination
        target_dir = 'D:/Projects/UEProjectTemp'

        # A folder directory for copying UE sample project
        UE_source_folder = "D:/Projects/UnreaProjects/ExampleUE_5_1_1"

        # Define the UE sample project .uproject name
        example_uproject_name = 'ExampleUE_5_1_1.uproject'

        # Inside UE project define mother folder
        UEContent_folder_name = 'Content'

        # Example Folder Common
        folder_path_common = 'D:/Projects/UnreaProjects/ExampleFoldersCommon'

        # Example Folder Character
        folder_path_character = 'D:/Projects/UnreaProjects/ExampleFoldersCharacter'

        # Example Folder VPXR
        folder_path_vpxr = 'D:/Projects/UnreaProjects/ExampleFoldersVPXR'

        # Example Folder Env
        folder_path_env = 'D:/Projects/UnreaProjects/ExampleFoldersEnv'

        # Get the current date
        today = datetime.date.today()

        # Format the date as YYYY-MM-DD
        date_str = today.strftime('%Y%m')

        # Get input values from text fields and remove space and replace to '_'
        top_folder_entry_remove_colon = top_folder_entry.replace(':', "")
        top_folder_entry_remove_space = top_folder_entry_remove_colon.replace(" ", "_")
        top_folder_name = top_folder_entry_remove_space
        date_top_folder_name = date_str + '_' + top_folder_name

        # Define 2nd lvl Folder names
        sub_folder__Common = '_Common'
        sub_folder_01Env = '01_Env'
        sub_folder_02Ch = '02_Ch'
        sub_folder_03Seq = '03_Seq'
        sub_folder_04Temp = '04_Temp'



        # create the target directory if it doesn't already exist
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # copy the source folder to the target directory
        copied_folder_path = os.path.join(target_dir, top_folder_name)
        shutil.copytree(UE_source_folder, copied_folder_path)

        # rename the copied folder
        new_folder_name = date_top_folder_name
        new_folder_path = target_dir + '/' + new_folder_name
        shutil.move(copied_folder_path, new_folder_path)

        # rename .uproject
        old_uproject_path_name = new_folder_path +'/' + example_uproject_name
        new_uproject_name = top_folder_entry_remove_space + '.uproject'
        new_uproject_path_name = new_folder_path + '/' + new_uproject_name
        os.rename(old_uproject_path_name, new_uproject_path_name)
        print(old_uproject_path_name, new_uproject_path_name)

        # Create level 2 subfolder path
        self.sf_Common_path = Path(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder__Common))
        self.sf01Env_path = Path(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_01Env))
        self.sf02Ch_path = Path(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_02Ch))
        self.sf03Seq_path = Path(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_03Seq))
        self.sef04Temp_path = Path(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_04Temp))

        # create level 2 subfolders _Common
        shutil.copytree(folder_path_common, self.sf_Common_path)
        common_example_folder = self.sf_Common_path.joinpath('ExampleFoldersCommon')
        if os.path.exists(common_example_folder):
            os.rename(common_example_folder, self.sf_Common_path)

        # create level 2 subfolders
        self.sf01Env_path.mkdir()
        self.sf02Ch_path.mkdir()
        self.sf03Seq_path.mkdir()
        self.sef04Temp_path.mkdir()

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
        filepath = os.path.join(new_folder_path, 'Content', filename)
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
                        shutil.copytree(folder_path_env, SetPath)
                        example_folder = SetPath.joinpath('ExampleFoldersEnv')
                        if os.path.exists(example_folder):
                            os.rename(example_folder, SetPath)


            except Exception as e1:
                print(f'An error occurred: {e1}')

        # Pass Sets path for Unreal Script use, store into a setsPath.txt file
        filename = 'setsPath.txt'
        filepath = os.path.join(new_folder_path, 'Content', filename)
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
                        shutil.copytree(folder_path_character, ChPath)
                        ch_example_folder = ChPath.joinpath('ExampleFoldersCharacter')
                        if os.path.exists(ch_example_folder):
                            os.rename(ch_example_folder, ChPath)

            except Exception as e2:
                print(f'An error occurred: {e2}')

        # Pass Sets path for Unreal Script use, store into a setsPath.txt file
        filename = 'chsPath.txt'
        filepath = os.path.join(new_folder_path, 'Content', filename)
        with open(filepath, 'w') as f:

            #Get shots array and into a txt file
            f.writelines(chPathArray)

if __name__ == '__main__':
    pass
    # create the application and main window
    folder_creator = FolderAniCreator()


