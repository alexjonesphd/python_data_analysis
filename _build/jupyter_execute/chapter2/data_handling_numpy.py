#!/usr/bin/env python
# coding: utf-8

# # Data Handling with Python
# ## The `NumPy` module

# ### `import`
# It's time to crunch some data. Before that, we need to access some new modules. Last week, we used exclusively functions and data types in what's known as 'base' Python - the bare bones installation.
# 
# But there are thousands of extra functions and data types out there to help with specific tasks, just like data handling. In order to actually *use* them, we need to use `import`, a special command that activates the modules and allows you to access them. `NumPy` and `Pandas` are examples of modules that need to be imported.
# 
# 

# ### How `import` works
# When you import a module, you have access to all of its functions, data types, and submodules (collections of related functions). However, they all live under the import *alias* - a name that Python recognises the module as. You place all of your `import` statements at the top of your code or notebook. **Once imported, the functions will be available until the end of the session**. Importing NumPy works like this:

# In[1]:


# Import NumPy!
import numpy


# In[2]:


# Using the 'sqrt' function in NumPy
square_root = numpy.sqrt(40)
print(square_root)


# ### `import` alias - importing something `as`
# You can see one issue with this. Everytime you import a module like `NumPy`, to use its functions, you have to type `numpy.function_name`, which can be a hassle. Thankfully, Python has the ability to assign modules to a name of your choosing, using the `as` keyword. This can be anything, but conventions indicate `NumPy` should be imported as `np` - its *alias*. 

# In[3]:


# Import NumPy with its conventional alias, and use it to calculate a square root
import numpy as np
print(np.sqrt(40))


# ### Selective imports
# Some modules are massive, and you don't need all the functions they offer. Python is flexible enough to let you take one or several functions to use from a module, without requiring the alias, using the `from` keyword.

# In[4]:


# Import sqrt and square functions from NumPy
from numpy import sqrt, square

value = 10
print(sqrt(square(value)))


# You can even selectively import a function and give it a different name! Be careful with this - down this road lies madness...

# In[5]:


# Demonstrate selective import and aliasing
from numpy import square as SQUAREEEE
print(SQUAREEEE(value))


# # Data Handling with Python
# ## The NumPy module
# While dictionaries and lists will get you places, they are not built for real data manipulation. NumPy's main feature is a special data type, called the `array`. This is a data collection built for holding data of a **single data type** (e.g. integers, floats) in multiple dimensions, and is capable of performing mathematical operations on them quickly and efficiently.

# ### `np.array`
# To make a NumPy array, we need to pass a list of numbers to the `np.array` function - that is, the `array` function accessed in the NumPy module.

# In[6]:


# Import
import numpy as np

# Make a small array
arr = np.array([3, 4, 8, 9, 10])

print(arr)
print(type(arr))


# In[7]:


np.random.seed(42)


# ### Mathematical operations with NumPy
# With lists, if we wanted to multiply each element, we'd need a for loop, and a way to make sure the data was actually a number of some kind. Carrying out operations on a NumPy array is very simple - each element will be changed simply by carrying out some kind of operation. If you have two arrays with the same dimensions, each element is operated on by the corresponding position in the other array.

# In[8]:


# Maths with NumPy #
# Add 5 to each element
arr_add5 = 5 + arr

# Multiply by 3
arr_times3 = 3 * arr

print(arr, arr_add5, arr_times3)


# In[9]:


# It's even possible to do operations with two arrays of the same size - more on this later
arr1 = np.array([1, 5, 10])
arr2 = np.array([1, 1, 1])

added = arr1 + arr2
print(added)


# ### Array dimensions - 1D
# In NumPy, each array has an associated 'shape', which indicates its dimensions - that is, does the array live in 1, 2, or 3 dimensions? NumPy can store data in multidimensional arrays beyond what we can imagine. The power of all data handling comes from understanding these multidimensional arrays. You can find the shape of an array with the `.shape` attribute (like a method, but not a function - just returns some useful information).

# In[10]:


# Arrays in 1 dimension
arr_1d = np.array([1, 2, 3, 4, 5])

# Print shape
print(arr_1d.shape)


