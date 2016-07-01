entries = []
skip_counter = 0;
for row in traitify_data:
    try:
        entries.append(row['email'].strip() + " " + row['personality']['personality_blend']['personality_type_1']['name'].strip() + "  " + row['personality']['personality_blend']['personality_type_2']['name'].strip())
        for x in range(0,56):
            entries.append(row['personality']['personality_traits'][x]['personality_trait']['name'].strip() + " " + row['personality']['personality_traits'][x]['score'].strip())

    except Exception as e:
        skip_counter = skip_counter + 1

entries = ['Email', 'Personality Type 1', 'Personality Type 2']
for x in range(0,56):
    entries.append(traitify_data[0]['personality']['personality_traits'][x]['personality_trait']['name'])
