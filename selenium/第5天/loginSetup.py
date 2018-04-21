# coding=utf-8
from selenium import webdriver
from time import sleep
from loginQq import QqLogin
from loginWy import WyLogin



class LoginSetup():
 
    #初始化，两个下划横杠
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        url = 'http://www.baidu.com'
        self.init_url = url
        self.driver.get(url)

    #登录
    def login(self):
        user_file = open('user_info.txt','r')
        lines = user_file.readlines()
        user_file.close()

        try:
            json_lines = []
            
            for line in lines:
                lineArr = line.split(',')
                mail_type = lineArr[0]
                mail = lineArr[1]
                username = lineArr[2]
                pwd = lineArr[3]

                # 打开浏览器窗口，定位当前窗口
                url = 'http://'+mail
                self.open_url(url)

                json_line = {}
                json_line['username'] = username
                json_line['pwd'] = pwd
                json_line['mail'] = mail
                json_line['mail_type'] = mail_type
                json_lines.append(json_line)
                #for end

            print(json_lines)
            self.open_login(json_lines)

            #关闭浏览器
            #self.driver.quit()

        except BaseException as error:
            print('error:',error)
            #self.driver.quit()
        #end login

    #打开新窗口
    def open_url(self,url):
        js = 'window.open("'+url+'")'
        print(js)
        self.driver.execute_script(js)
        '''
        win_handles = self.driver.window_handles
        print( len(win_handles) )
        for hand in win_handles:
            print( hand )
        
        cur_window = self.driver.current_window_handle
        self.driver.switch_to.window(cur_window)
        print('now url is ',self.driver.current_url)
        '''
        # win_handles = self.driver.window_handles
        #end open_url

    #定位新打开窗口,登录
    def open_login(self,json_lines):
        dr = self.driver
        cur_windows = dr.window_handles
        print( len(cur_windows) )
        username = ''
        pwd = ''
        mail_type = ''
    
        for cur_window in cur_windows:
            dr.switch_to.window(cur_window)
            cur_url = dr.current_url
            print('cur_url 1 = ',cur_url)

            for line in json_lines:
                mail = line['mail']
                mail_in = mail.replace('www.','')
                print(mail_in,cur_url)
                if mail_in in cur_url:
                    print('username')
                    mail_type = line['mail_type']
                    username = line['username']
                    pwd = line['pwd']

            
            print(mail_type,username)
                
            if username == '':
                continue

            #调用登录方法
            print('username is ',username)
            if 'QQ' in mail_type:
                QqLogin.user_login(dr,username,pwd)                    
            if 'WY' in mail_type:
                WyLogin.user_login(dr,username,pwd)     
            
        # end open_login

    
                
#调用登录方法
LoginSetup().login()

   
