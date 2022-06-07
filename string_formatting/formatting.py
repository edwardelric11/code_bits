
person = {'name': 'Jack', 'age': 23}

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)


sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)

# Print out tagged text
tag = 'h1'
text = 'This is a headline'

tagged_text = '<{0}>{1}</{0}>'.format(tag, text)
print(tagged_text)


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '23')

sentence2 = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence2)

# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
# print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)

# Print pi to two decimal places
pi = 3.14159265
pi_value = 'Pi is equal to {:.2f}'.format(pi)

print(pi_value)


# Comma separated large values
sentence3 = '1 MB is equal to {,} bytes'.format(1000**2)

print(sentence3)


# Print out Dates
import datetime
my_date = datetime.datetime(2020, 9, 24, 12, 30, 45)

# September 24, 2021
formatted_date = '{:%B %d, %Y}'.format(my_date)

print(formatted_date)

# September 24, 2021 fell on a Friday and was the 267 day of the year.

sentence_date = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)

print(sentence_date)
