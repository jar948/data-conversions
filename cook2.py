
# read vegetables.csv

import csv

with open('veggies.csv') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

#convert to json
import json

with open('veggies.json', 'w') as f:
	json.dump(vegetables, f, indent=2)


