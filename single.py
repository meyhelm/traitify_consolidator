with open("data.json", "w") as outfile:
    json.dump({'Email': email, 'Personality 1': person1, 'Personality 2': person2, 'Traits': traits}, outfile, indent=4)

with open("data.json") as file:
    result = file.read()

jString = json.dumps({'Email': email, 'Personality 1': person1, 'Personality 2': person2, 'Traits': traits}, indent = 4)
jsonData = json.loads(jString)

email = traitify_data[25]['email']
person1 = traitify_data[25]['personality']['personality_blend']['personality_type_1']['name']
person2 = traitify_data[25]['personality']['personality_blend']['personality_type_2']['name']
traits = []
for x in range(0,56):
    traits.append(str(traitify_data[25]['personality']['personality_traits'][x]['score']))

    keys = [email, person1, person2]
    mylist = []
    for k in keys:
            mylist.append(k)
    for i in traits:
            mylist.append(i)

    with open('traitify25.csv', 'wb') as myfile:
        w = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        w.writerow(mylist)
