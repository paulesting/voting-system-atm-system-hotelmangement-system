import math,random
import sys
import matplotlib.pyplot as plt
import time
#import pyttsx3
class VotingSystem:
    def __init__(self,eVoters='',logindetails='',Edepartment='',Department='',Mdepartment='',department='',sex='',MatricNo='',password='',pword='',MatricNo1='',password1='',pword1='',string='',AuthCode='',length='',Pcandidate1='',Pcandidate2='',Pcandidate3='',Pcandidate4=''):
        print('''--------------------------------------------
                 -                                          -
                 -                                          -
                 -             E-VOTING SYSTEM              -
                 -                                          -
                 -                 by LEON                             -
                 --------------------------------------------''')
        self.eVoters=eVoters
        self.logindetails=logindetails
        self.department=department
        self.sex=sex
        self.MatricNo=MatricNo
        self.password=password
        self.pword=pword
        self.MatricNo1=MatricNo1
        self.password1=password1
        self.pword1=pword1
        self.string=string
        self.AuthCode=AuthCode
        self.length=length
        self.Pcandidate1=Pcandidate1
        self.Pcandidate2=Pcandidate2
        self.Pcandidate3=Pcandidate3
        self.Pcandidate4=Pcandidate4
        self.Edepartment=Edepartment
        self.Mdepartment=Mdepartment
        self.Department=Department
    def RegistrationPage(self):
        #self.Department=[]
        #self.Edepartment=['CHEMICAL ENGINEERING','AGRICULTURAL ENGINEERING','MECHANICAL ENGINEERING','COMPUTER ENGINEERING', 'FOOD SCIENCE ENGINEERING','ELECTRICAL AND ELECTRONIC ENGINEERING']
        #self.Mdepartment=['ACCOUNTING','TRANSPORT MANAGEMENT','ECONOMICS']
        Voters=input("Enter Number of voters:")
        self.eVoters=int(Voters)
        self.logindetails=[]
        for i in range(0,self.eVoters):
            #department=input('Enter Department:')
            #self.department=department.upper()
           # self.Department.append(self.department)
            #self.sex=input('Sex:')
            self.MatricNo=input('Matric No:')
            self.password=input('Enter Password:')
            self.pword=self.MatricNo+self.password
            self.logindetails.append(self.pword)
    def LoginPage(self):
        self.Pcandidate=0 
        self.Pcandidate1=0 
        self.Pcandidate2=0
        self.Pcandidate3=0
        self.Pcandidate4=0
        self.VPcandidate=0 
        self.VPcandidate1=0 
        self.VPcandidate2=0
        self.VPcandidate3=0
        self.VPcandidate4=0
        self.Gcandidate=0 
        self.Gcandidate1=0 
        self.Gcandidate2=0
        self.Gcandidate3=0
        self.Gcandidate4=0
        self.Fcandidate=0 
        self.Fcandidate1=0 
        self.Fcandidate2=0
        self.Fcandidate3=0
        self.Fcandidate4=0
        self.PRcandidate=0 
        self.PRcandidate1=0 
        self.PRcandidate2=0
        self.PRcandidate3=0
        self.PRcandidate4=0
        for i in range(0,self.eVoters):
            self.MatricNo1=input("MATRIC NO:")
            self.password1=input("PASSWORD:")
            self.pword1=self.MatricNo1+self.password1
            while self.pword1 not in self.logindetails:               
                print("Incorrect details, enter again")
                self.MatricNo1=input("Matric No:")
                self.password1=input("Password:")
                self.pword1=self.MatricNo1+self.password1
            else:
                    self.string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    self.AuthCode=""
                    self.length=len(self.string)
                    for i in range(6):
                        self.AuthCode+=self.string[math.floor(random.random()*self.length)]
                    print(self.AuthCode)
                      
            res=input("Enter Authentication Code:")
            if res==self.AuthCode:
                
                    print('STUDENT UNION GOVERNMENT ELECTION')
