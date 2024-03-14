# '''
# a=["ram",10,1234,"Abahy","Akash"]
# print(a)
# a[2]="Atharava"
# print(a)
# del a[1]
# print(a)
# '''
# '''
# a=['Atharva','Akash','Gaurav','Anish']
# for i in range(len(a)):
#     print(a[i])
# '''

# '''
# A=['AKASH','ATHARAVA','GAURAV',10,4557]
# # TO FIND LENGTH OF LIST WE USE 'len(LIST NAME)' FUNCTION
# print("LENGTH OF A LIST IS",len(A))'''


# B=[4511,12445,320,20,478854,10]
# # TO FIND MAX VALUE IN A LIEST WE USE "max(LIST_NAME)" FUNCTION
# print("MAXIMUM OF A STRING IS",max(B))
# # TO FIND MINIMUM VALUE IN A LIST WE USE "min(LIST_NAME)" FUNCTION
# print("MINIMUM VALUYE OF A LIST IS",min(B))

# C=[120,320,4511,12445,478854]
# # TO COMPARE TWO LIST WE USE 'cmp(LIST1,LIST2)' FUNCTION
# # print(cmp(B,C))

# #  TO ADD A VALUE AT LAST IN THE LIST WE USE "list_name.apppend(ELEMENT)" FUNCTION
# B.append(2)
# print(B)

# # TO FIND FREQUENCY OF A LIST MEANS COUNT HOW MANY TIMES A ELEMENT OCCUR IN LIST WE USE "listr_name.count(ELEMENT)" FUNCTION
# d=['RAM','RAM','ATHARAVA','AKASH']
# X=d.count("RAM")
# print("Frequency is",X)

# # TO FIND INDEX OF A PARTICULAR ELEMENT OF A LSIT WE USE "list_name.index(ELEMENT)" FUNCTION
# y=d.index("ATHARAVA")
# print("Index =",y)

# # TO INSERT A ELEMENT IN A LIST WE USE "list_name.insert(INDEX,ELEMENT)" FUNCTION
# d.insert(2,'GAURAV')
# print(d)

# # TO REMOVE A ELEMENT FROM A LIST WE USE "list_name.remove(ELEMENT)" FUNCTION
# d.remove('RAM')
# print(d)

# #  TO REVERSE A LIST WE USE "list_name.reverse()" FUNCTION
# print(d.reverse()) 
# # IT CREATE A BLANK LIST
# a=[] 
# for i in range(len(d)):
#     x=int(input("Enter list element:"))
#     a.append(x)
# print("Original list is" ,a)
# a.reverse()
# print("List after reverse",a)

# # TO REMVOE LAST ELEMENT FROM THE LIST WE USE "list_name.pop()" FUNCTION
# print(d.pop())
# print(d)

# #  TO SORT A LIST IN ASCENDIJNG AND DESCENDING ORDER WE USE "list_name.sort()" FUNCTIION
# a=[] 
# for i in range(len(B)):
#     x=input("Enter the list element:")
#     a.append(x)
# print(a)
# a.sort()
# print(a)
# # To sort a list in Descending order 
# a.sort(reverse="False")
# print(a)



# q=(11,112,13,440)
# print(sorted(q))
# a="AB","CS","CD","SL"
# print(sorted(a))



def greeting(name):
    print("Name-",name)
