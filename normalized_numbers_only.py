# entire thing
import csv
success_counter = 0
skip_counter = 0
for row in traitify_data:
    try:

        traits = []
        for x in range(0,56):
            traits.append(traitify_data[0]['personality']['personality_traits'][x]['personality_trait']['name'])
        keyList = sorted(traits)

        attributes = {}
        for i in range(0,56):
            k = row['personality']['personality_traits'][i]['personality_trait']['name']
            v = (str(row['personality']['personality_traits'][i]['score']/100)) #normalize score
            attributes[k] = v

        d.update(attributes) #combine both dicts together

        with open('traitifyNum.csv', 'a') as myfile:
            writer = csv.DictWriter(myfile, keyList)
            writer.writerow(d)

        success_counter = success_counter + 1

    except Exception as e:
        skip_counter = skip_counter + 1

print "Successes: %d" % success_counter
print "Failures: %d" % skip_counter
