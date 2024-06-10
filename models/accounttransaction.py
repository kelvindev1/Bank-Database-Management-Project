from __init__ import CURSOR, CONN

class AccountTransaction():
    def __init__(self, account_id, transaction_id):

        self.account_id = account_id
        self.transaction_id = transaction_id

    def create_table(cls):
        sql = """
            CREATE TABLE account_transactions (
                account_id INTEGER,
                transaction_id INTEGER,
                CONSTRAINT PK_account_transactions PRIMARY KEY (account_id, transaction_id),
                CONSTRAINT FK_Account FOREIGN KEY (account_id) REFERENCES Account(account_id),
                CONSTRAINT FK_Transaction FOREIGN KEY (transaction_id) REFERENCES Transaction(transaction_id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()




    