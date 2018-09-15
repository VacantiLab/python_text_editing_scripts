# Script to convert comma separated file to tab delimited file
import pdb
import re
import pdb

input_file = '/Users/Nate/Dropbox/Research/Vacanti_Laboratory/Greece_Conference_2018_09/dietary_mRNA_expression/analysis/sample_descriptions.txt'
output_file[:-4] + '_output.txt'


# Get a list of the genes from the pasted pathway information from KEGG
subject_list = list()
with open(input_file,'r') as file_read:
    line_list = file_read.readlines()
    n_lines = len(line_list)
    for line in line_list:
        item_list = re.findall('\tsubject.*\t;',line)

pdb.set_trace()

# Write the gene symbols and their descriptions to a text file
with open(output_file,'w') as file_write:
    n_lines = length(item_list)
    i = 1
    for item in item_list:
        line = item + '\n'
        if i == n_lines - 1:
            line = item_list[i]
        file_write.write(line)
        i = i + 1
