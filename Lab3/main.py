# import serializers
# from serializers import JsonSerializer, XmlSerializer, SerializersFactory, SerializerType


import math
from serializers.src import factory

from Serializators.Factory import SerializerFactory

def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass

def MyGen(x):
    while x:

        x -= 1

def Gen(x):
    if x == 0:
        return 0
    if x == 1:
        return 0
    return Gen(x - 1) + Gen(x - 2)

# ser = factory.create_serializer('json')
# ser = factory.SerializersFactory.create_serializer(factory.SerializerType.XML)
# ser = factory.Factory.create_serializer(factory.JSON_DATA_TYPE)

ser = SerializerFactory.get_serializer('json')

# var = 15
# var_ser = ser.dumps(var)
# var_des = ser.loads(var_ser)
# print(var_des)

C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

c = C(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())


def f(a):
    for _ in a:
        yield _


gen = f([1, 2, 3 , 4])
print(next(gen))
f_s = ser.dumps(gen)
f_d = ser.loads(f_s)
print(next(f_d))
#lst = ()
#print(Gen(2))

# f = C(1, 2)
# print(f.my_sin(11))



