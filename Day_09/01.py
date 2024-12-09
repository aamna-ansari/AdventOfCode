from pathlib import Path

# File input path
fn = "D:/AdventOFCode/Day_09/input.txt"

# Read and parse input data
data = open(fn).read().strip()
s = data.split("\n")[0]

# Initialize layout
layout = []
file_id = 0

# Build the layout
for i, ch in enumerate(s):
    length = int(ch)
    if i % 2 == 0:  # File blocks
        layout.extend([str(file_id)] * length)
        file_id += 1
    else:  # Empty spaces
        layout.extend(["."] * length)

# Rearrange files to fill gaps
gap_index = 0
for i in range(len(layout)):
    if layout[i] == ".":
        if gap_index <= i:
            gap_index = i  # Update the gap index to the current gap
        while gap_index < len(layout) and layout[gap_index] == ".":
            gap_index += 1
        if gap_index < len(layout):
            # Swap the file from the right into the current gap
            layout[i], layout[gap_index] = layout[gap_index], "."

# Calculate checksum
checksum = sum(i * int(ch) for i, ch in enumerate(layout) if ch != ".")
print(checksum)
