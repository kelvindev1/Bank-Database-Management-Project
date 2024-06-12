from datetime import datetime
# from account import Account
from __init__ import CURSOR, CONN

class Transaction():
    all = {}
    def __init__(self, type, amount, date, id = None):

        self.id = id
        self.type = type
        self.amount = int(amount)
        self.date = date

    def __repr__(self):
        return f"<Transaction {self.id}: {self.type}, {self.amount}, {self.date}"
    
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        if isinstance(value, str) and len(value):
            self._type = value
        else:
            raise ValueError("Transaction type is expected to be Non-empty string")
        
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, value):
        if isinstance(value, int):
            self._amount = value
        else:
            raise ValueError("Transaction Amount should be an integer")
        
    @property
    def date(self):
        return self._date   
    @date.setter
    def date(self, value):
        try:
            self._date = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format, expected YYYY-MM-DD")
        
        

    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            type TEXT NOT NULL,
            amount INTEGER,
            date DATE NOT NULL)
        """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS transactions;
        """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        sql = """
            INSERT INTO transactions (type, amount, date)
            VALUES(?, ?, ?)
        """
        CURSOR.execute(sql, (self.type, self.amount, self.date))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    @classmethod
    def create(cls, type, amount, date):
        transaction = cls(type, amount, date)
        transaction.save()
        return transaction

    @classmethod
    def instance_from_db(cls, row):
        transaction = cls.all.get(row[0])
        if transaction:
            transaction.type = row[1]
            transaction.amount = row[2]
            transaction.date = row[3]
        else:
            transaction = cls(row[1], row[2], row[3])
            transaction.id = row[0]
            cls.all[transaction.id] = transaction
        return transaction

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM transactions
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, type):
        sql = """
            SELECT *
            FROM transactions
            WHERE type = ?
        """
        rows = CURSOR.execute(sql, (type,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    

    def update(self):
        sql = """
            UPDATE transactions
            SET type = ?, amount = ?, date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.type, self.amount, self.date, self.id))
        CONN.commit()


    def delete(self):
        sql = """
            DELETE FROM transactions
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM transactions
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
