import json
import csv

data_parsed = json.loads(traitify_data)
data = open('/Users/meyhel01/Documents/tData.csv')
csvwriter = csv.writer(data)
count = 0
for person in data:
      if count == 0:
             header = traitify_data.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(data.values())
