# conding=unicode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
#加载

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
#driver = webdriver.Ie()


#打开百度
driver.get("http://www.baidu.com")

#搜索Selenium2


try:
    kw = driver.find_element_by_id("kw")
    su = driver.find_element_by_id("su")
   
except:
    print ('element does not exist')

print("kw is " , kw.is_enabled() ) #判断元素是否有效

assert "百度" in driver.title
kw.send_keys('selenium2')

#tab的定位相相于清除了密码框的默认提示信息，等同上面的clear()
su.click()

#退出
driver.quit()

