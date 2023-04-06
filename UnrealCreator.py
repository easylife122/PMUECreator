
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
        listSeqRename = listSeq.replace('\\', '/')
        listSeqs.append(listSeqRename)

for text in listSeqs:
    split_line = text.split('+')
    pathsArray.append(split_line[0])
    shotsArray.append(split_line[1])

# Print the resulting list of listSeqseqs
print(pathsArray)