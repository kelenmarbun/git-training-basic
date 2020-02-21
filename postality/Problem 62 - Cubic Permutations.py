#!/usr/bin/env python
# coding: utf-8

# # Problem 62 - Cubic Permutations
# ---
# 
# ## Problem Description: [Click here to read the full description of this problem](https://projecteuler.net/problem=62)
# ---
# 
# ## Problem Solution Algorithm:
# 
# 1. Create a list and name it cubes
# 2. For each and every iteration, create a sorted list of string of cube of the number [sorted(list(string(i3)))]
# 3. Add that cube to the cubes list
# 4. Count the number of times cube is in the cubes list. If it is 5 times, then break the loop and print the cube of first instance of cube in the list.
# 
# Credits: http://radiusofcircle.blogspot.com
# 

# ### Step 1

# In[1]:


# list to store cubes
cubes = []


# ### Step 2-4

# In[2]:


# iterator
i = 0

# while loop
while True:
 # cube of the number
 cube = sorted(list(str(i**3)))
 # appending the cube to cubes list
 cubes.append(cube)
 # check if it occured 5 times
 if cubes.count(cube) == 5:
  # print the cube of the smallest such cube
  print("The smallest cube for which exactly five permutations of its digits are cube: ", (cubes.index(cube))**3)
  break
 i += 1


# ***PROBLEM SOLVED***
