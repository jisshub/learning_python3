
from csv import DictWriter,writer
values=[]
values.append({"id":222,
                    "name":"sasas",
                    "age":33})
with open("details.csv","w") as file:
	headers=["id","name","age"]
	new_file=DictWriter(file,fieldnames=headers)
	new_file.writeheader()
	for v in values:
		new_file.writerow(v)
