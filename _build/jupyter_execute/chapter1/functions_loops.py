#!/usr/bin/env python
# coding: utf-8

# ## Functions
# 
# Functions are nothing new to you - we have used them before!
# * `print`
# * `type`
# * `dict`
# * `list`
# 
# A function is a piece of reusable code that is suited for a particular task, that can be reused. Python has thousands of functions built in, as well as across different packages we will come to in the future. 
# 

# #### Functions example
# How do we use functions? With the following general approach:
# 
# `output = function_name(work_on_this, more_arguments)`
# 
# Two built in functions we can play with are `min` and `max`. 

# In[1]:


# Example
scores = [2.39, 1.12, 5.21, 8.92, 1.24]

# Find the range by using min and max
lowest = min(scores)
highest = max(scores)

# Compute the span
print(highest - lowest)


# #### Functions examples
# `max` and `min` are really simple functions, with a single input. Sometimes functions have more than one input, or **argument**. More than one argument is entered by separating with a `,`.
# 
# A common data analysis function is `round`, which rounds numbers to a degree of precision set by you. Its first input is a value you want to round, and the second is the level of precision you want.

# In[2]:


# Multi-argument function example
value = 3.193849291

# Use round 
rounded = round(value, 3)

print(rounded)


# #### Functions examples
# Functions often have what are known as default arguments. What happens if we just give `round` a single argument, the number we want to round?

# In[3]:


# Testing round
print(round(value))


# Python has made a guess about what you want - rounded to a whole number. That is, the second argument has a **default** value - zero.

# #### `help`!
# If you ever get confused about what a function does, or what arguments it requires, you can ask for help. 
# `help` is a function whose job is to give you a print out of how a function works. What does it say about `round`?

# In[4]:


# Get help on round
help(round)


# ## Methods
# We've seen methods before - the special functions that a `list` can use to make alterations to itself. 
# 
# But methods are everywhere, and depend on the variable in question. You can use `help` on a specific data type to see what methods it has. 
# 
# `string` data has a range of useful methods that make working with text data simple.
# 
# For example, we can use:
# * `.upper()`
# * `.lower()`
# * `.count()`
# * `.split()`
# * `.join()`
# 
# for various exciting possibilities. 

# In[5]:


# Define a string
basic = 'We are going to play with this!'


# In[6]:


# How does .upper() work?
print(basic.upper())


# In[7]:


# So lower should...
print(basic.lower())


# In[8]:


# How many 'a's in this sentence?
print(basic.count('a'))


# In[9]:


# Chop this up by the number of space
print(basic.split(' '))


# In[10]:


# Join is cool!
split_list = basic.split(' ')
print('!'.join(split_list))


# ## Loops
# Things are getting more advanced now. There is one programming practice that you should master to fully control your data. 
# 
# What we've seen so far is straightforward, defining collections like lists and dictionaries, and retrieving data from them through indexing. Sometimes, we want to do something with each element in a data collection - perhaps call a function on it, read a file, remove a piece of data, etc. How can we do this without manually accessing each element manually?
# 
# The answer is the `for` loop, a special piece of syntax that allows us to *iterate* over a sequance or collection and retrieve the values inside by temporarily passing them to a new variable of whatever name we choose. 
# 
# The format looks like this:
# 
# `for variable in sequence:`
# 
#     `do something with variable`
#     
# Not the indentation on the second line - as you'll see, this is part of the code. Python uses this to differentiate code that is in the for loop with that outside of it. 

# For loops can be confusing, so some examples are required!

# In[11]:


# Make a list - these values all need to be rounded to two decimal places!
data_list = [12.394, 9.0948, 1.02, 39.4023, 2.392, 50.12948912]

# Write a for loop that prints each element in turn
for score in data_list:
    print(score)


# At each iteration, the value of `score` changed to be the next element in the list. So it started with the element in the position `[0]`, then `[1]`, and then onwards until `data_list` was finished. 

# Let's say we want to modify each element of a list, by rounding the numbers. This could be achieved as follows:

