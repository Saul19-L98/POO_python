def f1(object):
    def wrapper(*args, **kwargs):
        # print('started')
        value = object(*args, **kwargs)
        # print('ended')
        return value

    return wrapper

@f1
def run(a,b):
    print(a,b) 

@f1
def plus(x,y):
    return x + y

if __name__ == "__main__":
    run(8,4)
    print(plus(4,7))
