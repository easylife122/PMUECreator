import unreal

# Set the desired folder path and sequence name
folder_path = '/Game/MyFolder'
level_name = 'MyLevel'

# Set sequence folder path from .txt file
folder_path_seq = []

# Create an asset_tools from AssetToolsHelper
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Create a new Level Sequence asset in the specified folder
factorySeq = unreal.LevelSequenceFactoryNew()

# Set the path to the text file
file_path = 'D:/Projects/UEProjectTemp/202304_MofaBoca/Saved/shotsPath.txt'

# Create an empty list to store the listSeqseqs
listSeqs = []
shotsArray = []
pathsArray = []

# Open the text file for reading
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        # Convert the line to a list and add it to the list
        listSeq = line.strip()
        listSeqRenameSlash = listSeq.replace('\\', '/')
        listSeqSplit = listSeqRenameSlash.split('/Content')
        listSeqArray = '/Game' + listSeqSplit[1]
        listSeqs.append(listSeqArray)

# Split listSeqs into pathsArray and shotsArray
for text in listSeqs:
    split_line = text.split('+')
    pathsArray.append(split_line[0])
    shotsArray.append(split_line[1])
    sequence = asset_tools.create_asset(split_line[1], split_line[0], unreal.LevelSequence, factorySeq)

# Create a new Level asset in the specified folder
factoryLvl = unreal.WorldFactory()
new_level = asset_tools.create_asset(level_name, folder_path, unreal.World, factoryLvl)

# Save all modified assets
unreal.EditorAssetLibrary.save_loaded_assets()
