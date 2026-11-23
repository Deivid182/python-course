# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.



from data import countries, countries_data


separate = "------------------------------"

land_countries = [country for country in countries if "land" in country]
print(land_countries)

print(separate)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print(reversed_fruits)

print(separate)

# Go to the data folder and use the countries_data.py file. 

# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world

all_languages = {lang for country in countries_data for lang in country['languages']}
total_languages = len(all_languages)
print(f"Total number of languages: {total_languages}")

# Find the ten most spoken languages from the data

language_count = {}

for country in countries_data:
  for language in country['languages']:
    if language in language_count:
      language_count[language] += 1
    else:
      language_count[language] = 1

# Find the ten most spoken languages from the data
sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
top_ten_languages = [lang for lang, count in sorted_languages[:10]]
print(f"Top ten most spoken languages: {top_ten_languages}")

# Find the 10 most populated countries in the world
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
top_ten_populated_countries = [country['name'] for country in sorted_countries[:10]]
print(f"Top ten most populated countries: {top_ten_populated_countries}")