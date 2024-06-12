from __init__ import CURSOR, CONN
from account import Account
from customer import Customer
from transaction import Transaction
from accounttransaction import AccountTransaction

def store_database():
    Account.drop_table()
    Customer.drop_table()
    Transaction.drop_table()
    AccountTransaction.drop_table()

    Account.create_table()
    Customer.create_table()
    Transaction.create_table()
    AccountTransaction.create_table()



    Customer1 = Customer.create("Kelvin", "Mutugi", 2345, "kelvin@gmail.com")

    Account1 = Account.create("Savings", 2000.00, "2024-04-11", Customer1.id)

    Transaction1 = Transaction.create("Withdrawal", 2,  "2024-05-14")
    Transaction2 = Transaction.create("Deposit", 150, "2024-06-12")

    AccountTransaction.create(Account1.id, Transaction1.id)
    AccountTransaction.create(Account1.id, Transaction2.id)


store_database()
print("Successfully stored the database")