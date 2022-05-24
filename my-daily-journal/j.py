# journal with database
# journal.py

import sqlite3
import time
import cipher

connection = sqlite3.connect('/Users/vaibhavblayer/my-daily-journal/journal.db')
cursor = connection.cursor()

sql = '''create table if not exists journalDecrypted(title, description)'''
cursor.execute(sql)
connection.commit()



def insert(title, description):
	entry = 'INSERT INTO journalDecrypted (title, description) VALUES (\"{0}\", \"{1}\");'.format(title, description)
	cursor.execute(entry)
	connection.commit()

def decryptAndTransfer(m, n):
	query = 'select * from journal where rowid >={0} and rowid <={1};'.format(m, n)
	for item in cursor.execute(query):
		insert(item[1], cipher.decrypt(item[2], 13))

def transfer(m, n):
	query = 'select * from journal where rowid >={0} and rowid <={1};'.format(m, n)
	for item in cursor.execute(query):
		insert(item[1], item[2])






