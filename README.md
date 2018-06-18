# butterfly
butterfly names alignment

THIS ALIGNMENT IS COMPLETE, BUT NOT TESTED. TESTING IN PROGRESS. USE WITH CAUTION.

This is an alignment of Lepidopteran names in four classifications and ten list of names used by monitoring projects.
Classifications
1. ITIS
2. NABA
3. Pelham
4. Opler & Warren

Project Lists
1. Illinois Butterfly Monitoring Network
2. Cascades Butterfly Project
3. Colorado Butterfly Monitoring Network
4. Florida Butterfly Monitoring Network
5. Iowa Butterfly Survey Network
6. Michigan Butterfly Network
7. MPG Ranch Butterfly Monitoring Program
8. Ohio Butterfly Monitoring Network
9. Orange County Butterfly Monitoring Network
10. Tennessee Butterfly Monitoring Network

*Note: Orange County Butterfly Monitoring Network was also known as Irvine Ranch

alignment_test.ipynb is a jupyter notebook to use to test the alignment. Go to the mybinder link below to use it.

http://mybinder.org/repo/diatomsrcool/butterfly
The jupyter notebook will allow one query at a time. For bulk query, use bulk_alignment.py

## File Descriptions
alerts.p - This is a pickled dictionary that looks up warning messages for different results. The key is the species name, the starting list, and the ending list separated by underscores. The value is the warning message. Use the pickle Python library to load the dictionary.

alignment_test.ipynb - The jupyter notebook that allows users to submit one query at a time. The species, starting list, and ending list are given manually. The output is the species equivalent in the ending list and a warning message if applicable.

base.p - This is a pickled dictionary that links each project with its base list.

bulk_alignment.py - This code does the same thing as the jupyter notebook, only it allows bulk submission of queries.

butterfly_taxa.txt - This is a tab-delimited text file that contains the mapping between the lists. Taxa in the project lists are linked to taxa in the base lists via a parent/child relationship. The project taxa are the children and the base taxa are the parent. The base lists are then linked to the "switchboard" via a parent/child relationship. The switchboard is the highest level classification. All the base lists are related to each other through the switchboard. The base taxa are the children and the switchboard taxa are the parents.

input.txt - This is the input for the bulk_alignment.txt file. The file is tab-delimited with a header row. It has three columns. First: the starting list. Second: the taxon in the starting list. Third: the ending list. All input files need to be in this format with the three columns and the header row.

meta.xml - This file describes the structure of the butterfly_taxa.txt file in compliance with Darwin Core standard.

problem_taxa.p - This is a pickled list that contains the species names of taxa that require warning messages. If a species is not in this list, the code to look up the warning message will not be triggered.

results.txt - This the output file from bulk_alignment.py. This file is tab-delimited with five columns. There is no header row. First: the starting list. Second: the taxon in the starting list. Third: the ending list. Fourth: taxon in the ending list. Fifth: warning message, if applicable.

source_dict.p - This dictionary links the abbreviated list names with the full names in the data file.

test.txt - Test data set for developing bulk_alignment.py

## Adding more project lists
The mapping (butterfly_taxa.txt) is designed so that new lists can be added. New projects need to declare their base list (NABA, O&W, or Pelham) and any deviations from that base list. Then the new project list can be added with each taxon a child of the corresponding taxon in the base list. This should be done in accordance with the Darwin Core standard.
