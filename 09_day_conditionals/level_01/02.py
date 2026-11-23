# 2. Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' 
# for bigger differences, and a custom text if my_age = your_age

my_age = 25
your_age = int(input("Enter your age: "))

if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
else:
    print("We are the same age.")