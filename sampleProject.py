# Code By Bismaya 2024
from datetime import datetime as dt
print("Code Executed Date: ", dt.now(), "Author: Duke Bismaya")


#TODO: Method 1
def ev_recur1(num=0):
    if num>100: return
    print(num)
    ev_recur1(num+2)
#ev_recur1() #NOTE: Unhash to execute ev_recur1

#TODO: Method 2
def ev_recur2(num=0, end=100):
    if num>end: return []
    return [num]+ev_recur2(num+2, end)
#print(*ev_recur2()) #NOTE: Unhash to execute ev_recur2

#TODO: Method 3
def ev_recur3(num=0, end=100):
    if num>end: return
    print(num)
    return ev_recur3(num+2, end)
#ev_recur3() #NOTE: Unhash to execute ev_recur3

#TODO: Method 4
ev_recur4 = (lambda f: (lambda x: f(f, x)))(lambda self, x: None if x>100 else (print(x),self(self, x+2)))
#ev_recur4(0) #NOTE: Unhash to execute the code


#TODO: Method 5
def ev_recur5(num=0):
    if num>100: return
    yield num
    yield from ev_recur5(num+2)

#NOTE: Unhash the following two code lines to execute the code
#for i in ev_recur5():
#    print(i)

#TODO: Method 6
def ev_recur6(num=0, even_numbers=list()):
    if num>100: return even_numbers
    return ev_recur6(num+2, even_numbers+[num])

#print(ev_recur6()) #NOTE: Unhash to execute ev_recur6

#TODO: Method 7
def ev_recur7(num=0):
    if num>100: return []
    return [num] + ev_recur7(num+2)
print(*[i for i in ev_recur7()]) #NOTE: Unhash to execute ev_recur7

#TODO: Method 8
mem=dict()
def ev_recur8(num=0):
    if num>100: return []
    if num in mem: return mem[num]
    mem[num] = [num] + ev_recur8(num+2)
    return mem[num]

#print(*ev_recur8()) #NOTE: Unhash to execute ev_recur8