# So the above array has a single number in its `shape` - and that's how you know it's only 1-dimensional. It has 5 elements in dimension **zero**. In this case, it looks a lot like a list. 

# ### Array dimensions - 2D
# Think back to data you have analysed in something like SPSS and Excel. This data had a *two dimensional* structure - not a single row or column of data, but a set of them. Most data in psychology is stored as 2D arrays in some way, so understanding the 2D array is the building block of most data operations.
# 
# 2D arrays are essentially a series of 1D arrays stacked on top of each other - each 'row' must contain the same number of elements. So:

# In[11]:


# Define a 2D array like this
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d)
print(arr_2d.shape)


# Now, `.shape` has two numbers - two dimensions. Dimension zero has two elements - two rows, and dimension one has three elements - three columns. This row, column format is the key to understanding these data structures.
# 
# We'll be sticking mostly to 2D arrays for the remainder of the course, but explore 3D and above arrays using NumPy. For example, photographs are seen by Python has a 3D array - the height is the number of rows, the width is the number of columns, and the 'depth' represents the colour channels.

# ### Slicing and dicing NumPy arrays
# When you have data in an array, you will want to access it. You can access data in an array using a similar approach to lists, with a separate entry for each dimension.

# In[12]:


# 1D array slicing example is easy
arr_1d = np.array([1, 2, 3, 4, 5, 6])

print(arr_1d[1:5:2])


# In[13]:


# 2D slicing examples
arr_2d = np.array([[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21]])

# Get the first element of the rows, and the second element of the columns - by passing those indices
print(arr_2d)
print('\n', arr_2d[0, 1])


# In[14]:


# 2D slicing examples
# How to remove a whole row? Or a whole column?
one_row = arr_2d[-1, :]
one_col = arr_2d[:, 2]

print(one_row, one_col)
print(one_row.shape, one_col.shape)


# In[15]:


print(arr_2d)


# In[16]:


# 2D slicing examples
# Select specific sets of numbers from different rows and columns
subset = arr_2d[[0, 1], [1, 0]]
print(subset)


# In[17]:


# 2D slicing examples
# Strides are allowed
strided = arr_2d[:, :3:2]
print(strided)


# ### Merging and shaping data arrays
# Sometimes, your data doesn't come in a neat package, and you need to stitch things together - perhaps an extra participant's data was collected later, or a new column needs to be added to each data file. Arrays are not fixed, just like lists, they are *mutable* data types. There are a set of NumPy functions that allow you to merge arrays together, as long as they are the same size *on the dimension you want to join*. Remember, arrays must be square/rectangular!
# 
# Other times, you will need to alter the structure or shape of your data to suit some kind of purpose. That's handled efficiently by NumPy too.

# In[18]:


# Make some 1D arrays
arr_one = np.array(range(0,10))
arr_two = np.array(range(11,21))

print(arr_one.shape, arr_two.shape)


# In[19]:


# Put these next to each other as-columns using 'concatenate'!
stacked = np.column_stack((arr_one, arr_two))
print(stacked, stacked.shape)


# In[20]:


# Once they are joined by column_stack, we can put arr_one on *top* of arr_two with a transpose, using the .T method!
transposed = stacked.T
print(transposed, transposed.shape)


# In[21]:


# Stacking 2D arrays is easy as long as dimensions match!
doubled_up = np.column_stack((stacked, stacked[::-1, ::-1]))
print(doubled_up, doubled_up.shape)


# ### Merging and shaping arrays
# `np.column_stack` is a powerful function for joining arrays. But there is one thing you should know about how it works behind the scenes that can really trip you up. There is a general purpose function for joining arrays called `np.concatenate` that lets you join arrays together by across any axis you desire. But, there's one caveat.
# 
# `arr_one` and `arr_two` are 1-D arrays. Trying to concatenate them like with `column_stack` ends badly:

# In[22]:


# Try to concat - axis argument is '1' to join on columns - this will break!
#concat_stack = np.concatenate((arr_one, arr_two), axis=1)


# An error - axis 1 *does not exist for a one dimensional array!* `np.column_stack` converted the inputs silently into two dimensional arrays, even if they only had a single element in the second dimension. How can we coerce these input arrays? Using the array method `.reshape`, which modifies the shape of an array with the arguments you give it.

