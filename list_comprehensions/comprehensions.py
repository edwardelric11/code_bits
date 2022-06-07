nums = [1,2,3,4,5,6,7,8,9,10]

# Get 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

# Get even 'n' in nums
even_list = []
for n in nums:
  if n%2 == 0:
    even_list.append(n)
print(even_list)

# Get (letter, num) pair for each letter in 'abcd' and each number in '0123'
alphanumeric_list = []
for letter in 'abcd':
  for num in range(4):
    alphanumeric_list.append((letter,num))
print(alphanumeric_list)

# List Comprehension
alphanumeric_list2 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(alphanumeric_list2)

# dict{'name': 'hero'} for each name,hero in zip(names, heros)
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

superhero_dict = {}
for name, hero in zip(names, heroes):
    superhero_dict[name] = hero
print(superhero_dict)

# Dictionary Comprehension
my_dict = [name: hero for name, hero in zip (names, heroes)]


# Superheroes except Spiderman
without_spiderman_dict = [name: hero for name, hero in zip (names, heroes) if hero != 'Spiderman']
print(without_spiderman_dict)


# Generator Expressions
# Yield 'n*n' for each 'n' in nums

# def gen_func(nums):
#     for n in nums:
#        yield n*n

# my_gen = gen_func(nums)

my_gen = (n*n for n in nums)

for i in my_gen:
    print i
