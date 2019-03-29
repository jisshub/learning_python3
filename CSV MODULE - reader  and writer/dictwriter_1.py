from csv import DictWriter

with open("employee.csv","w") as file:
	headers=["name","department","salary"]
	new_file=DictWriter(file,fieldnames=headers)
	new_file.writeheader()
	values=[{"name":"jissmon","department":"MCA","salary":45000},
			{"name":"jerin","department":"mtech","salary":45000}]
	for v in values:
		new_file.writerow(v)
	


