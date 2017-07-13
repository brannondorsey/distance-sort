import csv
from collections import OrderedDict
from geopy.distance import vincenty

with open('data/17-0711 Syria Cultural Sites.csv', 'r', encoding='utf8') as f:
	reader = csv.DictReader(f)
	data = OrderedDict()
	for row in reader:
	    for column, value in row.items():
	        data.setdefault(column, []).append(value)

	print([k for k in data.keys()])
	for i in range(len(data['source_id'])):
		for j in range(len(data['source_id'])):
			pass

