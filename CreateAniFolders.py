import os
import shutil
import datetime
import ShotGridInterface

# Get ShotGridInterface.py to a query instance
c_query = ShotGridInterface.query

class FolderAniCreator():
    def __init__(self):
        super().__init__()

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
        self.sf01Env_path = os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_01Env)
        self.sf02Ch_path = os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_02Ch)
        self.sf03Seq_path = os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_03Seq)
        self.sef04Temp_path = os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_04Temp)

        # create level 2 subfolders
        os.makedirs(self.sf01Env_path)
        os.makedirs(self.sf02Ch_path)
        os.makedirs(self.sf03Seq_path)
        os.makedirs(self.sef04Temp_path)

        # Create Sequences subfolders
        # assets = c_query.shotgridAsset(project_id)
        # print(assets)
        #shots = c_query.shotgridShot(project_id)
        #print(shots)

        # Create Sequences subfolders
        sequences = c_query.shotgridSequence(project_id)
        # print(sequences)
        for sequence in sequences:
            if sequence:
                # os.makedirs(self.sf03Seq_path, sequence['code'])
                print(self.sf03Seq_path)
                print(sequence['code'])


if __name__ == '__main__':
    pass
    # create the application and main window
    folder_creator = FolderAniCreator()


