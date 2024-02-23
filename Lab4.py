import math
a=int(input())
b=math.radians(a)
c=round(b, 6)
print(c)
# -----
import math
a=int(input())
b=int(input())
c=int(input())
d=(((c+b)/2)*a)
print(d)
# -----
import math
a=int(input())
b=int(input())
c=(a*b**2)/(4*math.tan(math.pi/a))
print(c)
# -----
import math
a=int(input())
b=int(input())
c=a*b
print(c)
# -----
def abc(n):
    for i in range(int(n)):
        yield i**2
n=input()
Generator=abc(n)
for i in Generator:
    print(i)
# -----
def abc(n):
    for i in range(int(n)):
        if (i%2==0):
            yield i
n=input()
generator=abc(n)
for i in generator:
    print(i,end=",")
# -----
def abc(n):
    for i in range(int (n)):
        if((i%3)==0)or((i%4)==0):
            yield i
n=input()
generator=abc(n)
for i in generator:
    print(i)
# -----
def abc(n,m):
    for i in range(int(n), int(m)):
        yield i**2
n=input()
m=input()
generator=abc(n,m)
for i in generator:
    print(i)
# -----
def abc(n):
    for i in reversed(range(int(n))):
        yield i
n=input()
generator=abc(n)
for i in generator:
    print((i))
# -----
import datetime
now=datetime.datetime.now()
a=(now.day-5)
print(now.year,"-",now.month,"-",a)
# -----
import datetime
now=datetime.datetime.now()
a=(now.day-1)
b=(now.day+1)
print(a,"-",now.day,"-",b)
# -----
import datetime
now=datetime.datetime.now()
now_1=now.replace(microsecond=0)
print(now_1)
# -----
import datetime
format = "%Y-%m-%d %H:%M:%S"
a_str = input()
b_str = input()
a = datetime.datetime.strptime(a_str, format)
b = datetime.datetime.strptime(b_str, format)
c = b - a
d = c.total_seconds()
print(d)