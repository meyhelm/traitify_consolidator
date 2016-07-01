import glob

read_files = glob.glob("/Users/meyhel01/Documents/Traitify/*.json")

with open("/Users/meyhel01/Documents/merged_file.json", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
            outfile.write(',\n')