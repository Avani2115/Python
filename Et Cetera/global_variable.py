balance = 0

def main():
    print(f"Balance: {balance}")
    deposit(100)
    withdraw(50)
    print(f"Balance: {balance}")

def deposit(n):
    global balance
    #we have to write global before, so that we can tell python that it is okay to change its value
    #if we don't, then we get LocalUnboundedError.
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()