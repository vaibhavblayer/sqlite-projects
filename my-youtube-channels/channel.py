#channel.py
#connects database youtube.db

import sqlite3

connection = sqlite3.connect('/Users/vaibhavblayer/sqlite-projects/my-youtube-channels/youtube.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS latex_tutorials(id INTEGER PRIMARY KEY, title TEXT, description TEXT);')
connection.commit()

def info():
	global title
	title = input(' Title : ') or "How to make circle in tikz/latex"
	global description
	description = input(' Description : ') or "This video is about tikz."

def insert(title, description):
	sql1 = 'INSERT INTO latex_tutorials(title, description) VALUES(\"{0}\", \"{1}\")'.format(title, description)
	cursor.execute(sql1)
	connection.commit()



if __name__=='__main__':
	info()
	insert(title, description)



