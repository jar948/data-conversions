#import JSON library from python

import json

#label rows accoridng to veggies

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "cucumber", "color": "green"},
 {"name": "potato", "color": "brown"},
]

#oepn a JSON file
with open ('cooked_veggies.json', 'w') as f:
	json.dump(vegetables, f, indent=2)