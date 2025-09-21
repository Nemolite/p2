import time

print("test")

# Циклы
# while
a = 1
b = 10

while a<b:
    print(a,b,sep='|')
    a+=1

c = 1
d =10

while d>c:
    print(d,c,sep='||')
    d-=1
else:
    print(d, c, sep='||',end=' Цикл завершен')

k = 1
m = 10
while True:
    if m>k:
        print('*'*k)
        k+=1
    else:
        print(f'Цикл завершен')
        break


# for

for n in range(10):
    print(n, end=" ")

print(end='\n')


str1 = 'Hello World'

for c in str1:
    print(c)


print("Загрузка", end="", flush=True)
for i in range(10):
    time.sleep(1)
    print(".", end="", flush=True)