#!/usr/bin/env python
# coding: utf-8

# # The Basics
# ## Comments, the `print` function, and Python as a calculator

# ### Commenting code
# When writing code, you are your own worst enemy. You might remember what something means at the time of writing, but when you return a day later, a week, or even a month later, you *will* forget. Comment code using by starting a line with `#` - anything following will be ignored by Python.

# In[1]:


# Any line of code you preface with a '#' symbol is a comment. Python will ignore it - its just for you to read. 
# ALWAYS COMMENT YOUR CODE! #


# ### The `print` function
# When you write code, you often want to see the results of it. Python will happily run code all day, but unless you ask to see the output of certain pieces of code, it will go about its business silently. Anything you put inside the `print` function will be... printed.

# ### Python is capable of basic maths - it can be used as a calculator.

# In[2]:


# Addition
print(10 + 5)

# Subtraction
print(10 - 5)

# Division
print(10 / 2)

# Modulus
print(10 % 3)

# Exponent
print(10 ** 2)

# Do the print outs below make sense?


# More complex maths can be done, but follow the order of operations...

# In[3]:


# Is this answer surprising?
print(4 * 5 / 2 + 7)


# In[4]:


# One of Python's rules is 'be explicit.' Python will now work within brackets, inside-out
print( (4 * (5 / 2)) + 7 )


# In[5]:


# Greater complexity
print( (10 * (4 + (10 / 2))) - 5 )


# ### Variables and data types
# Almost always, we want to store information in some way to interact with it later. This is achieved through the use of *variables*. 
# 
# A variable is a kind of box that contains some data, which can be of a variety of *types*.

# ### Assigning a variable - 'putting something in a box'
# Assigning a variable is very straightforward, and we'll be doing a lot of it. Variable assignment has rules!
# * **Must** begin with a letter (a-z, A-Z) or an underscore, _
# * Other characters may be letters, numbers or underscores
# * Variables are **case sensitive**. `my_variable` is different to `My_variable`!
# * Can be any length, but be sensible.
# * Some words you cannot use as a variable name, because Python has reserved them
#     * Examples include `and`, `or`, `for`, `return`, `del`, `def`, `in`, `yield`, `True`, `False`
# 

# In[6]:


# An example
weight = 90

print(weight)


# In[7]:


# Another
height = 1.90

print(height)


# Its now possible to work with these variables as if they are raw numbers, since they are just pointing to those numbers!

# In[8]:


BMI = weight / (height ** 2)
print(BMI)


# What if we made a mistake? Python is a forgiving language. We can simply overwrite the earlier valuable by reassigning it, or altering it in some way!

# In[9]:


# We've gained weight!
weight = 95

print(weight)


# Since we can interact with variables as if they are numbers, the following approaches are also valid.

# In[10]:


# We need to increase the height
height = height + 0.10

print(height)

# I can't seem to get this right...
height = height - 0.10
height = height + 0.05

print(height)


# ### 'Syntactic sugar'
# It's pretty common to reassign a variable using the notation above. But that is a lot of typing. Python has some excellent shortcuts that can speed these operations up, which are known as 'syntactic sugar' - sweet code!

# In[11]:


# How to alter a variable quickly
age = 30

# My birthday is this week, so...
age += 1

print(age)


# It's possible to use `+=`, `-=`, `/=`, `%=`, and `**=` to carry out the various operations on variables in place, **if** the variables refer to a single number.

# ### Variable types
# Not all variables and data are the same, and what you can do with a variable depends on its type. Each type comes with its own abilities and uses.
# 

# There are several common data types that you see during analysis. 
# 
# * Integers, known as `int`. These are whole numbers, e.g. `1`, `45`.
# * Floating points, or `float`. These are numbers with extra precision, e.g. `3.894`, `99.100000003`
# 
# 
# * Booleans, or `bool`. These are special variables that are represented by `True` and `False`. These have a range of uses in **comparing** variables, or checking whether certain conditions are met.
# * Strings, or `str`. These represent text data and have a range of uses in data analysis. 
# 
# How do you know what type your variable is? Use the `type` function!

# In[12]:


# Make an integer
an_integer = 1
print(type(an_integer))


# In[13]:


# Make a float
a_float = 5.78
print(type(a_float))


# In[14]:


# Booleans already exist, but we can assign them to a variable
is_true = True
print(type(is_true))


# In[15]:


# Make a string
a_string = 'Hello world'

another_string = "Hello again"

formatted_string = """Any text tha
t star
ts with three quotes     
will be formatted just like you type!"""

print(type(a_string))

