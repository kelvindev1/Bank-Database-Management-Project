from __init__ import CURSOR, CONN
from account import Account
from transaction import Transaction

class AccountTransaction():
    
    all = {}

    def __init__(self, account_id, transaction_id):
        self.account_id = account_id
        self.transaction_id = transaction_id


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS account_transactions (
                account_id INTEGER,
                transaction_id INTEGER,
                CONSTRAINT PK_account_transactions PRIMARY KEY (account_id, transaction_id),
                CONSTRAINT FK_Account FOREIGN KEY (account_id) REFERENCES Account(account_id),
                CONSTRAINT FK_Transaction FOREIGN KEY (transaction_id) REFERENCES "Transaction"(transaction_id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS account_transactions;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO account_transactions (account_id, transaction_id)
            VALUES(?, ?)
        """
        CURSOR.execute(sql, (self.account_id, self.transaction_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, account_id, transaction_id):
        account_transaction = cls(account_id, transaction_id)
        account_transaction.save()
        return account_transaction
    


    def update(self, account_id = None, transaction_id = None):
        if account_id is not None:
            self.account_id = account_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        sql = """
            UPDATE account_transactions
            SET account_id = ?, transaction_id = ?
            WHERE account_id = ? AND transaction_id = ?
        """
        CURSOR.execute(sql, (self.account_id, self.transaction_id, self.account_id, self.transaction_id))
        CONN.commit()
        type(self).all[self.id] = self


    @classmethod
    def instance_from_db(cls, row):
        account_transaction = cls.all.get((row[0], row[1]))
        if account_transaction:
            account_transaction.account_id = row[0]
            account_transaction.transaction_id = row[1]
        else:
            account_transaction = cls(row[0], row[1])
            account_transaction.id = CURSOR.lastrowid
            cls.all[(account_transaction.account_id, account_transaction.transaction_id)] = account_transaction
        return account_transaction
    

    def delete(self):
        sql = """
            DELETE FROM account_transactions
            WHERE account_id = ? AND transaction_id = ?
        """
        CURSOR.execute(sql, (self.account_id, self.transaction_id))
        CONN.commit()
        del type(self).all[self.id]

    @classmethod
    def get(cls, account_id, transaction_id):
        sql = """
            SELECT * FROM account_transactions
            WHERE account_id = ? AND transaction_id = ?
        """
        CURSOR.execute(sql, (account_id, transaction_id))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def find_by_account(cls, account_id):
        sql = """
            SELECT * FROM account_transactions
            WHERE account_id = ?
        """
        CURSOR.execute(sql, (account_id,))
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]
    
    @classmethod
    def find_by_transaction(cls, transaction_id):
        sql = """
            SELECT * FROM account_transactions
            WHERE transaction_id = ?
        """
        CURSOR.execute(sql, (transaction_id,))
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def all_records(cls):
        sql = """
            SELECT * FROM account_transactions
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]
    
    
def __repr__(self):
        return f"<AccountTransaction account_id={self.account_id} transaction_id={self.transaction_id}>"