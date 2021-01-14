#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests')


# In[2]:


get_ipython().system('pip install  BeautifulSoup4')


# In[3]:


import requests
from bs4 import BeautifulSoup


# In[4]:


url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)


# In[9]:


# Beautiful Soupで構造解析する
# parser = htmlの構造を解析する
soup = BeautifulSoup(res.text, 'html.parser')
soup


# In[25]:


soup.find_all('p')


# In[32]:


subscribers = soup.find_all('p', attrs={'class':'subscribers'})[0]
subscribers.text


# In[34]:


# 文字列と数値が入っているものに対して数字だけとってきたい場合
n_subscribers = int(subscribers.text.split('：')[1])
n_subscribers


# In[39]:


reviews = soup.find_all('p', attrs={'class':'reviews'})[0]
n_reviews = int(reviews.text.split('：')[1])
n_reviews


# In[40]:


# cssのセレクタで抽出
soup.select('.subscribers')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




