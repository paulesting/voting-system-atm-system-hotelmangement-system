import sys
import getpass
import time
import datetime
class Bank_Account:
    def __init__(self):
        self.balance=0
        self.amount=0
        self.amont=0
        self.tamount=0
        self.t=0
        self.d={'shayo':'1234','remond':'2345','toyin':'9001','josh':'0011'}
        self.a=list(self.d.keys())
        self.b=list(self.d.values())
        self.username=input('enter username:') 
        self.username=self.username.lower()
        self.counter=1
        self.delay=3
        self.c=['1234567890','0012334567','2222255555','0011223344']
        self.today=datetime.datetime.now()
        self.date=self.today.strftime('%B %d,%y')
        self.time=self.today.strftime('%H:%M')
        print('''
              #############################################################################
              ##                                                                         ##
              ##               welcome TO CEPHAS DIGITAL BANK ATM POINT                  ##
              ##                                                                         ##
              #############################################################################
              ''')
        
    def login_page(self):
        print(' kindly sign-in')
        self. counter=0
        #self.username=input('enter username:')
        self.username=self.username.lower()
        while self.username.lower() not in self.d.keys():
            print('DEAR',self.username.upper(),',\nyou have not register with us ,kindly visit our customer care for further enquries')
            sys.exit()
        while self.username.lower() in self.a:
            print('welcome',self.username.upper(),'\n','kindly enter your password')
            self.password=getpass.getpass('enter your password:')
            while  self.password!=self.b[self.a.index(self.username)]: 
                print('error!!!!,try again you have',2-self.counter,'more attempt')
                self.password=getpass.getpass('kindly re-enter your password:')
                self.counter+=1 
                if self.counter>=3:
                    print('your account has been deactivated,kindly visit our nearest branch')
                    sys.exit()
            if self.password==self.b[self.a.index(self.username)]:
                    self.count=0
                    self.delay=3
                    for i in range(self.delay,0,-1):
                        print('please wait while your account is being verify',self.delay+self.count,'secs')
                        time.sleep(1)
                        self.count-=1
                    print('login successful')
                    break
        self.accountno=self.c[self.a.index(self.username)]
    def deposit(self):
               print('''
                     ########################################################################
                     ##            press the following to deposit the specifyed amount:    ##
                     ########################################################################
                   1.500                                                                  5.10000
                   2.1000                                                                 6.15000
                   3.2000                                                                 7.50000
                   4.5000                                                                 8. other amount
                ''')
               self.option=input('select the amount you want to deposit:')
               while self.option not in['1','2','3','4','5','6','7','8']:
                   print('kindly pick option between 1-8')
                   self.option=input('pick the amount you want to deposit:')
               if self.option=='8':
                     print('enter the amount you to deposit:')
                     self.amount=input('enter amount to deposit here:')
                
                     while  not self.amount.isdecimal():
                        print('error!!!!!! kindly enter floating nimber:')
                        self.amount=input('enter amount to deposit  here:')
               elif self.option=='1':
                    self.amount=500
               elif self.option=='2':
                      self.amount=1000
               elif self.option=='3':
                      self.amount=2000
               elif self.option=='4':
                      self.amount=5000
               elif self.option=='5':
                      self.amount=10000
               elif self.option=='6':
                      self.amount=15000
               elif self.option=='7':
                      self.amount=50000
               self.amount=float(self.amount)
               self.balance+=self.amount
               print('\n AMOUNT DEPOSITED=','#',self.amount)
    def withdraw(self):
                print('''
                      #########################################################################
                      ##         press the following to withdraw the specifyed amount:       ##
                      #########################################################################
                   1.500                                                                  5.10000
                   2.1000                                                                 6.15000
                   3.2000                                                                 7.50000
                   4.5000                                                                 8. other amount
                ''')
    
                option=input('pick the amount you want to withdraw:')
                while option not in['1','2','3','4','5','6','7','8']:
                   print('kindly pick option between 1-8')
                   option=input('pick the amount you want to withdraw:')
                if option==8:
                     print('enter the amount you to withdraw:')
                     self.amont=input('enter amount to withdraw here:')
                
                     while  not self.amont.isdecimal():
                        print('error!!!!!! kindly enter floating nimber:')
                        self.amont=input('enter amount to withdraw here:')
                elif option=='1':
                    self.amont=500
                elif option=='2':
                      self.amont=1000
                      print('you want to withdraw #1000 ')
                elif option=='4':
                      self.amont=2000
                elif option=='4':
                      self.amont=5000
                elif option=='5':
                      self.amont=10000
                elif option=='6':
                      self.amont=15000
                elif option=='7':
                      self.amont=50000
                self.amont=float(self.amont)
                if self.balance>=float(self.amont):
                 self.balance-=self.amont
                 print('\n you withdraw #',self.amont)
                else:
                    print('\n insufficient balance')
    def account_balance(self):
                print('\n account balance=#',self.balance)
    def Transfer(self):
        print('''
              ########################################################################
              ##                welcome to bank transfer page                       ##
              ########################################################################
                              kindly pick the bank you want to transfer to
            1.cephas digital bank                                2.city bank
            3.kuda microfinance bank
        ''')
        self.bank=input('choose the bank you want to transfer to:')
        while self.bank not in('1','2','3'):
            print('error!!!!!you have input an invalid number,kindly try again')
            self.bank=input('choose the bank you want to transfer to:')
        if self.bank=='1':
            print('you want to transfer to CEPHAS DIGITAL BANK:')
            self.user=input('enter 10 digit customer account number:')
            while self.user not in self.c:
                print('error!!!!!,you enter an unregistered account number,kindly enter again:')
                self.user=input('enter 10 digit customer username:') 
            self.tamount=input('enter the amount you want to transfer here:')
            while  not self.tamount.isdecimal():
                print('error!!!1,kindly enter digit not alphebet:')
                self.tamount=input('enter the amount you want to transfer here:')
            self.tamount=float(self.tamount)
            if self.balance>=self.tamount:
                print('you want to transfer #',self.tamount,'to',self.a[self.c.index(self.user)])
                print('if you want to proceed press 1 press 2 to cancel:')
                k=input('enter responses:')
                while k not in['1','2']:
                    print('invalid input,kindlyr re-enter again:')
                    k=input('enter responses,enter 1 to procced and 2 to cancel:')
                if  k=='1':
                    self.balance-=self.tamount
                    self.t+=self.tamount
                    print('\n you have successful transfer #',self.tamount,'to',self.a[self.c.index(self.user)],'with accountnumber',self.user.upper())
                else:
                    print('you have been log out,kindly login to start again:')
                    sys.exit()
            else:
                self.t+=0
                print('\n insufficient balance\ntransfer error!!!!')
        elif self.bank=='2': 
             print('you want to transfer to CITY BANK:')
             self.user=input('enter 10 digit customer username or account number:')
             while len(self.user)!=10:
                 print('error,you have input invalid account number,kindly re-enter again:')
                 self.user=input('enter 10 digit customer username or account number:')
             self.tamount=input('enter the amount you want to transfer here:')
             while not self.tamount.isdecimal():
                 print('error!!!!! kindly enter floating number:')
                 self.tamount=input('enter the amount you want to transfer here:')
             self.tamount=float(self.tamount)
             if self.balance>=self.tamount:
                 print('you want to transfer',self.tamount,'to',self.user)
                 print('if you want to proceed press 1 press 2 to cancel:')
                 k=input('enter responses:')
                 while k not in['1','2']:
                    print('invalid input,kindlyr re-enter again:')
                    k=input('enter responses,enter 1 to procced and 2 to cancel:')
                 if  k=='1':
                    self.balance-=self.tamount
                    self.t+=self.tamount
                    print('\n you have successful transfer #',self.tamount,'to',self.user)
                 else:
                    print('you have been log out,kindly login to start again:')
                    sys.exit()
             else:
                 self.t+=0
                 print('\n insufficient balance\ntransfer error!!!!')
        elif self.bank=='3': 
             print('you want to transfer to KUDA MIRCOFINANCE BANK:')
             self.user=input('enter 10 digit customer username or account number:')
             while len(self.user)!=10:
                 print('error,you have input invalid account number,kindly re-enter again:')
                 self.user=input('enter 10 digit customer username or account number:')
             self.tamount=input('enter the amount you want to transfer here:')
             while not self.tamount.isdecimal():
                 print('error!!!!! kindly enter floating number:')
                 self.tamount=input('enter the amount you want to transfer here:')
             self.tamount=float(self.tamount)
             if self.balance>=self.tamount:
                 print('you want to transfer #',self.tamount,'to',self.user)
                 print('if you want to proceed press 1 press 2 to cancel:')
                 k=input('enter responses:')
                 while k not in['1','2']:
                    print('invalid input,kindlyr re-enter again:')
                    k=input('enter responses,enter 1 to procced and 2 to cancel:')
                 if  k=='1':
                    self.balance-=self.tamount
                    self.t+=self.tamount
                    print('\n you have successful transfer #',self.tamount,'to',self.user)
                 else:
                    self.t+=0
                    print('you have been log out,kindly login to start again:')
                    sys.exit()
             else:
                 print('\n insufficient balance\ntransfer error!!!!')    
    def change_pin(self):
        self.c=['1234567890','0012334567','2222255555','0011223344']
        print('''
                  ###############################################################
                  ##            welcome to pin change page                     ##
                  ################################################################
              ''')
        self.use=input('enter your 4 digit old pin:')
        #user=float(user)
        while not self.use.isdecimal() :
            print('error!!!,kindly enter your 4 didit old password:')
            self.use=input('re-enter your 4 digit old pin:')
        self.r=input('kindly verify by enter your account number:')
        while self.r not in self.c:
            print('you enter and invalid account number:')
            self.r=input('kindly verify by enter your account number:')
        while not self.c[self.c.index(self.r)]  :
            print('invalid account number,kindly re-enter your account number 10digit')
            self.r=input('kindly verify by enter your account number:')
        while self.b.index(self.use)!=self.c.index(self.r):
            print('error!!!! unable to verify kindly try again:')
            self.use=input('enter your 4 digit old pin:')
            self.r=input('kindly verify by enter your account number:')
        print('verification was successful:')
        self.newpin=input('enter your new four digit new pin here:')
        while len(self.newpin)!=4:
            print('error, enter 4 digitnumber:')
            self.newpin=input('enter your new four digit new pin here:')
        self.b[self.b.index(self.use)]=self.newpin
        print('your password has been changed successfully:')
    def print_receipt(self):
        print(''' 
                   ###################################################
                   ##           CEPHAS DIGITAL BANK RECEIPT         ##
                   ###################################################
              ''')
        print('              Transaction    History                           ')
        print('DATE:',self.date)
        print('TIME:',self.time)
        print('CUSTOMER USERNAME=',self.username)
        print('CUSTOMER ACCOUNT NO=',self.accountno)
        print('AMOUNT DEPOSITED=',self.amount)
        print('AMOUNT WITHDRAW=#',self.amont)
        print('AMOUNT TRANSFER=#',self.t)
        print('ACCOUNT BALANCE:#',self.balance)
        print('DEAR',self.username.upper(),'THANKS FOR BANKING WITH US\nWE PROMISE YOU THE BEST\nWE LOVE YOU')
    def accounttransaction(self): 
        m= self.amount
        mo=str(m)
        o=self.amont
        oo=str(o)
        t=self.t
        to=str(t)
        f=self.balance 
        fo=str(f)
        f=open('trying.doc','a') 
        f.write('              Transaction    History                           ')
        f.write('\n')
        f.write('DATE:')
        f.write(self.date)
        f.write('\n')
        f.write('TIME:')
        f.write(self.time)
        f.write('\n')
        f.write('CUSTOMER USERNAME=')
        f.write(self.username)
        f.write('\n')
        f.write('CUSTOMER ACCOUNT NO=')
        f.write(self.accountno)
        f.write('\n')
        f.write('AMOUNT DEPOSITED=#')
        f.write(mo)
        f.write('\n')
        f.write('AMOUNT WITHDRAW=#')
        f.write(oo)
        f.write('\n')
        f.write('AMOUNT TRANSFER=#')
        f.write(to)
        f.write('\n')
        f.write('ACCOUNT BALANCE:#')
        f.write(fo)
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.close()
    def another_trasaction(self):   
        self.password=getpass.getpass('enter your password:')
        counter=0
        while  self.password!=self.b[self.a.index(self.username)]: 
                 print('error!!!!,try again you have',2-counter,'more attempt')
                 self.password=getpass.getpass('kindly re-enter your password:')
                 counter=1 
                 if counter>=3:
                     print('your account has been deactivated,kindly visit our nearest branch')
                     sys.exit()
        if self.password==self.b[self.a.index(self.username)]:
            print('login successful')
        
c=Bank_Account()
choice=1

while choice!='0':
    c.login_page()
    print('''
          press 1 to deposit
          presss 2 to withdraw
          press 3 to check account balance
          press 4 to transfer
          press 5 to change ATM PIN
          press 6 to view account trasaction
          press 7 to quit
          ''')
    d=input('enter your option:')
    while d not in['1','2','3','4','5','6','7']:
        print('error!!!!,you enter and invalid key,re-enter again:')
        d=input('enter your option:')
    if d=='1':
        c.deposit()
    elif d=='2':
        c.withdraw()
    elif d=='3':
        c.account_balance()
    elif d=='4':
        c.Transfer()
    elif d=='5':
        c.change_pin()
    elif d=='6':
        c.print_receipt()
    elif d=='7':
        print('you have successfully logout:')
        print('THANKS FOR BANKING WITH US')
        sys.exit()
    c.accounttransaction()
    print('press 1 to carry out another transaction and press 0 to quit:')
    #c.another_trasaction()
    choice=input()
    while not choice in ['1','0']:
        print('error!!!,invalid key')
        choice=input('re-enter another value')
    