#                     friend=pyttsx3.init()
#                     speech='Welcome, please vote for your favorite candidate'
#                     friend.say(speech)
#                     friend.runAndWait()
                    print('''PRESIDENTIAL CANDIDATES''')
                    print('''
                          1. LEON
                          2. FAMOUS
                          3. ANUOLUWA
                          4. EINSTEIN''')
                    ans=input('')
                    if ans=='1':
                        self.Pcandidate1+=1
                    elif ans=='2':
                        self.Pcandidate2+=1
                    elif ans=='3':
                        self.Pcandidate3+=1
                    elif ans=='4':
                        self.Pcandidate4+=1
                    else:
                        self.Pcandidate+=0
                
                
                           
                    print('''VICE PRESIDENTIAL CANDIDATES''')
                    print('''
                          1. MEG
                          2. SALVATION
                          3. TOPE
                          4. SHAYO''')
                    ans=input('')
                    if ans=='1':
                        self.VPcandidate1+=1
                    elif ans=='2':
                        self.VPcandidate2+=1
                    elif ans=='3':
                        self.VPcandidate3+=1
                    elif ans=='4':
                        self.VPcandidate4+=1
                    else:
                        self.VPcandidate+=0
                        
                 
                    print('''GENERAL SECRETARY CANDIDATES''')
                    print('''
                          1. TOLUENE
                          2. RAIN
                          3. Blessing
                          4. IFEOLUWA''')
                    ans=input('')
                    if ans=='1':
                        self.Gcandidate1+=1
                    elif ans=='2':
                        self.Gcandidate2+=1
                    elif ans=='3':
                        self.Gcandidate3+=1
                    elif ans=='4':
                        self.Gcandidate4+=1
                    else:
                        self.Gcandidate+=0
                
                 
                    print('''FINANCIAL SECRETARY CANDIDATES''')
                    print('''
                          1. CHRISTOPHER
                          2. FEMI
                          3. DOLLAR
                          4. NAIRA''')
                    ans=input('')
                    if ans=='1':
                        self.Fcandidate1+=1
                    elif ans=='2':
                        self.Fcandidate2+=1
                    elif ans=='3':
                        self.Fcandidate3+=1
                    elif ans=='4':
                        self.Fcandidate4+=1
                    else:
                        self.Fcandidate+=0
                        
                 
                
                    print('''PRO CANDIDATES''')
                    print('''
                          1. PODEM
                          2. STARCO
                          3. SAOLA
                          4. PRECIOUS''')
                    ans=input('')
                    if ans=='1':
                        self.PRcandidate1+=1
                    elif ans=='2':
                        self.PRcandidate2+=1
                    elif ans=='3':
                        self.PRcandidate3+=1
                    elif ans=='4':
                        self.PRcandidate4+=1
                    else:
                        self.PRcandidate+=0
        
            else:
                print("Error!")
                res=input("Enter Authentication Code:")
    def Result(self):
        try:
            print('''PRESIDENTIAL CANDIDATES''')
            print("LEON",self.Pcandidate1,"votes")
            print("FAMOUS",self.Pcandidate2,"votes")
            print("ANUOLUWA",self.Pcandidate3,"votes")
            print("EISTEIN",self.Pcandidate4,"votes")

            values =[self.Pcandidate1,self.Pcandidate2,self.Pcandidate3,self.Pcandidate4]
            colors = ['g','r','y','b']

            labels = ['LEON', 'FAMOUS', 'ANUOLUWA','EISTEIN']
            plt.pie(values, colors= colors, labels=labels, autopct='%1.1f%%')
            plt.title('PRESIDENTIAL ELECTION RESULTS')
            plt.show()

            print('''VICE PRESIDENTIAL CANDIDATES''')
            print("MEG",self.VPcandidate1,"votes")
            print("SALVATION",self.VPcandidate2,"votes")
            print("TOPE",self.VPcandidate3,"votes")
            print("SHAYO",self.VPcandidate4,"votes")

            values =[self.VPcandidate1,self.VPcandidate2,self.VPcandidate3,self.VPcandidate4]
            colors = ['g','r','y','b']
            labels = ['MEG', 'SALVATION', 'TOPE','SHAYO']
            plt.pie(values, colors= colors, labels=labels, autopct='%1.1f%%')
            plt.title('VICE PRESIDENTIAL ELECTION RESULTS')
            plt.show()

            print('''GENERAL SECRETARY CANDIDATES''')
            print("TOLUENE",self.Gcandidate1,"votes")
            print("RAIN",self.Gcandidate2,"votes")
            print("BLESSING",self.Gcandidate3,"votes")
            print("IFEOLUWA",self.Gcandidate4,"votes")

            values =[self.Gcandidate1,self.Gcandidate2,self.Gcandidate3,self.Gcandidate4]
            colors = ['g','r','y','b']

            labels = ['TOLUENE', 'RAIN', 'BLESSING','IFEOLUWA']
            plt.pie(values, colors= colors, labels=labels, autopct='%1.1f%%')
            plt.title('GENERAL SECRETARY ELECTION RESULTS')
            plt.show()

            print('''FINANCIAL SECRETARY CANDIDATES''')
            print("CHRISTOPHER",self.Fcandidate1,"votes")
            print("FEMI",self.Fcandidate2,"votes")
            print("DOLLAR",self.Fcandidate3,"votes")
            print("NAIRA",self.Fcandidate4,"votes")

            values =[self.Fcandidate1,self.Fcandidate2,self.Fcandidate3,self.Fcandidate4]
            colors = ['g','r','y','b']

            labels = ['CHRISTOPHER', 'FEMI', 'DOLLAR','NAIRA']
            plt.pie(values, colors= colors, labels=labels, autopct='%1.1f%%')
            plt.title('FINANCIAL SECRETARY ELECTION RESULTS')
            plt.show()

            print('''PRO CANDIDATES''')
            print("PODEM",self.PRcandidate1,"votes")
            print("STARCO",self.PRcandidate2,"votes")
            print("SAOLA",self.PRcandidate3,"votes")
            print("PRECIOUS",self.PRcandidate4,"votes")

            values =[self.PRcandidate1,self.PRcandidate2,self.PRcandidate3,self.PRcandidate4]


            labels = ['PODEM', 'STARCO', 'SAOLA','PRECIOUS']
            plt.pie(values, colors= colors, labels=labels, autopct='%1.1f%%')
            plt.title('PRO ELECTION RESULTS')
            plt.show()
        except:
            print('result not available yet')

def main():
    a=VotingSystem()
    while True:
        print('''
              1. Register/Create Account
              2. Login 
              3. Voting Result
              4. Log Out
              ''')
        res=(input("Enter a number:"))
        if res=='1':
            a.RegistrationPage()     
        if res=='2':
            a.LoginPage()
        if res=='3':
            a.Result()
        if res=='4':
            print('bye')
            break;
            
        
main()
