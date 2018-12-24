import random
import sys
import os

#Operators
'''
#print("5 + 2 = ", 5+2)
#print("5 - 2 = ", 5-2)
#print("5 * 2 = ", 5*2)
#print("5 / 2 = ", 5/2)
#print("5 % 2 = ", 5%2)
#print("5 ** 3 = ", 5**3)
#print("5 // 2 = " , 5//2)
#print("1 + 2 - 3 * 2 =" , 1+2-3*2)
#print("1 + 2 - 3 =" , 1+2-3)

'''

#Strings
quote = 'always'
multi_line = '''ab 
cd '''
#print('\n' * 5)
#print(quote+multi_line)
#print("%s %s %s" % ('like this ', quote, multi_line))

#List
grocery = ['juice','veggies', 'fruits']
to_do = ['play','shop','sleep']
events=[grocery,to_do]
#print(events)
#print(events[0][0])
to_do.append('aa')
#print(to_do)
grocery.insert(1,'pickle')
#print(grocery)
grocery.remove('pickle')
#print(grocery)
grocery.sort()
#print(grocery)
grocery.reverse()
#print(grocery)

#print(len(grocery))
#print(max(grocery))

#Tuple
pi_tuple=(6,4,8,2)
#print(pi_tuple)

new_tuple = list(pi_tuple)
#print(new_tuple)

new_list = tuple(new_tuple)
#print(new_list)
#print(len(new_tuple))

#Dictionary
super_dict={'a':'aa','b':'bb','c':'cc','d':'dd'}
#print(super_dict['c'])
#print(super_dict.keys())
#print(super_dict.values())
del super_dict['a']
#print(super_dict)

'''
age=14
if age > 18:
    print('eligible')
else:
    print('not eligible')

for x in range(0,10):
    print(x)
    
num_list=[[1,2,3],[11,22,33],[111,222,333]]
print(num_list[1])
for x in range(0,3):
    for y in range(0,3):
        #print(num_list[x][y])
'''


'''
random_num = 15#random.randrange(0,15)
print(random_num)

while(random_num == 15):
    print('num found as random',random_num)
    random_num=random.randrange(13,17)
    print(random_num)
'''
        
def add(num1, num2):
    sum = num1 + num2
    return sum

#print(add(11, 13))

#print('what is ur name?')
#name=sys.stdin.readline()
#print('name is '+name)  

long_str='   This is supposed to be is a long string    '

'''
print(long_str[1:6])
print(long_str[1:])
print(long_str[:6])
print(long_str[:-5])
print(long_str[-5:])
print(long_str.capitalize())
print(long_str.find('This'))
print(long_str.isalpha())
print(long_str.isalnum())
print(long_str.replace('is','was'))

str=long_str.strip()  #remove leading and trailing spaces
print(long_str)
print(str)
'''
quote1 = 'let it be, let it be, let it be'
#print(quote1.find('let'))
#print(quote1.find('let',2))
#print(quote1.find('let',2,14))

list = quote1.split(',')
#print(list)

space='a '
list = space.split(' ')
#print(len(list))

test_file = open("test.txt","wb")
#print(test_file.mode)
#print(test_file.name)
test_file.write(bytes("Sample text in file\n", "UTF-8"))
test_file.close()

test_file = open("test.txt", "r+")
text_in_file = test_file.read()
#print(text_in_file+)

class Animal:
    __name = "animal1"
    __height = 0
    __weight = 0
    __sound = 0
    
#Constructor
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

#Getters and Setters
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height
        
    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight
        
    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound
        
    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")
        
    def toString(self):
        return "{} is {} cm tall and {} kg of weight and sounds {}".format(self.__name,self.__height,self.__weight,self.__sound)

#Creating object  
cat = Animal("animal",22,33,"meow")

#print(cat.toString())

#Inheritence

class Dog(Animal):
    __owner = ""
    
    def __init__(self,name,height,weight,sound,owner):
        super(Dog, self).__init__(name,height,weight,sound)
        self.__owner = owner
        
    def set_owner(self, owner):
        self.__owner = owner
        
    def get_owner(self):
        return self.__owner
    
    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kg of weight, sounds {} and owner is {}".format(self.get_name(),
                                                                                        self.get_height(),
                                                                                        self.get_weight(),
                                                                                        self.get_sound(),
                                                                                        self.__owner)
        #return "The owner is {}".format(self.__name)
    
    def multiple_sounds(self,how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)
        
spot = Dog("spot",11,22,"Ruff","ji")
print(spot.toString())

#Polymorphism
class AnimalTesting:
    def getType(self, animal):
        animal.get_type()
        
testAnimal = AnimalTesting()

#testAnimal.getType(spot)
#testAnimal.getType(cat)

#spot.multiple_sounds()
#spot.multiple_sounds(3)
