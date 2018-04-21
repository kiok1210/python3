from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import ctime
from time import sleep

driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#driver = webdriver.Ie()

#设置隐式等待为10秒
driver.implicitly_wait(10)

url = 'http://www.126.com'
driver.get(url)
print("title is ",driver.title)

#element = WebDriverWait( driver,5, 0.5).until(
#    EC.presence_of_element_located((By.NAME,'wd'))
#    )

'''
try:
    idInput = driver.find_elements_by_xpath('//a')
    #等同
    #idInput = driver.find_elements_by_css_selector('a')
    print(len(idInput))
    for a in idInput:
        print(a.get_attribute('id') )
except:
    print("test error")

try:
    
    element = WebDriverWait( driver,10, 0.5).until(
       EC.presence_of_element_located((By.ID,'dologin'))
    )
    idInput = driver.find_elements_by_css_selector('input')
    print(len(idInput))
    for a in idInput:
        print(a.get_attribute('id') )
except:
    print("test error")
'''
#定位到iframe
try:
    sleep(10) #chrome下需要等待
    print( ctime(),'| url=',driver.current_url )
    #driver.switch_to.frame("x-URS-iframe")#定位到登录frame
    print('begin定位到x-URS-iframe')
    driver.switch_to.frame("x-URS-iframe")
    print('end定位到x-URS-iframe')
    

    inputs = driver.find_elements_by_xpath("//input")
    print( len(inputs) )
    for input in inputs:
        print('input id is ',input.get_attribute("id"),
              '| input name is ',input.get_attribute("name") )
        
    
    dologin = driver.find_element_by_id("dologin")
    email = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")
 
    print('email is_displayed ',email.is_displayed() )
    print('email is_enabled  ',email.is_enabled() )
    email.clear()
    #email.send_keys('kiokyw')#火狐此方法不行

    #调用js 输入成功
    
    email_id = email.get_attribute("id")
    js = "document.getElementById('"+email_id+"').value='kiokyw'"
    print(js)
    driver.execute_script(js)
   
    
    password.clear()
    password.send_keys('Yy19861121')

    print( 'email class = ', email.get_attribute('class') )
    print( 'email value = ', email.get_attribute('value') )
    print( 'password value = ', password.get_attribute('value') )

    
    js = "document.getElementById('dologin').click()"
    print(js)
    driver.execute_script(js)
    #dologin.click()#IE下此方法不行
    print('登录成功')


    #切回主frame
    driver.switch_to.default_content()

    #当前url
    now_url = driver.current_url
    print(now_url)

    #获取当前登录用户名
    user = driver.find_element_by_id('spnUid').text
    print(user)
    
except  BaseException as msg:
    print(msg)

print("关闭浏览器")
driver.quit()




