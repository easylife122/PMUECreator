
# Set the path to the text file
file_path = 'D:/Projects/UEProjectTemp/202304_MofaBoca/Saved/shotsPath.txt'

# Create an empty list to store the listSeqseqs
listSeqs = []

# Open the text file for reading
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        # Convert the line to a list and add it to the list
        listSeq = line.strip()
        listSeqs.append(listSeq)

# Print the resulting list of listSeqseqs
print(listSeqs)