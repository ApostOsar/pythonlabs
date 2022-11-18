# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

numbers = []

for number in range(0, 16):
    numbers.append({bin.__name__: bin(number), 'dec': number, hex.__name__: hex(number), oct.__name__: oct(number)})

pprint(numbers)