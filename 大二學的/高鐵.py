#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver

#開瀏覽器

driver = webdriver.Chrome('C:/Users/ACER/Desktop/chromedriver.exe')
driver.get('https://irs.thsrc.com.tw/IMINT/?student=university')
driver.current_url

#點我同意

driver.find_element_by_css_selector('#btn-confirm').click()

#選擇站別，之後可以改老恩選擇器，預設台北到台中

driver.find_element_by_css_selector('#content > tbody > tr:nth-child(1) > td:nth-child(2) > span > select').click()
driver.find_element_by_css_selector('#content > tbody > tr:nth-child(1) > td:nth-child(2) > span > select > option:nth-child(3)').click()
driver.find_element_by_css_selector('#content > tbody > tr:nth-child(1) > td:nth-child(2) > select').click()
driver.find_element_by_css_selector('#content > tbody > tr:nth-child(1) > td:nth-child(2) > select > option:nth-child(8)').click()

#點依車次訂票

driver.find_element_by_css_selector('#bookingMethod_1').click()

#填寫日期

driver.find_element_by_css_selector('#toTimeInputField').clear()
inputDate = driver.find_element_by_css_selector('#toTimeInputField')
inputDate.send_keys('日期')

#填寫車次號碼

driver.find_element_by_css_selector('#toTrainID > input[type="text"]').click()
inputNum = driver.find_element_by_css_selector('#toTrainID > input[type="text"]')
inputNum.send_keys('車次號碼')

#填驗證碼


#點開始查詢

driver.find_element_by_css_selector('#SubmitButton').click()

#進入填資料頁面，填身分證

inputId=driver.find_element_by_css_selector('#idNumber')
inputId.click()
inputId.send_keys('身分證字號')

#填電話

driver.find_element_by_css_selector('#mobileInputRadio').click()
inputPhone = driver.find_element_by_css_selector('#mobilePhone')
inputPhone.send_keys('電話')

#填電子郵件

inputEmail=driver.find_element_by_css_selector('#name2622')
inputEmail.send_keys('電子郵件')

#點我同意

driver.find_element_by_css_selector('#content > table.table_simple > tbody > tr:nth-child(1) > td:nth-child(1) > input').click()

#點完成訂位

driver.find_element_by_css_selector('#isSubmit').click()

#關閉瀏覽器

driver.quit()


# In[ ]:




