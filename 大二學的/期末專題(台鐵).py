#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


driver = webdriver.Chrome('C:/Users/ACER/Desktop/chromedriver.exe')
driver.get('http://railway.hinet.net/Foreign/TW/etno1.html')
driver.current_url


# In[3]:


#填身分證

inputId=driver.find_element_by_css_selector('#person_id')
inputId.send_keys('L125398618')


# In[6]:


#乘車日期，只有20天之內的日期，須改老恩選日期

driver.find_element_by_css_selector('#getin_date > option:nth-child(1)').click()


# In[7]:


#填起迄站，須改老恩，預設台北到台中

driver.find_element_by_css_selector('#from_station > option:nth-child(55)').click()
driver.find_element_by_css_selector('#to_station > option:nth-child(95)').click()


# In[8]:


#填車次代碼

inputNum=driver.find_element_by_css_selector('#train_no')
inputNum.send_keys('149')


# In[9]:


#點開始訂票

driver.find_element_by_css_selector('body > div > div.row.contents > div > form > div > div.col-xs-12 > button').click()


# In[ ]:


#填驗證碼

