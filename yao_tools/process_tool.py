# -*- coding: UTF-8 -*-
import threading

'''
线程管理类
version:0.1 
author:yaowei
date:2018-04-10
'''


class MyThread(threading.Thread):

    def __init__(self, func, args, name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

