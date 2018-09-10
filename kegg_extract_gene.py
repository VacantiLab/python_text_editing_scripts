# Script to convert comma separated file to tab delimited file
import pdb
import re
import mygene
import pdb

# Make the mygene object
mg = mygene.MyGeneInfo()

pathway_file = '/Users/Nate/Desktop/Temp_Desktop/glycolysis_gluconeogenesis.txt'
pathway_symbols_descriptions_file = pathway_file[:-4] + '_symbols_descriptions.txt'
pathway_symbols_file = pathway_file[:-4] + '_symbols.txt'


# Get a list of the genes from the pasted pathway information from KEGG
gene_list = list()
with open(pathway_file,'r') as file_read:
    line_list = file_read.readlines()
    n_lines = len(line_list)
    i = 1
    for line in line_list:
        gene_names = re.search('\t.*;',line)
        gene_name = gene_names.group(0)
        gene_name = gene_name[1:-1]
        i = i + 1
        gene_list.append(gene_name)

# get all of the desired gene information
gene_info_list = mg.querymany(gene_list, scopes='symbol', fields='name', species='human')

# extract the gene descriptions into a list from the output above
gene_description_list = list()
gene_list_info_counter = 0
for gene_symbol in gene_list:
    if gene_symbol == gene_info_list[gene_list_info_counter]['query']:
        gene_description = gene_info_list[gene_list_info_counter]['name']
        gene_description = gene_description
            #the .encode('utf-8') converts them to "normal" strings from unicode strings
        gene_description_list.append(gene_description)
    gene_list_info_counter = gene_list_info_counter + 1

# Write the gene symbols and their descriptions to a text file
with open(pathway_symbols_descriptions_file,'w') as file_write:
    i = 0
    n_lines = len(gene_list)
    for gene_symbol in gene_list:
        line = gene_list[i] + '\t' + gene_description_list[i] + '\n'
        if i == n_lines - 1:
            line = gene_list[i] + '\t' + gene_description_list[i]
        file_write.write(line)
        i = i + 1

with open(pathway_symbols_file,'w') as file_write:
    i = 0
    n_lines = len(gene_list)
    for gene_symbol in gene_list:
        line = gene_list[i] + '\n'
        if i == n_lines - 1:
            line = gene_list[i]
        file_write.write(line)
        i = i + 1
