# Script to convert comma separated file to tab delimited file

csv_file = '/Users/nate/Dropbox/Research/Lehtio_Laboratory/Projects/breast_cancer/cell_lines/rotenone/rotenone_proteomics/quantification_jorrit_correct/protein_quantities_gene_symbol/quantities.csv'
txt_file = csv_file[:-3] + 'txt'

with open(csv_file,'r') as file_read:
    with open(txt_file,'w') as file_write:
        for line in file_read:
            newline = line.replace(',','\t')
            file_write.write(newline)
