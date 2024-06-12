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



    Customer1 = Customer.create("Steve", "Otieno", 254705000001, "Steve@gmail.com")
    Customer2 = Customer.create("Kelvin", "Mutugi", 254759447393, "kelvin@gmail.com")
    Customer3 = Customer.create("Sarafina", "Cheche", 254712000900, "Sarafina@gmail.com")
    Customer5 = Customer.create("Brandon", "Dando", 254111111111, "Brandon@gmail.com")
    Customer6 = Customer.create("Mike", "Robe", 254722000011, "Mike@gmail.com")

    Account1 = Account.create("Savings", 20000.00, "2023-04-11", Customer1.id)
    Account2 = Account.create("MMA", 2000.52, "2024-01-10", Customer1.id)
    Account3 = Account.create("Savings", 5000.43, "2024-06-11", Customer2.id)
    Account4 = Account.create("HSA", 800.91, "2010-08-23", Customer6.id)
    Account.create("MMA", 10000.67, "2022-10-10", Customer3.id)
    Account.create("Savings", 12000.01, "2024-04-20", Customer5.id)

    Transaction1 = Transaction.create("Withdrawal", 2000,  "2024-05-14")
    Transaction2 = Transaction.create("Deposit", 1500, "2024-06-12")
    Transaction3 = Transaction.create("Deposit", 300, "2024-03-20")
    Transaction4 = Transaction.create("Deposit", 200, "2023-12-19")

    AccountTransaction.create(Account1.id, Transaction4.id)
    AccountTransaction.create(Account2.id, Transaction1.id)
    AccountTransaction.create(Account4.id, Transaction3.id)
    AccountTransaction.create(Account3.id, Transaction2.id)



store_database()
print("Successfully stored the database")