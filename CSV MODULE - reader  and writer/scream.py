
#reading and writing from and into a file
from csv import reader,writer
with open("fighters.csv","r") as file:
    csv_reader=reader(file)
    #next(csv_reader)
    new_row=[[each.upper() for each in rows] for rows in csv_reader]
    #print(new_row)
#     for rows in csv_reader:
#         print(rows)
#here the fighters.csv is close next v open screaming_fighters.csv file.
with open("screaming_fighters.csv","w") as file:
    csv_writer=writer(file)
    for each in new_row:
        csv_writer.writerow(each)


