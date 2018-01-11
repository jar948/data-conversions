vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "cucumber", "color": "green"},
 {"name": "potato", "color": "brown"},
]

# write header file to csv

import csv

with open('veggies.csv', 'w') as blabla:
	typer = csv.writer(blabla)
	typer.writerow(['name', 'length', 'color'])
  
  
	# loop through each vegetable
	for x in vegetables:
	# for each veg, write a row to the csv
		firstthing = x['name']
		secondthing = len(firstthing)
		thirdthing = x['color']
		typer.writerow([firstthing, secondthing, thirdthing])

