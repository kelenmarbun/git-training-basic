#!/usr/bin/env python
# coding: utf-8

# # Problem 61 - Cyclical Figurate Numbers
# ---
# 
# ## Problem Description: [Click here to read the full description of this problem](https://projecteuler.net/problem=61)
# ---
# 
# ## Problem Solution Algorithm:
# 
# 1. Calculate the range of n for each polygonal type by solving the Quadratic Equations
# 2. Define the set of numbers for each polygonal type (triangle, square, pentagonal, hexagonal, heptagonal, and octagonal) based on the range of n known
# 3. Split the 4-digit-numbers into 2-2 digit numbers for each polygonal type
# 4.  

# ### Step 1-3

# In[1]:


import cmath, math


# In[2]:


lower_bond = 999
upper_bond = 10000


# #### Triangle Numbers

# In[3]:


# Solving the quadratic equations from Triangle formula

at = 1
bt = 1
ctl = -lower_bond*2
ctu = -upper_bond*2
dl = (bt**2) - (4*at*ctl)
du = (bt**2) - (4*at*ctu)

n_lower_triangle = math.ceil(((-bt+cmath.sqrt(dl))/(2*at)).real)
n_upper_triangle = math.ceil(((-bt+cmath.sqrt(du))/(2*at)).real)

# Define Triangle numbers and split them

tr_numbers = [int(n*(n+1)/2) for n in range(n_lower_triangle, n_upper_triangle)]
triangle_numbers = [item for item in tr_numbers if (len(str(item))>3)]

tr_splitted = [(int(x/100), int(x - int((x/100))*100)) for x in triangle_numbers]
triangle_splitted = [item for item in tr_splitted if (len(str(item))>7)]


# In[4]:


n_lower_triangle


# In[5]:


n_upper_triangle


# In[6]:


triangle_numbers


# In[7]:


triangle_splitted


# #### Square Numbers

# In[8]:


asq = 1
bsq = 0
csql = -lower_bond
csqu = -upper_bond
dsql = (bsq**2) - (4*asq*csql)
dsqu = (bsq**2) - (4*asq*csqu)

n_lower_square = math.ceil(((-bsq+cmath.sqrt(dsql))/(2*asq)).real)
n_upper_square = math.ceil(((-bsq+cmath.sqrt(dsqu))/(2*asq)).real)

sq_numbers = [int(n**2) for n in range(n_lower_square, n_upper_square)]
square_numbers = [item for item in sq_numbers if (len(str(item))>3)]

sq_splitted = [(int(x/100), int(x - int((x/100))*100)) for x in square_numbers]
square_splitted = [item for item in sq_splitted if (len(str(item))>7)]


# In[9]:


n_lower_square


# In[10]:


n_upper_square 


# In[11]:


square_numbers


# In[12]:


square_splitted


# #### Pentagonal Numbers

# In[13]:


# Solving the quadratic equations from Pentagonal formula

apnt = 3
bpnt = -1
cpntl = -lower_bond*2
cpntu = -upper_bond*2
dpntl = (bpnt**2) - (4*apnt*cpntl)
dpntu = (bpnt**2) - (4*apnt*cpntu)

n_lower_pentagonal = math.ceil(((-bpnt+cmath.sqrt(dpntl))/(2*apnt)).real)
n_upper_pentagonal = math.ceil(((-bpnt+cmath.sqrt(dpntu))/(2*apnt)).real)

# Define Pentagonal numbers

pent_numbers = [int(n*((3*n)-1)/2) for n in range(n_lower_pentagonal, n_upper_pentagonal)]
pentagonal_numbers = [item for item in pent_numbers if (len(str(item))>3)]

pent_splitted = [(int(x/100), int(x - int((x/100))*100)) for x in pentagonal_numbers]
pentagonal_splitted = [item for item in pent_splitted if (len(str(item))>7)]


# In[14]:


n_lower_pentagonal


# In[15]:


n_upper_pentagonal


# In[16]:


pentagonal_numbers


# In[17]:


pentagonal_splitted


# #### Hexagonal Numbers

# In[18]:


# Solving the quadratic equations from Hexagonal formula

ahex = 2
bhex = -1
chexl = -lower_bond
chexu = -upper_bond
dhexl = (bhex**2) - (4*ahex*chexl)
dhexu = (bhex**2) - (4*ahex*chexu)

n_lower_hexagonal = math.ceil(((-bhex+cmath.sqrt(dhexl))/(2*ahex)).real)
n_upper_hexagonal = math.ceil(((-bhex+cmath.sqrt(dhexu))/(2*ahex)).real)

# Define Hexagonal numbers

hex_numbers = [int(n*((2*n)-1)) for n in range(n_lower_hexagonal, n_upper_hexagonal)]
hexagonal_numbers = [item for item in hex_numbers if (len(str(item))>3)]

hex_splitted = [(int(x/100), int(x - int((x/100))*100)) for x in hexagonal_numbers]
hexagonal_splitted = [item for item in hex_splitted if (len(str(item))>7)]


# In[19]:


n_lower_hexagonal


# In[20]:


n_upper_hexagonal


# In[21]:


hexagonal_numbers


# In[23]:


hexagonal_splitted


# #### Heptagonal Numbers

# In[24]:


# Solving the quadratic equations from Heptagonal formula

ahep = 5
bhep = -3
chepl = -lower_bond*2
chepu = -upper_bond*2
dhepl = (bhep**2) - (4*ahep*chepl)
dhepu = (bhep**2) - (4*ahep*chepu)

n_lower_heptagonal = math.ceil(((-bhep+cmath.sqrt(dhepl))/(2*ahep)).real)
n_upper_heptagonal = math.ceil(((-bhep+cmath.sqrt(dhepu))/(2*ahep)).real)

# Define Heptagonal numbers

hep_numbers = [int(n*((5*n)-3)/2) for n in range(n_lower_heptagonal, n_upper_heptagonal)]
heptagonal_numbers = [item for item in hep_numbers if (len(str(item))>3)]

hep_splitted = [(int(x/100), int(x - int((x/100))*100)) for x in heptagonal_numbers]
heptagonal_splitted = [item for item in hep_splitted if (len(str(item))>7)]


# In[25]:


n_lower_heptagonal


# In[26]:


n_upper_heptagonal


# In[28]:


heptagonal_numbers


# In[30]:


heptagonal_splitted


# #### Octagonal Numbers

# In[31]:


# Solving the quadratic equations from Octagonal formula

aoct = 3
boct = -2
coctl = -lower_bond
coctu = -upper_bond
doctl = (boct**2) - (4*aoct*coctl)
doctu = (boct**2) - (4*aoct*coctu)

n_lower_octagonal = math.ceil(((-boct+cmath.sqrt(doctl))/(2*aoct)).real)
n_upper_octagonal = math.ceil(((-boct+cmath.sqrt(doctu))/(2*aoct)).real)

# Define Octagonal numbers

oct_numbers = [int(n*(3*n-2)) for n in range(n_lower_octagonal, n_upper_octagonal)]
octagonal_numbers = [item for item in oct_numbers if (len(str(item))>3)]

oct_splitted = [(int(x/100), int(x - int((x/100))*100)) for x in octagonal_numbers]
octagonal_splitted = [item for item in oct_splitted if (len(str(item))>7)]


# In[32]:


n_lower_octagonal


# In[33]:


n_upper_octagonal


# In[34]:


octagonal_numbers


# In[35]:


octagonal_splitted


# In[ ]:




