# youtube videos list with database
# youtube.py

import sqlite3

connection = sqlite3.connect('/Users/vaibhavblayer/youtube/youtube.db')
cursor = connection.cursor()

title = input(' Title : ')
why = input(' Why : ')
what = input(' What : ')
how = input(' How : ')
tags = input(' Tags : ')

def insert(title, why, what, how, tags): 
	entry = 'INSERT INTO mechanics (title, why, what, how, tags) VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\");'.format(title, why, what, how, tags)
	cursor.execute(entry)
	connection.commit()

def show(n=5):
	query = 'select * from mechanics order by rowid desc limit {0};'.format(n)
	for item in cursor.execute(query):
		print('{0} : {1} : {2} : {3} : {4}'.format(item[0], item[1], item[2], item[3], item[4]))


insert(title, why, what, how, tags)
show(1)

#connection.close()

