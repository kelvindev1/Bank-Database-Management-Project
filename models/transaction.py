

class Transaction():
    def __init__(self, type, amount, date, id = None):

        self.id = id
        self.type = type
        self.amount = amount
        self.date = date
