"""
Challenge for the Week of 2019/10/21
-------------------------------------
Given input integer n, calculate the Fibonacci sequence up to index n, lists 0 indexes of course.
"""

x = int(input("Index: "))  # Not Counted
a=[0,1]  # Counted
while(len(a)<=x):z=a[-2]+a[-1];a.append(z)  # Counted
print(z)  # Not Counted
