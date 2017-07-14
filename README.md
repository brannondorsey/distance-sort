# Distance Sort

Given a set of points of syrian cultural significance, sort them by their distance to the nearest neighbor location in order to remove possible duplicates from multiple data sources. Original, and sorted, data can be found in `data/`.

## Usage

```bash
# install dependency
pip3 install geopy

# run the distance sort. Performs 12,000 * 12,000 = 144 Million distance comparisons. 
# Takes ~40 minutes to terminate on one 4.2GHz processor. Could be parallelized, but I didn't have time.
python3 distance-sort.py
```

This should work on any csv that has at least the following columns: `source_id`, `lat`, `long`. Adds the columns `nearest_neighbor` (the `source_id` of the closest location) and `nearest_neighbor_distance` (in kilometers).