# In[23]:


### Demonstrate reshape
print(arr_one, arr_one.shape)

shaped = arr_one.reshape(1, 10)
print(shaped, shaped.shape)


# So to coerce the more general purpose `np.concatenate` to work, we need to reshape our arrays. You can get far with `np.column_stack` and transposing, but if you're not aware of this caveat, you can land up very confused.

# In[24]:


# Replicate column_stack functionality
concat_stack = np.concatenate((arr_one.reshape(10,1), arr_two.reshape(10,1)), axis=1)
print(concat_stack, concat_stack.shape)


# # Data Handling with Python
# ### Data selection, generation, and basic statistics
# You should now be able to manipulate 2D arrays of various sizes. In this final NumPy section, we will explore how to do some serious aspects of data handling that are important for reproducible research:
# 
# * Simulating data - when designing experiments, you can simulate data to plan your analysis correctly.
# * Data cleaning, and preparation - finding certain cases to extract/outliers to remove
# * Basic summary statistics - computing the mean, median, standard deviation
# 
# These are all essential parts of any reproducible analysis workflow, but you may not have undertaken these steps yourself in the past depending on your research experience.
# 

# ### Simulating data
# Why would we want to simulate data? One reason is to plan our analyses before we start. In the past, psychologists would throw statistical tests at a dataset they had collected because a particular test 'fit' the data. 
# 
# However, if you have some data in hand to start, you can carefully plan your analysis (perhaps as part of a pre-registration), or use it to highlight issues with your design you might not have foreseen.
# 

# ### The `np.random` module
# NumPy has all the tools we need to generate random data, in a submodule called `random`. This module contains a huge range of possible distributions that you can randomly generate data from - such as the normal distribution, an *F* distribution, chi-square, and so on. 
# 
# Most psychological data is normally distributed. How can we make an array of normally distributed data? Using the function `normal` in the `random` module of NumPy - `np.random.normal()`

# In[25]:


# Demonstrate use of normal - distribution has a mean of zero and SD of 1
single_int = np.random.normal()

# Pass in dimension values as arguments to create a very long row of random numbers!
lots = np.random.normal(size=1000)


# In[26]:


import matplotlib.pyplot as plt
import seaborn as sns

show_fig, ax = plt.subplots(1,1)

sns.distplot(lots, ax=ax)


# In[27]:


# Is it normal? 
show_fig


# `np.random.normal` has keyword arguments to create distributions of different widths, centred on different means. The utility of this is obvious - you can generate samples for different variables, as if you had collected the data already.

# In[28]:


# Compared to original....
# Same width, different mean
mean2 = np.random.normal(loc=2.0, scale=1, size=1000)

# Different width, same mean 
sd2 = np.random.normal(loc=0.0, scale=3, size=1000)

# Different width, different mean
diff = np.random.normal(loc=-10.0, scale=0.5, size=1000)


# In[29]:


show_fig, axes = plt.subplots(1,1, figsize=(10,5))

sns.kdeplot(lots, label='Mean=0, SD=1', color='blue', alpha=0.2, ax=axes, fill=True)
sns.kdeplot(mean2,label='Mean=2, SD=1', color='green', alpha=0.2, ax=axes, fill=True)
sns.kdeplot(sd2, label='Mean=0, SD=3', color='red', alpha=0.2, ax=axes, fill=True)
sns.kdeplot(diff, label='Mean=-10, SD=1.5', color='yellow', alpha=0.2, ax=axes, fill=True)
axes.legend();


# In[30]:


# Illustrate
show_fig


# There are other useful functions for generating data - for example, `np.random.randint` can generate datasets of a specific size and shape, of numbers between a certain bound.

# In[31]:


# Generate some fake personality data with `randint`, for 100 participants
big5 = np.random.randint(low=1, high=6, size=(100, 5))

print(big5[:5, :])


# ### Data cleaning and preparation
# Almost all datasets require some form of cleaning - removal of participants who didn't complete all the trials, variables with too many missing values, or scores outside acceptable ranges. You may not have had the opportunity to do this yourself at this stage, or maybe you did it manually in Excel or other data pipelines. 
# 
# As you might expect, Python and NumPy can find data that fits a certain critera and lets you specify exactly what you want to do to it. You've already used the basic tools of this approach before - logicals. The difference now is that these logicals are computed for every value in an array, whatever its shape, giving you wide flexibility. In fact, most operations return a *Boolean array*, sometimes known as a 'mask', where your conditional is true/false. 

