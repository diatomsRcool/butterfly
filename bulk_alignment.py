import pickle

#This data file contains links between taxa across projects
in_file = open('butterfly_taxa.txt', 'r')

#This data file contains the taxa you want to query
data = open('input.txt', 'r')

#This file contains the results of the query
out_file = open('results.txt', 'w')

#This dictionary links the abbreviated list names with the full names in the data file.
source_dict = pickle.load(open('source_dict.p', 'rb'))

#This dictionary links each project with its base list
base = pickle.load(open('base.p', 'rb'))

#This is a list of all the problem taxa
geog = pickle.load(open('problem_taxa.p', 'rb'))

#This is a list of all error messages
nope = pickle.load(open('alerts.p', 'rb'))

#This code can answer the question, "What is the equivalent of Taxon A from List 1 in List 2?
#Enter inside the quotes: 1) the full binomial or trinomial for the taxon you are starting with
#as it appears in the starting project 2) the list you are starting with, and 3) the list
#you are ending with

#This bit of code finds the parent id of the taxon in the starting project list.
def find_parent_id_start(taxon, start_list):
	found_name = 0
	found_source = 0
	sources = []
	in_file.seek(0)
	for line in in_file:
		row = line.split('\t')
		n = len(row)
		if len(row) > 4:
			taxon_id = row[0]
			name = row[1]
			parent_id = row[2]
			source = row[4].strip()
			if name == taxon and source == source_dict[start_list]:
				found_name = 1
				if source in sources:
					pass
				else:
					sources.append(source)
				found_source = 1
				parent_ids.append(parent_id)
	if found_name == 0 or found_source == 0:
		print('Error. Please check taxon spelling (capitals and spaces count). Make sure taxon is supposed to be in the start list. Please use one of the following: ITIS, Pelham, OW, Illinois, Michigan, MPG, Colorado, Tennessee, Orange, Ohio, Cascades, Florida, Iowa. Then try again.')
	return(parent_ids)

#This code finds the taxon in the base list its parent id in the switchboard
def find_switchboard_id(parent_ids):
	found_base = 0
	sources = []
	for pid in parent_ids:
		in_file.seek(0)
		for line in in_file:
			row = line.split('\t')
			taxon_id = row[0]
			name = row[1]
			parent_id = row[2]
			if len(row) > 4:
				source = row[4]
				if pid == taxon_id:
					found_base = 1
					if source in sources:
						pass
					else:
						sources.append(source)
					parent_ids_1.append(parent_id)
			else:
				pass
	if found_base == 0:
		print('Error finding base list')
	return(parent_ids_1)

#This code uses the switchboard to find the taxon in the base list of the ending project list.
def find_base(parent_ids_1):
	found_switch = 0
	sources = []
	for pid in parent_ids_1:
		in_file.seek(0)
		for line in in_file:
			row = line.split('\t')
			taxon_id = row[0]
			name = row[1]
			parent_id = row[2]
			if len(row) > 4:
				source = row[4].strip()
				if pid == parent_id:
					found_switch = 1
					if source == source_dict[base[end_list]]:
						if source in sources:
							pass
						else:
							sources.append(source)
						taxon_ids.append(taxon_id) #This makes a list of all the taxa in the base list
													#that have the same parent in the switchboard
			else:
				pass
	if found_switch == 0:
		print('Error switching bases')
	return(taxon_ids)

#This code uses the taxon id of the taxon in the base list to find the child taxon in 
#the ending project list and looks up any warning messages.
def find_taxon(end_list, taxon_ids):
	error_message = ''
	found_name = 0
	sources = []
	for pid in taxon_ids:
		in_file.seek(0)
		for line in in_file:
			row = line.split('\t')
			taxon_id = row[0]
			name = row[1]
			parent_id = row[2]
			if len(row) > 4:
				source = row[4].strip()
			if pid == parent_id:
				if source == source_dict[end_list]:
					if source in sources:
						pass
					else:
						sources.append(source)
					found_name = 1
					names.append(name)
					
	if taxon in geog:
		st = taxon + '_' + start_list + '_' + end_list
		if st in nope:
			error_message = nope[st]
			
	if len(names) == 0:
		found_name = 0

	if found_name == 0:
		error_message = 'There is no match in this list (species assumed absent).'
	elif error_message != '':
		error_message = 'Proceed with caution. ' + error_message
	return(names,error_message)

#This code iterates over the input file. Each line in the file is a query. Each query
#result is a separate line in the output file.
next(data)
for line in data:
	taxon_ids = []
	names = []
	parent_ids = []
	parent_ids_1 = []
	line = line.strip('\n')
	row = line.split('\t')
	start_list = row[0]
	taxon = row[1]
	end_list = row[2]
	print(taxon)
	print(start_list)
	print(end_list)
	z,e = find_taxon(end_list,find_base(find_switchboard_id(find_parent_id_start(taxon, start_list))))
	s = set(z)
	out_file.write(line + '\t' + '|'.join(s) + '\t' + e + '\n')