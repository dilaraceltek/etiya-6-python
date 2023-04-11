#import maths
#print(maths.sum(10,20))

#import maths as m  #takma ad dosyalara göre değişmez.
import random
from maths import sum as Sum_1
from classes import human

#print(m.sum(10,20))
print(random.randint(0,100))

print(Sum_1(10,20))  #import edilen alan yazılır.

human1 =human("Elif")
human1.talk("Merhaba")
