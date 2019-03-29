from csv import DictReader
with open("fighters.csv") as file:
    csv_dictreader=DictReader(file)
    for each in csv_dictreader:
   #     print(each)
        #each row is an ordered dict object
        #here headers will be served as keys.
        #can use this keys to get the values.
        print(each['Name'])
        print(each['Country'])
        print(each['Height (in cm)'])
