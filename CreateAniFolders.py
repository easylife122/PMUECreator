import os
import shutil
import datetime


class FolderAniCreator():
    def create_folders(self, top_folder_entry):

        target_dir = 'D:/Projects/UEProjectTemp'
        UE_source_folder = "D:/Projects/UnreaProjects/ExampleUE_5_1_1"
        UEContent_folder_name = 'Content'

        # Get the current date
        today = datetime.date.today()

        # Format the date as YYYY-MM-DD
        date_str = today.strftime('%Y%m')

        # get input values from text fields
        top_folder_name = top_folder_entry.text()
        date_top_folder_name = date_str + '_' + top_folder_name
        sub_folder_01Env = '01_Env'
        sub_folder_02Ch = '02_Ch'
        sub_folder_03Seq = '03_Seq'
        sub_folder_04Temp = '04_Temp'
        sub_folder_set1 = 'Set1'

        # create the target directory if it doesn't already exist
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # copy the source folder to the target directory
        copied_folder_path = os.path.join(target_dir, top_folder_name)
        shutil.copytree(UE_source_folder, copied_folder_path)

        # rename the copied folder
        new_folder_name = date_top_folder_name
        new_folder_path = os.path.join(target_dir, new_folder_name)
        shutil.move(copied_folder_path, new_folder_path)

        # create the subfolders inside the top level folder
        os.makedirs(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_01Env))
        os.makedirs(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_02Ch))
        os.makedirs(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_03Seq))
        os.makedirs(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_04Temp))
        os.makedirs(os.path.join(target_dir, date_top_folder_name, UEContent_folder_name, sub_folder_01Env, sub_folder_set1))

if __name__ == '__main__':

    # create the application and main window
    app = QApplication(sys.argv)
    folder_creator = FolderAniCreator()
    folder_creator.show()

    # start the event loop
    sys.exit(app.exec_())

