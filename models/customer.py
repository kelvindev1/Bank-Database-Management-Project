from __init__ import CURSOR, CONN

class Customer():

    all = {}

    def __init__(self, first_name, last_name,  phone_number, email, id = None):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email


    def __repr__(self) -> str:
        return f'<Customer {self.id}: {self.first_name} {self.last_name}: {self.phone_number}, {self.email}>'
    


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            phone_number INTEGER NOT NULL,
            email VARCHAR(35) NOT NULL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    
    def save(self):
        sql = """
            INSERT INTO customers(first_name, last_name, phone_number, email)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.phone_number, self.email))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self



    @classmethod
    def create(cls, first_name, last_name, phone_number, email):
        customer = cls(first_name, last_name, phone_number, email)
        customer.save()
        return customer
    

    def update(self):
        sql = """
            UPDATE customers
            SET first_name = ?, last_name = ?, phone_number = ?, email = ? 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.phone_number, self.email, self.id))
        CONN.commit()


    def delete(self):
        sql = """
            DELETE FROM customers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):
        customer = cls.all.get(row[0])
        if customer:
            customer.first_name = row[1]
            customer.last_name = row[2]
            customer.phone_number = row[3]
            customer.email = row[4]
        else:
            customer = cls(row[1], row[2]), row[3], row[4]
            customer.id = row[0]
            cls.all[customer.id] = customer
        return customer


    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM customers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]


    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM customers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None


    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM customers
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None


    def accounts(self):
        from account import Account
        sql = """
            SELECT * FROM accounts
            WHERE customer_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [
            Account.instance_from_db(row) for row in rows
        ]

