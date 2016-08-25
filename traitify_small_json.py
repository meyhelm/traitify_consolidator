def create_new_json(data):

    new_data = {}
    new_data['Email'] = data['email']

    blend = data['personality']['personality_blend']['name']
    new_data['Blend'] = '/'.join(sorted(blend.split('/')))

    traits = []
    for x in range(0,56):
        traits.append(data['personality']['personality_traits'][x]['personality_trait']['name'])
    new_data['Traits'] = traits

    new_data['Personality Type 1'] = data['personality']['personality_blend']['personality_type_1']['name']
    new_data['Personality Type 2'] = data['personality']['personality_blend']['personality_type_2']['name']

    attributes = {}
    for trait in data['personality']['personality_traits']:
        attributes[trait['personality_trait']['name']] = trait['score']

    new_data['Trait Scores'] = attributes

    data_dump = json.dumps(new_data)
    new_json = json.loads(data_dump)

    return new_json
