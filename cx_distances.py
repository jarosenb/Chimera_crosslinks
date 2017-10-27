import chimera
import csv
from collections import defaultdict
from chimera import runCommand as rc
from chimera.selection import currentAtoms

##### USER PARAMETERS: #####

input_filename = "UVPD_xlink.csv"
output_filename = "output_common.csv"

# only plot distances below this threshold (angstroms)
distance_threshold = 50
PDB_ID = "3v03"

# Chimera commands to execute before finding crosslinks. Here chain B is deleted.
preprocessing_commands = ["delete :.B"]

############################

csvfile = open(input_filename, 'r')
f = open(output_filename, "w")
f.write("Residue 1,Residue 2,Distance\n")

# read in BSA structure from PDB and delete B-chain
rc("open " + PDB_ID)
for command in preprocessing_commands:
    rc(command)

# cxdict keeps track of duplicate crosslinks
cxdict = defaultdict(list)

for row in csv.reader(csvfile):

    # select alpha-carbons of the first and second residues
    sel_string = " :" + row[0] + "@CA :" + row[1] + "@CA"
    rc("sel" + sel_string)

    try:
        a1, a2 = currentAtoms()
    except ValueError:
        continue

    dist = a1.coord().distance(a2.coord())

    # computation is over so we unselect the selected atoms
    rc("~sel" + sel_string)

    # write residue numbers and distance to the output file
    f.write(row[0] + "," + row[1] + "," + str(dist) + "\n")

    # plot the crosslink on the structure if above theshold and not duplicate
    cxdict[row[0]].append(row[1])
    if row[0] in cxdict[row[1]] or dist > distance_threshold:
        pass
    else:
        rc("distance" + sel_string)

# housekeeping
f.close()
csvfile.close()
