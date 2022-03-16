import datetime
import time

#function to recall while loop of user input 
def Validate(inpMess, arr, mess):
    fA = input(inpMess)
    while fA not in arr:
        print(mess)
        fA = input(inpMess)
    return fA
        

#function to validate check in date
def dateVal():
    date_text = input("Enter checkin date in format YYYY-MM-DD")
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return date_text
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        return dateVal()
    
#Genral class
class Hotelmanagement:
    def __init__(self):
       
        print('''
                    *******************************************************************************************
                    *                    Welcome to Cephas Hotel management System!!!                         *
                    *    Cephas Hotel is a home of suitness,where we offer an excellence and lofty services,  *
                    *    your comfortability is our concern,we give a top-notch services where you can make a *
                    *        full recommendation of our hotel.We take full responsibility of your security.   *
                    *                                   Enjoy your Stay!!!                                    *
                    ********************************************************************************************
                    
    
            ''')
        #database 
        database = {'name':[],
                    'phonenumber':[],
                    'kin-phonenumber':[],
                     'Home-address': [],
                    'home-Town':[],
                    'checkindate':[],
                    'Totalamount':0,
                    'services-used':[],
                    
        }
        
        def Receipt(): 
                print('''
                                             *************************
                                             *          Receipt      *  
                                             *************************
                    ''')
                print("                      NAME: ", database['name'][0]) 
                print("                      PHONE NUMBER: ",database['phonenumber'][0])
                print("                      NEXT OF KIN PHONE NUMBER: ",database['kin-phonenumber'][0])
                print("                      HOME ADDRESS: ",database['Home-address'][0])
                print("                      CHECK IN DATE: ",database['checkindate'])
                print("                      Below are the services")
                for x in database['services-used']:
                    print(x)
                print("                      TOTAL AMOUNT SPENT: ",'$',database['Totalamount'])
                
        #fuction to only allow a number from a user
        def test_int(mess, err):
            try:
                val = input(mess)
                val = int(val)
                return val
            except:
                print(err)
                return test_int(mess, err)
        #function to continue or exit
        def exitorcont(func):
            print('''
            press 1 for another services or 0 to exit
            ''')
            res = Validate('Enter your choice',['1','0'],'Enter a valid choice')
            if res=='1':
                func()
            elif res=='0':
                Receipt()

        res = Validate('Press 1 to proceed',['1'],'Enter a valid choice')
        if res == '1':
            
            # contact details
            def contactdetails(self):
                    print('''
                                     *************************
                                     *   CONTACT DETAILS     *  
                                     *************************
                    ''')
                    nam = input('Enter your full name: ').upper()
                    pho = test_int('Enter your phone number: +234', 'Please Enter A Number')
                    while  len(str(pho)) != 10:
                        print('Error!!!enter a correct phone number: ')
                        pho =test_int('Enter your phone number: +234', 'Please Enter A Number')
                        continue
                    pho2 = test_int('Enter next of kin phone nunber: +234', 'Please Enter A Number')
                    while  len(str(pho2)) != 10:
                        print('Error!!! enter a valid phone number: ')
                        pho2 = test_int('Enter next of kin phone nunber: +234', 'Please Enter A Number')
                        continue
                    homeadd= input('Enter your home address: ').upper()
                    townadd =input('Enter your home town: ').upper()
                    mydate = dateVal()
                
                    cont = Validate('press 1 to contine and Submit: ',['1'],'Enter a valid choice')
                    if cont == '1':
                        database['name'].append(nam)
                        database['phonenumber'].append(pho)
                        database['kin-phonenumber'].append(pho2)
                        database['Home-address'].append(homeadd)
                        database['home-Town'].append(townadd)
                        database['checkindate'] = mydate
            
                        
                        #function of other sservices
                        def otherservices():
                            print('''
                            #################################################################### 
                                                Welcome to other services
                                        where you have opportunities for various services
                                           press 1 for Drink Serices
                                           press 2 for Food services
                                           press 3 for Gym Servies
                                           press 4 for lundry services
                                           press 5 for swimming services
                            ######################################################################         
                                        
                                    ''')
                            res = input('Enter your choice')  
                            while res not in ['1','2','3','4','5']:
                                print('Enter a valid choice')
                                res = input('Enter your choice') 
                            if res == '1':
                                print('''
                                    we have these drinks for you:
                    1. coke ------@$300   3. Gulder ------@$500  5. Yoguart -----@$700 
                    2. fanta ------@$400  4. Guiness-----@$600  6. 5Alive ------@800
                                ''')
                                val = Validate('Enter your choice',['1','2','3','4','5','6'],'Enter a valid choice')
                                if val=='1':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*300
                                    database['services-used'].append('coke')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)                                        
                                if val == '2':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*400
                                    database['services-used'].append('fanta')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '3':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount']+= res*500
                                    database['services-used'].append('gulder')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '4':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*600
                                    database['services-used'].append('Guiness')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '5':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*700
                                    database['services-used'].append('Yoquart')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '6':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*800
                                    database['services-used'].append('5Alive')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                            if res == '2':
                                print('''
                                                we have these food for you;
                                                
                        1. Jollof and fried Rice -----@$200/spoon  3. Beans -----@$300/spoon 5. Eba -----@$500/spoon 
                        
                        2. Yam ------@$200/spoon    4. Amala ----@$400/spoon     6.Pounded yam ----@$600/spoon
                        
                                ''')
                                val = Validate('Enter your choice',['1','2','3','4','5','6'],'Enter a valid choice')
                                if val == '1':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*200
                                    database['services-used'].append('Jollof and fried Rice ')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '2':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*200
                                    database['services-used'].append('Yam')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '3':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*300
                                    database['services-used'].append('Beans')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '4':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*400
                                    database['services-used'].append('Amala')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '5':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*500
                                    database['services-used'].append('Eba')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '6':
                                    res = int(input('How many quantities: '))
                                    database['Totalamount'] += res*600
                                    database['services-used'].append('Pounded yam')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                            if res =='3':
                                print('''
                                            Enroll for your Gym Services
                            1. One Month -----@$100  3. Three month -----@$300
                            2. Two Month -----@$200  4. Four Month ------@$400
                                    ''')
                                val = Validate('Enter your choice',['1','2','3','4'],'Enter a valid choice')
                                if val == '1':
                                    database['Totalamount'] += 1*100
                                    database['services-used'].append('Gym one Month')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '2':
                                    database['Totalamount'] += 2*100
                                    database['services-used'].append('Gym Two Month')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '3':
                                    database['Totalamount'] += 3*100
                                    database['services-used'].append('Gym Three Month')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '4':
                                    database['Totalamount'] += 4*100
                                    database['services-used'].append('Gym Four Month')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                            if res == '4':
                                print('''
                                            We provide the following Services for your laundry works:
                                            
                                                        1. Per cloth (wash only ) = $100
                                                        2. per cloth(wash,starching and ironing) = $250
                                    ''')
                                val = Validate('Enter your choice',['1','2'],'Enter a valid choice')
                                if val == '1':
                                    n = int(input('How many cloths?: '))
                                    database['Totalamount'] += n*100
                                    database['services-used'].append(' laundry Per cloth (wash only )')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '2':
                                    n = int(input('How many cloths?: '))
                                    database['Totalamount'] += n*250
                                    database['services-used'].append(' laundry Per cloth (wash,starching and ironing)')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                            if res == '5':
                                print('''###################################################
                                      #              Welcome to swimming services          #
                                      #  1. 1 hour ------@$100 3.    3 hours ----@$300     # 
                                      #  2. 2 hours -----@$200 4.    4 hours ----@$400     # 
                                      ######################################################
                                ''')
                                val = Validate('Enter your choice',['1','2','3','4'],'Enter a valid choice')
                                if val == '1': 
                                    n = int(input('How many people?: '))
                                    database['Totalamount'] += n*100
                                    database['services-used'].append(' Swimming 1 hour')
                                    print('You bill is ',database['Totalamount'])
                                    print('''
                                        press 1 for another services or 0 to exit
                                    ''')
                                    res = Validate('Enter your choice',['1','0'],'Enter a valid choice')
                                    if res=='1':
                                        service()
                                if val == '2': 
                                    n = int(input('How many people?: '))
                                    database['Totalamount'] += n*200
                                    database['services-used'].append(' Swimming 2 hours')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '3': 
                                    n = int(input('How many people?: '))
                                    database['Totalamount'] += n*300
                                    database['services-used'].append(' Swimming 3 hours')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)
                                if val == '4': 
                                    n = int(input('How many people?: '))
                                    database['Totalamount'] += n*400
                                    database['services-used'].append(' Swimming 4 hour')
                                    print('You bill is ',database['Totalamount'])
                                    exitorcont(service)  
                        #function of main services
                        def service():
                                print('''
                                       ********************************************************************     
                                       *                         HERE ARE OUR SERVICES:                   *
                                       *     press 1 for Suit Services(Room only)                         *
                                       *     press 2 for wood Services(Room and food  only)               *
                                       *     press 3 for Sliver Services (Room,food,spar only)            *
                                       *     press 4 for Platinum Services(Room Gym,swimming andspar only)*
                                       *     press 5 for Gold Services(Room,food,spar,swimming,Gym only)  *
                                       *     press 6 for others Services.                                 *
                                       ********************************************************************
                                            ''') 
                                choice = Validate("Enter your choice", ['1','2','3','4','5','6'], 'select a valid choice' )
                                if choice == '1':
                                    print('''
                                            Welcome to Suit services!!!
                                            
                                            Suit Services cost N1500
                                            press 1 to proceed and 0 to go back 
                                            ''')
                                    
                                    res = Validate("Enter your choice", ['1','0'], 'selct a valid choice' )
                                    if res == '0':
                                         service()
                                    if res == '1':
                                         n = test_int("How many nights will you like to stay: ", "Enter Number Only")
                                         amount = 1500*int(n)
                                         database['Totalamount'] += amount
                                         database['services-used'].append(' Suit services')
                                         exitorcont(service)
                                        
                                if choice == '2':
                                     print('''
                                            Welcome to wood services!!!
                                            
                                            Wood Services cost N10000
                                            press 1 to proceed and 0 to go back 
                                            ''')
                                     res = input('Enter your choice')
                                     while res!='1' and res != '0':
                                         print('selct a valid choice')
                                         res = input('Enter your choice')
                                     if res == '0':
                                         service()
                                     if res == '1':
                                        n = test_int("How many nights will you like to stay: ", "Enter Number Only") 
                                        amount = 10000*n
                                        database['Totalamount']+=amount
                                        database['services-used'].append('Wood service')
                                        exitorcont(service)
                                        
                                if choice =='3':
                                     print('''
                                            Welcome to Sliver services!!!
                                            
                                            Sliver Services cost N17000
                                            press 1 to proceed and 0 to go back 
                                            ''')
                                     res = input('Enter your choice')
                                     while res!='1' and res != '0':
                                         print('selct a valid choice')
                                         res = input('Enter your choice')
                                     if res == '0':
                                         service()
                                     if res == '1':
                                         n = test_int("How many nights will you like to stay: ", "Enter Number Only")
                                         amount = 17000*int(n)
                                         database['Totalamount']+=amount
                                         database['services-used'].append('Sliver Service')
                                         exitorcont(service)
                                if choice =='4':
                                     print('''
                                            Welcome to Platinum services!!!
                                            
                                            Platinum Services cost N25000
                                            press 1 to proceed and 0 to go back 
                                            ''')
                                     res = input('Enter your choice')
                                     while res!='1' and res != '0':
                                         print('selct a valid choice')
                                         res = input('Enter your choice')
                                     if res == '0':
                                         service()
                                     if res == '1':
                                         n = test_int("How many nights will you like to stay: ", "Enter Number Only")
                                         amount = 25000*int(n)
                                         database['Totalamount']+=amount
                                         database['services-used'].append('Platinum Services')
                                         exitorcont(service)
                                if choice =='5':
                                     print('''
                                            Welcome to Gold services!!!
                                            
                                            Gold Services cost N30000
                                            press 1 to proceed and 0 to go back 
                                            ''')
                                     res = input('Enter your choice')
                                     while res!='1' and res != '0':
                                         print('selct a valid choice')
                                         res = input('Enter your choice')
                                     if res == '0':
                                         service()
                                     if res == '1':
                                         n = test_int("How many nights will you like to stay: ", "Enter Number Only")
                                         amount = 30000*int(n)
                                         database['Totalamount']+=amount
                                         database['services-used'].append('Gold Services')
                                         exitorcont(service)
                                if choice == '6':
                                    otherservices()
                                        
                    service()
                                    
                                    
            contactdetails(self)
                
Hotelmanagement()