from account import Account
from customer import Customer
from transaction import Transaction

def exit_program():
    print("Bye!")
    exit()

def list_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(customer)

def find_customer_by_name():
    first_name = input("Enter the customer's First Name: ")
    last_name = input("Enter the customer's last Name: ")
    customer = Customer.find_by_name(first_name, last_name)
    print(customer) if customer else print(f'Customer {first_name, last_name} not in Database')

def find_customer_by_id():
    id_ = input("Enter the customer's ID: ")
    customer = Customer.find_by_id(id_)
    print(customer) if customer else print(f"Customer {id_} not in Database")

def create_customer():
    first_name = input("Enter the customer's First Name: ")
    last_name = input("Enter the customer's Last Name: ")
    phone_number = input("Enter the customer's Phone Number: ")
    email = input("Enter the customer's email: ")
    try:
        customer = Customer.create(first_name, last_name, phone_number, email)
        print(f"You have Successfully created {customer}")
    except Exception as exc:
        print("There was an error creating customer: ", exc)

def update_customer():
    id_ = input("Enter the customer's ID: ")
    if customer := Customer.find_by_id(id_):
        try:
            first_name = input("Enter customer's First Name: ")
            customer.first_name = first_name
            last_name = input("Enter customer's Last Name: ")
            customer.last_name = last_name
            phone_number = input("Enter customer's Phone Number: ")
            customer.phone_number = phone_number
            email = input("Enter customer's email: ")
            customer.email = email
            customer.update()
            print(f"Success: You have update {customer}")
        except Exception as exc:
            print("There was a Error Updating customer: ", exc)
    else:
        print(f"Customer {id_} not in Database")

def delete_customer():
    id_ = input("Enter the customer's ID: ")
    if customer := Customer.find_by_id(id_):
        customer.delete()
        print(f"Customer {id_} Deleted")
    else:
        print(f"Customer {id_} not in Database")
        




def list_accounts():
    accounts = Account.get_all()
    for account in accounts:
        print(account)

def find_account_by_type():
    type = input("Enter account's type: ")
    account = Account.find_by_name(type)
    print(account) if account else print(f"{type} is not account's type")

def find_account_by_id():
    id_ = input("Enter account's ID: ")
    account = Account.find_by_id(id_)
    print(account) if account else print(f"ID: {id_} not in Database")

def create_account():
    type = input("Enter Account Type: ")
    balance = input("Enter Top-up Amount: ")
    date = input("Enter Date(YYYY-MM-DD) : ")
    customer_id = input("Enter customer ID: ")
    try:
        customer = Customer.find_by_id(customer_id)
        if customer:
            account = Account.create(type, balance, date, customer_id=customer_id)
            print(f"Successfully created: {account}")
    except Exception as exc:
        print("There was a Error creating Account: ", exc)

def update_account():
    id_ = input("Enter Account's ID: ")
    if account := Account.find_by_id(id_):
        try:
            type = input("Enter Account Type: ")
            account.type = type
            balance = input("Enter Account Balance: ")
            account.balance = float(balance)
            date = input("Enter Date(YYYY-MM-DD): ")
            account.date = date
            customer_id = input("Enter Account's customer ID: ")
            account.customer_id = int(customer_id)
            account.update()
            print(f'Success: You have updated {account}')
        except Exception as exc:
            print(f'Error updating Account: ', exc)
    else:
        print(f"Account {id} not in Database")

def delete_account():
    id_ = input("Enter Account's ID: ")
    if account := Account.find_by_id(id_):
        account.delete()
        print(f"Account {id_} Deleted")
    else:
        print(f"Account {id_} not in Database")

def list_customer_accounts():
    customer_id_ = input("Enter the Customer's ID: ")
    if customer := Customer.find_by_id(customer_id_):
        accounts = customer.accounts()
        if accounts:
            for account in accounts:
                print(account)
        else:
            print("No account found for this Customer")
    else:
        print(f"Customer {customer_id_} not in Database")




def list_transactions():
    transactions = Transaction.get_all()
    for transaction in transactions:
        print(transaction)

def find_transaction_by_type():
    type = input("Enter Type of Transaction: ")
    transaction = Transaction.find_by_name(type)
    print(transaction) if transaction else print(
        f'Transaction {type} not found')
    
def find_transaction_by_id():
    id_ = input("Enter the transaction's id: ")
    transaction = Transaction.find_by_id(id_)
    print(transaction) if transaction else print(f'Transaction {id_} not found')

def create_transaction():
    type = input("Enter type of Transaction: ")
    amount = input("Enter amount to Transact: ")
    date = input("Enter Date(YYYY-MM-DD): ")
    try:
        transaction = Transaction.create(type, amount, date)
        print(f'Successfully created {transaction}')
    except Exception as exc:
        print("There was an Error creating transaction: ", exc)

def update_transaction():
    id_ = input("Enter transaction's ID: ")
    if transaction := Transaction.find_by_id(id_):
        try:
            type = input("Enter transaction's  Type: ")
            transaction.type = type
            amount = input("Enter transaction Amount: ")
            transaction.amount = int(amount)
            date = input("Enter Date(YYYY-MM-DD): ")
            transaction.date = date 
            transaction.update()
            print(f"Success: You have updated {transaction}")
        except Exception as exc:
            print("There was a Error Updating Transaction: ", exc)
    else:
        print(f"Transaction {id_} not in Database")

def delete_transaction():
    id_ = input("Enter the Transaction ID: ")
    if transaction := Transaction.find_by_id(id_):
        transaction.delete()
        print(f'Transaction {id_} Deleted')
    else:
        print(f'Transaction {id_} not in Database')
