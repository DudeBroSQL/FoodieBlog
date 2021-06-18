
def decFunc(func):
    print('decoration pre inner function execution')
    def inner1(*args, **kwargs): 
        func(*args, **kwargs) 
    print('decorator execution post inner function')
    return inner1

@decFunc   
def pnm(name):
    print(name)






pnm('seanC')




