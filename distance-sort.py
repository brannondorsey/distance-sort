import csv, time
from collections import OrderedDict
from geopy.distance import vincenty

with open('data/17-0711 Syria Cultural Sites.csv', 'r', encoding='utf8') as f:
    
    reader = csv.DictReader(f)
    # tmp dict has keys for each column name paired with lists of value
    tmp = OrderedDict()
    for row in reader:
        for column, value in row.items():
            tmp.setdefault(column, []).append(value)

    data = [] # data will hold a dict of each csv row with column names as keys
    for i in range(len(tmp['source_id'])):
        row = OrderedDict()
        for key in tmp.keys():
            row[key] = tmp[key][i]
        data.append(row)

    print('Comparing distances of {} locations...'.format(len(data)))
    start_time = time.time()
    # 2D for loop that compares each location against all locations except itself
    for i in range(len(data)):
        # always save the current nearest distance, location pairs
        nearest = [float('inf'), None]
        for j in range(len(data)):
            if i == j: continue
            dist = vincenty((float(data[i]['lat']), float(data[i]['long'])), 
                            (float(data[j]['lat']), float(data[j]['long']))).kilometers
            if dist < nearest[0]:
                nearest = [dist, data[j]['source_id']]
        args = [i + 1, len(data), (i / len(data)) * 100, nearest[1], data[i]['source_id'], nearest[0]]
        print('{}/{} ({:.2f}%): {} is nearest to {} with a distance of {:.6f} kilometers'.format(*args))
        data[i]['nearest_neighbor'] = nearest[1]
        data[i]['nearest_neighbor_distance'] = '{:.6f}'.format(nearest[0])

    # sort by distance ascending, if needed
    # data.sort(key=lambda x: x['nearest_neighbor_distance'])

    with open('data/17-0711 Syria Cultural Sites with Distances.csv', 'w', encoding='utf8') as f:
          writer = csv.DictWriter(f, fieldnames=data[0].keys())
          writer.writeheader()
          for d in data:
            writer.writerow(d)
    # for d in data:
    #   print('{} {} {} {} {}'.format(d['source_id'], d['nearest_neighbor'], d['lat'], d['long'], d['nearest_neighbor_distance']))

    print('Finished in {} seconds'.format(int(time.time() - start_time)))
