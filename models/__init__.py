import sqlite3

CONN = sqlite3.connect("Bank.db")
CURSOR = CONN.cursor()