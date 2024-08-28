family = {
    'child1': {'name':'John', 'birth':1998},
    'child2': {'name':'Doe', 'birth':2008},
}
# print(family['child1']['birth'])
# print(family.get('child1').get('birth'))

family = {
    'child1': {
        'name':'John',
        'birth':1998,
        'hobbies':['travelling', 'music', 'writing']
    }
}

print(family['child1']['hobbies'][-3])