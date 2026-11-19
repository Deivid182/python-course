# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# tuple with initial values

tpl = ('item1', 'item2','item3')

fruits = ('banana', 'orange', 'mango', 'lemon')

# checking the length of a tuple using len() builtin function
tpl = ('item1', 'item2', 'item3')
len(tpl)


### Accessing Tuple Items

tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]


tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]


## changing tuples to lists and lists to tuples

tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')