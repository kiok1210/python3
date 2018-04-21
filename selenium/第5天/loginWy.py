from time import sleep

class WyLogin():
	
    #登录
    def user_login(driver,username,pwd):
        sleep(1)
        print( driver.current_url )
        driver.switch_to.frame('x-URS-iframe')
        emailInput = driver.find_element_by_name("email")
        emailInput.clear()
        #emailInput.send_keys(username)#火狐执行无效
        email_id = emailInput.get_attribute("id")
        js = 'document.getElementById("'+email_id+'").value="'+username+'"'
        print(js)
        driver.execute_script(js)#执行js
        pwdInput = driver.find_element_by_name("password")
        pwdInput.clear()
        pwdInput.send_keys(pwd)
        dologin = driver.find_element_by_id("dologin").text
        dologin.click()

        print('网易邮箱登陆成功')
        
        driver.switch_to.default_content()
        

    #退出
    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()

    #写信
    def write(self,driver):
        #获取写信按钮：先获取包含‘写’字的span，再取它的上级li
        xx = driver.find_element_by_xpath('//span[contains( text(),"写" )]/parent::li')
        sx = driver.find_element_by_xpath('//span[contains( text(),"收" )]/parent::li')
        print('写：',xx.text,'--收：',sx.text)
        print('写：',xx.get_attribute('class'),'--收：',sx.get_attribute('class'))
        xx.click()

        #收件人
        sjr = driver.find_element_by_xpath('//input[@class="nui-editableAddr-ipt"]')
        sjr.clear()
        #sjrId = sjr.get_attribute('id')
        #js = 'document.getElementById('+sjrId+').innerText=448671246@qq.comWW'
        #driver.execute_script(js)
        sjr.send_keys('1130551075@qq.com')
        

        #主题
        zt = driver.find_element_by_xpath('//div[@class="bz0"]/div/input[@class="nui-ipt-input"]')
        #print( len(zt) )
        zt.send_keys('我是主题')

        #利用xpath获取frame 再switch_to
        frame = driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']")
        driver.switch_to.frame(frame)

        #等待1秒，再获取frame内容
        sleep(2)
        
        #内容
        bd = driver.find_element_by_xpath('//body[@class="nui-scroll"]')
        bd.send_keys('我是测试内容002')

        #返回主页面后，需要等待一下，否则可能定位不到元素
        driver.switch_to.default_content()
        sleep(2)

        #随便选择一个发送按钮，点击发送
        fs = driver.find_elements_by_xpath('//span[@class="nui-btn-text"]/parent::div[contains(@class,"nui-btn-hasIcon nui-mainBtn-hasIcon")]')
        print('fs len is ',len(fs))
        fs[0].click()#发送
        


        
            
            
            
        
        
