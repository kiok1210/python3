user_file = open('user_info.txt','r')
lines = user_file.readlines()
user_file.close()

for line in lines:
    mail = line.split(',')[0]
    username = line.split(',')[1]
    pwd = line.split(',')[2]
    print(mail,username,pwd)

