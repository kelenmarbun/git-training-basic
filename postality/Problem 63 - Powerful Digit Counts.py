#!/usr/bin/env python
# coding: utf-8

# # Problem 62 - Cubic Permutations
# ---
# 
# ## Problem Description: [Click here to read the full description of this problem](https://projecteuler.net/problem=63)
# ---
# 
# Credits: http://radiusofcircle.blogspot.com
# 

# In[1]:


# counter to count the number of instances
counter = 0

# for loop to loop from 1 to 9
for i in range(1, 10):
    power = 1
    while True:
        if power == len(str(i ** power)):
            counter += 1
        else:
            break
        power += 1

# print the number of instances found
print("The number of n-digit positive integers which are also an nth power: ", counter)


# ***PROBLEM SOLVED***
