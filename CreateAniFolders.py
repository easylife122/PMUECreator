import os
import shutil
import datetime
import ShotGridInterface

# Get ShotGridInterface.py to a query instance
c_query = ShotGridInterface.query

class FolderAniCreator():
    def create_folders(self, top_folder_entry):

        target_dir = 'D:/Projects/UEProjectTemp'
        UE_source_folder = "D:/Projects/UnreaProjects/ExampleUE_5_1_1"
        UEContent_folder_name = 'Content'
        example_uproject_name = 'ExampleUE_5_1_1.uproject'

        # Get the current date
        today = datetime.date.today()

        # Format the date as YYYY-MM-DD
        date_str = today.strftime('%Y%m')

        # get input values from text fields
        top_folder_entry_remove_space = top_folder_entry.replace(" ", "_")
        top_folder_name = top_folder_entry_remove_space
        date_top_folder_name = date_str + '_' + top_folder_name

        # 2 lvl Folder names
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

        # create level 2 subfolder inside the top level folder
        os.makedirs(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_01Env))
        os.makedirs(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_02Ch))
        os.makedirs(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_03Seq))
        os.makedirs(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_04Temp))

        # create level 3 subfolder inside 03Seq
        sequences = c_query.shotgridData()


        # rename uproject
        old_uproject_path_name = new_folder_path +'/' + example_uproject_name
        new_uproject_name = top_folder_entry_remove_space + '.uproject'
        new_uproject_path_name = new_folder_path + '/' + new_uproject_name
        os.rename(old_uproject_path_name, new_uproject_path_name)
        print(old_uproject_path_name, new_uproject_path_name)

if __name__ == '__main__':

    # create the application and main window
    app = QApplication(sys.argv)
    folder_creator = FolderAniCreator()
    folder_creator.show()

    # start the event loop
    sys.exit(app.exec_())

