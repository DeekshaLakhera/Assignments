from abc import ABC,abstractmethod
from math import *
class Base(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def sub(self,a,b):
        pass
    @abstractmethod
    def mul(self,a,b):
        pass
    @abstractmethod
    def div(self,a,b):
        pass
class SciClaci(Base):
    def getValue(self):
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        return a,b
    def add(self,a,b):
        s=a+b
        print("sum= ",s)
    def sub(self,a,b):
        s=a-b
        print("sub= ",s)
    def mul(self,a,b):
        s=a*b
        print("mul= ",s)
    def div(self,a,b):
        s=a/b
        print("div= ",s)
    def rvalue(self):
        self.a=int(input("Enter Radian value: "))
        return self.a
    def sine(self):
        print("sine value: ",sin(self.a))
    def cosine(self,a):
        print("cos value: ",cos(self.a))
    def tangent(self,a):
        print("tan value: ",cos(self.a))
print("enter 1 to add two numbers")
print("enter 2 to sub two numbers")
print("enter 3 to multiply two numbers")
print("enter 4 to divide two numbers")
print("enter 5 to get sine value")
print("enter 6 to get cos value")
print("enter 7 to get tan value")
ch=int(input("enter your choice"))
s=SciClaci()
if ch==1:
    a,b=s.getValue()
    s.add(a,b)
if ch==2:
    a,b=s.getValue()
    s.sub(a,b)
if ch==3:
    a,b=s.getValue()
    s.mul(a,b)
if ch==4:
    a,b=s.getValue()
    s.div(a,b)
if ch==5:
    s.rvalue()
    s.sine()
if ch==6:
    s.rvalue()
    s.cosine()
if ch==7:
    s.rvalue()
    s.tangent()
