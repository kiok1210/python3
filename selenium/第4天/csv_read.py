import csv

data = csv.reader( open('csv_read.csv', 'r') )

for user in data:
    print(user)
    print('url = ',user[0],' | user = ',user[1], ' | pwd = ', user[2])