# In[32]:


# An example of NumPy boolean logic
toy = np.random.randint(low=1, high=11, size=(10, 4))
print(toy)


# In[33]:


# Find scores above 6
above6 = toy > 6
print(np.column_stack((toy, above6)))


# Now that we have a Boolean array, or a masked array, we can use it to extract values in our array through array indexing. Let's say we want all the values above 5.

# In[34]:


# Use the mask array
extract = toy[above6]
print(extract)


# Since the shape of the original array could not be preserved after indexing, NumPy collapsed it into a vector.
# 
# Also remember you can negate Booleans with `~`. So, we can easily get all values *not less than 6*:

# In[35]:


extract2 = toy[~above6]
print(extract2)


# ### Building complexity with Boolean indexing - `.all()` and `.any()`
# Getting the actual numbers that fit a certain criteria is clearly simple. However, sometimes we need more complex indexing.
# 
# Imagine you have data and someone has entered in some out-of-range values. This means they were likely not paying attention, and you can't trust their data on the other trials. How can we remove them, and just analyse the rest of the data?

# In[36]:


# First, make a simple dataset
removals = np.random.randint(low=3, high=21, size=(15, 4))

# Here, we generate a 'mask array' using random.choice which chooses elements from a list at random and generates a specific shape, and probabilites
inds = np.random.choice([True, False], p=[0.1, 0.9], size=removals.shape)

# Now place the 'mask' over 'removals' and alter the numbers by replacing with a high number
removals[inds] = 999

print(removals)


# In[37]:


# To find those erroneous participants is easy - create a new mask array
mask = removals > 20

print(mask)


# Now we have our mask, how can we use it to remove the participants who have made an error and given '999' as a response? We already know that subsetting the current 'mask' array will return a single vector, but what we want to do is completely remove the rows that contain problematic entries.
# 
# The solution is to use the array methods of `.any()` and `.all()`. These powerful methods allow you to identify which rows or columns match a condition.

# In[38]:


# Demonstrate any on mask array
# Moving across columns (axis 1), what rows have ANY values above 20?
remove_rows = mask.any(axis=1)

# Now use remove_rows to clean the data!
clean = removals[~remove_rows, :]

print(clean)


# In[39]:


# The reverse is easily done - what if we wanted to remove any column with a True?
remove_cols = mask.any(axis=0)

# Empty!!
print(removals[:, ~remove_cols])


# These removal operations are carried out in steps above, but once you are comfortable with them mentally you can do the operations in a single line of code.

# In[40]:


clean_quick = removals[~(removals > 20).any(axis=1), :]
print(clean_quick)


# To quickly demonstrate, `.all()` works in the exact same way:

# In[41]:


# Set a row to be all 999 in removals
removals[5,:] = 999
print(removals)


# In[42]:


# This time in one line and specifying exactly to match to the number 999
drop = removals[~(removals == 999).all(axis=1), :]
print(drop)


# ### More complex Booleans 
# As with lists, you are able to build more complex conditions that allow for greater flexibility in accessing your data. However, unlike with lists, you will use the **bitwise** operators - `&` and `|`. These allow for comparisons of individual elements of an array. Using these also requires a little extra skill compared to `and` and `or`.

# In[43]:


# Make some more data
a = np.random.randint(low=3, high=12, size=(1, 10))
b = np.random.randint(low=5, high=15, size=(1, 10))


# How could we find the locations where `a` is greater than 5, AND `b` is less than 9? The obvious solution is:
# 
# `get_vals = a > 5 and b < 9`
# 
# This won't work! In fact, neither will:
# 
# `get_vals = a > 5 & b < 9`
# 
# This is due to something called *operator precedence* - not something you need to know for this course, but how it impacts how you query data is important.
# 
# To carry out these complex conditions with arrays, use the following format (similar to how complex comparisons are performed with single integers with regular `and` and `or`):

# In[44]:


get_vals = (a > 5) & (b < 9)
print(get_vals)


