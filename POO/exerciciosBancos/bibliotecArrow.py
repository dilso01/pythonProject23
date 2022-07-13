import arrow

data = arrow.now()
print(data)

data = arrow.now().format("DD/MM/YYYY")
print(data)

data = arrow.now().format("HH:mm:ss")
print(data)

data = arrow.get(25315326)
print(data)


date_1 = arrow.get('1983-09-26 18:40:48','YYYY-MM-DD HH:mm:ss')
date_2 = arrow.get('2022-07-14 13:18:20','YYYY-MM-DD HH:mm:ss')
diff = date_2 - date_1
print(diff)