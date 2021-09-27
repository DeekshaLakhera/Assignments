from pickle import *
import os
class ATM:
    pin=input("Enter your pin: ")
    def view(self):
        file = open(path+pin+'.pickle','rb')
        data=load(file)
        for d in data.items():
            print(d)
##        print("Account balance is : ",data['Amount'])
    def withdraw(self):
        wamt=int(input("Enter amount to withdrawl"))
        amt=data['Amount']
        data['Amount']=amt-wamt
        file = open(path+filen+'.pickle','wb')
        dump(data,file)
        file.close()
    def deposite(self):
        damt=int(input("Enter amount to deposite"))
        amt=data['Amount']
        data['Amount']=amt+damt
        file = open(path+pin+'.pickle','wb')
        dump(data,file)
        file.close()
os.chdir('E:\\Python Course\\python tutorial\\FileHandling\\Homewrk120821\\')
files=os.listdir()
os.chdir('../')
##print(files)
pf=[]
for file in files:
    if file.endswith('.pickle'):
        pf.append(file)
##print(pf)
path = "E:\\Python Course\\python tutorial\\FileHandling\\Homewrk120821\\"
pin=ATM.pin
a=ATM()
##pin = int(input("Enter Your Pin : "))
if (pin+'.pickle') in pf:
    print("Enter 1 to view balance")
    print("enter 2 to withdrawl")
    print("enter 3 to deposite")
    ch = int(input("Enter your choice : "))
    if ch==1:
        a.view()
    if ch==2:
        a.withdraw()
    if ch==3:
        a.deposite()

