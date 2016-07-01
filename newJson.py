email = traitify_data[0]['email']
person1 = traitify_data[0]['personality']['personality_blend']['personality_type_1']['name']
person2 = traitify_data[0]['personality']['personality_blend']['personality_type_2']['name']
traits = []
for x in range(0,56):
    traits.append(str(traitify_data[0]['personality']['personality_traits'][0]['score']))
