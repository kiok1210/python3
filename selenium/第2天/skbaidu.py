from selenium import webdriver
from time import sleep

'''
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")

kw = driver.find_element_by_id("kw")
kw.send_keys('selenium2')
kw.clear()
kw.send_keys('love')
su = driver.find_element_by_id("su")
su.click()
'''

# driver.quit()
'''
driver.get("http://mail.126.com")
# email = driver.find_element_by_name("email")
driver.switch_to_frame('x-URS-iframe')
sleep(3)
email = driver.find_element_by_name("email")
email.send_keys('kiok111')
pwd = driver.find_element_by_name("password")
pwd.send_keys('19871210')
# dologin = driver.find_element_by_id("dologin")
# dologin.click()
js = 'document.getElementById("dologin").click()'


#driver.switch_to.default_content() #返回主frame

user = driver.find_element_by_id('spnUid').text
print(user)



driver.quit()
'''
s = '112'
b = '1123'
c = '2234'
if s in b:
    print(s,b)
if s in c:
    print(s,c)

sb =  s in b
print( sb)
print( s in c)

