#    ATM   
c = 1
pin = 1529
Amount = 48145

while True:
    print("Welcome\nAttempt", c)
    pn = int(input("Enter Your PIN: "))

    if pin == pn:
        print(f"Your current Amount is: {Amount}")

        print("1. Withdraw")
        print("2. Deposit")
        print("3. Exit")

        choice = int(input("Choose Option: "))

        if choice == 1:
            draw = int(input("Enter Amount To Withdraw: "))
            if draw <= Amount:
                Amount -= draw  
                print(f"Withdrawn: {draw}\nCurrent Balance: {Amount}")
            else:
                print("Insufficient Balance!")

        elif choice == 2:  
            dep = int(input("Enter Amount To Deposit: "))
            Amount += dep 
            print(f"Deposited: {dep}\nCurrent Balance: {Amount}")

        elif choice == 3:
            print("Thank you!")
            break

        else:
            print("Invalid option!")

    else:
        c += 1
        print("You Entered Wrong PIN")

        if c > 3:
            print("Your account is blocked for 24 hours")
            break
