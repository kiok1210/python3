# conding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()

#隐式等待
driver.implicitly_wait(10)
driver.get("http://mail.163.com")

print('Before login----')

#打印当前页面title
title = driver.title
print(title)

#打印当前页面url
now_url = driver.current_url
print(now_url)


# 登录
"""
user = driver.find_element_by_id('idInput')
user.clear()
"""
user = driver.find_element_by_name('email')
print('user is ',user)

user.clear()
user.send_keys('kiokyw')

