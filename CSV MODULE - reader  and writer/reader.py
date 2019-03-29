from csv import reader
#open fighters.csv file using open function and gave aliases
with open("fighters.csv") as file:
    #file is read using reader()
    
    csv_reader=reader(file)
    
    #to remove the headers from the file ie first row.use next() -skip first and move to next row
    next(csv_reader)
    #iterate thru it and each row is printed
    for row in csv_reader:
        #print(f"{fighter[0]} is from {fighter[1]}")

        print(row) #each row is representead as a list


