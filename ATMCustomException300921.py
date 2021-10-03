import pickle as pk
class ATME(Exception):
    def __init__(self,am=''):
        print("Exception")
def WD(dw):
    if dw<=0:
        try:
            raise ATME("Amount is below 0rs.")
        except ATME as e:
            print(e)
    
def choice():
    print("Enter 1 to withdraw")
    print("Enter 2 to deposite")
    ch=int(input("enter your choice"))
    if ch==1:
        withdraw()
    if ch==2:
        deposite()
def withdraw():
    wmt = int(input("enter amount to withdraw"))
    WD(wmt)
    amt = data['Amount']
    if wmt<amt and wmt%100==0:
        amt=amt-wmt
        filepath='E:\\Python Course\\python tutorial\\FileHandling\\Homewrk120821\\'
        file = open(filepath+str(pin)+'.pickle','wb')
        data['Amount']=amt
        pk.dump(data,file)
        file.close()
        print("Balance Amount = ",amt)
    else:
        print("Invalid Amount")

def deposite():
    dmt = int(input("enter amount to deposite"))
    WD(dmt)
    amt = data['Amount']
    if dmt%100==0:
        amt=amt+dmt
        filepath='E:\\Python Course\\python tutorial\\FileHandling\\Homewrk120821\\'
        file = open(filepath+str(pin)+'.pickle','wb')
        data['Amount']=amt
        pk.dump(data,file)
        file.close()
        print("Balance Amount = ",amt)
    else:
        print("Invalid Amount")    
try:
    filepath='E:\\Python Course\\python tutorial\\FileHandling\\Homewrk120821\\'
    pin = int(input("Enter your Pin :"))
    file = open(filepath+str(pin)+'.pickle','rb')
    data=pk.load(file)
    print(data)
    choice()
except FileNotFoundError:
    print("Please Enter Correct Pin")
except ValueError:
    print("Pin must be in integer")
