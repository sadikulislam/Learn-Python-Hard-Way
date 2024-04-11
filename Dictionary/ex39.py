states = {'Oregon': 'OR','Florida': 'FL','California': 'CA','New York': 'NY','Michigan': 'MI'}

cities = {'CA': 'San Francisco', 'MI': 'Detroit','FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")