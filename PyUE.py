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

# Shots path text file
file_path_shots = '/Game/shotsPath.txt'

# Sets path text file
file_path_sets = '/Game/setsPath.txt'

# Create an empty list to store the listSeqseqs
listSeqs = []
shotsArray = []
pathsArray = []
listSets = []

# Open the text file for reading
with open(file_path_shots, 'r') as file:
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

# Open the text file for Env path and names
with open(file_path_sets, 'r') as fileSets:
    # Read each line from the file
    for lineSet in fileSets:
        # Convert the line to a list and add it to the list
        listSet = lineSet.strip()
        listSetRenameSlash = listSet.replace('\\', '/')
        listSetSplit = listSetRenameSlash.split('/Content')
        listSetArray = '/Game' + listSetSplit[1]
        listSets.append(listSetArray)

# Split listSets into SetsPathArray and SetsNameArray
for textSet in listSets:
    split_setsline = textSet.split('+')
    _level = asset_tools.create_asset('_' + split_setsline[1], split_setsline[0], unreal.World, factoryLvl)
    level_light = asset_tools.create_asset(split_setsline[1] + '_Light', split_setsline[0], unreal.World, factoryLvl)
    level_prop = asset_tools.create_asset(split_setsline[1] + '_Props', split_setsline[0], unreal.World, factoryLvl)


