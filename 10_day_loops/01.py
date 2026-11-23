# Iterate 0 to 10 using for loop, do the same using while loop.

separate = "--------------------"

count = 0
while count <= 10:
  print(count)
  count += 1

print(separate)

# Iterate 10 to 0 using for loop, do the same using while loop.

count = 10
while count >= 0:
  print(count)
  count -= 1

print(separate)

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

# Output:

#
##
###
####
#####
######
#######

output = ""
for i in range(7):
  output += "#"
  print(output)

print(separate)

# Use nested loops to create the following pattern:

  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #

rows = 8
cols = 8
for i in range(rows):
  for j in range(cols):
    print("#", end=" ")
  print()  # line break

print(separate)

# Print the following pattern:

#  0 x 0 = 0
#  1 x 1 = 1
#  2 x 2 = 4
#  3 x 3 = 9
#  4 x 4 = 16
#  5 x 5 = 25
#  6 x 6 = 36
#  7 x 7 = 49
#  8 x 8 = 64
#  9 x 9 = 81
#  10 x 10 = 100

for i in range(11):
  print(f"{i} x {i} = {i * i}")

print(separate)

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

frameworks = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for framework in frameworks:
  print(framework)

print(separate)

# Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(101):
  if i % 2 == 0:
    print(i)

print(separate)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
  if i % 2 != 0:
    print(i)

print(separate)