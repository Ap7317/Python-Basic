# D={"john":40,"peter":45}
# print("john"in D)


# class Name:
#     def __init__(self,name):
#         self.name=name
#     def show_name(name):
#         print(name)
    
# obj1=Name('harsh')
# obj2=Name('anurag')
# obj1.show_name('ABES')


# d={0:'a',1:'b',2:'c'}
# for i in d:
#     print( _______ )


# a=[5,5,6,7,7,7]
# b=set(a)
# def test(lst):
#     if lst in b:
#         return 1
#     else:
#         return 0
# for i in filter(test,a):
#     print(i,end=" ")


# print(16%15//16)
# print(4/(3*(2-1)))
# print(4/3*(2-1))


# print(3*1**3)

# d1={"john":40,"peter":45}
# d2={"jonh":466,"peter":45}
# print(d1==d2)



# a={1:"A",1:"B",3:"C"}
# print(a.get(1,3))


# a=True
# b=False
# c=False
# if not a or b:
#     print("a")
# elif not a or not b and c:
#     print('b')
# elif not a or b or not b and a:
#     print('c')
# else:
#     print('d')
    

# print(
# "".join("Which language do u like".split()))


# ran1=lambda x:bool(x**2-2)
# numbers =[n for n in range(7)]
# print(numbers)
# n=list()
# for i in numbers:
#     if ran1(i):
#         continue
#     else:
#         break


# print(3^4)


# x=['ab','cd']
# for i in x:
#     i.upper()
# print(x)



# class abc:
#     def summ(self,a,b):
#         print(a+b)
#     def sum(self,a,b,c):
#         print(a+b+c)
# a=abc()
# a.sum(1,2,3)

# x=1
# print("Value of b",b)

# def f(values):
#     values[0]=29
# v=[1,2,3]
# f(v)
# print(v)



# def fun(n):
#     if(n>100):
#         return n-5
#     return fun(fun(n+11));
#     print(fun(45))


# foo_list=["i","am","new","to","the","python"]
# print(foo_list[-2][-1])


# x='abcd'
# for i in range(len(x)):
#     print(i,end=" ")


# def My_Name(insert):
#     return insert+(insert)*45
# My_Name(17)
# print(insert)


# print("xyyzxyzxzxyy".count('yy',1))


# m=[[x,x+1,x+2] for x in range(0,3)]
# print(m)


# print(float(22//3+3/3))

# print(not(10<20)and not(10>30))

# class Person:
#     def __init__(self,name,age=0):
#         self.name=name
#         self.__age=age
#     def display(self):
#         print(self.__age)


# y=6
# z=lambda x:x*y
# print(z(8))


# def cube(x):
#     return x*x*x
# x=cube(3)
# print(x)


# def maximum(x,y):
#     if x>y:
#         return x
#     elif x==y:
#         return 'The number are equal'
#     else:
#         return y
# print(maximum(2,3))



# def say(message,times=1):
#     print(message*times)
# say('Hello')
# say('World',5)


# def printmax(a,b):
#     if a>b:
#         print(a,'is maximum')
#     elif a==b:
#         print(a,'is equal to',b)
#     else:
#         print(b,'is maximum')
# printmax(3,4)


# print("a"+"bc")
# print("abcd"[2:])


# str1='hello'
# str2=','
# str3='world'
# print(str1[-1:])


# print(r"\nhello")
# print('new''line')
# print('x/97\x98')



# str1='helloworld'
# print(str1[::-1])
# print(0xA+0xB+0xC)


# list1=[.5*x for x in range(0,4)]
# print(list1)


# a=(1,2,3)
# b=('A','B','C')
# c=zip(a,b)
# print(c)

# str1='5432112345'
# str2=str1*3
# print(str2)
# s=str2[5:25:3]
# print(s)

# names=['Amir','Bear','Carlton','Daman']
# print(names[-1][-1])

# d={"peter":45,"john":40}
# print(d["susan"])



# a=0
# b=2
# c=3
# x=c or a
# print(x)

# n=int(input("Enter the number"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()


# tupl=()
# l=list(tupl)
# for i in range(5):
#     n=input("Enter the value")
#     l.append(n)
# print(l)
# tupl=tuple(l)
# print(tupl)



# def ToH(n,A,B,C):
#     if(n==0):
#         return 
#     ToH(n-1,A,C,B)
#     print("Move disk from rod ",A," to rod ",C)
#     ToH(n-1,B,A,C)
# ToH(3,"BEG","AUX","END")






M1=[[1 ,2],[3 ,4],[5 ,6]]
M2=[[2,3,6],[4,5,8]]
ans=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(M1)):
    for j in range(len(M2[0])):
        for k in range(len(M2)):
            ans[i][j]+=M1[i][k]*M2[k][j]
print("Output Matrix:")
for r in ans:
    print(r)    