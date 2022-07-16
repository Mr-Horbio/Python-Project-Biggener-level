# """ Now I am going to learn python automation from the book 
# it will be help me for learning hacking skills"""
# #write the first program
# # '''print('Hello')
# # print('What is your name?')#ask my name
# # name=input()
# # print('It is good to meet you,',name)
# # print('your name length is ')
# # print(len(name))

# # print('What is your age?')
# # age=int(input())
# # print("age is :",age)

#  #Elements of conditions


# # if name=='Marry':
# #     print('Hello')
# #     if password=='swordfish':     
# #        print('Access Granted')
# #  else:
# #      print('Wrong password')


# name = ''
# while name != 'your name':
#   print('Please type your name.')
#   name = input()
# print('Thank you!')


# print('enter the number:')
# spam=int(input())
# if spam<=5:
#   print('hi')
#   spam=spam+2

#using while loop
# print('Enter the number:')
# num=int(input())
# while num<5:
#   print('hi')
#   num=num+1
       

#for loop with range
# print('Enter the number:')
# num=int(input())
# for i in range(1,10):
#     num=num+i
#     print('hello')


# total = 0
# for num in range(101):

#  total = total + num
#  print(total)

# import random
# for i in range(1):
#   print(random.randint(1,6))

#ending a program early with sys.exit()

'''import sys
while True:
  print ('Type exit to exit')
  response = input()
  if response =='exit':
    sys.exit()
  print('you typed' +response+ ',')
'''
'''sum= not ((5>4) or(3==5))
print(sum)'''
'''
a=(True and True) and (True == False)
print(a)'''

# print((not False ) or (not True))
'''
spam=int(input())
if spam==1:
  print('Hello')
elif spam==2:
  print('Howdy')
else:
  print('Greetings!')'''
'''
num=0
for i in range(1,10):
    num=num+1
    print(num)'''


'''num=0
while num<10:

  num=num+1
  print(num)'''

'''a=round(2.115544,3)
print(a)'''

'''import requests
b= requests.get('https://www.w3schools.com/python/showpython.asp?filename=demo_requests_get_url')
print(b)
'''

#list  in python

'''
print("Enter the no. of car1: ")
carname1= input()
print("Enter the no. of car2: ")
carname2= input()
print("Enter the no. of car3: ")
carname3= input()
print("Enter the no. of car4: ")
carname4= input()
print("Enter the no. of car5: ")
carname5= input()
print("Enter the no. of car6: ")
carname6= input()
print("Enter the no. of car7: ")
carname7= input()
print('The car names are :')
print(carname1+ '' + carname2+  '' + carname3 + '' + carname4 + ''  +carname5 + ''  + carname6 + '' + carname7 + '')'''

'''catNames = []
while True:
 print('Enter the name of cat ' + str(len(catNames) + 1) +
' (Or enter nothing to stop.):')
 name = input()
 if name == '':
     break
catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)'''
    
'''
for i in [0,1,2,3]:
  print(i)'''

'''from sympy import cartes


car=['Tesla','Lamborgini','Thar']
a='swift' not in  car
print(a)'''
'''
cars=['Tesla','Thar','Lambo']
print("Enter the car name:")
name = input()
if name not in cars:
  print("I don't have this car")
else:
  print( name  + ' ' +'is my car')'''

'''cars=['Thar','lambor']
cars.append('tesla')
print(cars)

cars.insert(2,'Roolsroyals')
print(cars)

cars.remove('lambor')
print(cars)

cars.sort()
print(cars)
'''
'''list=('cat')
print(type(list))
'''
'''def sum(a,b):

  c=a+b
  print('your total is:',c)

sum(10,2)
sum(8,78)
  
'''

'''import copy
spam=['A','B','C','D']
cheese=copy.copy(spam)
print(spam)
print(cheese)
cheese[1]="change"
print(spam)
print(cheese)'''

# Practices Question
'''  Q1: spam=[2,4,6,8,10]
print('The orginal value of spam is :\n',spam)
print("After changing the value of spam")
spam[3]='hello'
print(spam)
'''
# spam =['a','b','c','d']
''' Q:2 spam=[int(int('3'*2)/11)]
print(spam)'''

#next question

# bacon=[3.14,'cat',11,'cat','cat','True']
# print(bacon.index(3.14))
'''bacon.append(99)
print(bacon)
bacon.remove('cat')
print(bacon)
bacon.remove('cat')
print(bacon)
bacon.append('cat')
print(bacon)
bacon.remove('cat')
print(bacon)
'''
'''bacon.pop(0)
print(bacon)
'''
'''bacon.remove('cat')
print(bacon)
'''
'''del bacon[0]
print(bacon)'''
'''
tuple=(42)
print(tuple)'''

'''tuple=(1,2,3,4)
print(type(tuple))
list=[tuple]
print(type(list))'''

'''list1=[1,1,1,1,1]
tuple1=tuple(list1)
print(tuple1)

list1=[tuple1]
print(list1)
'''

'''import copy
a=(1,1,1,1,1,1)
b=copy.copy(a)
print(b)
print(a)
c=copy.deepcopy(b)
print(c)'''


def collatz(number):
 if number%2==0:
  print("The number is even ")
   
 else:
  print("The number is odd")


