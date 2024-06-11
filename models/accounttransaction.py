from __init__ import CURSOR, CONN

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
    def create(cls, account_id, transaction_id):
        account_transaction = cls(account_id, transaction_id)
        account_transaction.save()
        return account_transaction
    
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
