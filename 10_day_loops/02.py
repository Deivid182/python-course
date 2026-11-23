# Use for loop to iterate from 0 to 100 and print the sum of all numbers.

total = 0
separate = "------------------------------"

for i in range(101):
  total += i

print(f"The sum of all numbers from 0 to 100 is: {total}")

print(separate)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

even_sum = 0
odd_sum = 0

for i in range(101):
  if i % 2 == 0:
    even_sum += i
  else:
    odd_sum += i

print(f"The sum of all even numbers from 0 to 100 is: {even_sum}")
print(f"The sum of all odd numbers from 0 to 100 is: {odd_sum}")