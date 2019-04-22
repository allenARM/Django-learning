lambda x: x**2

x = 50

def func():
    global x
    x = 1000

func()
print(x)
