'''print('Atharava Pratap Singh')
print("Name=","Atharava Pratap Singh")
a=5
b=10
print('Sum=',(a+b))'''





# INPUT IN PYTHIN

'''
name=input("Enter Your Name:")
print("WELCOME Mr.",name)
'''



# IN PYTHON IT ALWAYS TAKE STRING FORMAT INPUT

'''
marks=int(input("Enter Your Marks:"))
print("Your Marks are=",marks)
ygpa=float(input("Enteryour ygpa in first year:"))
print("Your first year ygpa is =",ygpa)
'''




# VARIABLES
'''
* Every variables name should start with only alpha character.
* No varibale name should start with digit or any special symbol.
* We can use numeric value and underscore(_) and no other specific symbol are used.
* Underscore and Digit both of them can not be used in start to declare a variable.
* In Variable don't need to specifiy the datatype.
'''

# ADDITION OF TWO NUMBER

'''
a=int(input("Enter Your first number:"))
b=int(input("Enter Your second number:"))
print("Sum of two number are=",a+b)
'''



# Arithmetic Operator


'''
* ADDITION(+)
* SUBTRACTION(-)
* MULTIPLY(*)
* DIVISION (/)
*MODULO(REMAINDER)(%)
* POWER OPERATOR(**)   
* FLOOR DIVISION (//)  (IT REMOVES THE DECIMAL VALUE AFTER DIVISION)
'''

# ONE NEW METHOD TO SHOW NOT EQUAL TO IS (<> OR !=)

#  LOGICAL OPERATOR

'''  
1. WE USE "and" FOR AND OPERATOR
2. WE USE "or" FOR OR OPERATOR
3. WE USE "not" FOR NOT OPERATOR
4. NOT OPERATOR IS USED TO RETURN REVERSE VALUE
'''



# IDENTITY OPERATOR

'''
1. IS OPERATOR(is) USED TO CHECK BOTH VARIABLES ARE SAME OBJECT AND IT RETURNS TRUE 
2. IS NOT OPERATOR(is not) USED TO CHECK BOTH VARIABLES ARE NOT SAME OBJECT THEN IT RETRUNS TRUE
'''
'''
x=5
if(type(x) is int):
    print("Correct")
else:
    print("Incorrect")
'''


'''
y=4.6
if(type(y) is not float):
    print("Correct")
else:
    print("Incorrect")
'''



# MEMBERSHIP OPERATOR

'''
"in"-IT CHECK THE VALUE WHICH IS SAY a PRESENT IN THE GIVEN LIST OR NOT, IF PRESENT THEN TRUE .
"not in"-IT CHECK THE VALUE IS SAY a IF IT IS NOT PRESENT IN GIVEN LIST THEN RETURN TRUE.
'''

# BITWISE OPERATOR
'''
X=00000110
Y=00001000

1.AND OPERATOR(&)- X&Y=00000000(IT RETURN 1 IF BOTH OF THEM HAVE 1 AT SAME INDEX OTHERWISE 0)
2.OR OPERATOR(|)-  X|Y=00001110(IT RETURN 1 IF ANY OF THEM OR BOTH HAVE 1 AT SAME INDEX OTHERWISE 0)
3.XOR OPERATOR(^)- X^Y=00001110(IT RETURN 1 IF ONLY ANY OF THEM HAVE 1 AT SAME INDEX OTHERWISE 0)
4.COMPLEMENT(~)- ~(X)=11111001(IT RETURN REVERSE VALUE)
5.LEFT SHIFT(<<)- X<<1=00001100
6.RIGHT SHIFT(>>)- x>>1=00000011
'''


# OPERATION BETWEEN TWO NUMBER

'''
a=10
b=25
print("Sum of two number =",a+b)
print("Difference of two number =",a-b)
print("Multiply of two number =",a*b)
print("Division of two number =",a/b)
print("Power of a =",a**2)
print("Power of b=",b**2)
print("Floor division of b and a = ",b//a)
'''


# AREA AND PERIMETER OF RECTANGLE

'''
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area of rectangle =",l*b)
print("Perimeter of rectangle =",2*(l+b))
'''

# AREA AND PERIMETER OF A SQUARE

'''
s=int(input("Enter side of square:"))
print("Area of square =",s*s)
print("Perimeter of square =",4*s)
'''


# AREA AND PERIMETER OF A CIRCLE
'''
r=int(input("Enter radius of a circle:"))
pi=3.14
print("Area of a circle =",pi*r**2)
print("Perimeter of a circle =",2*pi*r)
'''


# FOR LOOP IN PYTHON

# for i in range(Start,End+1,Step value)
# for i ing range(Start,End+1)
'''
for i in range(1,11):
    print(i)
for j in range(10,0,-1):
    print(j)
else:
    print("program terminated")
'''


# WHILE LOOP IN PYTHON


