#!/usr/bin/env python
# coding: utf-8

# ## Data collections
# 
# So far, we've seen data stored in single variables. But we usually want to collect data together somehow - different variables for each participants, different experimental conditions, or different data files for each participants. 
# 
# How can a bunch of variables be stored together? Python has a range of `collections` - special structures that can store data together. The two we'll focus on are called `lists` and `dictionaries`.

# ### The list
# The `list` is a workhorse of data manipulation and analysis. A list is group of variables of various types, set in a particular order, that are stored together in a single variable.
# 
# Consider this example from an analysis perspective - data from an experimental participant on a personality test. It would be clumsy to refer to these all the time individually, so let's use a list.

# In[1]:


# Define some data variables
pid = '001'; age = 29; sex = 'female'; extraversion = 5; neuroticism = 3


# In[2]:


# Store these in a list!
data = [pid, age, sex, extraversion, neuroticism]
print(data)


# The data is now stored together in one collection, with varying types. Each part of a list is known as an element, and has a position. It's worth noting that each element can be any Python data type or structure - even another list!

# In[3]:


# Nested list
nest = [1, 4, 5, ['inside', 'the', 'list']]
print(nest)


# ### The list
# We've got our data in a list. But what if we need to interact with the elements? How can we access different elements? Using an `index`, and different `methods`. 
# 
# Welcome to one of Python's quirkiest parts: list indexing.

# #### Simple indexing
# You can access any element of a list by passing its **index value** to the list variable, using square brackets, `[]`, in this format:
# `list_name[number]`.
# List indexing **starts from zero**. That is, the first element is in the '0th' position.

# In[4]:


# Get the participant ID from the data list
retrieved_pid = data[0]
print(retrieved_pid)


# In[5]:


# Get the extraversion score
print(data[3])


# In[6]:


# Lists can also be accessed in reverse order, by using negative indexes!
# Grab the final element of a list
print(data[-1])


# In[7]:


# Or grab the FIRST element of a list using reverse indexing
print(data[-5])


# A graphic for rememebring list indexing:
# ![List%20Index.png](attachment:List%20Index.png)

# ### List slicing
# Getting things out of a list one by one would involve a lot of typing. Often, we might want to access a range of values all at once. This is achieved through specific notation using a colon, `:`, and specific index locations.

# In[8]:


# The first few elements of `data` have demographics. Let's get those out
print(data[0:3])


# In[9]:


# Or if you are starting from the very beginning, the 0 can be omitted
print(data[:3])


# In[10]:


# Reverse slicing works in the same way
print(data[-3:])


# In[11]:


# Nested lists can be indexed one after the other 
print(nest)
print(nest[3][-1])


# Do you notice anything interesting about the slicing? To access the first three elements, you have to pass `[0:3]`. List slicing works on the basis that:
# 
# * The first value specifies the start and is ***included***.
# * The value after the colon specifics the end and is ***not*** included.
# 
# A good way of remembering this is to think Python sees a slice as 'start here, and take ***up to, but not including*** this number'

# ### Stepped indexing 
# It's possible to use different steps to jump over lists in different ways, using a set of three values and colon operators, that specify where to start, where to stop, and how many steps to take, like this:
# 
# `a_list[start:stop:steps]`

# In[12]:


# Define a longer list
long = ['a', 1, 'c', 45, 'd', 77, 'st', 4.321]


# In[13]:


# Index with steps
print(long[1:6:2])


# In[14]:


# Another variation
print(long[:5:3])


# In[15]:


# In reverse!
print(long[5:1:-1])


# ### List `.methods` and other tricks
# Lists are pretty powerful, but there additional things that make them even cooler. Lists (along with many other data structures in Python) have **methods**. A **method** is a function that 'lives' in a variable, and can do specific things to the data in that variable. Not all data structures have methods, but the ones that do usually have great uses. A method is accessed by the `.` operator.

# Let's say we want to add data to a list. How can we do this? Using the `.append` method.

# In[16]:


# Add some Agreeableness scores to the personality data
print(data)


# In[17]:


# Define Agreeableness score
agreeableness = 1
# Append it!
data.append(agreeableness)
print(data)


# Sometimes, you can't remember the location of a specific element in a list when you want to get to it. There is an `.index` method that takes a value that is in the list, and will return the index. 

# In[18]:


# We need the position of the sex variable. We know they are female, so...
ind = data.index('female')
print(ind)

# Use that index
print(data[2])


