cities = {
    'Beijing': {
        'Country': 'China',
        'Population': 2154,
        'Event': 'International Film Festival'
    },
    'New York': {
        'Country': 'USA',
        'Population': 8537,
        'Event': "Times Square New Year's Eve Celebration"
    },
    'London': {
        'Country': 'UK',
        'Population': 8908,
        'Event': 'Wimbledon Tennis Championship'
    }
}

for k,v in cities.items():
    print("name:",k)
    print("\t","country:",v['Country'])
    print("\t","population:",v['Population'])
    print("\t","event:",v['Event'],"\n")