
import time

class BalanceExceptionError(Exception):
    pass

class AttemptLimitExceededError(Exception):
    pass
attempts=1
def withdraw():
    global attempts
    saved_pin=123456 #Hardcoded pin.
    balance=10000    #Hardcoded balance.
    pin=int(input("Enter your PIN: "))
    if pin==saved_pin:
        try:
            amt=float(input("Enter amount to withdraw: "))
            temp_balance=balance-amt
            if temp_balance<500:
                raise BalanceExceptionError("Insufficient balance.")
            balance=balance-amt
            print(f'\033[32mWithdrawal successful. Your new balance is: {balance}\033[0m')
        except BalanceExceptionError as e:
            print(f'\033[31m{e}\033[0m')
    else:
        ans=input('\033[31mIncorrect PIN. Do you want to try again? (yes/no): \033[0m').strip().lower()
        if ans=='yes':
            attempts+=1
            try:
                if attempts==4:
                    raise AttemptLimitExceededError("Your account has been locked due to multiple incorrect PIN attempts. Please try again after 5 minutes.")
            except AttemptLimitExceededError as e:
                print(f'\033[31m{e}\033[0m')
                time.sleep(300) # Simulating a lockout period.
            else:
                withdraw()
        else:
            print('\033[31mThank you for using our service. Goodbye!\033[0m')
            return
withdraw()