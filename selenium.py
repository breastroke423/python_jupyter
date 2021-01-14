#!/usr/bin/env python
# coding: utf-8

# In[19]:


get_ipython().system('pip install selenium')


# In[2]:


from selenium import webdriver


# In[38]:


import pandas as pd


# In[22]:





# In[6]:


# ブラウザを開く
browser = webdriver.Chrome('chromedriver.exe')
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
# URLに飛ぶ
browser.get(url)
# ユーザーネームとパスワードを自動入力後クリック。検証ツールから一意のタグを見つけてきて入力。今回はidをつかう。
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()


# In[19]:


# ある文字をとってきて表示
elem_name = browser.find_element_by_id('name')
name = elem_name.text
elem_company = browser.find_element_by_id('company')
company = elem_company.text
elem_birthday = browser.find_element_by_id('birthday')
birthday = elem_birthday.text
elem_come_from = browser.find_element_by_id('come_from')
come_from = elem_come_from.text
elem_hobby = browser.find_element_by_id('hobby')
hobby = elem_hobby.text


# In[20]:





# In[22]:


# 改行のｎを削除
hobby.replace('\n',',')


# In[34]:


# 複数のタグの内容をとってくる
elems_th = browser.find_elements_by_tag_name('th')
# 配列に入れてみる
keys =[]
# for文ですべて表示する
for elem in elems_th:
    key = elem.text
    keys.append(key)
keys


# In[37]:


# 複数のタグの内容をとってくる
elems_td = browser.find_elements_by_tag_name('td')
# 配列に入れてみる
values =[]
# for文ですべて表示する
for elem in elems_td:
    value = elem.text.replace('\n',',')
    values.append(value)
values


# In[39]:


df = pd.DataFrame()


# In[40]:


df['項目'] = keys
df['値'] = values


# In[41]:


df


# In[44]:


df.to_csv('講師情報.csv', index = False)


# In[ ]:




