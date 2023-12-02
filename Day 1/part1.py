from pathlib import Path
import numpy as np

infile_example = Path(__file__).parent / "example1"
infile_data = Path(__file__).parent / "data1"

with open(infile_data) as f:
    count = 0
    for line in f.readlines():
        listline = list(line)
        listbool = np.array([1 if item.isnumeric() else 0 for item in listline])
        locs = np.where(listbool == 1)
        count += int(listline[np.amin(locs)] + listline[np.amax(locs)])

print(count)
