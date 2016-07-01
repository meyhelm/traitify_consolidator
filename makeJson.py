#write new json file

with open("data.json", "w") as outfile:
    json.dump({'Email': email, 'Personality 1': person1, 'Personality 2': person2, 'Traits': traits}, outfile, indent=4)

with open("data.json") as file:
    result = file.read()
print(type(result))
###
jString = json.dumps({'Email': email, 'Personality 1': person1, 'Personality 2': person2, 'Traits': traits}, indent = 4)
jsonData = json.loads(jString)
