1.#A program to segereate odd and even number
Lt = [10,501,22,37,100,999,87,351]
lt_even = []
lt_odd = []
for i in Lt:
    if i % 2 == 0:
        lt_even.append(i)
    else:
        lt_odd.append(i)
print(lt_even)
print(lt_odd)

#2.In a python list[10,501,22,37,100,999,87,35]count all prime number 
#and create a new python list in which it will have prime number in it.
Lt = [10,501,22,37,100,999,87,351,7]
Lt_prime = []
for i in Lt:
    if i<= 0:
        print("Negative number")
    elif i == 1:
        print("1")
    elif i == 2:
        print("2")
    else:
        c = 0
        for j in range(1,i+1):
            if i%j == 0:
                c = c+1
        if c <= 2:
            Lt_prime.append(i)
            print(i," : Prime")
        else:
            print(i," : Not Prime")
print(Lt_prime)       
Num = int(input("Enter a Number : "))
cache = []
strs = str(Num)
print(cache)

#3.Find how many number are there in agiven python list which are happy numbers
a=[10,501,22,37,100,999,87,351]
b=[]
def happy(a):
    for i in range(len(a)):
        sum=a(i)
        while sum!=1 and sum!=4:
            tempsum=0
            for digit in str(sum):
                sum=tempsum
                if sum==1:
                    b.append(a[i])
                    return b
                print(happy(a))

#4.python program to find sum of the first and last digit of an integer
number = 3456
number = str(number)
first_digit = int(number[0])
last_digit = int(number[-1])
addition = first_digit + last_digit
print("Addition of first and last digit of the number is:", addition)
#5.minimum and maximum number of mangoes in each student bag.
def man(n,m):
    res=1
    if m>n-m:
        m=n-m
        for i in range(0,m):
         res*=(n-1)
        res/=(i+1)
        return res
    def calculate(n,m):
        if n<m:
            return 0
        ways=man(m+n-1,m-1)
        return int (ways)
    if__name__== main
    n=7
    m=5
    result=calculate(n,m)
    print(result)
    
#6. duplicates in three list
Lt_1 =[1,2,9,64,345]
Lt_2 = [64,9,78,342,345,35]
Lt_3 = [35,64,9,345,5,3,3,7]
cache = []
for j in Lt_1:
    if j in Lt_2 and Lt_3:
        cache.append(j)
print(cache)

#7. first non repeating element
Lt = [1,2,7,5,2,46,1]
c =[]
for i in range(0,len(Lt)):
    if Lt[i] not in Lt[i+1:]+Lt[:i]:
        c.append(Lt[i])
print("First Non-Reprating elememt : ",c[0])

#8.Find the minimum element in a rated and sorted list
list1 = [21, 67, 3, 98]
list1.sort()
print("Smallest element is:", list1[0])

#9.Find the triplet in the list whose sum is equal to the given value
from itertools import combinations
def findTriplets(lst, key):
 def valid(val):
  return sum(val) == key

 return list(filter(valid, list(combinations(lst, 3))))
lst = [10,20,30,9]
print(findTriplets(lst, 59))

#10. python code to find if there is a sublist with sum equals to zero
Lt = [4,2,-3,1,6]
for i in range(0,len(Lt)):
    for j in Lt[i+1:]:
        if Lt[i]+j == 0:
            print("The sublist is : ",Lt[i],j)