# The `|` operator functions in much the same way.

# In[45]:


or_vals = (a > 5) | (b < 9)
print(or_vals)


# NumPy offers flexibility in how you want to achieve your goals of Boolean comparisons. The functions `np.logical_and` and `np.logical_or` may be easier to interpret for you - use whatever works.

# In[46]:


# Demonstrate function versions of and/or
func_and = np.logical_and(a > 5, b < 9)
print(np.all(get_vals == func_and))

func_or = np.logical_or(a > 5, b < 9)
print(np.all(or_vals == func_or))


# ### The power of np.where
# One of the most powerful functions available to you is `np.where`. This function returns the indices (locations) of values that match your query - and with those, you are able to modify an array or carry out other computations. For example:

# In[47]:


# Demonstrate np.where
data = np.random.randint(low=1, high=15, size=(4,5))
print(data)


# In[48]:


# Get indices with np.where of values less than 5 or above 10
inds = np.where((data < 5) | (data > 10))
print(inds)


# In[49]:


# Use indices to alter the array
data[inds] = 30
print(data)


# But `np.where` has additional functionality. Aside from its first argument (the conditional), it also has an additional two arguments that specify *what you want* if the conditions are met (first additional argument) and if they are not met (second additional argument).

# In[50]:


# Demonstrate np.where additional args
data = np.random.randint(low=1, high=15, size=(4,5))

cool = np.where(data == 5, 9999, 1111)
print(data)
print(cool)


# In[51]:


data = np.random.randint(low=1, high=15, size=(4,5))

cool = np.where(data > 5, data, -1)
print(data)
print(cool)


# `np.where` breakdown:
# 
# `np.where(conditional_statement, a, b)`
# 
# * **conditional_statement** - this is a conditional statement that can be as simple or as complex as you like. 
# * **a** - A value you would like returned *where the condition is True*. This can be an integer, or if you pass it an array, it will be the values of that array where the condition is True - shapes must fit!
# * **b** - A value you would like returned *where the condition is False*. Same rules apply as above.

# ### NaN
# Sometimes, participants dont respond at all, never mind responding strangely. In order to fill in these gaps, there is a special data type called `NaN` - Not a Number. This is a simple placeholder for missing values in an array, and has special functions associated with finding it, such as `np.isna()`.

# In[52]:


# Add some NaN's to a dataset - only works with floats!
removals = removals.astype('float')
removals[(removals == 999)] = np.NaN
print(removals)


# In[53]:


# Demonstrate isnan
nan_mask = np.isnan(removals)

# This won't be helpful!
invalid_nan = removals == np.nan
print(nan_mask, invalid_nan)


# In[54]:


# With isnan, remove
print(removals[~np.isnan(removals).any(axis=1), :])


# ### Basic summary statistics
# Once you have your data, you almost always want to compute some kind of descriptive statistics with it. For example, what is the mean score per participant across trials? What's the standard deviation for a certain variable, so we can remove participants who are above or below that? NumPy has a range of methods that can compute statistics on data. The most common used are `.mean()`, `.std()`, and `.median()`.
# 
# Each method has certain inputs - the most important of which is the 'axis' argument, which indicates which axis to compute the statistic across - zero means 'across the rows', or the first dimension, and 1 means 'across the columns', or the second dimension. Higher dimensional arrays also work the same.

# In[55]:


# Demonstrate use of summary stats - this line is generating data, can you figure out how?
data = np.column_stack([np.random.normal(*stats) for stats in [(4, 1, 20), (3, 5, 20), (6, 2, 20), (3, 2, 20)]])
print(data)


# In[56]:


# What is mean and standard deviation for the whole data? Call methods with NO arguments
grand_mean, grand_std = data.mean(), data.std()

print(grand_mean, grand_std)


# In[57]:


# Summary statistics per VARIABLE - so across rows, one score per column
var_mean = data.mean(axis=0)
print(var_mean)


# In[58]:


# Summary statistics per PARTICIPANT - across columns, one score per row
ppt_mean = data.mean(axis=1)
print(ppt_mean)


# In[59]:


# Combined
descriptives = np.column_stack((data.mean(1), data.std(1)))
print(descriptives)

