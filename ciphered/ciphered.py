# ciphered with database
import sqlite3
import time
import cipher

connection = sqlite3.connect('/Users/vaibhavblayer/sqlite-projects/ciphered/ciphered.db')
cursor = connection.cursor()

sql = '''create table if not exists ciphered(title, description)'''
cursor.execute(sql)
connection.commit()


title = time.ctime()

description = input(f' Title : {time.ctime()} \n Description : ')
#cursor.execute('insert into ciphered(title, description) VALUES (\"{0}\", \"{1}\");'.format(title, description))


#def takeInputs():
#	'''Takes two user inputs using terminal, description and encryption & sets the inputs to the global variables. It takes no argumnets.'''
#	description = input(f' Title : {time.ctime()} \n Description : ')
#	encryption = input(' Encrypted : yes/no : ')


def insert(description, encryption = 'yes'):
	'''Inserts the data into the database SQLite. Takes two inputs, description as string and the other one encryption is optional.'''


	if encryption == 'yes':
		description = cipher.encrypt(description, 13)
	else:
		description = description

	entry = 'INSERT INTO ciphered (title, description) VALUES (\"{0}\", \"{1}\");'.format(title, description)
	cursor.execute(entry)
	connection.commit()

def show(n=5):
	'''Shows the entries from the database. It takes one argument n as integer which is optional.'''
	query = 'select * from ciphered order by rowid desc limit {0};'.format(n)
	for item in cursor.execute(query):
		print(f' {item[0]} : {cipher.decrypt(item[1], 13)}')


#connection.close()


if __name__=='__main__':
	insert(description, encryption='yes')

