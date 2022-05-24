# ciphered with database
import sqlite3
import time
import cipher
import sys

n = int(sys.argv[1])

connection = sqlite3.connect('/Users/vaibhavblayer/sqlite-projects/ciphered/ciphered.db')
cursor = connection.cursor()

sql = '''create table if not exists deciphered(title, description)'''
cursor.execute(sql)
connection.commit()

#dc = {}

def show(n):
	query = 'select * from ciphered order by rowid desc limit {0};'.format(n)
	for item in cursor.execute(query):
#		dc[item[0]] = cipher.decrypt(item[1], 13)
		entry = 'INSERT INTO deciphered (title, description) VALUES (\"{0}\", \"{1}\");'.format(item[0],  cipher.decrypt(item[1],13))
		cursor.execute(entry)
		connection.commit()

#connection.close()

if __name__=='__main__':
	show(n)

