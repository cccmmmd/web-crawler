#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen, urlretrieve
import json
import os
# for MAC
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

for m in range(12):
    url = "https://doodles.google/live/api/v1/doodles?order_by=date&sort_direction=desc&page=" + str(m + 1) + "&limit=16"
    print(url)
    response = urlopen(url)

    doodles = json.load(response)
    #doodles -> List d -> Dictionary
    for d in doodles:
        url = 'https' + d['url']
        print(d['title'], utl)
        
        #電腦創資料夾
        dirname = 'doodles/' + str(m + 1) + "/"
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        
        fname = dirname + url.split("/")[-1]
        urlretrieve(url, fname)

    
    #response = urlopen(url)
    #img = response.read()
    
    #f = open(fname, "wb")
    #f.write(img)
    #f.close()

    


# In[ ]:




