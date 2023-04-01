def greet(*args,**kwargs):
    print(args)
    print(kwargs)
    print(kwargs.get("name"))
    print(kwargs.get("name01","Not found!"))

greet(1,2,3,4,name="guru",age=39)

def say_hi(name,age):
    print(name)
    print(age)

params1 = {'name': 'guru', 'age': 39}
say_hi(**params1)
params2 = ['john',38]
say_hi(*params2)

