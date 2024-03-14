# name='ATHARAVA PRATAP SINGH'
# AGE=19
# education='pursuing btech in ABES ENGINEERING COLLEGE'
# profession='Student'
# address='Dharmupur Dubauliya Bazar Basti,Uttar Pradesh'
# print(name)
# print(AGE)
# print(education)
# print(address)


# rating=5.7
# print(rating,type(rating))


# Q1-insert *name ,*age, year of birth,is new user,list of  favourite food
# name="ATHARAV PRATAP SINGH"
# age=19
# dob="07/02/2002"
# user ="new"
# list_of_favourite_food=("panner","mushroo","dal")
# print(name)
# print(age)
# print(dob)
# print(user)
# print(list_of_favourite_food)


# OPERATORS

'''
a=10
b=7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
# a//b=cofficient before decimal after divide
print(a**b) 
# a**b=a^b
print(a%b)
'''


# Q1-average of three numbers

'''
a=2343
b=3444
c=23323433
d=(a+b+c)/3
print("average=",d)
'''

# Assignment operartor
'''
a=34
a+=34
a-=23
a*=2
a/=2
print(a)
'''

# Relational Operator

'''
a=23
b=45
print('a>b=',a>b)
print('a<b=',a<b)
print('a not equal to b=',a!=b)
print("a is equal to b =",a==b)
print('a less than equal to b',a<=b)
print('a greater than equal to b', a>=b)
'''

#  Logical operator

'''
x=True
y=False
print('x and y is ', x and y)
print('x or y is', x or y)
print('not x is',not x)
'''

# User Input

'''name=input()
print(name)'''


'''a=int(input())
b=int(input())
print(type(a))
print(type(b))
c=a+b
print(c)'''

'''E=int(input('enter marks of english\n'))
M=int(input('enter marks of mathematics\n'))
S=int(input('enter marks of science\n'))
average=(E+M+S)/3
percentage=(E+M+S)*100/300
print(average)
print(percentage)'''


# Conditional Statement
'''
age =int(input())
print(age,type(age))
if age > 18:
   print('you can vote')
else:
   print('you cannot vote')
'''

'''
num=int(input())
if num>0:
    print('positive number')
elif num==0:
    print('neither negative nor postive its zero')
else:
    print('negative number')   '''     

# Range() Function


'''a = list(range(10))
print(a)'''
# it will output-[0,1,2,3,4,5,6,7,8,9]

'''a=list(range(5,10))
print(a)'''
# It will print output - [5,6,7,8,9]

'''a=list(range(2,15,3))
print(a)'''
# It will print output- [2,5,8,11,14]
# 3 is the difference




# PYTHON LOOP

# For loop
'''
for x in range(10):
    print(2*x,end=",")'''


# a=['ANUJ','ROHIT','SHIVAM']
# for name in a:
#     print(name*5)


# While loop

'''n=10
while n>=0:
    print(n)
    n-=1'''

# STRINGS

'''fruit='APPLE'
print(fruit[-4])'''
# output-P

'''fruits='APPLE'
print(fruits[1])'''
# output-P

'''
a='APPLE'
print(a[1:4])'''

'''
c='abc'
b='def'
a=b+c
print(a)'''

'''a='ATHARAVA'
c=a*3
print(c)'''

'''
a='ATHARAVA'
for my_char in a:
    print(my_char*3)'''
'''
password='ATHARAVA123'
print(password.isalpha())'''

'''password='12345678'
print(password.isdigit())
'''
'''
password='ATHARAVA'
print(password.isupper())'''

'''a='ATHARAVA%^'
print(a.isupper())'''

'''a='  ATHARAVA  '
print(a.lstrip())'''

'''
a='ATHARAVA'
print(a.lower())'''

'''
a='atharava'
print(a.upper())'''


# PYHTON LISTS
'''
my_list[1,2,4,'ATHARAVA']
print(my_list)'''

'''fruits=['APPLE','GUAVA','BANANA','PAPAYA']
print(fruits[-1])
print(fruits[1])
print(fruits[2])
print(fruits[0])'''


# LIST COMPREHENSION
'''
first_name='ATHARAVA'
last_name='SINGH'
full_name=first_name +last_name
print('hello,full_name! I have delved into python')'''


# print("Enter the value of a:")
# a=input().split()
# print(a)
# print("Enter the value of b:")
# b=[int(i) for i in input().split()]
# print(b)



'''
print('Enter the marks of student:')
s=float(input())
if s<=100 and s>=80:
     print('A')
elif s<80 and s>=73:
    print('B')
elif s<73 and s>=65:
    print('C')
elif s<64 and s==0:
    print('D')
else:
    print('Z')
    '''

'''
n=float(input('Enter the number:'))
if n%2!=0:
    print('Weird')
else:
    if n>=2 and n<=5:
        print('Not Weird')
    elif n>=6 and n<=20:
        print('Weird')
    elif n>20:
        print('Weird')
'''



