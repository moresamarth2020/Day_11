#!/usr/bin/env python
# coding: utf-8

# # Match Case Statements
# - To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java like language, you must have heard of switch-case statements. If this is your first language, dont worry as I will tell you everything you need to know about match case statements in this video!
# - A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
# - The match case consists of three main entities :
# 
# 1. The match keyword
# 2. One or more case clauses
# 3. Expression for each case
# - The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.
# 
# 

# In[5]:


x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is Four")
    case _:
        print(x)


# In[3]:


x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)


# In[ ]:




