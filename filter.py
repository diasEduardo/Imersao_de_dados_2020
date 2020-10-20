import csv

def save(row):
	with open('MICRODADOS_ENEM_2019_SUB15.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(row)

with open('DADOS/MICRODADOS_ENEM_2019.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    NU_IDADE_index = 6
    for row in csv_reader:
    	split = row[0].split(";")
    	line_count+=1
    	
    	if line_count == 1 or int(split[6]) < 15:
    		save(row)
    	print(line_count)
    	