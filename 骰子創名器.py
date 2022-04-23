import random
import string

print('Name picker!')
num = int(input("How many names u wanna create?"))
          
while True:
    for num in range(num):
        adjs = ['sleepy', 'fat', 'thin', 'long','chubby',
      'elder','slender','golden','silver','fluffy',
      'clam','childish','clever','confident','cruel',
      'diligent','generous', 'humble','impolite','intelligent',
      'jealous','responsible','silent','silly','sincere',
      'alone','ancient','available','chemical','curious',
      'dumb','quick','slow','local']

        ns = ['cockroach','dinosaur','eagle','mosquito','angel',
    'devil','assistant','audience','beginner','businessman',
    'chirman','customer','director','expert','general',
    'judge','manager','military','president','principal',
    'banana','avocado','ketchup','papaya','spaghetti',
    'wine','pajamas','rectangle']
        adj = random.choice(adjs)

        n = random.choice(ns)

        number = random.randrange(0, 999)

        special = random.choice(string.punctuation)

        special2 = random.choice(string.punctuation)

        password = adj + special + n + str(number) + special2
        print('Your NEW name is: %s' % password)
    

    response= input('Would you like another name? y/n')
    if response == 'n':
    
        break
