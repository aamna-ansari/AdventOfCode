from pathlib import Path

# File input path
fn = "D:/AdventOFCode/Day_09/input.txt"
data = open(fn).read().strip()

# Parse the data and generate the initial layout
s = data.split("\n")[0]
layout = []
files_info = {}
file_id = 0

# Build the layout and file metadata
for i, ch in enumerate(s):
    length = int(ch)
    if i % 2 == 0:  # Add file blocks
        layout.extend([str(file_id)] * length)
        files_info[file_id] = [len(layout) - length, length]
        file_id += 1
    else:  # Add empty blocks
        layout.extend(["."] * length)

# Function to find a free span of a given length
def find_free_span(layout, file_start, file_length):
    """
    Finds the earliest free span of the required length in the layout
    before the given file_start position.
    """
    curr_count = 0
    for i in range(file_start - 1, -1, -1):  # Scan backward
        if layout[i] == ".":
            curr_count += 1
            if curr_count == file_length:
                return i - file_length + 1
        else:
            curr_count = 0
    return None

# Reorganize the layout by moving files to earlier slots if possible
for fid in sorted(files_info.keys(), reverse=True): 
    start_pos, length = files_info[fid]
    new_start = find_free_span(layout, start_pos, length)
    if new_start is not None:
       
        for i in range(start_pos, start_pos + length):
            layout[i] = "."
        
        for i in range(new_start, new_start + length):
            layout[i] = str(fid)
        files_info[fid][0] = new_start

checksum = sum(i * int(ch) for i, ch in enumerate(layout) if ch != ".")
print(checksum)