# Lists can be interacted with using the `*` and `+` operators, which result in interesting manipulations.

# In[19]:


# Make two lists
list_a = [3, 2, 1]; list_b = [4, 5, 6]


# In[20]:


# Try addition...
print(list_a + list_b)


# In[21]:


# What if I multiply a list?
print(list_a * 3)


# In[22]:


# Multiple operators
print(list_a * 3 + list_b * 2)


# We may sometimes want to alter lists in some way. That's easy enough to do using slicing or methods. Lists are known as a **mutable** data structure, because you can alter them once you have created them. 

# In[23]:


# Update the data list with new participant data
print(data)

# Update the scores
data[3:] = [5, 5, 5]

print(data)


# ## The dictionary - look it up!
# Lists are powerful ways to store variables and data of many different types. But it can be hard to keep track of what kind of variable is in what element. For example, in the `data` list, the first few elements were demographic data. Was the age the second element, or the third? 
# 
# That's not easy to remember. Fortunately, another data structure, the `dictionary`, addresses these shortcomings, by providing a set of *key:value* pairs, which are defined using curly braces notation `{}`. The keys must be an **immutable** data structure - a string usually works!
# 
# We can define a dictionary with some demographic data.

# In[24]:


# Create a dictionary
demographics = {'PID':'001', 'Age':30, 'Sex':'Female'}

# Or use the `dict` function, assigning the values with keyword arguments
demographics_1 = dict(PID='001', Age=30, Sex='Female')

print(demographics)
print(demographics_1)


# #### Looking things up in the dictionary
# Getting a value from a dictionary is as easy as providing the **key**, following this format. 
# 
# `dictionary_name[key_name]`

# In[25]:


# Retrieve the participant sex
print(demographics['Sex'])


# #### Adding data to the dictionary
# Adding extra data is as simple as providing a new *key:value* pair. Entire extra dictionaries can be provided through the dictionary `.update` method.

# In[26]:


# Add a score to the data
demographics['Extraversion'] = 4
print(demographics)


# In[27]:


# Create a new dictionary of scores to be added
scores = dict(Agreeableness=4, Neuroticism=2, Openness=1, Conscientiousness=3)

# Call the update method on the demographics dictionary
demographics.update(scores)

print(demographics)


# #### Important dictionary methods
# Like lists, dictionaries have a range of methods. Some useful ones to know are the following:
# * `.keys()` : returns a list of all the keys in the dictionary, useful if you aren't sure whats inside one.
# * `.values()` : returns a list of all the values (i.e. data) in the dictionary. Allows a look directly at the data.
# * `.items()` : returns a list, where each element is a tuple (like a list, but immutable), where the first element is the key, and the second, the value.

# In[28]:


# Look at the keys 
print(demographics.items())


# In[29]:


# Look at the values
print(demographics.values())


# In[30]:


# Look at it all!
print(demographics.items())


# #### Advanced dictionaries
# Like lists, dictionaries can also be nested, with a key referring to another dictionary. 
# 
# It follows that a value can be anything - a list, dictionary, string, or any of Python's many data types.

# In[31]:


# Demonstrate a nested dictionary
nest_dict = {'PID': 'John', 'Age': 25, 'Personality':{'Extra': 4, 'Neuro': 1}}


# In[32]:


# Accessing nested attributes
print(nest_dict['Personality'])
print(nest_dict['Personality']['Extra'])


# It should be clear by now that lists and dictionaries can be used together, to build complex data structures capable of storing a range of variables and data. Extracting data from a complex data structure is relatively straightforward, armed with what we know.

# In[33]:


# Create a somewhat complex data structure - notice we can split long commands across lines
participantA = {'PID': '001', 'age': 23, 
               'Anxiety_Score':{'Subscale1': 4.22, 'Subscale2': 2.34 },
              'RTs': [321, 230, 400, 593, 600, 102, 129]}

participantB = {'PID': '002', 'age': 25, 
               'Anxiety_Score':{'Subscale1': 1.20, 'Subscale2': 5.24 },
              'RTs': [876, 450, 291, 893, 864, 456, 983]}

full_data = {'ppt_A': participantA, 'ppt_B': participantB}


# In[34]:


# Extracting buried items - extract the last reaction time they gave
print(full_data['ppt_A']['RTs'][-1])


# In[35]:


# Or anxiety scores
print(full_data['ppt_B']['Anxiety_Score']['Subscale1'])

