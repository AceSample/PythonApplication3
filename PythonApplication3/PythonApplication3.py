'''from math import pi
print(pi)'''

from typing import cast


a=7
b=4
'''if a>7:
    print(1)
elif 0>a:
    print(0)
else:
    print(a)'''
'''while a<=10:
    print(a)
    a=a+1'''
'''for i in range(11):
    print(i)'''

'''def sum(a,b):
    a=5
    return a+b
print (sum(a,b))

def exp(num,e):
    return pow(num,e)
print(exp(3,4))'''

'''def min(a,b):
    print(a - b)
min(4,2)'''

'''def FizzBuzz(min,max):
    for i in range(min,max+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)

FizzBuzz(1,50)'''

'''def is_pallindrome():
    a=input()
    return a==a[::-1]
s=is_pallindrome()
print(s)'''

def feb(num):
    a,b,c=0,1,0
    count=0
    print(a)
    while count<num-1:
        c=a+b
        print(b)
        a,b=b,c
        count=count+1

'''def diff(a,b):
    a%=360
    b%=360
    if abs(a-b)>180:
         return 360-abs(a-b)
    else:
         return abs(a-b)
print(diff(-60,-850))'''

'''def rec_fib(n):
     if n==0:
        return 0
     if n==1:
        return 1
     return rec_fib(n-1)+rec_fib(n-2)
print(rec_fib(10))'''

'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(3))'''

'''a=[9,8,7,6,5,4,3,2,1,0]
def buble_sort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
    return list
print(buble_sort(a))'''

with open(".\bb.txt", "w") as f:
    f.write("fffffffff")
