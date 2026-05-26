#!/usr/bin/env python
# coding: utf-8

# In[7]:


import platform
vers = platform.python_version()
assert vers[0] == '3', "You must use Python 3, "+vers+" is not acceptable"
print("Python 3 confirmed.")

num_cakes = int(input("How many cakes would you like to make? "))
recipe_mult = 12/num_cakes
sweet_butter = (125*recipe_mult)
sugar = 225*recipe_mult
eggs = max(1,round(recipe_mult))
vanilla = (recipe_mult)
chocolate = (recipe_mult)
flour = (225*recipe_mult)
salt = (0.5*recipe_mult)
chips = (200*recipe_mult)
print(sweet_butter, "g sweet butter", "\n", sugar, "g sugar", "\n", eggs, " eggs", "\n", vanilla, " tsp vanilla extract", "\n",
      chocolate, " tsp chocolate extract", "\n", flour, "g flour", "\n", salt, " tsp salt", "\n", chips, "g chocolate chips", "\n")


