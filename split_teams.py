import csv
import sys

file_name = sys.argv[1]
file_name_no_ext = file_name.split('.')[0]
divisions = int(sys.argv[2])

with open(file_name) as csv_input:
    csv_reader = csv.reader(csv_input, delimiter=',')
    line_count = 0

    files = []
    file_writers =[]

    for i in range(divisions):
        files.append(open("{} - Division {}.csv".format(file_name_no_ext,i+1),"w+", newline=''))
        file_writers.append(csv.writer(files[i], delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL))

    for row in csv_reader:
        if line_count == 0:
            for file_writer in file_writers:
                file_writer.writerow(row)
            line_count += 1
        else:
            file_writers[(line_count-1) % divisions].writerow(row) 
            line_count += 1

    for file in files:
        file.close()    

    print(f'Processed {line_count-1} teams and created {divisions} divisions')