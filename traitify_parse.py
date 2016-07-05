# entire thing
success_counter = 0
skip_counter = 0
for row in traitify_data:
    try:

        keys = ["Email", "Personality Type 1", "Personality Type 2"]
        traits = []
        for x in range(0,56):
            traits.append(traitify_data[0]['personality']['personality_traits'][x]['personality_trait']['name'])
        keyList = keys+sorted(traits)

        d = {}
        d['Email'] = row['email']
        d['Personality Type 1'] = row['personality']['personality_blend']['personality_type_1']['name']
        d['Personality Type 2'] = row['personality']['personality_blend']['personality_type_2']['name']

        attributes = {}
        for i in range(0,56):
            k = row['personality']['personality_traits'][i]['personality_trait']['name']
            v = (str(row['personality']['personality_traits'][i]['score']))
            attributes[k] = v

        d.update(attributes)

        with open('traitify.csv', 'a') as myfile:
            writer = csv.DictWriter(myfile, keyList)    #fieldnames
            if success_counter == 0
                writer.writeheader()
            writer.writerow(d)

        success_counter = success_counter + 1

    except Exception as e:
        skip_counter = skip_counter + 1

print "Successes: %d" % success_counter
print "Failures: %d" % skip_counter
