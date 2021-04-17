import random
import time

database = {}

def init():
    try:

        # isValidOptionSelected = False
        print('Welcome to bankPhp')

        # while isValidOptionSelected == False:

        haveAccount = int(input('Do you have an account with us: \n 1 (Yes) \n 2. (No) \n'))

        if(haveAccount == 1):
            # isValidOptionSelected = True
            login()
        elif(haveAccount== 2):
            # isValidOptionSelected = True
            register()
        else:
            print('You have selected invalid option')
            init()
    except ValueError:
        print('Invalid Entry, Please try again')
        init()
        
def login():
    print('Login to your account')
    accountNumberFromUser = int(input('What is your account number:  '))
    password = input('What is your password:  ')
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if (userDetails[3] == password):
                bankOperation(userDetails)
    print('Invalid account or password')
    login()
    

    
    
def register():
    print('Enter your details to register')
    email = input('What is your email address\n')
    first_name = input('What is your first name?\n')
    last_name = input('what is your last name?\n')
    password = input('Create a password\n')

    availableBalance = 0
    accountNumber = generateAccountNumber()
    database[accountNumber] = [first_name, last_name, email, password, availableBalance]
    print('Your account hass been created. You can now make a deposit')
    print('Your account number is %s, make sure you keep it safe' % accountNumber)
    print('======================')
    print('Make sure you keep it safe')
    print('======================')
    print("Thank you for registering for Zuri Banking Network")
    nextOperation()
        
    # login()

def bankOperation(user):
    selectedOption = int(input('What would you like to do? (1) deposit (2) withdraw (3) Check Balace (4) Log Out (5) Exit (0) Help/Complaint\n'))
    if (selectedOption==1):
        time.sleep(2)
        depositOperation()
    elif (selectedOption==2):
        time.sleep(2)
        withdrawalOperation()
    elif(selectedOption==3):
        time.sleep(2)
        checkBalance()
    elif(selectedOption==4):
        time.sleep(2)
        login()
    elif(selectedOption==5):
        time.sleep(2)
        exit()
    elif(selectedOption==0):
        time.sleep(2)
        complaint()
    else:
        
        print('Invalid option selected')
        time.sleep(2)
        bankOperation(user)

def withdrawalOperation():
    amountToWithdrawn = int(input('Enter the amount you want to withdrawn:  '))
    for userDetails in database.items():
        if (userDetails[1][4] > 0):
            availableBalance = userDetails[1][4] - amountToWithdrawn
            userDetails[1][4] = availableBalance
            print('Please take your Cash') 
            time.sleep(2)
            print('Yours account balance is # %d' % availableBalance)
        elif (userDetails[1][4] < 0):
            print('Insufficcient Cash')
        else:
            print('Please try again with appropite entry or contact your bank')
            time.sleep(2)
        nextOperation()


def depositOperation():
    depositAmount= int(input('Enter the amount to be deposited:\n '))
    for userDetails in database.items():
        availableBalance = userDetails[1][4] + depositAmount
        userDetails[1][4] = availableBalance 
        time.sleep(2)
        print('Your account balance is # %d' % availableBalance)
        nextOperation()

def generateAccountNumber():
    return random.randrange(0000000000,9999999999)

def checkBalance():
    for userDetails in database.items():
        print('Your account balance is # %d' % userDetails[1][4])
        nextOperation()

def complaint():
    complaint = input('Please enter your complains below;\n')
    print('Your complaint has been successfully submit \n Thank you for Banking with Us')
    init()



def nextOperation():
    newOperation = int(input("Do you want perform another task?\n Press 1 for Yes \n Press 2 for No\n"))
    if (newOperation==1):
        time.sleep(2)
        login()
    elif newOperation==2:
        exit()
    else:
        print('Invalid option selected')
    init()


def logout():
    login()

def exit():
    exit    
    


init()

