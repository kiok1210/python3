from xml.dom import minidom

try:
    dom = minidom.parse('data_info.xml')

    root = dom.documentElement

    print(root.nodeName)
    print(root.nodeValue)
    print(root.nodeType)
    print(root.ELEMENT_NODE)

    browser = root.getElementsByTagName('browser')
    print(browser[0].firstChild.data)
    
    browser2 = root.getElementsByTagName('browser2')
    print(browser2[0].firstChild.data)

    mails = root.getElementsByTagName('mail')
    for mail in mails:
        print(mail.firstChild.data)

    users = root.getElementsByTagName('user')
    i = 0
    for user in users:
        name = user.getElementsByTagName('name')
        i += 1
        print(i,'---',name[0].firstChild.data)
        pwd = user.getElementsByTagName('pwd')
        print(i,'---',pwd[0].firstChild.data)
    
    
except BaseException as msg:
    print(msg)
