# The following list contains some fruits
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

# 1. Check if 'apple' is in the list
if 'apple' in fruits:
  print('That fruit already exists in the list')
else:
  fruits.append('apple')
  print(fruits)

