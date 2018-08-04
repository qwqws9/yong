from random import randint
a=randint(1,99)
print('{} : {}' .format(a, not bool(a%2)))
print('{} : {}' .format(a, a%2 == 0))

