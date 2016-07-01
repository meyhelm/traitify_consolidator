import glob
import json

read_files = glob.glob("/Users/meyhel01/Documents/Traitify/*.json")

with open("/Users/meyhel01/Downloads/merged_file.json", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
            outfile.write('\n')

traitify_data = []
with open('/Users/meyhel01/Downloads/merged_file.json') as f:
    for line in f:
        traitify_data.append(json.loads(line))