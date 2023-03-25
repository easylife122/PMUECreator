import os


def open_ue_project(uproject_path):
    
    # Opens the Unreal Engine Project with their prefer engine editor, with the specified project file.
    
    os.startfile(f'{uproject_path}')

