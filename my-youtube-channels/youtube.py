#youtube.py
#connects database youtube.db

import sqlite3

connection = sqlite3.connect('/Users/vaibhavblayer/sqlite-projects/my-youtube-channels/youtube.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS channels(id INTEGER PRIMARY KEY, name TEXT, email, topic TEXT);')
connection.commit()

def info():
	global name
	name = input(' Name : ') or "Vaibhav Blayer"
	global email
	email = input(' Email : vaibhavblayer@gmail.com : ') or "vaibhavblayer@gmail.com"
	global topic
	topic = input(' Topic : ') or "Physics"


def insert(name, email, topic):
	sql1 = 'INSERT INTO channels(name, email, topic) VALUES(\"{0}\", \"{1}\", \"{2}\");'.format(name, email, topic)
	cursor.execute(sql1)
	connection.commit()



if __name__=='__main__':
	info()
	insert(name, email, topic)



