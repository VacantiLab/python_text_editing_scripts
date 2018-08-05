# Script to convert comma separated file to tab delimited file

csv_file = '/Users/nate/Dropbox/Research/Vacanti_Laboratory/Greece_Conference_2018_09/dietary_protein_expression/GSE9419_series_matrix.txt'
txt_file = csv_file[:-4] + '2.txt'

with open(csv_file,'r') as file_read:
    line_list = file_read.readlines()
    n_lines = len(line_list)
    with open(txt_file,'w') as file_write:
        i = 0
        #file_write.write(str(n_lines) + '\n')
        #file_write.write(line_list[n_lines-1])
        for line in line_list:
            i = i + 1
            #Do not record the last line because it just indicates the matrix is over (there is no data)
            if line == line_list[n_lines-1]:
                print('found end')
                break
            if i > 71:
                file_write.write(line)