# In[12]:


# First, make an empty list to store our new data - just square brackets with no variables
rounded_data = []

# Iterate over the original list - round each element - and append to our empty list
for value in data_list:
    round_value = round(value, 2)
    rounded_data.append(round_value)
    
print(rounded_data)


# #### Building complexity with iteration
# You aren't limited to iterating just once. You can **nest** an iteration in the same way you can nest lists and dictionaries. This sometimes happens if you need to dig deeper into data structures to manipulate values.

# In[13]:


# Define a nested list
nest_list = [ ['001', 23, 'female'], ['002', 31, 'male'], ['003', 40, 'female'] ]

# Iterate over the main list
for participant in nest_list:
    
    # Iterate over the sub-list
    for score in participant:
        print(score)


# In[14]:


# Or access the sublists to do what we want!
for participant in nest_list:
    
    line = 'Participant ID = ' + participant[0] + ', age = ' + str(participant[1]) + ', sex = ' + participant[2]
    print(line)


# ## Loops
# #### `enumerate` 
# It should be clear from the above examples that when iterating over a list using `for`, we get back a variable that changes at each iteration. This is usually fine, but sometimes, we want to know the **actual position** of the element and do something with that. 
# 
# The `enumerate` function is used for dealing with this. We call `enumerate` on a sequence when we set up a `for` loop, and it returns a pair of variables - a counter, that returns the index, and a value, that returns the element, just like a normal `for` loop. 
# 
# The syntax looks like this!
# 
# `for index, value in enumerate(sequence):`
# 
#     `do stuff!`

# In[15]:


# Define a list
data_list = [123, 381, 'content', 'value']

for index, value in enumerate(data_list):
    line = 'Item in position ' + str(index) + ' is ' + str(value)
    print(line)


# In[16]:


# To demonstrate the use of index to actually access elements!
for index, value in enumerate(data_list):
    print(data_list[index])


# In[17]:


# Or to more efficiently replace elements - the original list is now lost
data_list = [12.394, 9.0948, 1.02, 39.4023, 2.392, 50.12948912]
print(data_list)

for index, value in enumerate(data_list):
    
    # Use the index to access and assign a new variable
    data_list[index] = round(value, 2)

print(data_list)


# ## Loops
# ### Iterating over dictionaries
# Dictionaries are a somewhat more complex structure compared to lists. For example, they don't 'remember' the order things were put in them, depending on the version of Python you use, so iterating over them in the same way as lists doesn't always make sense. 
# 
# If we remember the **methods** dictionaries had, we can iterate over those to access and play around with created dictionaries.

# In[18]:


# Make a dictionary
data_dict = {'Score_A': 45.2912, 'Score_B': 68.2945, 'Score_C': 88.9873}


# In[19]:


# Print out the keys
for key in data_dict.keys():
    print(key)
    


# In[20]:


# Or use the keys to access the data!
for key in data_dict.keys():
    print(data_dict[key])


# In[21]:


# Use this to grab the values - beware they may not be in the order you think
for value in data_dict.values():
    print(value)


# In[22]:


# Finally, use .items to get both key:value pairs out!
for key, value in data_dict.items():
    line = 'The key ' + key + ' returns the value: ' + str(value)
    print(line)


# In[23]:


# Makes sense to use this to modify the original dictionary
# Raise each value to the power of 3 to two decimal places
for k, v in data_dict.items():
    data_dict[k] = round(v ** 3, 2)
    
print(data_dict)


# The basics are covered! 
# 
# That's a lot of information to take in, but these are the fundamentals of working with data Python. Next time, we will cover the **NumPy** and **Pandas** libraries, which are built to process data efficiently and are the real workhorses of doing data analysis in Python.
# 
# If you're struggling or are stuck, do not worry. The learning curve is high and it will *take time*. The only way to improve is to keep coding. Try the exercises, and use the internet to look for answers where you aren't sure.

# In[24]:


from IPython.display import YouTubeVideo
display(YouTubeVideo('HluANRwPyNo'))

