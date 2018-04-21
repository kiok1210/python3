from selenium import webdriver
from public import Login
from time import sleep

#打开谷歌浏览器
dr = webdriver.Chrome()

#隐式等待10秒，等待页面元素加载完毕
dr.implicitly_wait(10)

#打开网页
url = 'http://mail.163.com'
dr.get(url)

#沉睡等待一秒后定位frame
sleep(1)
dr.switch_to.frame('x-URS-iframe')

try:
    #调用登录模块
    Login().user_login(dr)
    print('登录成功')
except BaseException as msg:
    print(msg)
    dr.quit()


#返回主frame
dr.switch_to.default_content()
sleep(1)

try:
    #退出
    Login().write(dr)
    print('写信成功')
except BaseException as msg:
    print(msg)
    sleep(1)
    dr.quit()


sleep(1)
try:
    #退出
    Login().user_logout(dr)
    print('退出成功')
except BaseException as msg:
    print(msg)
    dr.quit()

