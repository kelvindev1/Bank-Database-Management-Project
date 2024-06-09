import sqlite3


class Account():
    def __init__(self, account_id, customer_id, type, balance):
        
        self.account_id = account_id
        self.customer_id = customer_id
        self.type = type
        self.balance = balance