# # Break , Try , Except ,Continue, Pass

# In[ ]:


#break keyword escapes the loop, regardless of the iteration number. 
#Once break executes, the program will continue to execute after the loop.


# In[207]:


numbers = [0, 254, 2, -1, 3]
 
for num in numbers:
   if (num < 0):
    print("Negative number detected!")
    break
   print(num)



#Come out of the loop if a vowel is detected
d=['S','h','u','b','h','a','m']
for i in d:
    if (i=='u'):
        print('Coming out as vowel is detected')
        break
    print(i)

#Break Statement is coming out of loop however continue statement comes of iteration 


# In[21]:


##Come out of the loop if a vowel is detected
d=['S','h','u','b','h','a','m']
for i in d:
    if ((i=='u') or (i=='a')):
        print('Coming out as vowel is detected')
        continue
    print(i)
    
#Break Statement is coming out of loop however continue statement comes of iteration 


# In[33]:


#Pass statement does nothing
d=['S','h','u','b','h','a','m']
for i in d:
    if ((i=='u') or (i=='a')):
        print('pass executed')
        pass
    print(i)


# # Dictionary

# In[41]:


# Write a Python program to count the number of characters (character frequency) in a string.
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

d={}
s=input('Enter a string: ')
for i in s:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
print(d)
print(d.keys())
print(d.values())


# In[158]:


# Write a Python script to sort (ascending and descending) a dictionary by value
new={'a':4,'b':1,'c':3,'d':5,'e':2}
sorted(new.items())

dict(sorted(new.items(),key=lambda x:x[1]))


# In[ ]:


# Write a Python script to add a key to a dictionary
# Sample Dictionary : {0: 10, 1: 20}
# # Expected Result : {0: 10, 1: 20, 2: 30}


# In[83]:


a={0: 10, 1: 20}
a[2]='30'
print(a)


# In[ ]:


# Write a Python script to concatenate following dictionaries to create a new one.


# In[93]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)   


# In[ ]:


# Write a Python script to check whether a given key already exists in a dictionary. 


# In[110]:


new={1:'e',4:'y',7:'p',9:'t'}
def present(x):
    if x in new:
        print('Key is present')
    else:
        print('Key is not present')
        
        
present(2)
present(4)


# In[112]:


# Write a Python program to iterate over dictionaries using for loops
d={1:'e',4:'y',7:'p',9:'t'}
k={3:'g',8:'h'}
for i in d,k:
    print(i)


# In[151]:


# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n=int(input("Enter the number: "))
k={}

for i in range(1,n+1):
    k[i]=i*i

print(k)
    


# In[154]:


#  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) 
# and the values are square of keys. 


# In[153]:


k={}

for i in range(1,16):
    k[i]=i*i

print(k)


# In[157]:


# Write a Python script to merge two Python dictionaries.
f={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
t={7: 49, 8: 64, 9: 81, 10: 100}
f.update(t)
print(f)


# In[173]:


# Write a Python program to sum all the items in a dictionary
t={7: 49, 8: 64, 9: 81, 10: 100}
# print(sum(t.values()))
# print(sum(t.keys()))

ret=0
for i in t:
    ret=ret+t[i]
print(ret)
    


# In[171]:


# Write a Python program to multiply all the items in a dictionary.
t={7: 49, 8: 64, 9: 81, 10: 100}
res=1

for i in t:
    res=res*t[i]
print(res)


# In[176]:


# Write a Python program to remove a key from a dictionary.
t={7: 49, 8: 64, 9: 81, 10: 100}
t.pop(7)
print(t)


# In[188]:


# Write a Python program to map two lists into a dictionary. 
a=[1,2,3,4]
b=[1,4,9,16]
print(list(zip(a,b)))
print(dict(zip(a,b)))


# In[197]:


# Write a Python program to sort a dictionary by key.
t={8: 49, 7: 64, 10: 81, 6: 100}
t.items()
a=sorted(t.items())
print(a)
print(dict(a))


# In[201]:


# Write a Python program to get the maximum and minimum value in a dictionary.
print(max(t.values()))
print(min(t.values()))