# Just to show
print(formatted_string)


# ### Converting between types
# Variables do not have to stay as the type they were assigned to. 
# 
# The variable types - `int`, `float`, `bool`, and `str` can be used as functions to convert between types, but only if the variables have certain values.

# In[16]:


# Convert a float to a an integer
to_int = int(a_float)

print(type(to_int), to_int)


# In[17]:


# Convert an integer to a float
to_float = float(an_integer)

print(type(to_float), to_float)


# In[18]:


# Convert an integer to a boolean - anything 1 or more gets converted to True, zero is False
true_bool = bool(12)
false_bool = bool(0)

print(type(true_bool), true_bool)
print(type(false_bool), false_bool)


# In[19]:


# Converting types with strings can be tricky. You can only convert numbers-as-strings to actual numbers.
a_number = '1'

print(type(a_number), a_number)


# In[20]:


# Convert it to an integer
as_integer = int(a_number)

print(type(as_integer), as_integer)

# Notice how they look the same to us, but not to Python!


# In[21]:


# Turn a number to a string
as_string = str(1342)

print(type(as_string), as_string)


# ### Working with different variable types
# Variables of different types can interact in certain ways, but not in others. They can also behave in unexpected ways which can catch you out, so its worth learning this early.

# In[22]:


# Adding an integer and a float works!
float_ = float(3.21)
int_ = int(2)

print(float_ + int_)


# In[23]:


# Adding an integer and a boolean doesn't make any sense, but since True is seen as ONE - makes sense to Python
a_bool = True

print(int_ - a_bool)


# In[24]:


# Adding strings together is works just like a stitch, but subtraction doesn't work 
print('hello' + 'world')

# Remember your whitespace!
print('Hello' + ' ' + 'world')

# What happens if I multiply? Division doesn't work!
print('hello' * 10)


# In[25]:


# But working with strings and other types is as simple as a correct conversion - without, it will break
language = 'Python'
age = 30

sentence = 'The programming language ' + language + ' is ' + str(age) + ' years old'

print(sentence)


# ### Logic - comparing data and variables
# 
# A lot of data handling and analysis involves comparison of some kind. How can we compare whether one score is higher than another? How do we remove participants from an analysis who are above a certain age, or have a score outside of a normal range?
# 
# Computers are excellent at this kind of `logic`, and there are specific rules about how to compare values.

# The specific syntax for comparing variables:
# 
# * Are two variables the same, `==`
# * Are two variables **not** the same, `!=`
# 
# * Is one variable **greater** than another, `>`
# * Is one variable **less** than another, `<`
# 
# * Is one variable **greater than or equal** to another, `>=`
# * Is one variables **less than or equal** to another, `<=`

# These comparisons are known as **Boolean logic**, and the results of the comparisons will be either `True` or `False` - the special variables that are used to manage logical outcomes.

# In[26]:


# Variable comparison examples
# Define some simple variables - ';' can be used to have more than one statement on a line
a = 5; b = 3; c = 23; d = 23


# In[27]:


# Is a greater than b?
print(a > b)


# In[28]:


# Is b less than c?
print(b < c)


# In[29]:


# Is a greater than d?
print(a > d)


# In[30]:


# Are c and d the same?
print(c == d)

# Or is one equal to or greater than the other?
print(c >= d)


# Variable comparison is straightforward, but sometimes you may have a series of variables to compare, and this is a little more involved, and uses some extra keywords.
# 
# Introducing `and`, `or`, `not`:
# 
# * `and` compares a pair of booleans, and will return a `True` **only** if they are both the same. Also appears as the `&` operator!
# 
# * `or` compares a pair of booleans, and will return a `True` if at least one of them is `True`. Also appears as the `|` operator.
# 
# * `not` will invert a boolean value - so if its `True`, it will become `False`, and so on.
# 
# Let's look at some examples.

# In[31]:


# Define some variables
x = 10; y = 12; z = 15
a = 9; b = 22; c = 30
age = 30; sex = 'female'


# In[32]:


# Demonstrate 'and'
age > 20 and y > 10


# In[33]:


# Demonstrate 'or' 
sex == 'female' or age < 20


# In[34]:


# Demonstrate 'not'
not b < 20 and age >= 30


# There are more complex comparisons can be carried out using `()` to group subsets of comparisons that can make up larger comparisons.

# In[35]:


# More complex comparisons
(sex == 'female' and age < 30) or (a < 9 or c == 30)


# In[36]:


# More complex 
not (sex == 'male' and age < 30) and (b < 25 or z > 16)

