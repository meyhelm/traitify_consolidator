# entire thing
success_counter = 0
skip_counter = 0
for row in traitify_data:
    try:
        email = row['email']
        person1 = row['personality']['personality_blend']['personality_type_1']['name']
        person2 = row['personality']['personality_blend']['personality_type_2']['name']
        traits = []
        for x in range(0,56):
          traits.append(str(row['personality']['personality_traits'][x]['score']))

        jString = json.dumps({'Email': email, 'Personality 1': person1, 'Personality 2': person2, 'Traits': traits}, indent = 4)
        jsonData = json.loads(jString)

        keys = [email, person1, person2]
        mylist = []
        for k in keys:
              mylist.append(k)
        for i in traits:
              mylist.append(i)

        with open('traitifyFinal4.csv', 'a') as myfile:
            w = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            w.writerow(mylist)
        success_counter = success_counter + 1
    except Exception as e:
        skip_counter = skip_counter + 1
print "Successes: %d" % success_counter
print "Failures: %d" % skip_counter
