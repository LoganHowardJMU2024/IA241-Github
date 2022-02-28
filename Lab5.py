'''
Lab 5
'''

#3.1

alien_color = 'yellow'

if alien_color == 'green':
    print('you have earned 5 points')
    
#3.2

alien_color = 'yellow'

if alien_color == 'green':
    print('you have earned 5 points')
    
else:
    print('you have earned 10 points')
    
#3.3

favorite_fruits = ['apple','banana','orange']

if 'mango' in favorite_fruits:
    print('you really like mangos')
    
if 'apple' in favorite_fruits:
    print('you really like apples')
    
if 'peach' in favorite_fruits:
    print('you really like peaches')
    
#3.4

age = 23

if age <10:
    print('kid')

elif age>10 and age<20:
     print ('teenager')

else:
    print('adult')
    
    if age>65:
        print('elder')