import csv
all_ids = []


file = open('FileName3.csv') #name of file with data generated from part 1
csvreader = csv.reader(file)
datalist1 = [] 
dictionary1 = {} 
for row in csvreader:
    row.insert(1,"1") 
    datalist1.append(row) 
listlength = len(datalist1)
for i in range(listlength):
    currentlist = datalist1[i]
    if currentlist[0] not in all_ids:
        all_ids.append(currentlist[0])
for row in datalist1: 
    dictionary1[row[0]] = row 


file = open('FileName4') #name of another file with data generated from part 1
csvreader = csv.reader(file)
datalist2 = [] 
dictionary2 = {} 
for row in csvreader:
    row.insert(1,"2") 
    datalist2.append(row) 
listlength = len(datalist2)
for i in range(listlength):
    currentlist = datalist2[i] 
    if currentlist[0] not in all_ids:
        all_ids.append(currentlist[0])
for row in datalist2: 
    dictionary2[row[0]] = row

#can copy and paste lines 5-18 as needed to analyze more files
#ensure that the numbers are changed based on the file number

list_of_all = []
for i in range(len(all_ids)):
    current_tag = all_ids[i]
    if current_tag in dictionary1:
        list_of_all.append(dictionary1[current_tag]) 
    if current_tag in dictionary2:
        list_of_all.append(dictionary2[current_tag])

#can copy and paste lines 42-43 as needed to analyze more files
#ensure that the numbers line up with the file number


with open('FileName5.csv', 'w') as f:#name of file for data to be written into
    writer = csv.writer(f)
    writer.writerows(list_of_all)
   
