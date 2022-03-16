import sys
from datetime import datetime
now=datetime.now()
class CGPA_CALCULATOR:   
    def __init__(self,Institution='',GPA='',filename='',sex='',department='',name='',MATRIC_NO='',PROG='',Level='',Sex='',Name='',Session='',OPTION='',OPT='',PROGRAMME='',DATE='',GPA1='',TotalPointsObtainable='', ObtainedPoints=''):
        print("                WELCOME TO CEPHAS INSTITUTION         ")
        print("                      CGPA CALCULATOR               ")
        self.Institution=Institution
        self.department=department
        self.name=name
        self.MATRIC_NO=MATRIC_NO
        self.Level=Level
        self.filename=filename
        self.Sex=Sex
        self.sex=sex
        self.Name=Name
        self.Session=Session
        self.OPTION=OPTION
        self.OPT=OPT
        self.PROGRAMME=PROGRAMME
        self.PROG=PROG
        self.DATE=DATE
        self.ObtainedPoints= ObtainedPoints
        self.TotalPointsObtainable=TotalPointsObtainable
        self.GPA=GPA
        self.GPA1=GPA1
    #This function takes the user filename and also takes the user details    
    def student_data(self):
        self.filename=input("Enter Filename:") 
        Institution=input("INSTITUTION:")
        self.Institution=Institution.upper()
        department=input("DEPARTMENT:")
        self.department=department.upper()
        name=input("STUDENT NAME:")
        self.Name=name.upper()
        self.MATRIC_NO=input("MATRIC NO:")
        self.Level=input("LEVEL:")
        gender=['MALE','FEMALE','M','F']
        self.Sex=input("Sex:")
        self.sex=self.Sex.upper()[0]
        while self.Sex.upper() not in gender:
            #The user is allowed to input correct gender without terminating his progress 
            print("Error! Try Again")
            self.Sex=input("Sex:")
            self.sex=self.Sex.upper()[0]
        self.Session=input("SESSION:")
        self.OPTION=input("OPTION:")
        self.OPT=self.OPTION.upper()
        self.PROGRAMME=input("PROGRAMME:")
        self.PROG=self.PROGRAMME.upper()
        self.DATE=now.strftime("%d/%m/%Y, %H:%M:%S")
    #This function allows the user to calculate his/her CGPA and assist the user in providing information about CGPA system    
    def CGPA(self):
        print('''
             1. Calculate CGPA 
             2. Info
             3. Back''')
        res=input("Enter a valid number:")
        while res not in ('1','2','3'):
            print("Invalid Response!")
            res=input("Enter Number between 1-3:")
        def CGPA_CALCULATOR():
            print("CALCULATE CGPA")
             
            self.semester=int(input("Enter number of semester:"))
            self.TotalPointsObtainable=0
            self.ObtainedPoints=0
            
            for i in range(self.semester):
                if i%2 ==0:
                    print("FIRST SEMESTER")
                    
                if i%2 !=0:
                    print("SECOND SEMESTER")
                CourseReg=int(input("Number of courses registered:"))
                print("*********************")
                for x in range(CourseReg):
                    self.CourseCode=input("Course Code:")
                    self.CourseTitle=input("Course Title:")
                    unit=int(input( "Unit:"))
                    score=int(input("Enter Score:"))
                    
                    print("************************")
                    self.TotalPointsObtainable+=unit
                    if score >=70 and score<=100:
                        point=5.0
                        Grade="A"
                        Remark="PAssed"
                    elif score >=60 and score<=69:
                        point=4.0
                        Grade="B"
                        Remark="PAssed"
                    elif score >=50 and score<=59:
                        point=3.0
                        Grade="C"
                        Remark="PAssed"
                    elif score >=40 and score<=49:
                        point=2.0
                        Grade="D"
                        Remark="PAssed"
                    elif score >=35 and score<=39:
                        point=1.0
                        Grade="E"
                        Remark="PAssed"
                    elif score >=0 and score<=34:
                        point=0
                        Grade="F"
                        Remark="Failed"
                    else:
                        print("E")
                                            
                    self.ObtainedPoints+=unit*point
                    print("GRADE:",Grade)
                    print("REMARK:",Remark)
                    print("Total Points Obtained:", self.ObtainedPoints)
                    print("Total Unit:", self.TotalPointsObtainable)
                    ans=float(self.ObtainedPoints/self.TotalPointsObtainable)
                    answer=ans
                    self.GPA1="{:.2f}".format(answer)
            if self.semester ==1:
                self.GPA=self.GPA1
                print("GPA:", self.GPA)
            else:
                print("CGPA:", self.GPA1)
                   
         
       #This function provides this user information on what CGPA is about                   
        def INFO_ON_CGPA():
            print('''Cumulative Grade Point Average (CGPA) is an assessment tool used to evaluate your academic perfprmance. Your CGPA is calculated by dividing the sum of grade points earned by the total credit value of courses you have attempted.
        NOTE: IN THIS CGPA CALCULATOR, THE HIGHEST CGPA IS 5.0''')
            
        #Depending on the value assigned to res, the lines of code take the users to their most preferred         
        if res=='1':
            CGPA_CALCULATOR()
        if res=='2':
            INFO_ON_CGPA()
        if res=='3':
            main()
    #This function display the result of the students and also save the result in the filename opened by the school management
    def diaplay(self):
    #This function stores all the inputs from the user in a file
        
        print ("       ",self.Institution      )
        print("---------------------------------")
        
            
        print ("       ",self.department       )
        print("---------------------------------")
        print ("        STUDENT DETAILS         ")
        print("---------------------------------")
        print ("STUDENT NAME:", self.Name)
        print ("MATRIC NO:", self.MATRIC_NO)
        print ("LEVEL:", self.Level)
        print ("SEX:", self.sex)  
        print ("SESSION:", self.Session)
        print ("OPTION:", self.OPT)
        print ("PROGRAMME:", self.PROG)
        print ("DATE PRINTED:", self.DATE)
        print("---------------------------------")
        print("Total Points Obtained:", self.ObtainedPoints)
        print("Total Unit:", self.TotalPointsObtainable)
        if self.semester ==1:
            print ("GPA:", self.GPA)
           
        if self.GPA>='4.5' and self.GPA<='5.0':
            print("FIRST CLASS")
        if self.GPA>='3.5' and self.GPA<='4.49':
            print("SECOND CLASS UPPER")
        if self.GPA>='3.0' and self.GPA<='3.49':
            print("SECOND CLASS LOWER")
        if self.GPA>='2.5' and self.GPA<='2.99':
            print("THIRD PASS")
        if self.GPA>='2.0' and self.GPA<='2.49':
            print("PASS")
            
        if self.semester >1:
            print ("TOTAL CGPA:", self.GPA1)
            
        if self.GPA1>='4.5' and self.GPA1<='5.0':
            print("FIRST CLASS")
        if self.GPA1>='3.5' and self.GPA1<='4.49':
            print("SECOND CLASS UPPER")
        if self.GPA1>='3.0' and self.GPA1<='3.49':
            print("SECOND CLASS LOWER")
        if self.GPA1>='2.5' and self.GPA1<='2.99':
            print("THIRD PASS")
        if self.GPA1>='2.0' and self.GPA1<='2.49':
            print("PASS")
        print("---------------------------------")
    def file(self):
    
        with open(self.filename,'a') as f:
            f.write('INSTITUTION: ')
            f.write(self.Institution)
            f.write('\n')
            f.write('DEPARTMENT:')
            f.write(self.department)
            f.write('\n')
            f.write('\n')
            f.write("STUDENT DETAILS")
            f.write('\n')
            f.write('STUDENT NAME:')
            f.write(self.Name)
            f.write('\n')
            f.write('MATRIC NO:')
            f.write(self.MATRIC_NO)
            f.write('\n')
            f.write('LEVEL:')
            f.write(str(self.Level))
            f.write('\n')
            f.write('SEX:')
            f.write(self.sex)
            f.write('\n')
            f.write('SESSION:')
            f.write(self.Session)
            f.write('\n')
            f.write('OPTION:')
            f.write(self.OPT)
            f.write('\n')
            f.write('PROGRAMME:')
            f.write(self.PROG)
            f.write('\n')
            f.write('DATE:')
            f.write(self.DATE)
            f.write('\n')
            f.write('\n')
            f.write("TOTAL POINTS OBTAINED:")
            f.write(str(self.ObtainedPoints))
            f.write('\n')
            f.write("TOTAL UNIT:")
            f.write(str(self.TotalPointsObtainable))
            f.write('\n')
            f.write("CGPA:")
            f.write(str(self.GPA1))
    def About(self):
        print('''This calculator was developed by LEON together with David and Ayo on 14/10/2021 to assist students and school managements in calculating the GPA and CGPA of the students.
               Version 1.0''')
#This function serves as grandparent to the class object which i will call the parent. Through this assumed grandparent, the parents can easily be accessed, and the children(elements in the parents) can also function.                  
def main():
    a=CGPA_CALCULATOR()
    while True:
        print('''
              1. Enter Student Data
              2. Calculate Session CGPA
              3. Check Result
              4. About
              5. Exit''')
        res=(input("Enter a valid number:"))
        if res=='1':
            a.student_data()     
        if res=='2':
            a.CGPA()
            
        if res=='3':
            a.diaplay()
            a.file()
        if res=='4':
            a.About()
        if res=='5':
            sys.exit()
        
main()