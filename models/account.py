from datetime import datetime
from customer import Customer
# from transaction import Transaction
from __init__ import CURSOR, CONN

class Account():

    all = {}

    def __init__(self, type, balance, date, customer_id, id = None):
        self.id = id
        self.type = type
        self.balance = float(balance)
        self.date = str(date)
        self.customer_id = int(customer_id)


    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        if isinstance(value, str) and len(value):
            self._type = value
        else:
            raise ValueError("Acoount type must be a non-empty string")
        
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if isinstance(value, float):
            self._balance = value
        else:
            raise ValueError("Balance should be a float")
             
    @property
    def date(self):
        return self._date   
    @date.setter
    def date(self, value):
        try:
            self._date = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format, expected YYYY-MM-DD")
        
    @property
    def customer_id(self):
        return self._customer_id
    @customer_id.setter
    def customer_id(self, customer_id):
        if type(customer_id) is int and Customer.find_by_id(customer_id):
            self._customer_id = customer_id
        else:
            raise ValueError("Customer_id must reference a customer in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS accounts(
            id INTEGER PRIMARY KEY,
            type VARCHAR(20) NOT NULL,
            balance FLOAT NOT NULL,
            date DATE NOT NULL,
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS accounts;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO accounts (type, balance, date, customer_id)
        VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.type, self.balance, self.date, self.customer_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, type, balance, date, customer_id):
        account = cls(type, balance, date, customer_id)
        account.save()
        return account
    
    def update(self):
        sql = """
        UPDATE accounts
        SET type = ?, balance = ?, date = ?, customer_id = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.type, self.balance, self.date,
                              self.customer_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
        DELETE FROM accounts
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        account = cls.all.get(row[0])
        if account:
            account.type = row[1]
            account.balance = row[2]
            account.date = row[3]
            account.customer_id = row[4]
        else:
            account = cls(row[1], row[2], row[3], row[4])
            account.id = row[0]
            cls.all[account.id] = account
        return account
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM accounts
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM accounts
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, type):
        sql = """
            SELECT *
            FROM accounts
            WHERE type = ?
        """
        rows = CURSOR.execute(sql, (type,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]


    def __repr__(self):
        return (
            f"<Account {self.id}: {self.type} {self.balance} {self.date}>" + 
            f"<Customer ID: {self.customer_id}>"
        )