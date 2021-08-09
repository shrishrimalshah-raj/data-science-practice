# Global Scope
globalVariable = 4


def func():
    # Global Scope
    global pi
    pi = 3.14
    # Local Scope
    x = 4
    y = 7
    print(x)
    print(globalVariable)


func()

print(pi)
