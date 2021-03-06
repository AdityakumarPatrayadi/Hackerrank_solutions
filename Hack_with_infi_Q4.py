'''
Question:

Slowest Key Press 

Problem Statement 
Alex wants to be a faster typist and is taking a typing test to find out which key takes the longest time to press. 
Given the results of the test, determine which key takes the longest to press. 
For example, given keyTimes =[[0, 2], [1, 5], [0, 9], [2, 15]]. Interpret each keyTimes[i][0] as an encoded character in the range ascii[a-z] where a = 0, b = 1,...z = 25. 
The second element, represents the time the key is pressed since the start of the test. 
In the example, keys pressed, in order are abac at times 2, 5, 9, 15. From the start time, it took 2 - 0 = 2 to press the first key, 5 - 2 = 3 to press the second, and so on. 
The longest time it took to press a key was key 2, or 'c', at 15 - 9 = 6. 

Function Description 
Complete the function slowestKey in the editor below. The function must return a character, the slowest key that Alex presses. 
slowestKey has the following parameter(s): 
keyTimes[keyTimes[O],... keyTimes[n-1]]: an array of two integers: The character Alex pressed (encoded) and the time at which it was pressed 

Constraints 
• 1 <= n <= 10^5 
• 0 <= keyTimes[i][0] <= 25 (0 <= i <= n) 
• 1 <= keyTimes[i][1] <= 10^8 (0 <= i <= n) 
• It is guaranteed that there will only be one key with the worst time. Input Format For Custom Testing 
'''
#Answer:

n = int(input())
keys = []
time_taken = []
for i in range(n):
  k , t = map(int , input().split())
  keys.append(k)
  time_taken.append(t)
for i in range(n-1):
  time_taken[i+1] -= time_taken[i]
x = keys[time_taken.index(max(time_taken))]
x += 97
chr(x)
