# Script to convert comma separated file to tab delimited file
import pdb
import re

pathway_file = '/Users/Nate/Desktop/Temp_Desktop/glycolysis_gluconeogenesis.txt'
pathway_genes_file = pathway_file[:-4] + '_genes.txt'

with open(pathway_file,'r') as file_read:
    line_list = file_read.readlines()
    n_lines = len(line_list)
    with open(pathway_genes_file,'w') as file_write:
        i = 1
        #file_write.write(str(n_lines) + '\n')
        #file_write.write(line_list[n_lines-1])
        for line in line_list:
            gene_names = re.search('\t.*;',line)
            gene_name = gene_names.group(0)
            gene_name = gene_name[1:-1]
            gene_name_line = gene_name + '\n'
            if i==n_lines:
                gene_name_line = gene_name
            i = i + 1
            file_write.write(gene_name_line)