# Q1. First 10 natural number
'''
i=1
while(i<=10):
    print(i)
    i+=1
'''



'''
n=int(input("Enter the term which Natural Number are required"))
i=1
while(i<=n):
    print(i)
    i+=1
'''


# Q2.PROGRAM TO PRINT NATURAL NUMBER IN REVERSE ORDER

'''
n=int(input("Enter the number till which natural number should print:"))
while(n>=1):
    print(n)
    n-=1
'''


# Q3. WRITE A PROGRAM TO FIND SUM OF NUMBERS TILL N
'''
n=int(input("Enter the number"))
sum=0
for i in range(n):
    sum+=i
print("Sum of Number till",n, "=",sum)    
'''

# Q4.Sum of Square Till n

'''
n=int(input("Enter the number:"))
sum=0
for i in range(0,n):
    sum+=i**2
print("Sum =",sum)
'''


# Q5.Sum of Cube till n

'''
n=int(input("Enter the value of n:"))
sum=0
for i in range(0,n):
    sum+=i**3
print("Sum=",sum)
'''

# Q6. PROGRAM TO PRINT EVEN NUMBER BETWEEN 0 TO N AND SUM TILL N


'''
n=int(input("Enter the value of n"))
sum=0
for i in range(0,n,2):
    print(i)
    sum+=i 
print("Sum =",sum)'''


# Q7.PROGRAM TO PRINT ODD NUMBER BETWEEN 1 TO N

'''
n=int(input("Enter the value of n:"))
SUM=0
for i in range(1,n,2):
    print(i)
    SUM+=i
print("Sum =",SUM)
'''

# Q8.  PROGRAM TO FIND SUM OF DIGIT 

'''
n=int(input("Enter the number:"))
sum=0
while(n!=0):
    a=n%10
    sum+=a
    n=n//10
print("Sum=",sum)
'''
# Q7. PROGRAM TO FIND PRODUCT OF A GIVEN DIGIT

'''
n=int(input("Enter the number:"))
product=1
while(n>0):
    a=n%10
    product=product*a
    n=n//10
print("The Product of digit of a Number =",product)
'''



# Q8. PROGRAM TO FIND SUM OF EVEN DIGITS AND PRODUCT OF ODD DIGITS

'''
n=int(input("Enter the number:"))
sum=0
product=1
while(n>0):
    a=n%10
    if(a%2==0):
        sum+=a 
    else:
        product*=a
    n=n//10
print("Sum of even digit of a number =",sum)
print("Product of odd digit of a number =",product)
'''

# Q9. PROGRAM TO FIND SUM OF SQUARE AND SUM OF CUBE OF DIGIT OF A NUMBER

'''
n=int(input("Enter the number:"))
sum1=0
sum2=0
while(n>0):
    a=n%10
    sum1+=a**2
    sum2+=a**3
    n=n//10
print("SUM OF SQUARE OF A DIGIT=",sum1)
print("SUM OF CUBE OF A DIGIT=",sum2)
'''


# Q10. PROGRAM TO CHECK THAT NUMBER IS ARMSTRONG OR NOT

'''
n=int(input("Enter the number:"))
sum=0
i=n
while(n>0):
    a=n%10
    sum+=a**3
    n=n//10
if(sum==i):
    print("The given number is a Armstrong Number.")
else:
    print("The given number is not a Armstrong Number.")
'''



# Q11. PROGRAM TO FIND REVERSE OF A NUMBER


'''
n=int(input('Enter the number:'))
sum=0
while(n>0):
    a=n%10
    sum=sum*10+a
    n=n//10
print("REVERSE OF A GIVEN NUMBER IS",sum)
'''



# Q12. PROGRAM TO CHECK THAT A NUMBER IS PALLINDROME OR NOT

'''
n=int(input("Enter the number:"))
sum=0
i=n
while(n>0):
    a=n%10
    sum=sum*10+a
    n=n//10
if(sum==i):
    print("The given number is Pallindrome.")
else:
    print("The given number is not a Pallindrome")
'''


# Q13. PROGRAM TO FIND FACTORS OF A NUMBER AND COUNT THEM

'''
n=int(input("Enter the number:"))
i=1
c=0
while(i<=n):
    if(n%i==0):
        print(i)
        c+=1
    i+=1
print("Total number of factors are=",c)
'''



# Q14. FACTORIAL OF A NUMBER

'''
n=int(input("Enter the number:"))
fact=1
while(n>0):
   fact=fact*n
   n=n-1
print("The factorial of a number is ",fact)
''' 




# Q15. FIBBONACCI SERIES

'''
n=int(input("Enter the number of term till which fiboncci series will print:"))

f1=0
f2=1
i=1
print("Fibbonacci Series Till" ,n,"th term is:")
print(f1)
print(f2)
while(i<n-1):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3
    i=i+1
'''
