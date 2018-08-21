import random
import weakref

from tests.common import BaseCase

from dateutil import parser
import datetime


class Field(object):
    base_type = None

    def __init__(self, default, doc):
        self.default = default
        self.data = weakref.WeakKeyDictionary()

    def to_api(self):
        pass

    def from_api(self, value):
        pass

    def __get__(self, instance, owner):
        result = self.data.get(instance, self.default)
        # result = self.to_api()
        return result

    def __set__(self, instance, value):
        print('Setting')
        # self.from_api(value)
        self.data[instance] = value


class DateTimeField(Field):
    base_type = datetime.datetime

    # def set(self, value):
    #     if not isinstance(value, self.base_type):
    #         raise TypeError('%s is not a %s' % (value, self.base_type))
    #     self.value = value
    #     return self

    def to_api(self):
        return self.val.isoformat() + 'Z'

    def from_api(self, value):
        from dateutil.parser import parse
        self.val = parse(value)


class X(object):
    a = DateTimeField(datetime.datetime.utcnow, 'the A')

    def __init__(self, a):
        """

        :param a: Doc string for A
        :type a: Doc string for A
        """
        self.a = a

    @property
    def foobar(self):
        """Do something useful"""
        print('magic')
        return 'wat'

    @foobar.setter
    def foobar(self, v):
        print('magoo', v)

    def to_json(self):
        return dict(a=self.a)

class Y(X):
    @property
    def foobar(self):
        """Do something useful"""
        print('magic2')
        return 'wat2'

    @foobar.setter
    def foobar(self, v):
        print('magoo2', v)


class TestExperimental(BaseCase):
    def test1(self):
        x = Y(datetime.datetime.utcnow())
        x.foobar
        x.foobar = 5

    def test(self):
        x = X(datetime.datetime.utcnow())
        print('initial', x.a)
        print(x.a.val)
        x.a = datetime.datetime.utcnow()
        print(x.foobar)
        print(x)
        print(x.a)
        print(x.to_json())
        print(type(x.a))