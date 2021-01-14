#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[3]:


url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url)


# In[46]:


soup = BeautifulSoup(res.text, 'html.parser')


# In[47]:


# 観光地情報の取得
spots = soup.find_all('div', attrs={'class':'u_areaListRankingBox'})
spot = spots[0]
spot_name = spot.find('div', attrs={'class':'u_title'})
spot_name


# In[48]:


# spanタグの中身を削除　extract()
spot_name.find('span', attrs={'class':'badge'}).extract()


# In[49]:


spot_name


# In[50]:


spot_name = spot_name.text.replace('\n','')
spot_name


# In[63]:


# 評点 広い視野でみて、必要なものを絞っていく順序
eval_num = spot.find('div', attrs={'class':'u_rankBox'}).text
eval_num = float(eval_num.replace('\n',''))
eval_num


# In[79]:


categoryItems = spot.find('div', attrs={'class':'u_categoryTipsItem'})
categoryItems = categoryItems.find_all('dl')
# 楽しさだけとる
categoryItem = categoryItems[0]
category = categoryItem.dt.text
category


# In[82]:


rank = float(categoryItem.span.text)
rank


# In[89]:


details = {}
for categoryItem in categoryItems:
    category = categoryItem.dt.text
    rank = float(categoryItem.span.text)
    details[category] = rank


# In[95]:


datum = details
datum['観光地名'] = spot_name
datum['評点']=eval_num


# In[96]:


datum


# In[98]:


soup = BeautifulSoup(res.text, 'html.parser')
data = []
spots = soup.find_all('div', attrs={'class':'u_areaListRankingBox'})
for spot in spots:
    spot_name = spot.find('div', attrs={'class':'u_title'})
    spot_name.find('span', attrs={'class':'badge'}).extract()
    spot_name = spot_name.text.replace('\n','')
    eval_num = spot.find('div', attrs={'class':'u_rankBox'}).text
    eval_num = float(eval_num.replace('\n',''))
    categoryItems = spot.find('div', attrs={'class':'u_categoryTipsItem'})
    categoryItems = categoryItems.find_all('dl')
    details = {}
    for categoryItem in categoryItems:
        category = categoryItem.dt.text
        rank = float(categoryItem.span.text)
        details[category] = rank
    datum = details
    datum['観光地名'] = spot_name
    datum['評点']=eval_num
    datum
    data.append(datum)
data


# In[99]:


import pandas as pd


# In[100]:


df = pd.DataFrame(data)


# In[101]:


df


# In[105]:


df.columns


# In[108]:


df = df[['観光地名','評点','アクセス', '人混みの多さ', '景色', '楽しさ']]


# In[110]:


df.to_csv('観光地.csv', index=False)


# In[ ]:




