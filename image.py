#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests
from bs4 import BeautifulSoup


# In[29]:


url = 'https://scraping-for-beginner.herokuapp.com/image'
res = requests.get(url)


# In[30]:


res


# In[31]:


soup = BeautifulSoup(res.text, 'html.parser')


# In[32]:


img_tag = soup.find('img')
img_tag['src']


# In[33]:


root_url ='https://scraping-for-beginner.herokuapp.com'
img_url = root_url + img_tag['src']


# In[34]:


img_url


# In[35]:


from PIL import Image
import io


# In[42]:


img = Image.open(io.BytesIO(requests.get(img_url).content))
img.save('img/sample.jpg')


# In[40]:





# In[44]:


soup = BeautifulSoup(res.text, 'html.parser')
img_tags = soup.find_all('img')
for i, img_tag in enumerate(img_tags):
    root_url ='https://scraping-for-beginner.herokuapp.com'
    img_url = root_url + img_tag['src']
    img = Image.open(io.BytesIO(requests.get(img_url).content))
    img.save(f'img/{i}.jpg')


# In[ ]:




