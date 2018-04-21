from time import sleep, ctime
import threading
from _datetime import datetime
import time as stime
import multiprocessing

def music(func,loop):
    for i in range(loop):
        print('music', func, ctime())
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print('movie', func, ctime())
        sleep(4)

def testOne():
    music('简单的歌', 2)
    movie('两杆大烟枪', 2)
    print('all end', ctime())

def testTwo():
    threads = []
    t1 = threading.Thread(target=music, args=('喜欢的人',2) )
    threads.append(t1)

    t2 = threading.Thread(target=movie, args=('搏击俱乐部',2) )
    threads.append(t2)

    t3= threading.Thread(target=music, args=('喜欢的人2', 2))
    threads.append(t3)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print('all end', ctime())

class MyThread(threading.Thread):

    def __init__(self, func, args, name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def super_play(file_,time):
    for i in range(3):
        print('play', file_, ctime())
        sleep(time)


def time(args):
    pass


def testThree():
    threads = []
    lists = {'气球.mp3': 3, '电影.rmvb': 4, 'last.avg' : 2}
    for file_, time_ in lists.items():
        t = MyThread(super_play, (file_, time_), super_play.__name__)
        threads.append(t)

    files = range(len(lists))

    for f in files:
        threads[f].start()
    for f in files:
        threads[f].join()

    print('all end', ctime())


def testRun(num,time_):
    for i in range(3):
        print('num=', num, ctime())
        sleep(time_)


def threadsRun():
    # self.readPageOne(122)

    threads = []

    for i in range(1, 123):
        num = str(i)
        print(num)
        #t = MyThred(testRun, (num), self.testRun.__name__)
        t1 = threading.Thread(target=testRun, args=(num, 2))
        t2 = threading.Thread(target=testRun, args=(num, 3))
        t3 = threading.Thread(target=testRun, args=(num, 4) )
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
        # t.join()

    print('all end: %s' % ctime())

def processRun():
    # self.readPageOne(122)

    threads = []

    for i in range(1, 123):
        num = str(i)
        print(num)
        #t = MyThred(testRun, (num), self.testRun.__name__)
        t1 = multiprocessing.Process(target=testRun, args=(num, 2))
        t2 = multiprocessing.Process(target=testRun, args=(num, 3))
        t3 = multiprocessing.Process(target=testRun, args=(num, 4) )
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
        # t.join()

    print('all end: %s' % ctime())

if __name__ == '__main__':
    # testOne()
    # testTwo()
    # testThree()
    now = int(stime.time())
    print('now:', now)

    date = datetime.now()
    print('all begin ', ctime(), '开始！')

    processRun()

    now2 = int(stime.time())
    print('now2', now2)

    nowdate = now2 - now
    print('共', nowdate, '秒')

    print('all end ', ctime(), '完毕！')
