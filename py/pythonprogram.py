# Q1.

# import sys
# print(sys.argv)

# Q2.Matrix Multiplication

# M1=[[1 ,2],[3 ,4],[5 ,6]]
# M2=[[2,3,6],[4,5,8]]
# ans=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(M1)):
#     for j in range(len(M2[0])):
#         for k in range(len(M2)):
#             ans[i][j]+=M1[i][k]*M2[k][j]
# print("Output Matrix:")
# for r in ans:
#     print(r) 

# Q3.GCD of two numbers

# def gcd(a, b):
#     if a==0:
#         return b
#     return gcd(b%a,a)
      
# x = int(input("Enter first number = "))
# y = int(input("Enter second number = ")) 
# if(gcd(x, y)):
#     print('GCD of', x, 'and', y, '=', gcd(x,y))
# else:
#     print('GCD not found')



# Q4.Most Frequent Word in a text file.


# n=int(input("Enter range "))
# prime=[]
# for i in range(n+1):
#     prime.append(i)
# prime[0]=0
# prime[1]=0
# p=2
# while p*p<=n:
#     if(p!=0):
#         for i in range(2*p,n+1,p):
#             prime[i]=0
#     p=p+1
# print("The prime numbers are ")
# for i in prime:
#     if(i!=0):
#         print(i)



# 4
# file = open("text.txt", "r")
# frequent_word = ""
# max = 0
# words = []
# for line in file:
#     line_word = line.lower().replace(',', '').replace('.', '').split(" ")
#     for w in line_word:
#         words.append(w)
# for i in range(0, len(words)):
#     count = 1
#     for j in range(i + 1, len(words)):
#         if words[i] == words[j]:
#             count = count + 1

#     if count > max:
#         max = count
#         frequent_word = words[i]

# print("Most repeated word: " + frequent_word)
# print("Frequency: " + str(max))

# file.close()



# Merge Sort


# Merge part

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
arr = [12, 11, 13, 5, 6, 7]
print("Given array is")
for i in range(len(arr)):
   print(arr[i], end=" ")
mergeSort(arr)
print("\nSorted array is ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print()