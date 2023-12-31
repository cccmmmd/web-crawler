#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
import json
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://doodles.google/live/api/v1/doodles?order_by=date&sort_direction=desc&page=3&limit=16"
response = urlopen(url)

doodles = json.load(response)

for d in doodles:
    url = 'https' + d['url']
    print(d['title'], utl)
    
    fname = 'doodles/' + url.split("/")[-1]
    
    response = urlopen(url)
    img = response.read()

    
    f = open(fname, "wb")
    f.write(img)
    f.close()

    


# In[ ]:




