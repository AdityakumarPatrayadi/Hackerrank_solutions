Problem Statement: Let’s define a Beautiful Function F(x) in such a way: Add 1 to the value of x, if the result of addition contains any trailing zeros then remove them all. 
 
Example: 
F(11) = 12 
F(19) = 2 (20 –> 2) 
F(99) = 1(100 –> 10 –> 1) 
 
Let’s define a number to be reachable from x , if we can apply Beautiful Function some number of times (possibly zero) to x and get that number as result 
Ex. 102 can be reachable from 1099 as F(F(1099)) = F(101) = 102 
You are given a number N . Calculate how many numbers are reachable from N. 

 

Input Format: 
The first line contains an integer N. denoting the given number. 
 

Constrains: 1 <= N <= 10^9 

Solution:

def F(x):
  y = x // 10
  x = x % 10
  if x > 1:
    x -= 1
    if x > 1:
      if y != 0:
        print(str(y)+str(x-1))
      else:
        print(str(x-1))
    else:
      if y != 0:
        print(str(y)+ "99")
      else:
        print("99")
  else:
    print("9")
