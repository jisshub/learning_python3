#!/usr/bin/env python
# coding: utf-8

# # REGULAR EXPRESSIONS

# In[5]:


#import re module
import re
#create regex obect using re.compile() and save to 'pattern'
pattern=re.compile('\d{3} \d{3}-\d{4}')
# Scan through a string searching for a match to the regex, returning
#a Match object, or None if no match was found.
res=pattern.search('call me at 345 455-5678')
print(res)


# In[18]:


print(pattern)


# In[19]:


type(pattern)


# In[ ]:


help()


# In[4]:


res=pattern.search('shkad 982923')
print(res)
#here res returns a None since no match to the regex was found in the string.


# In[6]:


#to extract the exact match from the string,use group()
res.group()


# In[8]:


#search() only returns just one match in the string
res=pattern.search('call me at 403 344-3343 or 402 332-3438')
print(res)
#here it only returns just one match of regex.


# In[13]:


#so inroder to return all the matches of regex.use, findall() method
res=pattern.findall('call me at 403 344-3343,402 332-3438')
print(res)
#matches are printed in a list.


# In[11]:


#we can directly compile a regex object and search a string that matches the pattern
#so here each time we call search() regex is compiled.
res=re.search('\d{4}-\d{7}','call me 0484-2617278').group()
print(res)


# In[12]:


#sample


# In[20]:


import re
pattern=re.compile('(Mr\.) ([a-zA-Z]+ [a-zA-Z]+)')
result=pattern.search('Are you Mr. Jissmon Jose?').group()
print(result)


# In[ ]:




