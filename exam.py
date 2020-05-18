str1 ="#".join(str(i)for i in range(10))
print(str1)
str1 ="#" + str((str(i)for i in range(10)))
print(str1)
str2 = "#" +str([1,"2"])
print(str2)
print("\n".join([f"{j}"+str([f"{j}"+str(i)for i in range(10)]) for j in ["#","*","&"]]))
p = "\n".join([f"{j}"+str([f"{j}"+str(i)for i in range(10)]) for j in ["#","*","&"]])
print(len(p))
print("\n".join([f"{j}"+str([f"{j}"+str(i)for i in range(10)]) for j in ["#","*","&"]]))
dict2 = {str(["#","*","&"]):[i for i in range(10)]}


x = str([1,2,3])
print([i for i in x])
print(len(x))
print('*'.join(x))

for i in range(20):
    if i == 19:
        print("almost done")

def abc(h=5,*args):

    print(h)
    print(args)
abc(6,7,8,9)
b = [4,5,6]
c = [4,5,6]
def add(**k):
    # for u,y in k.items():
    #     print(u,y)
    # print(a)
    print(k['a'])

print(b+c)
add(a=6,b=7,c=8)
z= {"a":6,"b":7,"c":8}
def add2(a,b,c):
    print(a)
    print(b)
    print(c)

add2(**z)
# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
#
#
# args = ("Geeks", "for", "Geeks")
# myFun(*args)
#
# kwargs = {"a": "Geeks", "b": "for", "c": "Geeks"}
# myFun(**kwargs)
li = [1,2,3,2,3,4,5,5,5,6]
li2 =[]
# li = set(li)
# # print(li)
[li2.append(i) for i in li if i not in li2]
print(li2)

for j in range (5):
     a= []
     for i in range(5):
         a.append(0)
     a[j] = 1
     print(a)

for j in range (3):
     a= []
     for i in range(5):
         a.append("v")
     a[j] = "x"
     a[-j-1] = "x"
     print(a)

import math

from math import sqrt
dir(sqrt)
print(dir(math))
import math as m
def b():
    return 7
def t():
    b()
print(t())

items = [1,2,3,4,5]
def double(arg):
    return arg*2
for item in items:
   print(double(item))

y = map(lambda x:x*2,[1,2,3,4,5])
print(list(y))

def mul(arg):
    return lambda x:x*arg
duplicate = mul(2)
triple = mul(3)
print(duplicate(55))

funcs = [duplicate,triple]
for i in range(5):
    value=list(map(lambda x:x(i),funcs))
    print(value)

y=[1,2,3,4,5,6,7,44,8,9,56,45,44]
g=list(filter(lambda x:x<5,y))
print(g)

from functools import reduce
f= reduce(lambda x,y:x*y,[1,2,3,4])
print(f)

ab = [1,2,3,4]
cd = ['a','b','c','d']
zipped = zip(ab,cd)
print(list(zipped))
print(zipped)

g = [1,2,3,4,5,6,7,8]
y=[x*2 if x%2 else x*3 if x%3 else x for x in g ]
print(y)

matrix = [[i*j for i in range(5)]for j in range(6)]
print(matrix)
matrix2 = [x for i in matrix for x in i]
print(matrix2)

def reverse(str):
    return reduce(lambda x,y:y+x,str)
print(reverse("yehuda"))

def definer(function):
    return function("arg")
print(definer(lambda x:x*2))

def de(arg):
    return arg

def nested(arg):
    return arg

print(nested(de))


dict4 = {5:6}
for k,y in dict4.items():
    print(k,y)

dict5 = {"#" :lambda x : "#"+str(x),"x*2":lambda x:x*2,"x/2":lambda x:x/2}
print("\n".join([k +str([y(i) for i in range(10)])for k,y in dict5.items()]))

f = {"x"+g: "x" + g for g in ["*5","/2","**2","%3","+3","-1"]}
# [print(k + ": " + str([eval(v) for x in range(10)])) for k,v in f.items()]
for k,y in f.items():
    print(k,y)

fg ={x:x for x in range(10)}
for k,y in fg.items():
    print(k,y)

d = {m: [eval(m) for x in range(10)] for m in ['x*5','x/2','x**2','x%3','x+3','x-1']}
for i in d.keys(): print(i+':',d[i])

yth = [1,2,3,3,3,4,5,2,2,6,6,4,3,]
yth2 = set(yth)
print(yth2)
#
# times_of_dialog = input("how many times do you want this dialog to continue ? ")
# for dialog in range(int(times_of_dialog)):
#     first_input = input("please enter a sentance : ")
#     new_first_input = " ".join(first_input.split()[:-1]) + "?"
#     print(new_first_input)

math = [["math1",'math2'],["math3",'math4']]
print(math[0][1])
ag =[]
for i in range(5):
    af = []
    for g in range(5):
       af.append("O")
    af[i]="X"
    af[-i-1] ='X'
    ag.append(str(af))

print("\n".join(ag))

def wrapper(function):
    def inner(arg):
        print("this prints before func")
        function(arg)
        print("this prints after func")
    return inner
@wrapper
def printer(arg):
    print("this inner func prints"+arg)

printer("yehuda")

str6 = 'h,e,l,o,p,y,t,h,o,n,7.6'
str7 = str6[::2]
str8 = str7[:2]+str7[2]*2+" ".join(str7[3:5])+str7[5:10]+str(int(str7[10]+str7[11])/2)
str9 = str6.split(",")
print(str9[-1::-1])