#1.1 Write a Python Program to implement your own myreduce() function which works exactly
#like Python's built-in function reduce()
def myreduce(li):
    sum = 0
    for i in li: 
        sum = sum + i 
    return ("Sum of all the numbers in the list = ", sum)        
input_list = [1,2,3,4,5] 
y = myreduce (input_list)  
y            

#1.2 Write a Python program to implement your own myfilter() function which works exactly like
#Python's built-in function filter()
def myfilter(li):
    return (i for i in li if i < 0)
input_list = [-5,-4,-3,0,-2,4,6,8,9,10,-11]
z = list(myfilter(input_list))
print ("Output of myfilter function is: ", z)

#2. Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

x = [i for i in "ACADGILD"]
print (x) #['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

z =[]
n=1
for k in range (4):
    t = [(i*n) for i in "xyz"]
    z = z + t
    n=n+1    
print (z) #['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

n=1
i=0
z= []
for k in range (4):
    t = [(i*n) for i in "xyz"]
    z = z + t
    z.sort()
    n=n+1    
print (z) #['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

l = []
for j in range (2,5): 
    m = [[i] for i in range (j,j+3)]
    l = l + m
print (l) #[[2], [3], [4], [3], [4], [5], [4], [5], [6]]

l = []
for j in range (2,6): 
    m = [[i for i in range (j,j+4)]]
    l = l + m
print (l) #[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 

def takeSecond(elem):
    return elem[1]
p = [(i,j) for i in range (1,4) for j in range (1,4)]
p.sort(key = takeSecond)
print(p) # [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

#3. Implement a function longestWord() that takes a list of words and returns the longest one.
def longestWord(string):
     y= [(len(word), word) for word in string]
     y.sort(reverse=True)
     a = y[0]
     print ("Longest word in the list is ", a[1])     
input_words = input ("Enter words of differing lengths: ").split()
t = longestWord(input_words)
t
