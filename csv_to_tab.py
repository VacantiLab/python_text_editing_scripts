# Script to convert comma separated file to tab delimited file

csv_file = 'group_color_key.csv'
txt_file = csv_file[:-3] + 'txt'

with open(csv_file,'r') as file_read:
    with open(txt_file,'w') as file_write:
        for line in file_read:
            newline = line.replace(',','\t')
            file_write.write(newline)
