from __init__ import CURSOR, CONN

class Account():

    all = {}

    def __init__(self, type, balance, date, customer_id, id = None):
        self.id = id
        self.type = type
        self.balance = balance
        self.date = date
        self.customer_id = customer_id


    def __repr__(self):
        return (
            f"<Account {self.id}: {self.type} {self.balance} {self.date}>" +
            f"<Customer ID: {self.customer_id}>"
        )
    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS accounts(
            id INTEGER PRIMARY KEY,
            type VARCHAR(20) NOT NULL,
            balance REAL NOT NULL,
            date DATE NOT NULL,
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES accounts(id)
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
    def create_account(cls, type, balance, date, customer_id):
        account = cls(type, balance, date, customer_id)
        account.save()
        return account
    
    def update_account(self):
        sql = """
        UPDATE accounts
        SET type = ?, balance = ?, date = ?, customer_id = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.type, self.balance, self.date,
                              self.customer_id, self.id))
        CONN.commit()

    def delete_account(self):
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
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM accounts
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    
    def delete(self):
        sql = """
        DELETE FROM accounts
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None



# Account1 = Account("W", 200.28, "28/4/2024" , 1, 1)
# Account1.drop_table()
# Account1.delete_account([2])
# Account1.create_table()
# Account1.save()
# print(Account1)

