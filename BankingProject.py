import random
import maskpass

# Banking Application
Name = " "
Type = " "
Branch_code = " "
Account_no = 0
Mobile = 0
Balance = 0
User_id = " "
Password = " "

def create_accounts():

    global Name
    global Type
    global Branch_code
    global Account_no
    global Mobile
    global Balance
    Name = input("\nEnter the account holder name : ")
    Type = input("Enter the type of account[Current / Savings] : ")
    Branch_code = input("Enter your branch code : ")
    Account_no = random.randrange(10000000, 99999999)
    while True:
        Mobile = int(input("Enter your mobile number : "))
        if len(str(Mobile)) == 10:
            break
        else:
            print("\t\tIncorrect mobile number")
    Balance = int(input("Enter the initial amount to deposit : "))
    print('\nWelcome', Name, ', your account is created with account no.', Account_no)

def account_login():
    global User_id
    global Password
    User_id = input("\nEnter your User ID: ")
    Password = maskpass.askpass(prompt="Enter your Password: ", mask='*')
    print("\nYou have successfully logged in!")


def deposit(amount):

    global Balance
    Balance = Balance + amount
    check_balance()

def withdraw(amount):
    global Balance
    Balance = Balance - amount
    check_balance()

def check_balance():

    print("\nCurrent Balance : ", Balance)

def show_account_details():
    global Balance
    print("\nAccount Holder Name : ", Name,
    "\nAccount Number : ", Account_no,
    "\nBranch code : ", Branch_code,
    "\nType of Account : ", Type,
    "\nMobile Number : ", Mobile,
    "\nNet Available Balance : ", Balance)


print("\nWelcome to ENTRI\'S BANKING PROJECT")
choice1 = "y"
while (choice1 == "y"):
    print("\t1. Create an account"
          "\n\t2. Login to account"
          "\n\t3. Deposit"
          "\n\t4. Withdraw"
          "\n\t5. Check Balance"
          "\n\t6. Account Details")
    choice = int(input("Please select any option."))
    if (choice == 1):
        create_accounts()
    elif (choice == 2):
        account_login()
    elif (choice == 3):
        while True:
            amount = int(input("\nEnter the amount to deposit : "))
            if amount <= 50000:
                break
            else:
                print("\t\tDaily deposit amount limited to Rs.50000/-")
        deposit(amount)
    elif (choice == 4):
        while True:
            amount = int(input("\nEnter the amount to withdraw : "))
            if amount <= 30000:
                break
            else:
                print("\t\tDaily withdrawal amount limited to Rs.30000/-")
        withdraw(amount)
    elif (choice == 5):
        check_balance()
    elif (choice == 6):
        show_account_details()
    else:
        print("Please select any 4 options available above")
    print("\nDo you want to continue...press y")
    choice1 = input()