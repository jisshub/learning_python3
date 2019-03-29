from csv import reader,writer
with open("books_data.csv","r") as file:
    csv_reader=reader(file)
    # for r in csv_reader:
    #     print(r)
    new_data=[[items.upper() for items in r]for r in csv_reader]
with open("books.csv","w") as file:
    csv_writer=writer(file)
    for add in new_data:
        csv_writer.writerow(add)

#nested list comprehension--sample
name=['jissmon','aju','ajith']
new=[[r.upper() for r in value]for value in name]
print(new)
