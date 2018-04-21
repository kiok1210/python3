from selenium import webdriver
from time import sleep

#自动打开邮箱主页登录
#dr = webdriver.Firefox()
dr = webdriver.Chrome()
#dr = webdriver.Ie()
dr.get("http://mail.163.com")
sleep(2)
dr.switch_to.frame("x-URS-iframe")
idInput = dr.find_element_by_xpath('//input[@name="email"]')
pwdInput = dr.find_element_by_xpath('//input[@name="password"]')
idInput.clear()
idInput.send_keys("kiokyw")
pwdInput.clear()
pwdInput.send_keys("Yy19861121")

dr.find_element_by_id('dologin').click()

dr.quit()
