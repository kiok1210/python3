from selenium import webdriver
from time import sleep

class QqLogin():

    def user_login(dr,username,pwd):

        print(username,pwd)
        
        dr.switch_to.frame("login_frame")
        idInput = dr.find_element_by_id('u')
        pwdInput = dr.find_element_by_id('p')
        idInput.clear()
        idInput.send_keys(username)
        pwdInput.clear()
        pwdInput.send_keys(pwd)

        #登录
        dr.find_element_by_id('login_button').click()

        #返回上级frame
        #dr.switch_to.parent_frame()

        #返回主frame,此处两个方法都可以
        dr.switch_to.default_content()

        #调用返回主frame需要等一下
        sleep(1)

        switchs = dr.find_elements_by_css_selector('div')
        print( len(switchs) )

        #获取登录用户名、邮箱
        name = dr.find_element_by_id('useralias')
        email = dr.find_element_by_id('useraddr')
        print('qq登录成功|',name.text,'---',email.text)

        #dr.quit()
