import unreal

# Set the desired folder path and sequence name
folder_path = '/Game/MyFolder'
sequence_name = 'MySequence'
level_name = 'MyLevel'

# Set sequence folder path from .txt file
folder_path_seq = []

# Set the path to the text file
file_path = 'D:/Projects/UEProjectTemp/202304_MofaBoca/Saved/shotsPath.txt'
fileName_path = 'D:/Projects/UEProjectTemp/202304_MofaBoca/Saved/shotsName.txt'

# Create an empty list to store the listSeqs
listSeqs = []

# Open the text file for reading
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        # Convert the line to a list and add it to the list
        listSeq = line.strip()
        listSeqs.append(listSeq)

# Create an empty list to store shot names
shotNames = []

# Open the listSeqs.txt to get shots path
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        # Convert the line to a list and add it to the list
        listSeq = line.strip()
        listSeqs.append(listSeq)

# Open the shotsNames.txt to get shot names
with open(fileName_path, 'r') as fileNames:
    for lineName in fileNames:
        shotName = lineName.strip()
        shotNames.append(shotName)

# Create an asset_tools from AssetToolsHelper
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Create a new Level Sequence asset in the specified folder
factorySeq = unreal.LevelSequenceFactoryNew()
# sequence = asset_tools.create_asset(sequence_name, folder_path, unreal.LevelSequence, factorySeq)
for listSeq in listSeqs:
    for shotName in shotNames:
        sequence = asset_tools.create_asset(shotName, listSeq, unreal.LevelSequence, factorySeq)


# Create a new Level asset in the specified folder
factoryLvl = unreal.WorldFactory()
new_level = asset_tools.create_asset(level_name, folder_path, unreal.World, factoryLvl)

# Save all modified assets
unreal.EditorAssetLibrary.save_loaded_assets()
